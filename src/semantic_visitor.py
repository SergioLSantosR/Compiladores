# src/semantic_visitor.py
from __future__ import annotations

from typing import List, Optional

from src.ast_nodes import (
    AssignNode,
    BinaryExpr,
    BlockNode,
    BoolLiteral,
    CallExpr,
    DeclareNode,
    ExprNode,
    FuncDefNode,
    IfNode,
    IntLiteral,
    PrintNode,
    ProgramNode,
    ReturnNode,
    UnaryExpr,
    VarRef,
    WhileNode,
)


class SemanticVisitor:
    """Validación semántica con ámbitos anidados y funciones."""

    def __init__(self):
        self.errors: List[str] = []
        self.scopes: List[dict[str, str]] = []
        self.func_defs: dict[str, FuncDefNode] = {}
        self.in_function = False
        self.current_return_type: Optional[str] = None

    def _col_u(self, col: int) -> int:
        return col + 1

    def _err(self, line: int, col: int, msg: str) -> None:
        self.errors.append(
            f"[Error Semántico] Línea {line}, Columna {self._col_u(col)}: {msg}"
        )

    def has_errors(self) -> bool:
        return len(self.errors) > 0

    def report(self) -> str:
        return "\n".join(self.errors)

    def _push_scope(self) -> None:
        self.scopes.append({})

    def _pop_scope(self) -> None:
        self.scopes.pop()

    def _declare(self, name: str, t: str, line: int, col: int) -> bool:
        if name in self.scopes[-1]:
            self._err(line, col, f"Redeclaración de variable '{name}'.")
            return False
        self.scopes[-1][name] = t
        return True

    def _lookup_type(self, name: str) -> Optional[str]:
        for s in reversed(self.scopes):
            if name in s:
                return s[name]
        return None

    def analyze(self, program: ProgramNode) -> None:
        self.errors.clear()
        self.scopes.clear()
        self.func_defs.clear()
        self.in_function = False
        self.current_return_type = None

        for fd in program.functions:
            if fd.name in self.func_defs:
                self._err(fd.line, fd.col, f"Función '{fd.name}' declarada más de una vez.")
                continue
            pnames = [pn for _, pn in fd.params]
            if len(pnames) != len(set(pnames)):
                self._err(fd.line, fd.col, f"Parámetros duplicados en función '{fd.name}'.")
            self.func_defs[fd.name] = fd

        for fd in self.func_defs.values():
            self._analyze_function(fd)

        self._push_scope()
        try:
            for stmt in program.main_statements:
                self._visit_stmt(stmt)
        finally:
            self._pop_scope()

    def _analyze_function(self, fd: FuncDefNode) -> None:
        was_in = self.in_function
        prev_ret = self.current_return_type
        self.in_function = True
        self.current_return_type = fd.return_type
        self._push_scope()
        try:
            for pt, pn in fd.params:
                self._declare(pn, pt, fd.line, fd.col)
            self._visit_block(fd.body)
        finally:
            self._pop_scope()
            self.in_function = was_in
            self.current_return_type = prev_ret

    def _visit_block(self, block: BlockNode) -> None:
        self._push_scope()
        try:
            for stmt in block.statements:
                self._visit_stmt(stmt)
        finally:
            self._pop_scope()

    def _visit_stmt(self, stmt) -> None:
        if isinstance(stmt, DeclareNode):
            self._declare(stmt.name, stmt.type_name, stmt.line, stmt.col)
        elif isinstance(stmt, AssignNode):
            lt = self._lookup_type(stmt.name)
            if lt is None:
                self._err(stmt.line, stmt.col, f"Variable '{stmt.name}' no declarada.")
                return
            t = self._infer_expr(stmt.expr)
            if t is not None and t != lt:
                self._err(
                    stmt.line,
                    stmt.col,
                    f"Asignación: se esperaba tipo '{lt}', se obtuvo '{t}'.",
                )
        elif isinstance(stmt, IfNode):
            tc = self._infer_expr(stmt.condition)
            if tc is not None and tc != "bool":
                self._err(stmt.condition.line, stmt.condition.col, "La condición del if debe ser 'bool'.")
            self._visit_block(stmt.then_block)
            if stmt.else_block is not None:
                self._visit_block(stmt.else_block)
        elif isinstance(stmt, WhileNode):
            tc = self._infer_expr(stmt.condition)
            if tc is not None and tc != "bool":
                self._err(stmt.condition.line, stmt.condition.col, "La condición del while debe ser 'bool'.")
            self._visit_block(stmt.body)
        elif isinstance(stmt, PrintNode):
            self._infer_expr(stmt.expr)
        elif isinstance(stmt, ReturnNode):
            if not self.in_function or self.current_return_type is None:
                self._err(stmt.line, stmt.col, "'return' solo es válido dentro de una función.")
                return
            t = self._infer_expr(stmt.expr)
            if t is not None and t != self.current_return_type:
                self._err(
                    stmt.line,
                    stmt.col,
                    f"El retorno debe ser '{self.current_return_type}', se obtuvo '{t}'.",
                )

    def _infer_expr(self, expr: ExprNode) -> Optional[str]:
        if isinstance(expr, IntLiteral):
            return "int"
        if isinstance(expr, BoolLiteral):
            return "bool"
        if isinstance(expr, VarRef):
            t = self._lookup_type(expr.name)
            if t is None:
                self._err(expr.line, expr.col, f"Variable '{expr.name}' no declarada.")
                return None
            return t
        if isinstance(expr, UnaryExpr):
            if expr.op == "!":
                t = self._infer_expr(expr.operand)
                if t is None:
                    return None
                if t != "bool":
                    self._err(expr.line, expr.col, "La negación lógica (!) requiere tipo 'bool'.")
                    return None
                return "bool"
            if expr.op == "-":
                t = self._infer_expr(expr.operand)
                if t is None:
                    return None
                if t != "int":
                    self._err(expr.line, expr.col, "El menos unario requiere tipo 'int'.")
                    return None
                return "int"
            self._err(expr.line, expr.col, f"Operador unario desconocido '{expr.op}'.")
            return None
        if isinstance(expr, BinaryExpr):
            return self._infer_binary(expr)
        if isinstance(expr, CallExpr):
            return self._infer_call(expr)
        self._err(1, 0, "Expresión no reconocida en análisis semántico.")
        return None

    def _infer_call(self, expr: CallExpr) -> Optional[str]:
        if expr.name not in self.func_defs:
            self._err(expr.line, expr.col, f"Función '{expr.name}' no declarada.")
            return None
        fd = self.func_defs[expr.name]
        if len(expr.arguments) != len(fd.params):
            self._err(
                expr.line,
                expr.col,
                f"Función '{expr.name}': se esperaban {len(fd.params)} argumento(s), "
                f"se encontraron {len(expr.arguments)}.",
            )
            return None
        for i, ((pt, _pn), arg) in enumerate(zip(fd.params, expr.arguments)):
            at = self._infer_expr(arg)
            if at is not None and at != pt:
                self._err(
                    arg.line if hasattr(arg, "line") else expr.line,
                    arg.col if hasattr(arg, "col") else expr.col,
                    f"Función '{expr.name}': argumento {i + 1} debe ser '{pt}', se obtuvo '{at}'.",
                )
                return None
        return fd.return_type

    def _infer_binary(self, expr: BinaryExpr) -> Optional[str]:
        op = expr.op
        if op in ("*", "/", "+", "-"):
            ta = self._infer_expr(expr.left)
            tb = self._infer_expr(expr.right)
            if ta is None or tb is None:
                return None
            if ta != "int" or tb != "int":
                self._err(expr.line, expr.col, f"Operación '{op}' requiere operandos 'int'.")
                return None
            return "int"
        if op in ("<", "<=", ">", ">="):
            ta = self._infer_expr(expr.left)
            tb = self._infer_expr(expr.right)
            if ta is None or tb is None:
                return None
            if ta != "int" or tb != "int":
                self._err(expr.line, expr.col, f"Comparación '{op}' requiere operandos 'int'.")
                return None
            return "bool"
        if op in ("&&", "||"):
            ta = self._infer_expr(expr.left)
            tb = self._infer_expr(expr.right)
            if ta is None or tb is None:
                return None
            if ta != "bool" or tb != "bool":
                self._err(expr.line, expr.col, f"Operación '{op}' requiere operandos 'bool'.")
                return None
            return "bool"
        if op in ("==", "!="):
            ta = self._infer_expr(expr.left)
            tb = self._infer_expr(expr.right)
            if ta is None or tb is None:
                return None
            return "bool"
        self._err(expr.line, expr.col, f"Operador binario desconocido '{op}'.")
        return None
