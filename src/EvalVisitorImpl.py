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
        self.memoria = {}       # nombre -> valor (int/bool)
        self.tipos = {}         # nombre -> "int" | "bool"
        self.stdout_print = stdout_print
        self.salida = []        # Guarda textos impresos (para pruebas)

    # ---- Utilidades ----

    def _tipo_de(self, valor):
        if isinstance(valor, bool):
            return "bool"
        elif isinstance(valor, int):
            return "int"
        return "desconocido"

    def _asegurar_declarada(self, nombre, ctx):
        if nombre not in self.tipos:
            raise RuntimeError(f"Variable '{nombre}' no declarada (línea {ctx.start.line}).")

    def _asegurar_tipo(self, esperado, valor, ctx, descripcion="operación"):
        actual = self._tipo_de(valor)
        if esperado != actual:
            raise RuntimeError(
                f"Error de tipos en {descripcion} (línea {ctx.start.line}): "
                f"se esperaba {esperado}, obtuvo {actual}."
            )

    def _imprimir(self, texto):
        if self.stdout_print:
            print(texto)
        self.salida.append(str(texto))

    # ---- programa / bloque ----

    def visitPrograma(self, ctx: MiniLangParser.ProgramaContext):
        return self.visit(ctx.bloque())

    def visitBloque(self, ctx: MiniLangParser.BloqueContext):
        for s in ctx.sentencia():
            self.visit(s)
        return None

    # ---- declaraciones ----

    def visitDeclaracionVariable(self, ctx: MiniLangParser.DeclaracionVariableContext):
        t = ctx.tipo().getText()
        nombre = ctx.IDENTIFICADOR().getText()
        if nombre in self.tipos:
            raise RuntimeError(f"Redeclaración de variable '{nombre}' (línea {ctx.start.line}).")
        self.tipos[nombre] = t
        self.memoria[nombre] = 0 if t == "int" else False
        return None

    # ---- asignaciones ----

    def visitAsignacion(self, ctx: MiniLangParser.AsignacionContext):
        nombre = ctx.IDENTIFICADOR().getText()
        self._asegurar_declarada(nombre, ctx)
        valor = self.visit(ctx.expresion())
        esperado = self.tipos[nombre]
        self._asegurar_tipo(esperado, valor, ctx, "asignación")
        self.memoria[nombre] = valor
        self._imprimir(f"{nombre} = {valor}")
        return None

    # ---- if/else ----

    def visitCondicionalSi(self, ctx: MiniLangParser.CondicionalSiContext):
        condicion = self.visit(ctx.expresion())
        self._asegurar_tipo("bool", condicion, ctx, "condicional (if)")
        if condicion:
            self.visit(ctx.bloque(0))
        elif ctx.SINO():
            self.visit(ctx.bloque(1))
        return None

    # ---- print ----

    def visitImprimir(self, ctx: MiniLangParser.ImprimirContext):
        valor = self.visit(ctx.expresion())
        self._imprimir(valor)
        return None

    # ---- expresiones ----

    def visitNegacionLogica(self, ctx: MiniLangParser.NegacionLogicaContext):
        v = self.visit(ctx.expresion())
        self._asegurar_tipo("bool", v, ctx, "negación lógica (!)")
        return not v

    def visitMenosUnario(self, ctx: MiniLangParser.MenosUnarioContext):
        v = self.visit(ctx.expresion())
        self._asegurar_tipo("int", v, ctx, "negación aritmética (-)")
        return -v

    def visitParentesis(self, ctx: MiniLangParser.ParentesisContext):
        return self.visit(ctx.expresion())

    def visitMultiplicacionDivision(self, ctx: MiniLangParser.MultiplicacionDivisionContext):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        self._asegurar_tipo("int", izq, ctx, "multiplicación/división")
        self._asegurar_tipo("int", der, ctx, "multiplicación/división")
        if ctx.op.type == MiniLangParser.MULTIPLICACION:
            return izq * der
        if der == 0:
            raise RuntimeError(f"División por cero (línea {ctx.start.line}).")
        return izq // der

    def visitSumaResta(self, ctx: MiniLangParser.SumaRestaContext):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        self._asegurar_tipo("int", izq, ctx, "suma/resta")
        self._asegurar_tipo("int", der, ctx, "suma/resta")
        return izq + der if ctx.op.type == MiniLangParser.SUMA else izq - der

    def visitComparacion(self, ctx: MiniLangParser.ComparacionContext):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        self._asegurar_tipo("int", izq, ctx, "comparación relacional")
        self._asegurar_tipo("int", der, ctx, "comparación relacional")
        tipo_op = ctx.op.type
        if tipo_op == MiniLangParser.MENOR_QUE:
            return izq < der
        if tipo_op == MiniLangParser.MENOR_IGUAL:
            return izq <= der
        if tipo_op == MiniLangParser.MAYOR_QUE:
            return izq > der
        if tipo_op == MiniLangParser.MAYOR_IGUAL:
            return izq >= der
        raise RuntimeError("Operador relacional no reconocido.")

    def visitIgualdad(self, ctx: MiniLangParser.IgualdadContext):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        if ctx.op.type == MiniLangParser.IGUAL:
            return izq == der
        return izq != der

    def visitYLogico(self, ctx: MiniLangParser.YLogicoContext):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        self._asegurar_tipo("bool", izq, ctx, "operación lógica (&&)")
        self._asegurar_tipo("bool", der, ctx, "operación lógica (&&)")
        return izq and der

    def visitOLogico(self, ctx: MiniLangParser.OLogicoContext):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        self._asegurar_tipo("bool", izq, ctx, "operación lógica (||)")
        self._asegurar_tipo("bool", der, ctx, "operación lógica (||)")
        return izq or der

    def visitLiteralEntero(self, ctx: MiniLangParser.LiteralEnteroContext):
        return int(ctx.ENTERO().getText())

    def visitLiteralVerdadero(self, ctx: MiniLangParser.LiteralVerdaderoContext):
        return True

    def visitLiteralFalso(self, ctx: MiniLangParser.LiteralFalsoContext):
        return False

    def visitReferenciaVariable(self, ctx: MiniLangParser.ReferenciaVariableContext):
        nombre = ctx.IDENTIFICADOR().getText()
        self._asegurar_declarada(nombre, ctx)
        return self.memoria[nombre]
