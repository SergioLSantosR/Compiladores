# src/EvalVisitorImpl.py
from antlr4 import *
from gen.grammar.MiniLangParser import MiniLangParser
from gen.grammar.MiniLangVisitor import MiniLangVisitor

class EvalVisitor(MiniLangVisitor):
    """
    Visitor de evaluación adaptado a la gramática en español con tokens en mayúsculas.
    Soporta:
    - Tipos int y bool.
    - Aritmética: +, -, *, / (división entera)
    - Relacionales: ==, !=/<> , <, <=, >, >=
    - Lógicos: &&, ||, !
    - si / sino, imprime
    - Tabla de símbolos y chequeo de tipos.
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

    # ---- program / grupo ----
    def visitProgram(self, ctx: MiniLangParser.ProgramContext):
        return self.visit(ctx.grupo())

    def visitGrupo(self, ctx: MiniLangParser.GrupoContext):
        for s in ctx.sentencia():
            self.visit(s)
        return None

    # ---- declaraciones ----
    def visitDeclaraVariable(self, ctx: MiniLangParser.DeclaraVariableContext):
        t = ctx.tipo().getText()  # "int" o "bool"
        name = ctx.ID().getText()
        if name in self.types:
            raise RuntimeError(f"Redeclaración de variable '{name}' (línea {ctx.start.line}).")
        self.types[name] = t
        self.memory[name] = 0 if t == "int" else False
        return None

    # ---- asignaciones ----
    def visitSentenciaAsigna(self, ctx: MiniLangParser.SentenciaAsignaContext):
        name = ctx.ID().getText()
        self._ensure_declared(name, ctx)
        value = self.visit(ctx.expr())
        expected = self.types[name]
        self._ensure_type(expected, value, ctx, "asignación")
        self.memory[name] = value
        self._println(f"{name} = {value}")
        return None

    # ---- si / sino ----
    def visitSentenciaSI(self, ctx: MiniLangParser.SentenciaSIContext):
        cond = self.visit(ctx.expr())
        self._ensure_type("bool", cond, ctx, "condicional (si)")
        if cond:
            self.visit(ctx.grupo(0))          # bloque del 'si'
        elif ctx.SINO():                      # cláusula 'sino'
            self.visit(ctx.grupo(1))
        return None

    # ---- imprime ----
    def visitSentenciaImprime(self, ctx: MiniLangParser.SentenciaImprimeContext):
        value = self.visit(ctx.expr())
        self._println(value)
        return None

    # ---- expresiones ----
    def visitUnaryNot(self, ctx: MiniLangParser.UnaryNotContext):
        v = self.visit(ctx.expr())
        self._ensure_type("bool", v, ctx, "negación lógica (!)")
        return not v

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
        if ctx.op.type == MiniLangParser.MULTI:
            return l * r
        else:  # DIVIDE
            if r == 0:
                raise RuntimeError(f"División por cero (línea {ctx.start.line}).")
            return l // r

    def visitAddSub(self, ctx: MiniLangParser.AddSubContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)
        self._ensure_type("int", l, ctx, "suma/resta")
        self._ensure_type("int", r, ctx, "suma/resta")
        if ctx.op.type == MiniLangParser.SUMA:
            return l + r
        else:  # RESTA
            return l - r

    def visitRelational(self, ctx: MiniLangParser.RelationalContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)
        op_type = ctx.op.type
        if op_type in (MiniLangParser.EQ, MiniLangParser.NEQ):
            return (l == r) if op_type == MiniLangParser.EQ else (l != r)
        # Los relacionales restantes requieren ints
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
        if ctx.op.type == MiniLangParser.AND:
            return l and r
        else:  # OR
            return l or r

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