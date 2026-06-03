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
        elif ctx.VOID():
            tipo_retorno = "vacio"
        
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
        # Verificar si es variable de tipo struct
        if ctx.tipoStruct():
            tipo_struct = ctx.tipoStruct().getText()
            nombre = ctx.IDENTIFICADOR().getText()
            self.emitir(f"{nombre} = new {tipo_struct}")
            return None
        
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
        # Verificar si es asignación a struct (struct.campo)
        if ctx.accesoStruct():
            acceso = ctx.accesoStruct()
            nombre_struct = acceso.IDENTIFICADOR(0).getText()
            nombre_campo = acceso.IDENTIFICADOR(1).getText()
            valor = self.visit(ctx.expresion())
            self.emitir(f"{nombre_struct}.{nombre_campo} = {valor}")
            return None
        
        # Asignación normal
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
    
    def visitLiteralStruct(self, ctx):
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
    
    # ========== Operador Ternario ==========
    
    def visitOperadorTernario(self, ctx):
        condicion = self.visit(ctx.condicion)
        verdadero = self.visit(ctx.verdadero)
        falso = self.visit(ctx.falso)
        
        etiqueta_falso = self.nueva_etiqueta()
        etiqueta_fin = self.nueva_etiqueta()
        temp = self.nuevo_temporal()
        
        self.emitir(f"if {condicion} == false goto {etiqueta_falso}")
        self.emitir(f"{temp} = {verdadero}")
        self.emitir(f"goto {etiqueta_fin}")
        self.emitir(f"{etiqueta_falso}:")
        self.emitir(f"{temp} = {falso}")
        self.emitir(f"{etiqueta_fin}:")
        
        return temp
    
    # ========== Casting Explícito ==========
    
    def visitCastingExplicito(self, ctx):
        tipo_destino = ctx.tipo().getText()
        expr = self.visit(ctx.expresion())
        temp = self.nuevo_temporal()
        self.emitir(f"{temp} = ({tipo_destino}) {expr}")
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
    
    def visitAccesoStruct(self, ctx):
        nombre_struct = ctx.IDENTIFICADOR(0).getText()
        nombre_campo = ctx.IDENTIFICADOR(1).getText()
        temp = self.nuevo_temporal()
        self.emitir(f"{temp} = {nombre_struct}.{nombre_campo}")
        return temp
    
    def visitAccesoStructExpr(self, ctx):
        return self.visit(ctx.accesoStruct())
    
    # ========== Condicionales ==========
    
    def visitCondicionalSi(self, ctx: gramatica_v4Parser.CondicionalSiContext):
        condicion = self.visit(ctx.expresion())
        
        etiqueta_else = self.nueva_etiqueta()
        etiqueta_fin = self.nueva_etiqueta()
        
        self.emitir(f"if {condicion} == false goto {etiqueta_else}")
        
        # Bloque if
        self.visit(ctx.bloque(0))
        self.emitir(f"goto {etiqueta_fin}")
        
        # Bloque else
        self.emitir(f"{etiqueta_else}:")
        if ctx.SINO():
            self.visit(ctx.bloque(1))
        
        self.emitir(f"{etiqueta_fin}:")
        return None
    
    # ========== Switch/Case ==========
    
    def visitSentenciaSwitch(self, ctx: gramatica_v4Parser.SentenciaSwitchContext):
        expr = self.visit(ctx.expresion())
        temp_expr = self.nuevo_temporal()
        self.emitir(f"{temp_expr} = {expr}")
        
        etiqueta_fin = self.nueva_etiqueta()
        casos = list(ctx.caso())
        default_bb = None
        
        for caso_ctx in casos:
            valor_caso = self.visit(caso_ctx.expresion())
            etiqueta_caso = self.nueva_etiqueta()
            self.emitir(f"if {temp_expr} == {valor_caso} goto {etiqueta_caso}")
            default_bb = etiqueta_caso  # Último caso como posible default
        
        # Default si existe
        if ctx.casoDefault():
            etiqueta_default = self.nueva_etiqueta()
            self.emitir(f"goto {etiqueta_default}")
            
            # Generar casos
            for caso_ctx in casos:
                valor_caso = self.visit(caso_ctx.expresion())
                etiqueta_caso = self.nueva_etiqueta()
                self.emitir(f"if {temp_expr} == {valor_caso} goto {etiqueta_caso}")
                self.emitir(f"{etiqueta_caso}:")
                for sent in caso_ctx.sentencia():
                    self.visit(sent)
                self.emitir(f"goto {etiqueta_fin}")
            
            # Default
            self.emitir(f"{etiqueta_default}:")
            for sent in ctx.casoDefault().sentencia():
                self.visit(sent)
        else:
            # Sin default
            for caso_ctx in casos:
                valor_caso = self.visit(caso_ctx.expresion())
                etiqueta_caso = self.nueva_etiqueta()
                self.emitir(f"if {temp_expr} == {valor_caso} goto {etiqueta_caso}")
            
            for caso_ctx in casos:
                valor_caso = self.visit(caso_ctx.expresion())
                etiqueta_caso = self.nueva_etiqueta()
                self.emitir(f"{etiqueta_caso}:")
                for sent in caso_ctx.sentencia():
                    self.visit(sent)
                self.emitir(f"goto {etiqueta_fin}")
        
        self.emitir(f"{etiqueta_fin}:")
        return None
    
    def visitCaso(self, ctx: gramatica_v4Parser.CasoContext):
        return None  # Procesado en visitSentenciaSwitch
    
    def visitCasoDefault(self, ctx: gramatica_v4Parser.CasoDefaultContext):
        return None  # Procesado en visitSentenciaSwitch
    
    # ========== Ciclos ==========
    
    def visitCicloMientras(self, ctx: gramatica_v4Parser.CicloMientrasContext):
        etiqueta_inicio = self.nueva_etiqueta()
        etiqueta_fin = self.nueva_etiqueta()
        
        self.emitir(f"{etiqueta_inicio}:")
        condicion = self.visit(ctx.expresion())
        self.emitir(f"if {condicion} == false goto {etiqueta_fin}")
        
        self.pila_ciclos.append((etiqueta_inicio, etiqueta_fin))
        self.visit(ctx.bloque())
        self.pila_ciclos.pop()
        self.emitir(f"goto {etiqueta_inicio}")
        self.emitir(f"{etiqueta_fin}:")
        return None
    
    def visitCicloPara(self, ctx: gramatica_v4Parser.CicloParaContext):
        etiqueta_inicio = self.nueva_etiqueta()
        etiqueta_fin = self.nueva_etiqueta()
        
        # Inicialización
        if ctx.inicializacionPara():
            self.visit(ctx.inicializacionPara())
        elif ctx.asignacionPara():
            self.visit(ctx.asignacionPara())
        
        self.emitir(f"{etiqueta_inicio}:")
        
        # Condición
        if ctx.cond:
            condicion = self.visit(ctx.cond)
            self.emitir(f"if {condicion} == false goto {etiqueta_fin}")
        
        # Cuerpo
        self.pila_ciclos.append((etiqueta_inicio, etiqueta_fin))
        self.visit(ctx.bloque())
        self.pila_ciclos.pop()
        
        # Actualización
        if ctx.actualizacionPara():
            self.visit(ctx.actualizacionPara())
        
        self.emitir(f"goto {etiqueta_inicio}")
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
    
    # ========== Struct ==========
    
    def visitSentenciaStruct(self, ctx: gramatica_v4Parser.SentenciaStructContext):
        nombre_struct = ctx.IDENTIFICADOR().getText()
        self.emitir(f"struct {nombre_struct}")
        for campo_ctx in ctx.declaracionCampoStruct():
            tipo_campo = campo_ctx.tipo().getText()
            nombre_campo = campo_ctx.IDENTIFICADOR().getText()
            self.emitir(f"    {tipo_campo} {nombre_campo}")
        self.emitir(f"end_struct {nombre_struct}")
        return None