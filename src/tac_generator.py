# src/tac_generator.py
from gen.grammar.gramatica_v4Parser import gramatica_v4Parser
from gen.grammar.gramatica_v4Visitor import gramatica_v4Visitor


class TACGenerator(gramatica_v4Visitor):
    """
    Generador de Código de Tres Direcciones (TAC)
    Emite instrucciones como:
        t1 = y * 2
        t2 = x + t1
        z = t2
    """
    
    def __init__(self):
        super().__init__()
        self.instrucciones = []      # Lista de instrucciones TAC
        self.temp_counter = 0        # Contador para temporales (t1, t2, ...)
        self.label_counter = 0       # Contador para etiquetas (L1, L2, ...)
        self.funcion_actual = None   # Nombre de la función actual
        self.tabla_temporales = {}   # Mapa de expresiones a temporales
        self.pila_ciclos = []        # Pila de (etiqueta_inicio, etiqueta_fin) para break/continue
        
    def nuevo_temporal(self):
        """Genera un nuevo temporal (t1, t2, t3, ...)"""
        self.temp_counter += 1
        return f"t{self.temp_counter}"
    
    def nueva_etiqueta(self):
        """Genera una nueva etiqueta (L1, L2, L3, ...)"""
        self.label_counter += 1
        return f"L{self.label_counter}"
    
    def emitir(self, instruccion):
        """Agrega una instrucción a la lista"""
        self.instrucciones.append(instruccion)
    
    def get_tac(self):
        """Retorna el código TAC como string"""
        return "\n".join(self.instrucciones)
    
    # ========== Programa y funciones ==========
    
    def visitPrograma(self, ctx: gramatica_v4Parser.ProgramaContext):
        # Reiniciar contadores
        self.temp_counter = 0
        self.label_counter = 0
        self.instrucciones = []
        
        # Declaraciones de estructuras (a nivel de programa)
        for est_ctx in ctx.declaracionEstructura():
            self.visit(est_ctx)

        # Registrar funciones primero
        for func_ctx in ctx.funcionDeclaracion():
            self.visit(func_ctx)
        
        # Código para el bloque principal (función implícita main)
        self.funcion_actual = "main"
        self.emitir("; === Código principal ===")
        self.visit(ctx.bloque())
        self.emitir("; Fin del programa")
        
        return self.get_tac()
    
    def visitFuncionDeclaracion(self, ctx: gramatica_v4Parser.FuncionDeclaracionContext):
        nombre = ctx.IDENTIFICADOR().getText()
        self.funcion_actual = nombre
        
        # Determinar tipo de retorno
        tipo_retorno = "void"
        if ctx.tipo():
            tipo_retorno = ctx.tipo().getText()
        
        # Inicio de función
        self.emitir(f"\n; === Función {nombre} (retorna: {tipo_retorno}) ===")
        self.emitir(f"begin_func {nombre}")
        
        # Parámetros
        if ctx.parametros():
            params = []
            for p in ctx.parametros().parametro():
                nombre_param = p.IDENTIFICADOR().getText()
                tipo_param = p.tipo().getText()
                params.append(nombre_param)
                self.emitir(f"param {nombre_param}")
        
        # Cuerpo de la función
        self.visit(ctx.bloque())
        
        # Fin de función
        self.emitir(f"end_func {nombre}")
        
        return None
    
    # ========== Bloque ==========
    
    def visitBloque(self, ctx: gramatica_v4Parser.BloqueContext):
        for sentencia in ctx.sentencia():
            self.visit(sentencia)
        return None
    
    # ========== Declaraciones y asignaciones ==========
    
    def visitDeclaracionVariable(self, ctx: gramatica_v4Parser.DeclaracionVariableContext):
        tipo = ctx.tipo().getText()
        nombre = ctx.IDENTIFICADOR().getText()
        
        es_arreglo = ctx.CORCHETE_IZQ() is not None and ctx.CORCHETE_DER() is not None
        
        # Buscar valor de inicialización
        valor = None
        if ctx.expresion() is not None:
            valor = self.visit(ctx.expresion())
        else:
            # Buscar literalArreglo
            for child in ctx.getChildren():
                if isinstance(child, gramatica_v4Parser.LiteralArregloContext):
                    valor = self.visit(child)
                    break
        
        if valor is not None:
            if isinstance(valor, list):
                # Inicialización de arreglo
                for i, elem in enumerate(valor):
                    temp = self.nuevo_temporal()
                    self.emitir(f"{temp} = {elem}")
                    self.emitir(f"{nombre}[{i}] = {temp}")
            else:
                self.emitir(f"{nombre} = {valor}")
        elif es_arreglo:
            # Arreglo vacío
            self.emitir(f"{nombre} = []")
        else:
            # Inicialización por defecto
            if tipo == 'entero':
                self.emitir(f"{nombre} = 0")
            elif tipo == 'flotante':
                self.emitir(f"{nombre} = 0.0")
            elif tipo == 'booleano':
                self.emitir(f"{nombre} = false")
            elif tipo == 'cadena':
                self.emitir(f"{nombre} = \"\"")
        
        return None
    
    def visitAsignacion(self, ctx: gramatica_v4Parser.AsignacionContext):
        nombre = ctx.IDENTIFICADOR().getText()
        valor = self.visit(ctx.expresion())
        self.emitir(f"{nombre} = {valor}")
        return None
    
    def visitAsignacionArreglo(self, ctx: gramatica_v4Parser.AsignacionArregloContext):
        acceso = ctx.accesoArreglo()
        nombre = acceso.IDENTIFICADOR().getText()
        indice = self.visit(acceso.expresion())
        valor = self.visit(ctx.expresion())
        self.emitir(f"{nombre}[{indice}] = {valor}")
        return None

    # ========== Structs (Proyecto Final) ==========

    def visitDeclaracionEstructura(self, ctx):
        nombre = ctx.IDENTIFICADOR().getText()
        campos = ", ".join(c.IDENTIFICADOR().getText() for c in ctx.campoEstructura())
        self.emitir(f"; estructura {nombre} {{ {campos} }}")
        return None

    def visitDeclaracionVariableEstructura(self, ctx):
        tipo_struct = ctx.IDENTIFICADOR(0).getText()
        nombre = ctx.IDENTIFICADOR(1).getText()
        self.emitir(f"; {tipo_struct} {nombre}")
        return None

    def visitAsignacionCampo(self, ctx):
        acceso = ctx.accesoCampo()
        var = acceso.IDENTIFICADOR(0).getText()
        campo = acceso.IDENTIFICADOR(1).getText()
        valor = self.visit(ctx.expresion())
        # En TAC el acceso a campo se expresa como acceso indexado al struct.
        self.emitir(f"{var}.{campo} = {valor}")
        return None

    def visitAccesoCampoExpr(self, ctx):
        acceso = ctx.accesoCampo()
        var = acceso.IDENTIFICADOR(0).getText()
        campo = acceso.IDENTIFICADOR(1).getText()
        temp = self.nuevo_temporal()
        self.emitir(f"{temp} = {var}.{campo}")
        return temp
    
    # ========== Literales ==========
    
    def visitLiteralEntero(self, ctx):
        return ctx.ENTERO().getText()
    
    def visitLiteralFlotante(self, ctx):
        return ctx.FLOTANTE().getText()
    
    def visitLiteralCadena(self, ctx):
        s = ctx.CADENA().getText()
        return s
    
    def visitLiteralVerdadero(self, ctx):
        return "true"
    
    def visitLiteralFalso(self, ctx):
        return "false"
    
    def visitLiteralArreglo(self, ctx):
        valores = []
        if ctx.expresion():
            for expr in ctx.expresion():
                valores.append(self.visit(expr))
        return valores
    
    # ========== Expresiones aritméticas ==========
    
    def visitMultiplicacionDivisionModulo(self, ctx):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        op = ctx.op.text
        
        temp = self.nuevo_temporal()
        self.emitir(f"{temp} = {izq} {op} {der}")
        return temp
    
    def visitSumaResta(self, ctx):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        op = ctx.op.text
        
        temp = self.nuevo_temporal()
        self.emitir(f"{temp} = {izq} {op} {der}")
        return temp
    
    def visitNegacionLogica(self, ctx):
        expr = self.visit(ctx.expresion())
        temp = self.nuevo_temporal()
        self.emitir(f"{temp} = not {expr}")
        return temp
    
    def visitMenosUnario(self, ctx):
        expr = self.visit(ctx.expresion())
        temp = self.nuevo_temporal()
        self.emitir(f"{temp} = -{expr}")
        return temp
    
    def visitParentesis(self, ctx):
        return self.visit(ctx.expresion())

    # ========== Casting y ternario (Proyecto Final) ==========

    def visitCasting(self, ctx):
        val = self.visit(ctx.expresion())
        tipo = ctx.tipo().getText()
        temp = self.nuevo_temporal()
        self.emitir(f"{temp} = ({tipo}) {val}")
        return temp

    def visitTernario(self, ctx):
        cond = self.visit(ctx.cond)
        temp = self.nuevo_temporal()
        etiqueta_true = self.nueva_etiqueta()
        etiqueta_fin = self.nueva_etiqueta()

        self.emitir(f"if {cond} goto {etiqueta_true}")
        # Rama falsa
        val_sino = self.visit(ctx.sino)
        self.emitir(f"{temp} = {val_sino}")
        self.emitir(f"goto {etiqueta_fin}")
        # Rama verdadera
        self.emitir(f"{etiqueta_true}:")
        val_ent = self.visit(ctx.ent)
        self.emitir(f"{temp} = {val_ent}")
        self.emitir(f"{etiqueta_fin}:")
        return temp
    
    # ========== Expresiones relacionales y lógicas ==========
    
    def visitRelacional(self, ctx):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        op = ctx.op.text
        
        temp = self.nuevo_temporal()
        self.emitir(f"{temp} = {izq} {op} {der}")
        return temp
    
    def visitLogica(self, ctx):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        op = ctx.op.text
        
        temp = self.nuevo_temporal()
        self.emitir(f"{temp} = {izq} {op} {der}")
        return temp
    
    # ========== Referencias ==========
    
    def visitReferenciaVariable(self, ctx):
        nombre = ctx.IDENTIFICADOR().getText()
        return nombre
    
    def visitAccesoArreglo(self, ctx):
        nombre = ctx.IDENTIFICADOR().getText()
        indice = self.visit(ctx.expresion())
        temp = self.nuevo_temporal()
        self.emitir(f"{temp} = {nombre}[{indice}]")
        return temp
    
    def visitAccesoArregloExpr(self, ctx):
        return self.visit(ctx.accesoArreglo())
    
    # ========== Condicionales ==========
    
    def visitCondicionalSi(self, ctx: gramatica_v4Parser.CondicionalSiContext):
        condicion = self.visit(ctx.expresion())

        etiqueta_then = self.nueva_etiqueta()
        etiqueta_fin = self.nueva_etiqueta()

        # Salto condicional positivo: si la condición es verdadera, ir al bloque "then".
        self.emitir(f"if {condicion} goto {etiqueta_then}")

        # El bloque "else" cae por defecto (cuando la condición es falsa).
        if ctx.SINO():
            self.visit(ctx.bloque(1))
        self.emitir(f"goto {etiqueta_fin}")

        # Bloque "then".
        self.emitir(f"{etiqueta_then}:")
        self.visit(ctx.bloque(0))

        self.emitir(f"{etiqueta_fin}:")
        return None
    
    # ========== Ciclos ==========
    
    def visitCicloMientras(self, ctx: gramatica_v4Parser.CicloMientrasContext):
        etiqueta_cond = self.nueva_etiqueta()
        etiqueta_body = self.nueva_etiqueta()
        etiqueta_fin = self.nueva_etiqueta()

        # La condición se evalúa al final y se salta al cuerpo con un salto positivo.
        self.emitir(f"goto {etiqueta_cond}")
        self.emitir(f"{etiqueta_body}:")

        # continue → reevaluar condición; break → salir del ciclo.
        self.pila_ciclos.append((etiqueta_cond, etiqueta_fin))
        self.visit(ctx.bloque())
        self.pila_ciclos.pop()

        self.emitir(f"{etiqueta_cond}:")
        condicion = self.visit(ctx.expresion())
        self.emitir(f"if {condicion} goto {etiqueta_body}")
        self.emitir(f"{etiqueta_fin}:")
        return None
    
    def visitCicloPara(self, ctx: gramatica_v4Parser.CicloParaContext):
        etiqueta_cond = self.nueva_etiqueta()
        etiqueta_body = self.nueva_etiqueta()
        etiqueta_step = self.nueva_etiqueta()
        etiqueta_fin = self.nueva_etiqueta()

        # Inicialización
        if ctx.inicializacionPara():
            self.visit(ctx.inicializacionPara())
        elif ctx.asignacionPara():
            self.visit(ctx.asignacionPara())

        self.emitir(f"goto {etiqueta_cond}")
        self.emitir(f"{etiqueta_body}:")

        # continue → ejecutar actualización y reevaluar; break → salir.
        self.pila_ciclos.append((etiqueta_step, etiqueta_fin))
        self.visit(ctx.bloque())
        self.pila_ciclos.pop()

        # Actualización
        self.emitir(f"{etiqueta_step}:")
        if ctx.actualizacionPara():
            self.visit(ctx.actualizacionPara())

        # Condición con salto positivo al cuerpo.
        self.emitir(f"{etiqueta_cond}:")
        if ctx.cond:
            condicion = self.visit(ctx.cond)
            self.emitir(f"if {condicion} goto {etiqueta_body}")
        else:
            self.emitir(f"goto {etiqueta_body}")
        self.emitir(f"{etiqueta_fin}:")
        return None
    
    # ========== Switch / segun (Proyecto Final) ==========

    def visitSentenciaSegun(self, ctx: gramatica_v4Parser.SentenciaSegunContext):
        control = self.visit(ctx.expresion())
        etiqueta_fin = self.nueva_etiqueta()
        casos = ctx.casoSegun()
        etiquetas_caso = [self.nueva_etiqueta() for _ in casos]
        etiqueta_def = self.nueva_etiqueta() if ctx.casoDefecto() else etiqueta_fin

        # Saltos condicionales encadenados sobre el valor de control.
        for caso, etq in zip(casos, etiquetas_caso):
            val = self.visit(caso.expresion())
            self.emitir(f"if {control} == {val} goto {etq}")
        self.emitir(f"goto {etiqueta_def}")

        # Cuerpos de los casos (break → goto fin; fall-through si no hay break).
        self.pila_ciclos.append((etiqueta_fin, etiqueta_fin))
        for caso, etq in zip(casos, etiquetas_caso):
            self.emitir(f"{etq}:")
            for s in caso.sentencia():
                self.visit(s)
        if ctx.casoDefecto():
            self.emitir(f"{etiqueta_def}:")
            for s in ctx.casoDefecto().sentencia():
                self.visit(s)
        self.pila_ciclos.pop()

        self.emitir(f"{etiqueta_fin}:")
        return None

    def visitInicializacionPara(self, ctx: gramatica_v4Parser.InicializacionParaContext):
        tipo = ctx.tipo().getText()
        nombre = ctx.IDENTIFICADOR().getText()
        valor = self.visit(ctx.expresion())
        self.emitir(f"{nombre} = {valor}")
        return None
    
    def visitAsignacionPara(self, ctx: gramatica_v4Parser.AsignacionParaContext):
        nombre = ctx.IDENTIFICADOR().getText()
        valor = self.visit(ctx.expresion())
        self.emitir(f"{nombre} = {valor}")
        return None
    
    def visitActualizacionPara(self, ctx: gramatica_v4Parser.ActualizacionParaContext):
        nombre = ctx.IDENTIFICADOR().getText()
        valor = self.visit(ctx.expresion())
        self.emitir(f"{nombre} = {valor}")
        return None
    
    # ========== Funciones ==========
    
    def visitLlamadaFuncion(self, ctx: gramatica_v4Parser.LlamadaFuncionContext):
        nombre = ctx.IDENTIFICADOR().getText()
        args = []
        if ctx.expresion():
            for arg in ctx.expresion():
                args.append(self.visit(arg))
        
        temp = self.nuevo_temporal()
        args_str = ", ".join(args)
        self.emitir(f"{temp} = call {nombre}, {args_str}")
        return temp
    
    def visitLlamadaFuncionExpr(self, ctx: gramatica_v4Parser.LlamadaFuncionExprContext):
        nombre = ctx.IDENTIFICADOR().getText()
        args = []
        if ctx.expresion():
            for arg in ctx.expresion():
                args.append(self.visit(arg))
        
        temp = self.nuevo_temporal()
        args_str = ", ".join(args)
        self.emitir(f"{temp} = call {nombre}, {args_str}")
        return temp
    
    def visitSentenciaRetorna(self, ctx: gramatica_v4Parser.SentenciaRetornaContext):
        if ctx.expresion():
            valor = self.visit(ctx.expresion())
            self.emitir(f"return {valor}")
        else:
            self.emitir("return")
        return None
    
    # ========== Impresión ==========
    
    def visitImpresion(self, ctx: gramatica_v4Parser.ImpresionContext):
        valor = self.visit(ctx.expresion())
        self.emitir(f"print {valor}")
        return None
    
    # ========== Break y Continue ==========
    
    def visitSentenciaBreak(self, ctx: gramatica_v4Parser.SentenciaBreakContext):
        if self.pila_ciclos:
            _, etiqueta_fin = self.pila_ciclos[-1]
            self.emitir(f"goto {etiqueta_fin}")
        return None
    
    def visitSentenciaContinue(self, ctx: gramatica_v4Parser.SentenciaContinueContext):
        if self.pila_ciclos:
            etiqueta_inicio, _ = self.pila_ciclos[-1]
            self.emitir(f"goto {etiqueta_inicio}")
        return None
    
    # ========== Import ==========
    
    def visitSentenciaImportar(self, ctx: gramatica_v4Parser.SentenciaImportarContext):
        nombre_archivo = ctx.CADENA().getText()
        self.emitir(f"import {nombre_archivo}")
        return None