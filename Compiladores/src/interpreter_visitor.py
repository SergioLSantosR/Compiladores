# src/interpreter_visitor.py — Persona 4: intérprete (visitor de ejecución)
from __future__ import annotations

from gen.grammar.MiniLangParser import MiniLangParser
from gen.grammar.MiniLangVisitor import MiniLangVisitor


class ReturnSignal(Exception):
    __slots__ = ("value",)

    def __init__(self, value):
        super().__init__()
        self.value = value


class InterpreterVisitor(MiniLangVisitor):
    def __init__(self, stdout_print: bool = True, trace_assignments: bool = False):
        super().__init__()
        self.stdout_print = stdout_print
        self.trace_assignments = trace_assignments
        self.salida: list[str] = []
        self.scopes: list[dict[str, tuple[object, str]]] = []
        self.funciones: dict[str, dict] = {}
        self.function_depth = 0
        self._memoria_final: dict[str, object] | None = None

    @property
    def memoria(self) -> dict[str, object]:
        if self._memoria_final is not None:
            return self._memoria_final
        return self._flatten_scopes()

    def _flatten_scopes(self) -> dict[str, object]:
        merged: dict[str, object] = {}
        for scope in self.scopes:
            for nombre, (valor, _) in scope.items():
                merged[nombre] = valor
        return merged

    def _push_scope(self) -> None:
        self.scopes.append({})

    def _pop_scope(self) -> None:
        self.scopes.pop()

    def _current(self) -> dict[str, tuple[object, str]]:
        return self.scopes[-1]

    def _declare(self, nombre: str, tipo: str, valor: object, ctx) -> None:
        if nombre in self._current():
            raise RuntimeError(f"Redeclaración de '{nombre}' (línea {ctx.start.line}).")
        self._current()[nombre] = (valor, tipo)

    def _assign(self, nombre: str, valor: object, ctx) -> None:
        for scope in reversed(self.scopes):
            if nombre in scope:
                _, esperado = scope[nombre]
                self._asegurar_valor_tipo(esperado, valor, ctx, "asignación")
                scope[nombre] = (valor, esperado)
                if self.trace_assignments:
                    self._imprimir(f"{nombre} = {valor}")
                return
        raise RuntimeError(f"Variable '{nombre}' no declarada (línea {ctx.start.line}).")

    def _lookup(self, nombre: str, ctx) -> object:
        for scope in reversed(self.scopes):
            if nombre in scope:
                return scope[nombre][0]
        raise RuntimeError(f"Variable '{nombre}' no declarada (línea {ctx.start.line}).")

    def _tipo_valor(self, v: object) -> str:
        if isinstance(v, bool):
            return "bool"
        if isinstance(v, int):
            return "int"
        if isinstance(v, float):
            return "float"
        if isinstance(v, str):
            return "string"
        return "desconocido"

    def _asegurar_valor_tipo(self, esperado: str, valor: object, ctx, desc: str) -> None:
        actual = self._tipo_valor(valor)
        if esperado == actual:
            return
        if esperado == "float" and actual == "int":
            return
        raise RuntimeError(
            f"Error de tipos en {desc} (línea {ctx.start.line}): "
            f"se esperaba {esperado}, se obtuvo {actual}."
        )

    def _expect_bool(self, v: object, ctx) -> bool:
        if isinstance(v, bool):
            return v
        raise RuntimeError(f"Se esperaba bool (línea {ctx.start.line}).")

    def _imprimir(self, texto: object) -> None:
        if self.stdout_print:
            print(texto)
        self.salida.append(str(texto))

    def visitPrograma(self, ctx: MiniLangParser.ProgramaContext):
        for fn in ctx.funcion():
            self._registrar_funcion(fn)
        self._push_scope()
        try:
            for s in ctx.bloque().sentencia():
                self.visit(s)
        finally:
            self._memoria_final = self._flatten_scopes()
            self._pop_scope()
        return None

    def _registrar_funcion(self, ctx: MiniLangParser.FuncionContext) -> None:
        nombre = ctx.IDENTIFICADOR().getText()
        if nombre in self.funciones:
            raise RuntimeError(f"Función '{nombre}' redefinida (línea {ctx.start.line}).")
        params: list[tuple[str, str]] = []
        if ctx.listaParametros():
            for p in ctx.listaParametros().parametro():
                params.append((p.IDENTIFICADOR().getText(), p.tipo().getText()))
        tr = ctx.tipoRetorno()
        ret = "void" if tr.VOID() else tr.tipo().getText()
        self.funciones[nombre] = {"params": params, "return": ret, "ctx": ctx}

    def visitFuncion(self, ctx: MiniLangParser.FuncionContext):
        return None

    def visitBloque(self, ctx: MiniLangParser.BloqueContext):
        self._push_scope()
        try:
            for s in ctx.sentencia():
                self.visit(s)
        finally:
            self._pop_scope()
        return None

    def visitDeclaracionVariable(self, ctx: MiniLangParser.DeclaracionVariableContext):
        t = ctx.tipo().getText()
        nombre = ctx.IDENTIFICADOR().getText()
        if ctx.ASIGNACION():
            valor = self.visit(ctx.expresion())
            self._asegurar_valor_tipo(t, valor, ctx, "inicialización")
        else:
            valor = self._default_for_type(t)
        self._declare(nombre, t, valor, ctx)
        return None

    def _default_for_type(self, t: str):
        if t == "int":
            return 0
        if t == "bool":
            return False
        if t == "float":
            return 0.0
        if t == "string":
            return ""
        raise RuntimeError(f"Tipo interno no soportado: {t}")

    def visitAsignacion(self, ctx: MiniLangParser.AsignacionContext):
        nombre = ctx.IDENTIFICADOR().getText()
        valor = self.visit(ctx.expresion())
        self._assign(nombre, valor, ctx)
        return None

    def visitCondicionalSi(self, ctx: MiniLangParser.CondicionalSiContext):
        cond = self._expect_bool(self.visit(ctx.expresion()), ctx)
        if cond:
            self.visit(ctx.bloque(0))
        elif ctx.SINO():
            self.visit(ctx.bloque(1))
        return None

    def visitImprimir(self, ctx: MiniLangParser.ImprimirContext):
        v = self.visit(ctx.expresion())
        self._imprimir(v)
        return None

    def visitMientras(self, ctx: MiniLangParser.MientrasContext):
        while self._expect_bool(self.visit(ctx.expresion()), ctx):
            self.visit(ctx.bloque())
        return None

    def visitPara(self, ctx: MiniLangParser.ParaContext):
        self._push_scope()
        try:
            if ctx.paraInicio():
                self.visit(ctx.paraInicio())
            while True:
                if ctx.expresion() is not None:
                    if not self._expect_bool(self.visit(ctx.expresion()), ctx):
                        break
                self.visit(ctx.bloque())
                if ctx.paraActualizacion():
                    self.visit(ctx.paraActualizacion())
        finally:
            self._pop_scope()
        return None

    def visitParaInicio(self, ctx: MiniLangParser.ParaInicioContext):
        if ctx.tipo():
            t = ctx.tipo().getText()
            nombre = ctx.IDENTIFICADOR().getText()
            val = self.visit(ctx.expresion())
            self._asegurar_valor_tipo(t, val, ctx, "for (inicio)")
            self._declare(nombre, t, val, ctx)
        else:
            nombre = ctx.IDENTIFICADOR().getText()
            val = self.visit(ctx.expresion())
            self._assign(nombre, val, ctx)
        return None

    def visitParaActualizacion(self, ctx: MiniLangParser.ParaActualizacionContext):
        nombre = ctx.IDENTIFICADOR().getText()
        val = self.visit(ctx.expresion())
        self._assign(nombre, val, ctx)
        return None

    def visitRetorno(self, ctx: MiniLangParser.RetornoContext):
        if self.function_depth == 0:
            raise RuntimeError(f"'return' fuera de función (línea {ctx.start.line}).")
        val = None
        if ctx.expresion():
            val = self.visit(ctx.expresion())
        raise ReturnSignal(val)

    def visitLlamadaFuncionStmt(self, ctx: MiniLangParser.LlamadaFuncionStmtContext):
        self._invocar_funcion(ctx.IDENTIFICADOR().getText(), ctx.listaArgumentos(), ctx, allow_void=True)
        return None

    def _args_desde_lista(self, lista_ctx):
        if lista_ctx is None:
            return []
        return list(lista_ctx.expresion())

    def _invocar_funcion(self, nombre: str, lista_args_ctx, ctx_call, *, allow_void: bool):
        info = self.funciones.get(nombre)
        if not info:
            raise RuntimeError(f"Función '{nombre}' no definida (línea {ctx_call.start.line}).")
        fctx: MiniLangParser.FuncionContext = info["ctx"]
        params = info["params"]
        ret_tipo = info["return"]
        expresiones = self._args_desde_lista(lista_args_ctx)
        if len(expresiones) != len(params):
            raise RuntimeError(
                f"Llamada a '{nombre}': se esperaban {len(params)} argumentos, "
                f"hay {len(expresiones)} (línea {ctx_call.start.line})."
            )
        valores = [self.visit(e) for e in expresiones]
        for (pname, pt), val in zip(params, valores):
            self._asegurar_valor_tipo(pt, val, ctx_call, f"argumento de {nombre}")

        if ret_tipo == "void" and not allow_void:
            raise RuntimeError(
                f"La función '{nombre}' es void y no puede usarse como expresión "
                f"(línea {ctx_call.start.line})."
            )

        self._push_scope()
        for (pname, ptipo), val in zip(params, valores):
            self._declare(pname, ptipo, val, ctx_call)

        self.function_depth += 1
        try:
            try:
                self.visit(fctx.bloque())
            except ReturnSignal as rs:
                return self._finalizar_retorno(nombre, ret_tipo, rs, ctx_call)
            if ret_tipo != "void":
                raise RuntimeError(
                    f"Función '{nombre}' debe retornar un valor (línea {ctx_call.start.line})."
                )
            return None
        finally:
            self.function_depth -= 1
            self._pop_scope()

    def _finalizar_retorno(self, nombre: str, ret_tipo: str, rs: ReturnSignal, ctx_call):
        if ret_tipo == "void":
            if rs.value is not None:
                raise RuntimeError(
                    f"Función void '{nombre}' no debe retornar valor (línea {ctx_call.start.line})."
                )
            return None
        if rs.value is None:
            raise RuntimeError(f"Valor de retorno ausente en '{nombre}' (línea {ctx_call.start.line}).")
        self._asegurar_valor_tipo(ret_tipo, rs.value, ctx_call, f"return de {nombre}")
        return rs.value

    def visitNegacionLogica(self, ctx: MiniLangParser.NegacionLogicaContext):
        v = self.visit(ctx.expresion())
        return not self._expect_bool(v, ctx)

    def visitMenosUnario(self, ctx: MiniLangParser.MenosUnarioContext):
        v = self.visit(ctx.expresion())
        if isinstance(v, bool):
            raise RuntimeError(f"- no aplicable a bool (línea {ctx.start.line}).")
        if isinstance(v, str):
            raise RuntimeError(f"- no aplicable a string (línea {ctx.start.line}).")
        return -float(v) if isinstance(v, float) else -int(v)

    def visitParentesis(self, ctx: MiniLangParser.ParentesisContext):
        return self.visit(ctx.expresion())

    def visitMultiplicacionDivision(self, ctx: MiniLangParser.MultiplicacionDivisionContext):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        if isinstance(izq, str) or isinstance(der, str):
            raise RuntimeError(f"* o / no aplican a string (línea {ctx.start.line}).")
        if isinstance(izq, bool) or isinstance(der, bool):
            raise RuntimeError(f"* o / no aplican a bool (línea {ctx.start.line}).")
        a, b = self._num_pair(izq, der)
        if ctx.op.type == MiniLangParser.MULTIPLICACION:
            if isinstance(izq, float) or isinstance(der, float):
                return float(a * b)
            return int(a * b)
        if b == 0:
            raise RuntimeError(f"División por cero (línea {ctx.start.line}).")
        if isinstance(izq, float) or isinstance(der, float):
            return float(a) / float(b)
        return int(izq) // int(der)

    def _num_pair(self, izq, der):
        if isinstance(izq, float) or isinstance(der, float):
            return float(izq), float(der)
        return int(izq), int(der)

    def visitSumaResta(self, ctx: MiniLangParser.SumaRestaContext):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        if isinstance(izq, str) or isinstance(der, str):
            if ctx.op.type != MiniLangParser.SUMA:
                raise RuntimeError(f"'-' no definido para strings (línea {ctx.start.line}).")
            return self._str(izq) + self._str(der)
        if isinstance(izq, bool) or isinstance(der, bool):
            raise RuntimeError(f"+/- no aplican a bool (línea {ctx.start.line}).")
        a, b = self._num_pair(izq, der)
        if ctx.op.type == MiniLangParser.SUMA:
            if isinstance(izq, float) or isinstance(der, float):
                return float(a + b)
            return int(a + b)
        if isinstance(izq, float) or isinstance(der, float):
            return float(a - b)
        return int(a - b)

    def _str(self, v) -> str:
        if isinstance(v, bool):
            return "true" if v else "false"
        return str(v)

    def visitComparacion(self, ctx: MiniLangParser.ComparacionContext):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        op = ctx.op.type
        if type(izq) != type(der) and not (
            isinstance(izq, (int, float)) and isinstance(der, (int, float))
        ):
            raise RuntimeError(f"Tipos incompatibles en comparación (línea {ctx.start.line}).")
        if isinstance(izq, str):
            if op == MiniLangParser.MENOR_QUE:
                return izq < der
            if op == MiniLangParser.MENOR_IGUAL:
                return izq <= der
            if op == MiniLangParser.MAYOR_QUE:
                return izq > der
            if op == MiniLangParser.MAYOR_IGUAL:
                return izq >= der
        a, b = self._num_pair(izq, der) if isinstance(izq, (int, float)) else (izq, der)
        if op == MiniLangParser.MENOR_QUE:
            return a < b
        if op == MiniLangParser.MENOR_IGUAL:
            return a <= b
        if op == MiniLangParser.MAYOR_QUE:
            return a > b
        if op == MiniLangParser.MAYOR_IGUAL:
            return a >= b
        raise RuntimeError("Operador relacional no reconocido.")

    def visitIgualdad(self, ctx: MiniLangParser.IgualdadContext):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        eq = izq == der
        if ctx.op.type == MiniLangParser.IGUAL:
            return eq
        return not eq

    def visitYLogico(self, ctx: MiniLangParser.YLogicoContext):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        return self._expect_bool(izq, ctx) and self._expect_bool(der, ctx)

    def visitOLogico(self, ctx: MiniLangParser.OLogicoContext):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        return self._expect_bool(izq, ctx) or self._expect_bool(der, ctx)

    def visitLiteralEntero(self, ctx: MiniLangParser.LiteralEnteroContext):
        return int(ctx.ENTERO().getText())

    def visitLiteralFlotante(self, ctx: MiniLangParser.LiteralFlotanteContext):
        return float(ctx.FLOTANTE().getText())

    def visitLiteralCadena(self, ctx: MiniLangParser.LiteralCadenaContext):
        raw = ctx.CADENA().getText()
        inner = raw[1:-1]
        return (
            inner.replace("\\n", "\n")
            .replace("\\t", "\t")
            .replace("\\r", "\r")
            .replace("\\\\", "\\")
            .replace('\\"', '"')
        )

    def visitLiteralVerdadero(self, ctx: MiniLangParser.LiteralVerdaderoContext):
        return True

    def visitLiteralFalso(self, ctx: MiniLangParser.LiteralFalsoContext):
        return False

    def visitReferenciaVariable(self, ctx: MiniLangParser.ReferenciaVariableContext):
        return self._lookup(ctx.IDENTIFICADOR().getText(), ctx)

    def visitLlamadaFuncion(self, ctx: MiniLangParser.LlamadaFuncionContext):
        return self._invocar_funcion(
            ctx.IDENTIFICADOR().getText(), ctx.listaArgumentos(), ctx, allow_void=False
        )
