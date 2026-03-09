# src/EvalVisitorImpl.py
from antlr4 import *
from gen.grammar.MiniLangParser import MiniLangParser
from gen.grammar.MiniLangVisitor import MiniLangVisitor

class EvalVisitor(MiniLangVisitor):
    """
    Visitor de evaluación:
    - Soporta tipos int y bool.
    - Aritmética: +, -, *, / (DIVISIÓN ENTERA)
    - Relacionales: ==, !=/<> , <, <=, >, >=
    - Lógicos: &&, ||, !
    - if/else, print
    - Maneja tabla de símbolos y chequeo de tipos.
    """

    def __init__(self, stdout_print=True):
        super().__init__()
        self.memory = {}  # nombre -> valor (int/bool)
        self.types = {}   # nombre -> "int" | "bool"
        self.stdout_print = stdout_print
        self.output = []  # Guarda textos impresos (para pruebas)

    # ---- Utilidades ----
    def _type_of(self, value):
        if isinstance(value, bool):
            return "bool"
        elif isinstance(value, int):
            return "int"
        else:
            return "desconocido"

    def _ensure_declared(self, name, ctx):
        if name not in self.types:
            raise RuntimeError(f"Variable '{name}' no declarada (línea {ctx.start.line}).")

    def _ensure_type(self, expected, value, ctx, op_desc="operación"):
        actual = self._type_of(value)
        if expected != actual:
            raise RuntimeError(
                f"Error de tipos en {op_desc} (línea {ctx.start.line}): se esperaba {expected}, obtuvo {actual}."
            )

    def _println(self, text):
        if self.stdout_print:
            print(text)
        self.output.append(str(text))

    # ---- program / block ----
    def visitProgram(self, ctx: MiniLangParser.ProgramContext):
        return self.visit(ctx.block())

    def visitBlock(self, ctx: MiniLangParser.BlockContext):
        for s in ctx.stmt():
            self.visit(s)
        return None

    # ---- declaraciones ----
    def visitVarDecl(self, ctx: MiniLangParser.VarDeclContext):
        t = ctx.type_().getText() if hasattr(ctx, 'type_') else ctx.type().getText()
        name = ctx.ID().getText()
        if name in self.types:
            raise RuntimeError(f"Redeclaración de variable '{name}' (línea {ctx.start.line}).")
        self.types[name] = t
        self.memory[name] = 0 if t == "int" else False
        return None

    # ---- asignaciones ----
    def visitAssignStmt(self, ctx: MiniLangParser.AssignStmtContext):
        name = ctx.ID().getText()
        self._ensure_declared(name, ctx)
        value = self.visit(ctx.expr())
        # Chequeo de tipos
        expected = self.types[name]
        self._ensure_type(expected, value, ctx, "asignación")
        self.memory[name] = value
        # Imprimir resultado de la asignación (útil para ver operaciones)
        self._println(f"{name} = {value}")
        return None

    # ---- if/else ----
    def visitIfStmt(self, ctx: MiniLangParser.IfStmtContext):
        cond = self.visit(ctx.expr())
        self._ensure_type("bool", cond, ctx, "condicional (if)")
        if cond:
            self.visit(ctx.block(0))
        elif ctx.ELSE():
            self.visit(ctx.block(1))
        return None

    # ---- print ----
    def visitPrintStmt(self, ctx: MiniLangParser.PrintStmtContext):
        value = self.visit(ctx.expr())
        self._println(value)
        return None

    # ---- expresiones ----
    def visitUnaryNot(self, ctx: MiniLangParser.UnaryNotContext):
        v = self.visit(ctx.expr())
        self._ensure_type("bool", v, ctx, "negación lógica (!)")
        return (not v)

    def visitUnaryMinus(self, ctx: MiniLangParser.UnaryMinusContext):
        v = self.visit(ctx.expr())
        self._ensure_type("int", v, ctx, "negación aritmética (-)")
        return -v

    def visitParen(self, ctx: MiniLangParser.ParenContext):
        return self.visit(ctx.expr())

    def visitMulDiv(self, ctx: MiniLangParser.MulDivContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)
        self._ensure_type("int", l, ctx, "multiplicación/división")
        self._ensure_type("int", r, ctx, "multiplicación/división")
        if ctx.op.type == MiniLangParser.MUL:
            return l * r
        else:
            if r == 0:
                raise RuntimeError(f"División por cero (línea {ctx.start.line}).")
            # División entera
            return l // r

    def visitAddSub(self, ctx: MiniLangParser.AddSubContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)
        self._ensure_type("int", l, ctx, "suma/resta")
        self._ensure_type("int", r, ctx, "suma/resta")
        return l + r if ctx.op.type == MiniLangParser.ADD else l - r

    def visitRelational(self, ctx: MiniLangParser.RelationalContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)
        # Permitimos comparaciones entre ints y entre bools (==/!=) y relacionales solo en ints
        op_type = ctx.op.type
        if op_type in (MiniLangParser.EQ, MiniLangParser.NEQ):
            return (l == r) if op_type == MiniLangParser.EQ else (l != r)
        # El resto requiere ints
        self._ensure_type("int", l, ctx, "comparación relacional")
        self._ensure_type("int", r, ctx, "comparación relacional")
        if op_type == MiniLangParser.LT:
            return l < r
        if op_type == MiniLangParser.LE:
            return l <= r
        if op_type == MiniLangParser.GT:
            return l > r
        if op_type == MiniLangParser.GE:
            return l >= r
        raise RuntimeError("Operador relacional no reconocido.")

    def visitLogical(self, ctx: MiniLangParser.LogicalContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)
        self._ensure_type("bool", l, ctx, "operación lógica")
        self._ensure_type("bool", r, ctx, "operación lógica")
        return (l and r) if ctx.op.type == MiniLangParser.AND else (l or r)

    def visitIntLit(self, ctx: MiniLangParser.IntLitContext):
        return int(ctx.INT().getText())

    def visitTrueLit(self, ctx: MiniLangParser.TrueLitContext):
        return True

    def visitFalseLit(self, ctx: MiniLangParser.FalseLitContext):
        return False

    def visitIdRef(self, ctx: MiniLangParser.IdRefContext):
        name = ctx.ID().getText()
        self._ensure_declared(name, ctx)
        return self.memory[name]
