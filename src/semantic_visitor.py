# src/semantic_visitor.py
from gen.grammar.gramatica_v4Parser import gramatica_v4Parser
from gen.grammar.gramatica_v4Visitor import gramatica_v4Visitor
from src.symbol_table import TablaSimbolos

class SemanticVisitor(gramatica_v4Visitor):
    def __init__(self):
        super().__init__()
        self.tabla = TablaSimbolos()
        self.errores = []
        self.funcion_actual = None
        self.tipo_retorno_actual = None
        self.encontro_retorno_actual = False
        self.en_ciclo = 0  # Contador de ciclos anidados (para break/continue)
        self.en_switch = 0  # Contador de switch anidados (para break dentro de 'segun')
        self.estructuras = {}  # nombre_struct -> {campo: tipo}

    # ------------------------------------------------------------------
    # Utilidades
    # ------------------------------------------------------------------
    def agregar_error(self, ctx, mensaje):
        linea = ctx.start.line if ctx and ctx.start else 0
        columna = ctx.start.column if ctx and ctx.start else 0
        self.errores.append(
            f"[Error Semántico] Línea {linea}, Columna {columna}: {mensaje}"
        )

    def tiene_errores(self):
        return len(self.errores) > 0

    def reporte(self):
        return "\n".join(self.errores)

    def tipo_desde_ctx(self, ctx_tipo):
        if ctx_tipo is None:
            return "vacio"
        return ctx_tipo.getText()

    def es_tipo_numerico(self, tipo):
        return tipo in ("entero", "flotante")

    def tipos_compatibles(self, esperado, recibido):
        if esperado == "error" or recibido == "error":
            return True
        return esperado == recibido

    def es_arreglo(self, tipo):
        return tipo is not None and tipo.endswith('[]')

    def obtener_tipo_base(self, tipo_arreglo):
        if tipo_arreglo and tipo_arreglo.endswith('[]'):
            return tipo_arreglo[:-2]
        return tipo_arreglo

    def _visitar_bloque(self, ctx_bloque, crear_ambito=True):
        if crear_ambito:
            self.tabla.entrar_ambito()
        for sentencia in ctx_bloque.sentencia():
            self.visit(sentencia)
        if crear_ambito:
            self.tabla.salir_ambito()
        return None

    # ------------------------------------------------------------------
    # Programa y funciones
    # ------------------------------------------------------------------
    def visitPrograma(self, ctx: gramatica_v4Parser.ProgramaContext):
        # Pasada 0: registrar las estructuras (structs) para que estén
        # disponibles al analizar funciones y el bloque principal.
        for est_ctx in ctx.declaracionEstructura():
            self._registrar_estructura(est_ctx)
        # Primera pasada: registrar todas las funciones
        for func_ctx in ctx.funcionDeclaracion():
            self._registrar_funcion(func_ctx)
        # Segunda pasada: analizar los cuerpos de funciones
        for func_ctx in ctx.funcionDeclaracion():
            self._analizar_funcion(func_ctx)
        # Analizar bloque principal
        self.visit(ctx.bloque())
        return None

    # ------------------------------------------------------------------
    # Structs (Proyecto Final)
    # ------------------------------------------------------------------
    def _registrar_estructura(self, ctx: gramatica_v4Parser.DeclaracionEstructuraContext):
        nombre = ctx.IDENTIFICADOR().getText()
        if nombre in self.estructuras:
            self.agregar_error(ctx, f"La estructura '{nombre}' ya fue declarada")
            return
        campos = {}
        for campo_ctx in ctx.campoEstructura():
            tipo_campo = campo_ctx.tipo().getText()
            nombre_campo = campo_ctx.IDENTIFICADOR().getText()
            if nombre_campo in campos:
                self.agregar_error(
                    campo_ctx,
                    f"El campo '{nombre_campo}' está repetido en la estructura '{nombre}'",
                )
            campos[nombre_campo] = tipo_campo
        self.estructuras[nombre] = campos

    def visitDeclaracionEstructura(self, ctx):
        return None

    def visitDeclaracionVariableEstructura(self, ctx: gramatica_v4Parser.DeclaracionVariableEstructuraContext):
        tipo_struct = ctx.IDENTIFICADOR(0).getText()
        nombre = ctx.IDENTIFICADOR(1).getText()

        if tipo_struct not in self.estructuras:
            self.agregar_error(ctx, f"El tipo de estructura '{tipo_struct}' no ha sido declarado")
            return None

        creada = self.tabla.declarar(nombre, tipo_struct, ctx.start.line, ctx.start.column)
        if creada is None:
            self.agregar_error(ctx, f"La variable '{nombre}' ya fue declarada en este ámbito")
        return None

    def visitAsignacionCampo(self, ctx: gramatica_v4Parser.AsignacionCampoContext):
        tipo_campo = self._tipo_de_campo(ctx.accesoCampo())
        tipo_expr = self.visit(ctx.expresion())
        if tipo_campo == "error":
            return None
        if not self.tipos_compatibles(tipo_campo, tipo_expr):
            self.agregar_error(
                ctx,
                f"No se puede asignar una expresión de tipo '{tipo_expr}' al campo de tipo '{tipo_campo}'",
            )
        return None

    def visitAccesoCampoExpr(self, ctx: gramatica_v4Parser.AccesoCampoExprContext):
        return self._tipo_de_campo(ctx.accesoCampo())

    def _tipo_de_campo(self, acceso_ctx):
        nombre_var = acceso_ctx.IDENTIFICADOR(0).getText()
        nombre_campo = acceso_ctx.IDENTIFICADOR(1).getText()
        simbolo = self.tabla.buscar(nombre_var)
        if simbolo is None:
            self.agregar_error(acceso_ctx, f"La variable '{nombre_var}' no ha sido declarada")
            return "error"
        if simbolo.tipo not in self.estructuras:
            self.agregar_error(
                acceso_ctx, f"La variable '{nombre_var}' no es una estructura"
            )
            return "error"
        campos = self.estructuras[simbolo.tipo]
        if nombre_campo not in campos:
            self.agregar_error(
                acceso_ctx,
                f"La estructura '{simbolo.tipo}' no tiene un campo llamado '{nombre_campo}'",
            )
            return "error"
        return campos[nombre_campo]

    def _registrar_funcion(self, ctx: gramatica_v4Parser.FuncionDeclaracionContext):
        nombre = ctx.IDENTIFICADOR().getText()
        tipo_retorno = self.tipo_desde_ctx(ctx.tipo())
        parametros = []
        if ctx.parametros():
            for p in ctx.parametros().parametro():
                tipo_param = p.tipo().getText()
                nombre_param = p.IDENTIFICADOR().getText()
                parametros.append((nombre_param, tipo_param))
        creada = self.tabla.declarar_funcion(
            nombre,
            tipo_retorno,
            parametros,
            ctx.start.line,
            ctx.start.column,
        )
        if creada is None:
            self.agregar_error(ctx, f"La función '{nombre}' ya fue declarada")

    def _analizar_funcion(self, ctx: gramatica_v4Parser.FuncionDeclaracionContext):
        nombre = ctx.IDENTIFICADOR().getText()
        simbolo_func = self.tabla.buscar_funcion(nombre)
        if simbolo_func is None:
            return None

        funcion_anterior = self.funcion_actual
        tipo_retorno_anterior = self.tipo_retorno_actual
        retorno_anterior = self.encontro_retorno_actual

        self.funcion_actual = nombre
        self.tipo_retorno_actual = simbolo_func.tipo_retorno
        self.encontro_retorno_actual = False

        self.tabla.entrar_ambito()
        for nombre_param, tipo_param in simbolo_func.parametros:
            ok = self.tabla.declarar(
                nombre_param,
                tipo_param,
                ctx.start.line,
                ctx.start.column,
            )
            if ok is None:
                self.agregar_error(
                    ctx,
                    f"El parámetro '{nombre_param}' está repetido en la función '{nombre}'",
                )

        self._visitar_bloque(ctx.bloque(), crear_ambito=False)

        if self.tipo_retorno_actual != "vacio" and not self.encontro_retorno_actual:
            self.agregar_error(
                ctx,
                f"La función '{nombre}' debe retornar un valor de tipo '{self.tipo_retorno_actual}'",
            )

        self.tabla.salir_ambito()
        self.funcion_actual = funcion_anterior
        self.tipo_retorno_actual = tipo_retorno_anterior
        self.encontro_retorno_actual = retorno_anterior
        return None

    def visitFuncionDeclaracion(self, ctx: gramatica_v4Parser.FuncionDeclaracionContext):
        return None

    # ------------------------------------------------------------------
    # Bloques
    # ------------------------------------------------------------------
    def visitBloque(self, ctx: gramatica_v4Parser.BloqueContext):
        return self._visitar_bloque(ctx, crear_ambito=True)

    # ------------------------------------------------------------------
    # Declaraciones y asignaciones
    # ------------------------------------------------------------------
    def visitDeclaracionVariable(self, ctx: gramatica_v4Parser.DeclaracionVariableContext):
        tipo = ctx.tipo().getText()
        nombre = ctx.IDENTIFICADOR().getText()
        
        # Verificar si es declaración de arreglo
        es_arreglo = False
        if ctx.CORCHETE_IZQ() and ctx.CORCHETE_DER():
            es_arreglo = True
            tipo = tipo + "[]"
        
        creada = self.tabla.declarar(
            nombre,
            tipo,
            ctx.start.line,
            ctx.start.column,
        )
        
        if creada is None:
            self.agregar_error(
                ctx,
                f"La variable '{nombre}' ya fue declarada en este ámbito",
            )
            if ctx.expresion():
                self.visit(ctx.expresion())
            return None

        if ctx.expresion():
            tipo_expr = self.visit(ctx.expresion())
            if not self.tipos_compatibles(tipo, tipo_expr):
                self.agregar_error(
                    ctx,
                    f"No se puede inicializar '{nombre}' de tipo '{tipo}' con una expresión de tipo '{tipo_expr}'",
                )
        return None

    def visitAsignacion(self, ctx: gramatica_v4Parser.AsignacionContext):
        nombre = ctx.IDENTIFICADOR().getText()
        simbolo = self.tabla.buscar(nombre)
        tipo_expr = self.visit(ctx.expresion())

        if simbolo is None:
            self.agregar_error(ctx, f"La variable '{nombre}' no ha sido declarada")
            return None

        if not self.tipos_compatibles(simbolo.tipo, tipo_expr):
            self.agregar_error(
                ctx,
                f"No se puede asignar una expresión de tipo '{tipo_expr}' a la variable '{nombre}' de tipo '{simbolo.tipo}'",
            )
        return None

    def visitAsignacionArreglo(self, ctx: gramatica_v4Parser.AsignacionArregloContext):
        nombre = ctx.accesoArreglo().IDENTIFICADOR().getText()
        simbolo = self.tabla.buscar(nombre)

        if simbolo is None:
            self.agregar_error(ctx, f"El arreglo '{nombre}' no ha sido declarado")
            return None

        if not self.es_arreglo(simbolo.tipo):
            self.agregar_error(ctx, f"La variable '{nombre}' no es un arreglo")
            return None

        tipo_base = self.obtener_tipo_base(simbolo.tipo)
        tipo_expr = self.visit(ctx.expresion())

        if not self.tipos_compatibles(tipo_base, tipo_expr):
            self.agregar_error(
                ctx,
                f"No se puede asignar '{tipo_expr}' a elemento de arreglo de tipo '{tipo_base}'",
            )
        
        # Verificar que el índice sea entero
        tipo_indice = self.visit(ctx.accesoArreglo().expresion())
        if tipo_indice != "entero" and tipo_indice != "error":
            self.agregar_error(ctx, f"El índice del arreglo debe ser entero, no '{tipo_indice}'")
        
        return None

    def visitInicializacionPara(self, ctx: gramatica_v4Parser.InicializacionParaContext):
        tipo = ctx.tipo().getText()
        nombre = ctx.IDENTIFICADOR().getText()
        tipo_expr = self.visit(ctx.expresion())

        creada = self.tabla.declarar(
            nombre,
            tipo,
            ctx.start.line,
            ctx.start.column,
        )
        if creada is None:
            self.agregar_error(
                ctx,
                f"La variable '{nombre}' ya fue declarada en este ámbito",
            )
            return None

        if not self.tipos_compatibles(tipo, tipo_expr):
            self.agregar_error(
                ctx,
                f"No se puede inicializar '{nombre}' de tipo '{tipo}' con una expresión de tipo '{tipo_expr}'",
            )
        return None

    def visitAsignacionPara(self, ctx: gramatica_v4Parser.AsignacionParaContext):
        nombre = ctx.IDENTIFICADOR().getText()
        simbolo = self.tabla.buscar(nombre)
        tipo_expr = self.visit(ctx.expresion())

        if simbolo is None:
            self.agregar_error(ctx, f"La variable '{nombre}' no ha sido declarada")
            return None

        if not self.tipos_compatibles(simbolo.tipo, tipo_expr):
            self.agregar_error(
                ctx,
                f"No se puede asignar una expresión de tipo '{tipo_expr}' a la variable '{nombre}' de tipo '{simbolo.tipo}' en el ciclo para",
            )
        return None

    def visitActualizacionPara(self, ctx: gramatica_v4Parser.ActualizacionParaContext):
        nombre = ctx.IDENTIFICADOR().getText()
        simbolo = self.tabla.buscar(nombre)
        tipo_expr = self.visit(ctx.expresion())

        if simbolo is None:
            self.agregar_error(ctx, f"La variable '{nombre}' no ha sido declarada")
            return None

        if not self.tipos_compatibles(simbolo.tipo, tipo_expr):
            self.agregar_error(
                ctx,
                f"No se puede actualizar '{nombre}' de tipo '{simbolo.tipo}' con una expresión de tipo '{tipo_expr}'",
            )
        return None

    # ------------------------------------------------------------------
    # Condicionales, ciclos e impresión
    # ------------------------------------------------------------------
    def visitCondicionalSi(self, ctx: gramatica_v4Parser.CondicionalSiContext):
        tipo_cond = self.visit(ctx.expresion())
        if tipo_cond != "booleano" and tipo_cond != "error":
            self.agregar_error(
                ctx,
                f"La condición del 'si' debe ser de tipo 'booleano', no '{tipo_cond}'",
            )
        self.visit(ctx.bloque(0))
        if ctx.SINO():
            self.visit(ctx.bloque(1))
        return None

    def visitCicloMientras(self, ctx: gramatica_v4Parser.CicloMientrasContext):
        self.en_ciclo += 1
        tipo_cond = self.visit(ctx.expresion())
        if tipo_cond != "booleano" and tipo_cond != "error":
            self.agregar_error(
                ctx,
                f"La condición del 'mientras' debe ser de tipo 'booleano', no '{tipo_cond}'",
            )
        self.visit(ctx.bloque())
        self.en_ciclo -= 1
        return None

    def visitCicloPara(self, ctx: gramatica_v4Parser.CicloParaContext):
        self.en_ciclo += 1
        if ctx.inicializacionPara():
            self.visit(ctx.inicializacionPara())
        elif ctx.asignacionPara():
            self.visit(ctx.asignacionPara())

        if ctx.cond:
            tipo_cond = self.visit(ctx.cond)
            if tipo_cond != "booleano" and tipo_cond != "error":
                self.agregar_error(
                    ctx,
                    f"La condición del 'para' debe ser de tipo 'booleano', no '{tipo_cond}'",
                )

        if ctx.actualizacionPara():
            self.visit(ctx.actualizacionPara())

        self.visit(ctx.bloque())
        self.en_ciclo -= 1
        return None

    def visitSentenciaSegun(self, ctx: gramatica_v4Parser.SentenciaSegunContext):
        tipo_control = self.visit(ctx.expresion())
        if tipo_control not in ("entero", "error"):
            self.agregar_error(
                ctx,
                f"La expresión de control de 'segun' debe ser 'entero', no '{tipo_control}'",
            )
        self.en_switch += 1
        for caso in ctx.casoSegun():
            tipo_caso = self.visit(caso.expresion())
            if tipo_caso not in ("entero", "error"):
                self.agregar_error(
                    caso, f"La etiqueta de 'caso' debe ser 'entero', no '{tipo_caso}'"
                )
            for s in caso.sentencia():
                self.visit(s)
        if ctx.casoDefecto():
            for s in ctx.casoDefecto().sentencia():
                self.visit(s)
        self.en_switch -= 1
        return None

    def visitImpresion(self, ctx: gramatica_v4Parser.ImpresionContext):
        self.visit(ctx.expresion())
        return None

    # ------------------------------------------------------------------
    # Break y Continue
    # ------------------------------------------------------------------
    def visitSentenciaBreak(self, ctx: gramatica_v4Parser.SentenciaBreakContext):
        if self.en_ciclo == 0 and self.en_switch == 0:
            self.agregar_error(
                ctx, "La sentencia 'romper' solo puede usarse dentro de un ciclo o de un 'segun'"
            )
        return None

    def visitSentenciaContinue(self, ctx: gramatica_v4Parser.SentenciaContinueContext):
        if self.en_ciclo == 0:
            self.agregar_error(ctx, "La sentencia 'continuar' solo puede usarse dentro de un ciclo")
        return None

    # ------------------------------------------------------------------
    # Import
    # ------------------------------------------------------------------
    def visitSentenciaImportar(self, ctx: gramatica_v4Parser.SentenciaImportarContext):
        # Por ahora solo verificamos que sea una cadena válida
        # La resolución de imports se hará en tiempo de ejecución
        return None

    # ------------------------------------------------------------------
    # Return
    # ------------------------------------------------------------------
    def visitSentenciaRetorna(self, ctx: gramatica_v4Parser.SentenciaRetornaContext):
        if self.funcion_actual is None:
            self.agregar_error(ctx, "La sentencia 'retorna' solo puede usarse dentro de una función")
            if ctx.expresion():
                self.visit(ctx.expresion())
            return None

        self.encontro_retorno_actual = True

        if self.tipo_retorno_actual == "vacio":
            if ctx.expresion():
                tipo_expr = self.visit(ctx.expresion())
                if tipo_expr != "error":
                    self.agregar_error(
                        ctx,
                        f"La función '{self.funcion_actual}' es de tipo 'vacio' y no debe retornar un valor",
                    )
            return None

        if not ctx.expresion():
            self.agregar_error(
                ctx,
                f"La función '{self.funcion_actual}' debe retornar un valor de tipo '{self.tipo_retorno_actual}'",
            )
            return None

        tipo_expr = self.visit(ctx.expresion())
        if not self.tipos_compatibles(self.tipo_retorno_actual, tipo_expr):
            self.agregar_error(
                ctx,
                f"La función '{self.funcion_actual}' debe retornar '{self.tipo_retorno_actual}', no '{tipo_expr}'",
            )
        return None

    # ------------------------------------------------------------------
    # Llamadas a función
    # ------------------------------------------------------------------
    def _validar_llamada_funcion(self, ctx, usada_como_expresion=False):
        nombre = ctx.IDENTIFICADOR().getText()
        simbolo_func = self.tabla.buscar_funcion(nombre)

        if simbolo_func is None:
            self.agregar_error(ctx, f"La función '{nombre}' no ha sido declarada")
            return "error"

        args = list(ctx.expresion()) if ctx.expresion() else []
        params = simbolo_func.parametros

        if len(args) != len(params):
            self.agregar_error(
                ctx,
                f"La función '{nombre}' esperaba {len(params)} argumento(s), pero recibió {len(args)}",
            )

        for arg_ctx, (nombre_param, tipo_param) in zip(args, params):
            tipo_arg = self.visit(arg_ctx)
            if not self.tipos_compatibles(tipo_param, tipo_arg):
                self.agregar_error(
                    ctx,
                    f"El argumento para el parámetro '{nombre_param}' de la función '{nombre}' debe ser '{tipo_param}', no '{tipo_arg}'",
                )

        if usada_como_expresion and simbolo_func.tipo_retorno == "vacio":
            self.agregar_error(
                ctx,
                f"La función '{nombre}' es de tipo 'vacio' y no puede usarse como expresión",
            )
            return "error"

        return simbolo_func.tipo_retorno

    def visitLlamadaFuncion(self, ctx: gramatica_v4Parser.LlamadaFuncionContext):
        self._validar_llamada_funcion(ctx, usada_como_expresion=False)
        return None

    def visitLlamadaFuncionExpr(self, ctx: gramatica_v4Parser.LlamadaFuncionExprContext):
        return self._validar_llamada_funcion(ctx, usada_como_expresion=True)

    # ------------------------------------------------------------------
    # Expresiones
    # ------------------------------------------------------------------
    def visitNegacionLogica(self, ctx: gramatica_v4Parser.NegacionLogicaContext):
        tipo_expr = self.visit(ctx.expresion())
        if tipo_expr == "error":
            return "error"
        if tipo_expr != "booleano":
            self.agregar_error(
                ctx,
                f"El operador '!' solo puede aplicarse a 'booleano', no a '{tipo_expr}'",
            )
            return "error"
        return "booleano"

    def visitMenosUnario(self, ctx: gramatica_v4Parser.MenosUnarioContext):
        tipo_expr = self.visit(ctx.expresion())
        if tipo_expr == "error":
            return "error"
        if not self.es_tipo_numerico(tipo_expr):
            self.agregar_error(
                ctx,
                f"El menos unario solo puede aplicarse a tipos numéricos, no a '{tipo_expr}'",
            )
            return "error"
        return tipo_expr

    def visitParentesis(self, ctx: gramatica_v4Parser.ParentesisContext):
        return self.visit(ctx.expresion())

    def visitCasting(self, ctx: gramatica_v4Parser.CastingContext):
        tipo_destino = ctx.tipo().getText()
        tipo_origen = self.visit(ctx.expresion())
        if tipo_origen == "error":
            return "error"
        # Conversiones permitidas: entre numéricos, y booleano <-> entero.
        permitidas = {"entero", "flotante", "booleano"}
        if tipo_origen in permitidas and tipo_destino in permitidas:
            return tipo_destino
        if tipo_origen == tipo_destino:
            return tipo_destino
        self.agregar_error(
            ctx,
            f"No se puede convertir (casting) de '{tipo_origen}' a '{tipo_destino}'",
        )
        return "error"

    def visitTernario(self, ctx: gramatica_v4Parser.TernarioContext):
        tipo_cond = self.visit(ctx.cond)
        tipo_ent = self.visit(ctx.ent)
        tipo_sino = self.visit(ctx.sino)
        if "error" in (tipo_cond, tipo_ent, tipo_sino):
            return "error"
        if tipo_cond != "booleano":
            self.agregar_error(
                ctx,
                f"La condición del operador ternario debe ser 'booleano', no '{tipo_cond}'",
            )
            return "error"
        if tipo_ent == tipo_sino:
            return tipo_ent
        if self.es_tipo_numerico(tipo_ent) and self.es_tipo_numerico(tipo_sino):
            return "flotante" if "flotante" in (tipo_ent, tipo_sino) else "entero"
        self.agregar_error(
            ctx,
            f"Las dos ramas del operador ternario deben ser del mismo tipo, no '{tipo_ent}' y '{tipo_sino}'",
        )
        return "error"

    def visitMultiplicacionDivisionModulo(self, ctx: gramatica_v4Parser.MultiplicacionDivisionModuloContext):
        tipo_izq = self.visit(ctx.izq)
        tipo_der = self.visit(ctx.der)

        if tipo_izq == "error" or tipo_der == "error":
            return "error"

        # Operador módulo (%) - solo con enteros
        if ctx.op.type == gramatica_v4Parser.MODULO:
            if tipo_izq != "entero" or tipo_der != "entero":
                self.agregar_error(
                    ctx,
                    f"El operador '%' solo puede usarse con enteros, no con '{tipo_izq}' y '{tipo_der}'",
                )
                return "error"
            return "entero"

        # Multiplicación y división
        if self.es_tipo_numerico(tipo_izq) and self.es_tipo_numerico(tipo_der):
            if ctx.op.type == gramatica_v4Parser.DIVISION and tipo_izq == "entero" and tipo_der == "entero":
                return "entero"
            if tipo_izq == "flotante" or tipo_der == "flotante":
                return "flotante"
            return "entero"

        self.agregar_error(
            ctx,
            f"Los operadores '*' y '/' requieren operandos numéricos, no '{tipo_izq}' y '{tipo_der}'",
        )
        return "error"

    def visitSumaResta(self, ctx: gramatica_v4Parser.SumaRestaContext):
        tipo_izq = self.visit(ctx.izq)
        tipo_der = self.visit(ctx.der)

        if tipo_izq == "error" or tipo_der == "error":
            return "error"

        if ctx.op.type == gramatica_v4Parser.SUMA:
            if tipo_izq == "cadena" and tipo_der == "cadena":
                return "cadena"
            if self.es_tipo_numerico(tipo_izq) and self.es_tipo_numerico(tipo_der):
                if tipo_izq == "flotante" or tipo_der == "flotante":
                    return "flotante"
                return "entero"
            self.agregar_error(
                ctx,
                f"El operador '+' solo admite números o 'cadena' + 'cadena', no '{tipo_izq}' y '{tipo_der}'",
            )
            return "error"

        # Resta
        if self.es_tipo_numerico(tipo_izq) and self.es_tipo_numerico(tipo_der):
            if tipo_izq == "flotante" or tipo_der == "flotante":
                return "flotante"
            return "entero"

        self.agregar_error(
            ctx,
            f"El operador '-' requiere operandos numéricos, no '{tipo_izq}' y '{tipo_der}'",
        )
        return "error"

    def visitRelacional(self, ctx: gramatica_v4Parser.RelacionalContext):
        tipo_izq = self.visit(ctx.izq)
        tipo_der = self.visit(ctx.der)

        if tipo_izq == "error" or tipo_der == "error":
            return "error"

        if ctx.op.type in (gramatica_v4Parser.IGUAL, gramatica_v4Parser.DIFERENTE):
            if tipo_izq == tipo_der:
                return "booleano"
            if self.es_tipo_numerico(tipo_izq) and self.es_tipo_numerico(tipo_der):
                return "booleano"
            self.agregar_error(
                ctx,
                f"No se puede comparar con igualdad tipos incompatibles: '{tipo_izq}' y '{tipo_der}'",
            )
            return "error"

        if self.es_tipo_numerico(tipo_izq) and self.es_tipo_numerico(tipo_der):
            return "booleano"

        self.agregar_error(
            ctx,
            f"Los operadores relacionales '<', '<=', '>' y '>=' requieren operandos numéricos, no '{tipo_izq}' y '{tipo_der}'",
        )
        return "error"

    def visitLogica(self, ctx: gramatica_v4Parser.LogicaContext):
        tipo_izq = self.visit(ctx.izq)
        tipo_der = self.visit(ctx.der)

        if tipo_izq == "error" or tipo_der == "error":
            return "error"

        if tipo_izq == "booleano" and tipo_der == "booleano":
            return "booleano"

        self.agregar_error(
            ctx,
            f"Los operadores lógicos requieren operandos 'booleano', no '{tipo_izq}' y '{tipo_der}'",
        )
        return "error"

    def visitAccesoArregloExpr(self, ctx: gramatica_v4Parser.AccesoArregloExprContext):
        nombre = ctx.accesoArreglo().IDENTIFICADOR().getText()
        simbolo = self.tabla.buscar(nombre)

        if simbolo is None:
            self.agregar_error(ctx, f"El arreglo '{nombre}' no ha sido declarado")
            return "error"

        if not self.es_arreglo(simbolo.tipo):
            self.agregar_error(ctx, f"La variable '{nombre}' no es un arreglo")
            return "error"

        # Verificar que el índice sea entero
        tipo_indice = self.visit(ctx.accesoArreglo().expresion())
        if tipo_indice != "entero" and tipo_indice != "error":
            self.agregar_error(ctx, f"El índice del arreglo debe ser entero, no '{tipo_indice}'")
            return "error"

        return self.obtener_tipo_base(simbolo.tipo)

    # ------------------------------------------------------------------
    # Literales y referencias
    # ------------------------------------------------------------------
    def visitLiteralEntero(self, ctx: gramatica_v4Parser.LiteralEnteroContext):
        return "entero"

    def visitLiteralFlotante(self, ctx: gramatica_v4Parser.LiteralFlotanteContext):
        return "flotante"

    def visitLiteralCadena(self, ctx: gramatica_v4Parser.LiteralCadenaContext):
        return "cadena"

    def visitLiteralVerdadero(self, ctx: gramatica_v4Parser.LiteralVerdaderoContext):
        return "booleano"

    def visitLiteralFalso(self, ctx: gramatica_v4Parser.LiteralFalsoContext):
        return "booleano"

    def visitReferenciaVariable(self, ctx: gramatica_v4Parser.ReferenciaVariableContext):
        nombre = ctx.IDENTIFICADOR().getText()
        simbolo = self.tabla.buscar(nombre)

        if simbolo is None:
            self.agregar_error(ctx, f"La variable '{nombre}' no ha sido declarada")
            return "error"

        return simbolo.tipo

    def visitLiteralArreglo(self, ctx: gramatica_v4Parser.LiteralArregloContext):
        # El tipo se determinará por el contexto de la declaración
        # Por ahora, retornamos un tipo especial
        if ctx.expresion():
            for expr in ctx.expresion():
                self.visit(expr)
        return "arreglo"