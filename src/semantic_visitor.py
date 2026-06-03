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
        self.structs_globales = {}  # NUEVO: Para almacenar structs {nombre: {campo: tipo}}

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

    def es_struct(self, tipo):
        return tipo is not None and tipo in self.structs_globales

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
        # Primera pasada: registrar todas las funciones
        for func_ctx in ctx.funcionDeclaracion():
            self._registrar_funcion(func_ctx)
        # Segunda pasada: analizar los cuerpos de funciones
        for func_ctx in ctx.funcionDeclaracion():
            self._analizar_funcion(func_ctx)
        # Analizar bloque principal
        self.visit(ctx.bloque())
        return None

    def _registrar_funcion(self, ctx: gramatica_v4Parser.FuncionDeclaracionContext):
        nombre = ctx.IDENTIFICADOR().getText()
        tipo_retorno = self.tipo_desde_ctx(ctx.tipo())
        if ctx.VOID():
            tipo_retorno = "vacio"
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
    # NUEVO: Sentencia Struct
    # ------------------------------------------------------------------
    def visitSentenciaStruct(self, ctx: gramatica_v4Parser.SentenciaStructContext):
        nombre_struct = ctx.IDENTIFICADOR().getText()
        
        if nombre_struct in self.structs_globales:
            self.agregar_error(ctx, f"El struct '{nombre_struct}' ya fue declarado")
            return None
        
        campos = {}
        for campo_ctx in ctx.declaracionCampoStruct():
            tipo_campo = campo_ctx.tipo().getText()
            nombre_campo = campo_ctx.IDENTIFICADOR().getText()
            if nombre_campo in campos:
                self.agregar_error(campo_ctx, f"El campo '{nombre_campo}' ya fue declarado en el struct '{nombre_struct}'")
            else:
                campos[nombre_campo] = tipo_campo
        
        self.structs_globales[nombre_struct] = campos
        return None

    # ------------------------------------------------------------------
    # Declaraciones y asignaciones
    # ------------------------------------------------------------------
    def visitDeclaracionVariable(self, ctx: gramatica_v4Parser.DeclaracionVariableContext):
        # Verificar si es variable de tipo struct
        if ctx.tipoStruct():
            tipo_struct = ctx.tipoStruct().getText()
            nombre = ctx.IDENTIFICADOR().getText()
            
            if tipo_struct not in self.structs_globales:
                self.agregar_error(ctx, f"El struct '{tipo_struct}' no ha sido declarado")
                return None
            
            creada = self.tabla.declarar(
                nombre,
                tipo_struct,  # Almacenar como nombre del struct
                ctx.start.line,
                ctx.start.column,
            )
            
            if creada is None:
                self.agregar_error(
                    ctx,
                    f"La variable '{nombre}' ya fue declarada en este ámbito",
                )
            return None
        
        # Variable normal o arreglo
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
        # Verificar si es asignación a struct (struct.campo)
        if ctx.accesoStruct():
            acceso = ctx.accesoStruct()
            nombre_struct = acceso.IDENTIFICADOR(0).getText()
            nombre_campo = acceso.IDENTIFICADOR(1).getText()
            
            simbolo = self.tabla.buscar(nombre_struct)
            if simbolo is None:
                self.agregar_error(ctx, f"La variable '{nombre_struct}' no ha sido declarada")
                return None
            
            # Verificar que el tipo sea un struct
            if simbolo.tipo not in self.structs_globales:
                self.agregar_error(ctx, f"La variable '{nombre_struct}' no es un struct")
                return None
            
            # Verificar que el campo exista
            campos = self.structs_globales[simbolo.tipo]
            if nombre_campo not in campos:
                self.agregar_error(ctx, f"El campo '{nombre_campo}' no existe en el struct '{simbolo.tipo}'")
                return None
            
            # Verificar tipo del valor asignado
            tipo_expr = self.visit(ctx.expresion())
            if not self.tipos_compatibles(campos[nombre_campo], tipo_expr):
                self.agregar_error(
                    ctx,
                    f"No se puede asignar '{tipo_expr}' al campo '{nombre_campo}' de tipo '{campos[nombre_campo]}'",
                )
            return None
        
        # Asignación normal
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

    def visitImpresion(self, ctx: gramatica_v4Parser.ImpresionContext):
        self.visit(ctx.expresion())
        return None

    # ------------------------------------------------------------------
    # Break y Continue
    # ------------------------------------------------------------------
    def visitSentenciaBreak(self, ctx: gramatica_v4Parser.SentenciaBreakContext):
        if self.en_ciclo == 0:
            self.agregar_error(ctx, "La sentencia 'romper' solo puede usarse dentro de un ciclo")
        return None

    def visitSentenciaContinue(self, ctx: gramatica_v4Parser.SentenciaContinueContext):
        if self.en_ciclo == 0:
            self.agregar_error(ctx, "La sentencia 'continuar' solo puede usarse dentro de un ciclo")
        return None

    # ------------------------------------------------------------------
    # Import
    # ------------------------------------------------------------------
    def visitSentenciaImportar(self, ctx: gramatica_v4Parser.SentenciaImportarContext):
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
    # Operador Ternario
    # ------------------------------------------------------------------
    def visitOperadorTernario(self, ctx: gramatica_v4Parser.OperadorTernarioContext):
        tipo_cond = self.visit(ctx.condicion)
        if tipo_cond != "booleano" and tipo_cond != "error":
            self.agregar_error(
                ctx,
                f"La condición del operador ternario debe ser 'booleano', no '{tipo_cond}'",
            )
        
        tipo_verdadero = self.visit(ctx.verdadero)
        tipo_falso = self.visit(ctx.falso)
        
        if tipo_verdadero == "error" or tipo_falso == "error":
            return "error"
        
        if tipo_verdadero == tipo_falso:
            return tipo_verdadero
        
        if self.es_tipo_numerico(tipo_verdadero) and self.es_tipo_numerico(tipo_falso):
            if tipo_verdadero == "flotante" or tipo_falso == "flotante":
                return "flotante"
            return "entero"
        
        self.agregar_error(
            ctx,
            f"Tipos incompatibles en operador ternario: '{tipo_verdadero}' y '{tipo_falso}'",
        )
        return "error"

    # ------------------------------------------------------------------
    # Casting Explícito
    # ------------------------------------------------------------------
    def visitCastingExplicito(self, ctx: gramatica_v4Parser.CastingExplicitoContext):
        tipo_destino = ctx.tipo().getText()
        tipo_origen = self.visit(ctx.expresion())
        
        if tipo_origen == "error":
            return "error"
        
        # Castings válidos
        castings_validos = {
            "entero": ["flotante", "booleano"],
            "flotante": ["entero"],
            "booleano": ["entero"],
        }
        
        if tipo_destino == tipo_origen:
            return tipo_destino
        
        if tipo_origen in castings_validos and tipo_destino in castings_validos[tipo_origen]:
            return tipo_destino
        
        self.agregar_error(
            ctx,
            f"No se puede hacer casting de '{tipo_origen}' a '{tipo_destino}'",
        )
        return "error"

    # ------------------------------------------------------------------
    # Switch/Case
    # ------------------------------------------------------------------
    def visitSentenciaSwitch(self, ctx: gramatica_v4Parser.SentenciaSwitchContext):
        tipo_control = self.visit(ctx.expresion())
        
        if tipo_control != "entero" and tipo_control != "error":
            self.agregar_error(
                ctx,
                f"La expresión de 'switch' debe ser entero, no '{tipo_control}'",
            )
        
        # Verificar que no haya casos duplicados
        valores_vistos = set()
        for caso_ctx in ctx.caso():
            valor_expr = caso_ctx.expresion()
            # Evaluar el valor del case (debería ser constante)
            tipo_valor = self.visit(valor_expr)
            if tipo_valor != "entero" and tipo_valor != "error":
                self.agregar_error(
                    valor_expr,
                    f"Los valores de 'case' deben ser enteros, no '{tipo_valor}'",
                )
        
        return None

    def visitCaso(self, ctx: gramatica_v4Parser.CasoContext):
        for sentencia in ctx.sentencia():
            self.visit(sentencia)
        return None

    def visitCasoDefault(self, ctx: gramatica_v4Parser.CasoDefaultContext):
        for sentencia in ctx.sentencia():
            self.visit(sentencia)
        return None

    # ------------------------------------------------------------------
    # Acceso a Struct
    # ------------------------------------------------------------------
    def visitAccesoStruct(self, ctx: gramatica_v4Parser.AccesoStructContext):
        nombre_struct = ctx.IDENTIFICADOR(0).getText()
        nombre_campo = ctx.IDENTIFICADOR(1).getText()
        
        simbolo = self.tabla.buscar(nombre_struct)
        if simbolo is None:
            self.agregar_error(ctx, f"La variable '{nombre_struct}' no ha sido declarada")
            return "error"
        
        if simbolo.tipo not in self.structs_globales:
            self.agregar_error(ctx, f"La variable '{nombre_struct}' no es un struct")
            return "error"
        
        campos = self.structs_globales[simbolo.tipo]
        if nombre_campo not in campos:
            self.agregar_error(ctx, f"El campo '{nombre_campo}' no existe en el struct '{simbolo.tipo}'")
            return "error"
        
        return campos[nombre_campo]

    def visitAccesoStructExpr(self, ctx: gramatica_v4Parser.AccesoStructExprContext):
        return self.visit(ctx.accesoStruct())

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

    def visitLiteralArreglo(self, ctx: gramatica_v4Parser.LiteralArregloContext):
        if ctx.expresion():
            for expr in ctx.expresion():
                self.visit(expr)
        return "arreglo"

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

    def visitLiteralStruct(self, ctx: gramatica_v4Parser.LiteralStructContext):
        if ctx.expresion():
            for expr in ctx.expresion():
                self.visit(expr)
        return "struct"

    def visitReferenciaVariable(self, ctx: gramatica_v4Parser.ReferenciaVariableContext):
        nombre = ctx.IDENTIFICADOR().getText()
        simbolo = self.tabla.buscar(nombre)

        if simbolo is None:
            self.agregar_error(ctx, f"La variable '{nombre}' no ha sido declarada")
            return "error"

        return simbolo.tipo