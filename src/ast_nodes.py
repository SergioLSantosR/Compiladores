# src/ast_nodes.py
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Tuple, Union


@dataclass
class FuncDefNode:
    name: str
    return_type: str
    params: List[Tuple[str, str]]  # (tipo, nombre)
    body: BlockNode
    line: int
    col: int


@dataclass
class ProgramNode:
    functions: List[FuncDefNode]
    main_statements: List[StatementNode]
    line: int
    col: int


@dataclass
class BlockNode:
    statements: List[StatementNode]
    line: int
    col: int


StatementNode = Union[
    "DeclareNode",
    "AssignNode",
    "IfNode",
    "WhileNode",
    "PrintNode",
    "ReturnNode",
]


@dataclass
class DeclareNode:
    type_name: str
    name: str
    line: int
    col: int


@dataclass
class AssignNode:
    name: str
    expr: ExprNode
    line: int
    col: int


@dataclass
class IfNode:
    condition: ExprNode
    then_block: BlockNode
    else_block: Optional[BlockNode]
    line: int
    col: int


@dataclass
class WhileNode:
    condition: ExprNode
    body: BlockNode
    line: int
    col: int


@dataclass
class PrintNode:
    expr: ExprNode
    line: int
    col: int


@dataclass
class ReturnNode:
    expr: ExprNode
    line: int
    col: int


ExprNode = Union[
    "IntLiteral",
    "BoolLiteral",
    "VarRef",
    "UnaryExpr",
    "BinaryExpr",
    "CallExpr",
]


@dataclass
class IntLiteral:
    value: int
    line: int
    col: int


@dataclass
class BoolLiteral:
    value: bool
    line: int
    col: int


@dataclass
class VarRef:
    name: str
    line: int
    col: int


@dataclass
class UnaryExpr:
    op: str
    operand: ExprNode
    line: int
    col: int


@dataclass
class BinaryExpr:
    op: str
    left: ExprNode
    right: ExprNode
    line: int
    col: int


@dataclass
class CallExpr:
    name: str
    line: int
    col: int
    arguments: List[ExprNode] = field(default_factory=list)
