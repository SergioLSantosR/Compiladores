# src/interpreter_visitor.py
from __future__ import annotations

from typing import Any, Dict, List, Optional

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


class ReturnSignal(Exception):
    def __init__(self, value: Any):
        super().__init__()
        self.value = value


class InterpreterVisitor:
    """Ejecución del AST con ámbitos, while y funciones."""

    def __init__(self, stdout_print: bool = True):
        self.stdout_print = stdout_print
        self.salida: List[str] = []
        self.functions: Dict[str, FuncDefNode] = {}
        self.env_stack: List[Dict[str, Any]] = []
        self.in_function_depth = 0

    def _tipo_de(self, valor: Any) -> str:
        if isinstance(valor, bool):
            return "bool"
        if isinstance(valor, int):
            return "int"
        return "desconocido"

    def _imprimir(self, texto: Any) -> None:
        if self.stdout_print:
            print(texto)
        self.salida.append(str(texto))

    def _push_env(self) -> None:
        self.env_stack.append({})

    def _pop_env(self) -> None:
        self.env_stack.pop()

    def _lookup_frame(self, name: str) -> Optional[Dict[str, Any]]:
        for env in reversed(self.env_stack):
            if name in env:
                return env
        return None

    def _memoria_plana(self) -> Dict[str, Any]:
        merged: Dict[str, Any] = {}
        for env in self.env_stack:
            merged.update(env)
        return merged

    def run(self, program: ProgramNode) -> None:
        self.salida.clear()
        self.functions = {f.name: f for f in program.functions}
        self.env_stack.clear()
        self.in_function_depth = 0
        self._push_env()
        try:
            for stmt in program.main_statements:
                self._exec_stmt(stmt)
        finally:
            self._pop_env()

    def _exec_block(self, block: BlockNode) -> None:
        self._push_env()
        try:
            for stmt in block.statements:
                self._exec_stmt(stmt)
        finally:
            self._pop_env()

    def _exec_stmt(self, stmt) -> None:
        if isinstance(stmt, DeclareNode):
            if stmt.name in self.env_stack[-1]:
                raise RuntimeError(f"Redeclaración de '{stmt.name}' (línea {stmt.line}).")
            self.env_stack[-1][stmt.name] = 0 if stmt.type_name == "int" else False
        elif isinstance(stmt, AssignNode):
            frame = self._lookup_frame(stmt.name)
            if frame is None:
                raise RuntimeError(f"Variable '{stmt.name}' no declarada (línea {stmt.line}).")
            valor = self._eval_expr(stmt.expr)
            esperado = self._tipo_esperado(stmt.name)
            if esperado and self._tipo_de(valor) != esperado:
                raise RuntimeError(
                    f"Error de tipos en asignación (línea {stmt.line}): "
                    f"se esperaba {esperado}, obtuvo {self._tipo_de(valor)}."
                )
            frame[stmt.name] = valor
            self._imprimir(f"{stmt.name} = {valor}")
        elif isinstance(stmt, IfNode):
            c = self._eval_expr(stmt.condition)
            if self._tipo_de(c) != "bool":
                raise RuntimeError(f"Condición if (línea {stmt.line}): se esperaba bool.")
            if c:
                self._exec_block(stmt.then_block)
            elif stmt.else_block is not None:
                self._exec_block(stmt.else_block)
        elif isinstance(stmt, WhileNode):
            while True:
                c = self._eval_expr(stmt.condition)
                if self._tipo_de(c) != "bool":
                    raise RuntimeError(f"Condición while (línea {stmt.line}): se esperaba bool.")
                if not c:
                    break
                self._exec_block(stmt.body)
        elif isinstance(stmt, PrintNode):
            self._imprimir(self._eval_expr(stmt.expr))
        elif isinstance(stmt, ReturnNode):
            if self.in_function_depth == 0:
                raise RuntimeError(f"'return' fuera de función (línea {stmt.line}).")
            raise ReturnSignal(self._eval_expr(stmt.expr))

    def _tipo_esperado(self, name: str) -> Optional[str]:
        """Tipo declarado según el análisis semántico previo (reconstruido por valor inicial)."""
        # El semántico ya validó; aquí solo comprobamos consistencia con literales en memoria.
        for env in reversed(self.env_stack):
            if name in env:
                v = env[name]
                return self._tipo_de(v)
        return None

    def _eval_expr(self, expr: ExprNode) -> Any:
        if isinstance(expr, IntLiteral):
            return expr.value
        if isinstance(expr, BoolLiteral):
            return expr.value
        if isinstance(expr, VarRef):
            frame = self._lookup_frame(expr.name)
            if frame is None:
                raise RuntimeError(f"Variable '{expr.name}' no declarada (línea {expr.line}).")
            return frame[expr.name]
        if isinstance(expr, UnaryExpr):
            if expr.op == "!":
                v = self._eval_expr(expr.operand)
                if self._tipo_de(v) != "bool":
                    raise RuntimeError(f"Negación ! (línea {expr.line}): se esperaba bool.")
                return not v
            if expr.op == "-":
                v = self._eval_expr(expr.operand)
                if self._tipo_de(v) != "int":
                    raise RuntimeError(f"- unario (línea {expr.line}): se esperaba int.")
                return -v
            raise RuntimeError(f"Operador unario (línea {expr.line}).")
        if isinstance(expr, BinaryExpr):
            return self._eval_binary(expr)
        if isinstance(expr, CallExpr):
            return self._eval_call(expr)
        raise RuntimeError("Expresión no soportada.")

    def _eval_binary(self, expr: BinaryExpr) -> Any:
        op = expr.op
        izq = self._eval_expr(expr.left)
        der = self._eval_expr(expr.right)
        if op in ("*", "/", "+", "-"):
            if self._tipo_de(izq) != "int" or self._tipo_de(der) != "int":
                raise RuntimeError(f"Aritmética (línea {expr.line}): operandos int.")
            if op == "*":
                return izq * der
            if op == "/":
                if der == 0:
                    raise RuntimeError(f"División por cero (línea {expr.line}).")
                return izq // der
            if op == "+":
                return izq + der
            return izq - der
        if op in ("<", "<=", ">", ">="):
            if self._tipo_de(izq) != "int" or self._tipo_de(der) != "int":
                raise RuntimeError(f"Comparación (línea {expr.line}): operandos int.")
            if op == "<":
                return izq < der
            if op == "<=":
                return izq <= der
            if op == ">":
                return izq > der
            return izq >= der
        if op == "&&":
            if self._tipo_de(izq) != "bool" or self._tipo_de(der) != "bool":
                raise RuntimeError(f"&& (línea {expr.line}): operandos bool.")
            return izq and der
        if op == "||":
            if self._tipo_de(izq) != "bool" or self._tipo_de(der) != "bool":
                raise RuntimeError(f"|| (línea {expr.line}): operandos bool.")
            return izq or der
        if op == "==":
            return izq == der
        if op == "!=":
            return izq != der
        raise RuntimeError(f"Operador (línea {expr.line}).")

    def _eval_call(self, expr: CallExpr) -> Any:
        if expr.name not in self.functions:
            raise RuntimeError(f"Función '{expr.name}' no definida (línea {expr.line}).")
        fd = self.functions[expr.name]
        if len(expr.arguments) != len(fd.params):
            raise RuntimeError(
                f"Llamada '{expr.name}' (línea {expr.line}): "
                f"{len(fd.params)} argumento(s) esperados, {len(expr.arguments)} dados."
            )
        vals = [self._eval_expr(a) for a in expr.arguments]
        depth_before = len(self.env_stack)
        self._push_env()
        for (pt, pn), v in zip(fd.params, vals):
            if self._tipo_de(v) != pt:
                raise RuntimeError(
                    f"Llamada '{expr.name}' (línea {expr.line}): tipo de argumento incorrecto."
                )
            self.env_stack[-1][pn] = v
        self.in_function_depth += 1
        result: Any = None
        returned = False
        try:
            self._exec_block(fd.body)
        except ReturnSignal as rs:
            result = rs.value
            returned = True
        finally:
            self.in_function_depth -= 1
            while len(self.env_stack) > depth_before:
                self._pop_env()
        if not returned:
            raise RuntimeError(f"Función '{expr.name}' no ejecutó return.")
        if self._tipo_de(result) != fd.return_type:
            raise RuntimeError(f"Valor de retorno de '{expr.name}' no coincide con el tipo declarado.")
        return result

    @property
    def memoria(self) -> Dict[str, Any]:
        return self._memoria_plana()
