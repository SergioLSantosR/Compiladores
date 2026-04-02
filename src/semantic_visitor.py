from gen.grammar.MiniLangParser import MiniLangParser
from gen.grammar.MiniLangVisitor import MiniLangVisitor
from src.symbol_table import TablaSimbolos


class SemanticVisitor(MiniLangVisitor):
    def __init__(self):
        super().__init__()
        self.tabla = TablaSimbolos()
        self.errores = []
        self.funcion_actual = None
        self.tipo_retorno_actual = None
        self.encontro_retorno_actual = False

    # ---------------------------------------------------------
    # Utilidades
    # ---------------------------------------------------------
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

    def _visitar_bloque(self, ctx_bloque, crear_ambito=True):
        if crear_ambito:
            self.tabla.entrar_ambito()

        for sentencia in ctx_bloque.sentencia():
            self.visit(sentencia)

        if crear_ambito:
            self.tabla.salir_ambito()

        return None

    # ---------------------------------------------------------
    # Programa y funciones
    # ---------------------------------------------------------
    def visitPrograma(self, ctx: MiniLangParser.ProgramaContext):
        # Primera pasada: registrar todas las funciones
        for func_ctx in ctx.funcionDeclaracion():
            self._registrar_funcion(func_ctx)

        # Segunda pasada: analizar los cuerpos de funciones
        for func_ctx in ctx.funcionDeclaracion():
            self._analizar_funcion(func_ctx)

        # Analizar bloque principal
        self.visit(ctx.bloque())
        return None

    def _registrar_funcion(self, ctx: MiniLangParser.FuncionDeclaracionContext):
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

    def _analizar_funcion(self, ctx: MiniLangParser.FuncionDeclaracionContext):
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

        # Importante: NO crear otro scope extra para el bloque de la función
        self._visitar_bloque(ctx.bloque(), crear_ambito=False)

        if (
            self.tipo_retorno_actual != "vacio"
            and not self.encontro_retorno_actual
        ):
            self.agregar_error(
                ctx,
                f"La función '{nombre}' debe retornar un valor de tipo '{self.tipo_retorno_actual}'",
            )

        self.tabla.salir_ambito()

        self.funcion_actual = funcion_anterior
        self.tipo_retorno_actual = tipo_retorno_anterior
        self.encontro_retorno_actual = retorno_anterior
        return None

    def visitFuncionDeclaracion(self, ctx: MiniLangParser.FuncionDeclaracionContext):
        # No se usa directamente porque programa hace dos pasadas.
        return None

    # ---------------------------------------------------------
    # Bloques
    # ---------------------------------------------------------
    def visitBloque(self, ctx: MiniLangParser.BloqueContext):
        return self._visitar_bloque(ctx, crear_ambito=True)

    # ---------------------------------------------------------
    # Declaraciones y asignaciones
    # ---------------------------------------------------------
    def visitDeclaracionVariable(self, ctx: MiniLangParser.DeclaracionVariableContext):
        tipo = ctx.tipo().getText()
        nombre = ctx.IDENTIFICADOR().getText()

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

    def visitAsignacion(self, ctx: MiniLangParser.AsignacionContext):
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

    def visitInicializacionPara(self, ctx: MiniLangParser.InicializacionParaContext):
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

    def visitAsignacionPara(self, ctx: MiniLangParser.AsignacionParaContext):
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

    def visitActualizacionPara(self, ctx: MiniLangParser.ActualizacionParaContext):
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

    # ---------------------------------------------------------
    # Condicionales, ciclos e impresión
    # ---------------------------------------------------------
    def visitCondicionalSi(self, ctx: MiniLangParser.CondicionalSiContext):
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

    def visitCicloMientras(self, ctx: MiniLangParser.CicloMientrasContext):
        tipo_cond = self.visit(ctx.expresion())

        if tipo_cond != "booleano" and tipo_cond != "error":
            self.agregar_error(
                ctx,
                f"La condición del 'mientras' debe ser de tipo 'booleano', no '{tipo_cond}'",
            )

        self.visit(ctx.bloque())
        return None

    def visitCicloPara(self, ctx: MiniLangParser.CicloParaContext):
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
        return None

    def visitImpresion(self, ctx: MiniLangParser.ImpresionContext):
        self.visit(ctx.expresion())
        return None

    # ---------------------------------------------------------
    # Return
    # ---------------------------------------------------------
    def visitSentenciaRetorna(self, ctx: MiniLangParser.SentenciaRetornaContext):
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

    # ---------------------------------------------------------
    # Llamadas a función
    # ---------------------------------------------------------
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

    def visitLlamadaFuncion(self, ctx: MiniLangParser.LlamadaFuncionContext):
        self._validar_llamada_funcion(ctx, usada_como_expresion=False)
        return None

    def visitLlamadaFuncionExpr(self, ctx: MiniLangParser.LlamadaFuncionExprContext):
        return self._validar_llamada_funcion(ctx, usada_como_expresion=True)

    # ---------------------------------------------------------
    # Expresiones
    # ---------------------------------------------------------
    def visitNegacionLogica(self, ctx: MiniLangParser.NegacionLogicaContext):
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

    def visitMenosUnario(self, ctx: MiniLangParser.MenosUnarioContext):
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

    def visitParentesis(self, ctx: MiniLangParser.ParentesisContext):
        return self.visit(ctx.expresion())

    def visitMultiplicacionDivision(self, ctx: MiniLangParser.MultiplicacionDivisionContext):
        tipo_izq = self.visit(ctx.izq)
        tipo_der = self.visit(ctx.der)

        if tipo_izq == "error" or tipo_der == "error":
            return "error"

        if self.es_tipo_numerico(tipo_izq) and self.es_tipo_numerico(tipo_der):
            if (
                ctx.op.type == MiniLangParser.DIVISION
                and tipo_izq == "entero"
                and tipo_der == "entero"
            ):
                return "entero"

            if tipo_izq == "flotante" or tipo_der == "flotante":
                return "flotante"

            return "entero"

        self.agregar_error(
            ctx,
            f"Los operadores '*' y '/' requieren operandos numéricos, no '{tipo_izq}' y '{tipo_der}'",
        )
        return "error"

    def visitSumaResta(self, ctx: MiniLangParser.SumaRestaContext):
        tipo_izq = self.visit(ctx.izq)
        tipo_der = self.visit(ctx.der)

        if tipo_izq == "error" or tipo_der == "error":
            return "error"

        if ctx.op.type == MiniLangParser.SUMA:
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

    def visitRelacional(self, ctx: MiniLangParser.RelacionalContext):
        tipo_izq = self.visit(ctx.izq)
        tipo_der = self.visit(ctx.der)

        if tipo_izq == "error" or tipo_der == "error":
            return "error"

        if ctx.op.type in (MiniLangParser.IGUAL, MiniLangParser.DIFERENTE):
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

    def visitLogica(self, ctx: MiniLangParser.LogicaContext):
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

    # ---------------------------------------------------------
    # Literales y referencias
    # ---------------------------------------------------------
    def visitLiteralEntero(self, ctx: MiniLangParser.LiteralEnteroContext):
        return "entero"

    def visitLiteralFlotante(self, ctx: MiniLangParser.LiteralFlotanteContext):
        return "flotante"

    def visitLiteralCadena(self, ctx: MiniLangParser.LiteralCadenaContext):
        return "cadena"

    def visitLiteralVerdadero(self, ctx: MiniLangParser.LiteralVerdaderoContext):
        return "booleano"

    def visitLiteralFalso(self, ctx: MiniLangParser.LiteralFalsoContext):
        return "booleano"

    def visitReferenciaVariable(self, ctx: MiniLangParser.ReferenciaVariableContext):
        nombre = ctx.IDENTIFICADOR().getText()
        simbolo = self.tabla.buscar(nombre)

        if simbolo is None:
            self.agregar_error(ctx, f"La variable '{nombre}' no ha sido declarada")
            return "error"

        return simbolo.tipo