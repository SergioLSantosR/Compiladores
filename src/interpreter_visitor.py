# src/interpreter_visitor.py — Persona 4: intérprete (visitor de ejecución)
from __future__ import annotations

from gen.grammar.gramatica_v3Parser import gramatica_v3Parser
from gen.grammar.gramatica_v3Visitor import gramatica_v3Visitor


class SenalRetorno(Exception):
    __slots__ = ("valor",)

    def __init__(self, valor):
        super().__init__()
        self.valor = valor


class InterpreterVisitor(gramatica_v3Visitor):
    def __init__(self, stdout_print: bool = True, trace_assignments: bool = False):
        super().__init__()
        self.stdout_print = stdout_print
        self.trace_assignments = trace_assignments
        self.salida: list[str] = []
        self.scopes: list[dict[str, tuple[object, str]]] = []
        self.funciones: dict[str, dict] = {}
        self.profundidad_funcion = 0
        self._memoria_final: dict[str, object] | None = None

    @property
    def memoria(self) -> dict[str, object]:
        if self._memoria_final is not None:
            return self._memoria_final
        return self._aplanar_scopes()

    def _aplanar_scopes(self) -> dict[str, object]:
        merged: dict[str, object] = {}
        for scope in self.scopes:
            for nombre, (valor, _) in scope.items():
                merged[nombre] = valor
        return merged

    def _push_scope(self) -> None:
        self.scopes.append({})

    def _pop_scope(self) -> None:
        self.scopes.pop()

    def _actual(self) -> dict[str, tuple[object, str]]:
        return self.scopes[-1]

    def _declarar(self, nombre: str, tipo: str, valor: object, ctx) -> None:
        if nombre in self._actual():
            raise RuntimeError(f"Redeclaración de '{nombre}' (línea {ctx.start.line}).")
        self._actual()[nombre] = (valor, tipo)

    def _asignar(self, nombre: str, valor: object, ctx) -> None:
        for scope in reversed(self.scopes):
            if nombre in scope:
                _, esperado = scope[nombre]
                self._verificar_tipo_valor(esperado, valor, ctx, "asignación")
                scope[nombre] = (valor, esperado)
                if self.trace_assignments:
                    self._imprimir(f"{nombre} = {valor}")
                return
        raise RuntimeError(f"Variable '{nombre}' no declarada (línea {ctx.start.line}).")

    def _buscar(self, nombre: str, ctx) -> object:
        for scope in reversed(self.scopes):
            if nombre in scope:
                return scope[nombre][0]
        raise RuntimeError(f"Variable '{nombre}' no declarada (línea {ctx.start.line}).")

    def _tipo_de_valor(self, v: object) -> str:
        if isinstance(v, bool):
            return "booleano"
        if isinstance(v, int):
            return "entero"
        if isinstance(v, float):
            return "flotante"
        if isinstance(v, str):
            return "cadena"
        return "desconocido"

    def _verificar_tipo_valor(self, esperado: str, valor: object, ctx, desc: str) -> None:
        actual = self._tipo_de_valor(valor)
        if esperado == actual:
            return
        if esperado == "flotante" and actual == "entero":
            return
        raise RuntimeError(
            f"Error de tipos en {desc} (línea {ctx.start.line}): "
            f"se esperaba {esperado}, se obtuvo {actual}."
        )

    def _esperar_booleano(self, v: object, ctx) -> bool:
        if isinstance(v, bool):
            return v
        raise RuntimeError(f"Se esperaba booleano (línea {ctx.start.line}).")

    def _imprimir(self, texto: object) -> None:
        if self.stdout_print:
            print(texto)
        self.salida.append(str(texto))

    # ---- Programa y funciones ----

    def visitPrograma(self, ctx: gramatica_v3Parser.ProgramaContext):
        for fn in ctx.funcionDeclaracion():
            self._registrar_funcion(fn)
        self._push_scope()
        try:
            for s in ctx.bloque().sentencia():
                self.visit(s)
        finally:
            self._memoria_final = self._aplanar_scopes()
            self._pop_scope()
        return None

    def _registrar_funcion(self, ctx: gramatica_v3Parser.FuncionDeclaracionContext) -> None:
        nombre = ctx.IDENTIFICADOR().getText()
        if nombre in self.funciones:
            raise RuntimeError(f"Función '{nombre}' redefinida (línea {ctx.start.line}).")
        params: list[tuple[str, str]] = []
        if ctx.parametros():
            for p in ctx.parametros().parametro():
                params.append((p.IDENTIFICADOR().getText(), p.tipo().getText()))
        tipo_retorno = "vacio"
        if ctx.tipo():
            tipo_retorno = ctx.tipo().getText()
        self.funciones[nombre] = {"params": params, "return": tipo_retorno, "ctx": ctx}

    def visitFuncionDeclaracion(self, ctx: gramatica_v3Parser.FuncionDeclaracionContext):
        return None

    def visitBloque(self, ctx: gramatica_v3Parser.BloqueContext):
        self._push_scope()
        try:
            for s in ctx.sentencia():
                self.visit(s)
        finally:
            self._pop_scope()
        return None

    # ---- Declaraciones y asignaciones ----

    def visitDeclaracionVariable(self, ctx: gramatica_v3Parser.DeclaracionVariableContext):
        t = ctx.tipo().getText()
        nombre = ctx.IDENTIFICADOR().getText()
        if ctx.expresion():
            valor = self.visit(ctx.expresion())
            self._verificar_tipo_valor(t, valor, ctx, "inicialización")
        else:
            valor = self._valor_por_defecto(t)
        self._declarar(nombre, t, valor, ctx)
        return None

    def _valor_por_defecto(self, t: str):
        if t == "entero":
            return 0
        if t == "booleano":
            return False
        if t == "flotante":
            return 0.0
        if t == "cadena":
            return ""
        raise RuntimeError(f"Tipo interno no soportado: {t}")

    def visitAsignacion(self, ctx: gramatica_v3Parser.AsignacionContext):
        nombre = ctx.IDENTIFICADOR().getText()
        valor = self.visit(ctx.expresion())
        self._asignar(nombre, valor, ctx)
        return None

    # ---- Condicional, ciclos, impresión ----

    def visitCondicionalSi(self, ctx: gramatica_v3Parser.CondicionalSiContext):
        cond = self._esperar_booleano(self.visit(ctx.expresion()), ctx)
        if cond:
            self.visit(ctx.bloque(0))
        elif ctx.SINO():
            self.visit(ctx.bloque(1))
        return None

    def visitImpresion(self, ctx: gramatica_v3Parser.ImpresionContext):
        v = self.visit(ctx.expresion())
        self._imprimir(v)
        return None

    def visitCicloMientras(self, ctx: gramatica_v3Parser.CicloMientrasContext):
        while self._esperar_booleano(self.visit(ctx.expresion()), ctx):
            self.visit(ctx.bloque())
        return None

    def visitInicializacionPara(self, ctx: gramatica_v3Parser.InicializacionParaContext):
        t = ctx.tipo().getText()
        nombre = ctx.IDENTIFICADOR().getText()
        val = self.visit(ctx.expresion())
        self._verificar_tipo_valor(t, val, ctx, "inicialización para")
        self._declarar(nombre, t, val, ctx)
        return None

    def visitAsignacionPara(self, ctx: gramatica_v3Parser.AsignacionParaContext):
        nombre = ctx.IDENTIFICADOR().getText()
        val = self.visit(ctx.expresion())
        self._asignar(nombre, val, ctx)
        return None

    def visitActualizacionPara(self, ctx: gramatica_v3Parser.ActualizacionParaContext):
        nombre = ctx.IDENTIFICADOR().getText()
        val = self.visit(ctx.expresion())
        self._asignar(nombre, val, ctx)
        return None

    def visitCicloPara(self, ctx: gramatica_v3Parser.CicloParaContext):
        self._push_scope()
        try:
            if ctx.inicializacionPara():
                self.visit(ctx.inicializacionPara())
            elif ctx.asignacionPara():
                self.visit(ctx.asignacionPara())
            while True:
                if ctx.cond:
                    if not self._esperar_booleano(self.visit(ctx.cond), ctx):
                        break
                self.visit(ctx.bloque())
                if ctx.actualizacionPara():
                    self.visit(ctx.actualizacionPara())
        finally:
            self._pop_scope()
        return None

    # ---- Retorno ----

    def visitSentenciaRetorna(self, ctx: gramatica_v3Parser.SentenciaRetornaContext):
        if self.profundidad_funcion == 0:
            raise RuntimeError(f"'retorna' fuera de función (línea {ctx.start.line}).")
        val = None
        if ctx.expresion():
            val = self.visit(ctx.expresion())
        raise SenalRetorno(val)

    # ---- Llamadas a funciones ----

    def visitLlamadaFuncion(self, ctx: gramatica_v3Parser.LlamadaFuncionContext):
        self._invocar_funcion(ctx.IDENTIFICADOR().getText(), ctx.expresion(), ctx, permitir_vacio=True)
        return None

    def visitLlamadaFuncionExpr(self, ctx: gramatica_v3Parser.LlamadaFuncionExprContext):
        return self._invocar_funcion(ctx.IDENTIFICADOR().getText(), ctx.expresion(), ctx, permitir_vacio=False)

    def _invocar_funcion(self, nombre: str, lista_expr, ctx_call, *, permitir_vacio: bool):
        info = self.funciones.get(nombre)
        if not info:
            raise RuntimeError(f"Función '{nombre}' no definida (línea {ctx_call.start.line}).")
        fctx: gramatica_v3Parser.FuncionDeclaracionContext = info["ctx"]
        params = info["params"]
        tipo_ret = info["return"]
        expresiones = list(lista_expr) if lista_expr else []
        if len(expresiones) != len(params):
            raise RuntimeError(
                f"Llamada a '{nombre}': se esperaban {len(params)} argumentos, "
                f"hay {len(expresiones)} (línea {ctx_call.start.line})."
            )
        valores = [self.visit(e) for e in expresiones]
        for (pnombre, ptipo), val in zip(params, valores):
            self._verificar_tipo_valor(ptipo, val, ctx_call, f"argumento de {nombre}")

        if tipo_ret == "vacio" and not permitir_vacio:
            raise RuntimeError(
                f"La función '{nombre}' es de tipo 'vacio' y no puede usarse como expresión "
                f"(línea {ctx_call.start.line})."
            )

        self._push_scope()
        for (pnombre, ptipo), val in zip(params, valores):
            self._declarar(pnombre, ptipo, val, ctx_call)

        self.profundidad_funcion += 1
        try:
            try:
                self.visit(fctx.bloque())
            except SenalRetorno as sr:
                return self._finalizar_retorno(nombre, tipo_ret, sr, ctx_call)
            if tipo_ret != "vacio":
                raise RuntimeError(
                    f"Función '{nombre}' debe retornar un valor (línea {ctx_call.start.line})."
                )
            return None
        finally:
            self.profundidad_funcion -= 1
            self._pop_scope()

    def _finalizar_retorno(self, nombre: str, tipo_ret: str, sr: SenalRetorno, ctx_call):
        if tipo_ret == "vacio":
            if sr.valor is not None:
                raise RuntimeError(
                    f"Función vacio '{nombre}' no debe retornar valor (línea {ctx_call.start.line})."
                )
            return None
        if sr.valor is None:
            raise RuntimeError(f"Valor de retorno ausente en '{nombre}' (línea {ctx_call.start.line}).")
        self._verificar_tipo_valor(tipo_ret, sr.valor, ctx_call, f"retorno de {nombre}")
        return sr.valor

    # ---- Expresiones ----

    def visitNegacionLogica(self, ctx: gramatica_v3Parser.NegacionLogicaContext):
        v = self.visit(ctx.expresion())
        return not self._esperar_booleano(v, ctx)

    def visitMenosUnario(self, ctx: gramatica_v3Parser.MenosUnarioContext):
        v = self.visit(ctx.expresion())
        if isinstance(v, bool):
            raise RuntimeError(f"Menos unario no aplicable a booleano (línea {ctx.start.line}).")
        if isinstance(v, str):
            raise RuntimeError(f"Menos unario no aplicable a cadena (línea {ctx.start.line}).")
        return -float(v) if isinstance(v, float) else -int(v)

    def visitParentesis(self, ctx: gramatica_v3Parser.ParentesisContext):
        return self.visit(ctx.expresion())

    def visitMultiplicacionDivision(self, ctx: gramatica_v3Parser.MultiplicacionDivisionContext):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        if isinstance(izq, str) or isinstance(der, str):
            raise RuntimeError(f"* o / no aplican a cadena (línea {ctx.start.line}).")
        if isinstance(izq, bool) or isinstance(der, bool):
            raise RuntimeError(f"* o / no aplican a booleano (línea {ctx.start.line}).")
        a, b = self._par_numerico(izq, der)
        if ctx.op.type == gramatica_v3Parser.MULTIPLICACION:
            if isinstance(izq, float) or isinstance(der, float):
                return float(a * b)
            return int(a * b)
        if b == 0:
            raise RuntimeError(f"División por cero (línea {ctx.start.line}).")
        if isinstance(izq, float) or isinstance(der, float):
            return float(a) / float(b)
        return int(izq) // int(der)

    def _par_numerico(self, izq, der):
        if isinstance(izq, float) or isinstance(der, float):
            return float(izq), float(der)
        return int(izq), int(der)

    def visitSumaResta(self, ctx: gramatica_v3Parser.SumaRestaContext):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        if isinstance(izq, str) or isinstance(der, str):
            if ctx.op.type != gramatica_v3Parser.SUMA:
                raise RuntimeError(f"'-' no definido para cadenas (línea {ctx.start.line}).")
            return self._a_cadena(izq) + self._a_cadena(der)
        if isinstance(izq, bool) or isinstance(der, bool):
            raise RuntimeError(f"+/- no aplican a booleano (línea {ctx.start.line}).")
        a, b = self._par_numerico(izq, der)
        if ctx.op.type == gramatica_v3Parser.SUMA:
            if isinstance(izq, float) or isinstance(der, float):
                return float(a + b)
            return int(a + b)
        if isinstance(izq, float) or isinstance(der, float):
            return float(a - b)
        return int(a - b)

    def _a_cadena(self, v) -> str:
        if isinstance(v, bool):
            return "verdadero" if v else "falso"
        return str(v)

    def visitRelacional(self, ctx: gramatica_v3Parser.RelacionalContext):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        op = ctx.op.type
        if op in (gramatica_v3Parser.IGUAL, gramatica_v3Parser.DIFERENTE):
            eq = izq == der
            return eq if op == gramatica_v3Parser.IGUAL else not eq
        if type(izq) != type(der) and not (
            isinstance(izq, (int, float)) and isinstance(der, (int, float))
        ):
            raise RuntimeError(f"Tipos incompatibles en comparación (línea {ctx.start.line}).")
        if isinstance(izq, str):
            if op == gramatica_v3Parser.MENOR_QUE: return izq < der
            if op == gramatica_v3Parser.MENOR_IGUAL: return izq <= der
            if op == gramatica_v3Parser.MAYOR_QUE: return izq > der
            if op == gramatica_v3Parser.MAYOR_IGUAL: return izq >= der
        a, b = self._par_numerico(izq, der) if isinstance(izq, (int, float)) else (izq, der)
        if op == gramatica_v3Parser.MENOR_QUE: return a < b
        if op == gramatica_v3Parser.MENOR_IGUAL: return a <= b
        if op == gramatica_v3Parser.MAYOR_QUE: return a > b
        if op == gramatica_v3Parser.MAYOR_IGUAL: return a >= b
        raise RuntimeError("Operador relacional no reconocido.")

    def visitLogica(self, ctx: gramatica_v3Parser.LogicaContext):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        if ctx.op.type == gramatica_v3Parser.Y_LOGICO:
            return self._esperar_booleano(izq, ctx) and self._esperar_booleano(der, ctx)
        return self._esperar_booleano(izq, ctx) or self._esperar_booleano(der, ctx)

    # ---- Literales y referencias ----

    def visitLiteralEntero(self, ctx: gramatica_v3Parser.LiteralEnteroContext):
        return int(ctx.ENTERO().getText())

    def visitLiteralFlotante(self, ctx: gramatica_v3Parser.LiteralFlotanteContext):
        return float(ctx.FLOTANTE().getText())

    def visitLiteralCadena(self, ctx: gramatica_v3Parser.LiteralCadenaContext):
        raw = ctx.CADENA().getText()
        inner = raw[1:-1]
        return (
            inner.replace("\\n", "\n")
            .replace("\\t", "\t")
            .replace("\\r", "\r")
            .replace("\\\\", "\\")
            .replace('\\"', '"')
        )

    def visitLiteralVerdadero(self, ctx: gramatica_v3Parser.LiteralVerdaderoContext):
        return True

    def visitLiteralFalso(self, ctx: gramatica_v3Parser.LiteralFalsoContext):
        return False

    def visitReferenciaVariable(self, ctx: gramatica_v3Parser.ReferenciaVariableContext):
        return self._buscar(ctx.IDENTIFICADOR().getText(), ctx)
