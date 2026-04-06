# src/ast_builder.py
from gen.grammar.MiniLangParser import MiniLangParser
from gen.grammar.MiniLangVisitor import MiniLangVisitor

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


def _loc(ctx):
    t = ctx.start
    return t.line, t.column


class AstBuilder(MiniLangVisitor):
    """Construye el AST a partir del árbol de parsing ANTLR."""

    def visitPrograma(self, ctx: MiniLangParser.ProgramaContext):
        return self.visit(ctx.cuerpoPrincipal())

    def visitCuerpoPrincipal(self, ctx: MiniLangParser.CuerpoPrincipalContext):
        line, col = _loc(ctx)
        funcs = [self.visit(f) for f in ctx.declaracionFuncion()]
        main = [self.visit(s) for s in ctx.sentencia()]
        return ProgramNode(functions=funcs, main_statements=main, line=line, col=col)

    def visitDeclaracionFuncion(self, ctx: MiniLangParser.DeclaracionFuncionContext):
        line, col = _loc(ctx)
        ret = ctx.tipo().getText()
        name = ctx.IDENTIFICADOR().getText()
        params = []
        if ctx.listaParametros() is not None:
            for p in ctx.listaParametros().parametro():
                params.append((p.tipo().getText(), p.IDENTIFICADOR().getText()))
        body = self.visit(ctx.bloque())
        return FuncDefNode(
            name=name,
            return_type=ret,
            params=params,
            body=body,
            line=line,
            col=col,
        )

    def visitBloque(self, ctx: MiniLangParser.BloqueContext):
        line, col = _loc(ctx)
        stmts = [self.visit(s) for s in ctx.sentencia()]
        return BlockNode(statements=stmts, line=line, col=col)

    def visitSentencia(self, ctx: MiniLangParser.SentenciaContext):
        if ctx.declaracionVariable():
            return self.visit(ctx.declaracionVariable())
        if ctx.asignacion():
            return self.visit(ctx.asignacion())
        if ctx.condicionalSi():
            return self.visit(ctx.condicionalSi())
        if ctx.cicloMientras():
            return self.visit(ctx.cicloMientras())
        if ctx.imprimir():
            return self.visit(ctx.imprimir())
        return self.visit(ctx.retorno())

    def visitDeclaracionVariable(self, ctx: MiniLangParser.DeclaracionVariableContext):
        line, col = _loc(ctx)
        t = ctx.tipo().getText()
        name = ctx.IDENTIFICADOR().getText()
        return DeclareNode(type_name=t, name=name, line=line, col=col)

    def visitAsignacion(self, ctx: MiniLangParser.AsignacionContext):
        line, col = _loc(ctx)
        name = ctx.IDENTIFICADOR().getText()
        expr = self.visit(ctx.expresion())
        return AssignNode(name=name, expr=expr, line=line, col=col)

    def visitCondicionalSi(self, ctx: MiniLangParser.CondicionalSiContext):
        line, col = _loc(ctx)
        cond = self.visit(ctx.expresion())
        bloques = ctx.bloque()
        then_b = self.visit(bloques[0])
        else_b = self.visit(bloques[1]) if len(bloques) > 1 else None
        return IfNode(
            condition=cond,
            then_block=then_b,
            else_block=else_b,
            line=line,
            col=col,
        )

    def visitCicloMientras(self, ctx: MiniLangParser.CicloMientrasContext):
        line, col = _loc(ctx)
        return WhileNode(
            condition=self.visit(ctx.expresion()),
            body=self.visit(ctx.bloque()),
            line=line,
            col=col,
        )

    def visitImprimir(self, ctx: MiniLangParser.ImprimirContext):
        line, col = _loc(ctx)
        return PrintNode(expr=self.visit(ctx.expresion()), line=line, col=col)

    def visitRetorno(self, ctx: MiniLangParser.RetornoContext):
        line, col = _loc(ctx)
        return ReturnNode(expr=self.visit(ctx.expresion()), line=line, col=col)

    def visitNegacionLogica(self, ctx: MiniLangParser.NegacionLogicaContext):
        line, col = _loc(ctx)
        return UnaryExpr(op="!", operand=self.visit(ctx.expresion()), line=line, col=col)

    def visitMenosUnario(self, ctx: MiniLangParser.MenosUnarioContext):
        line, col = _loc(ctx)
        return UnaryExpr(op="-", operand=self.visit(ctx.expresion()), line=line, col=col)

    def visitLlamadaFuncion(self, ctx: MiniLangParser.LlamadaFuncionContext):
        line, col = _loc(ctx)
        name = ctx.IDENTIFICADOR().getText()
        args: list[ExprNode] = []
        la = ctx.listaArgumentos()
        if la is not None:
            for e in la.expresion():
                args.append(self.visit(e))
        return CallExpr(name=name, line=line, col=col, arguments=args)

    def visitParentesis(self, ctx: MiniLangParser.ParentesisContext):
        return self.visit(ctx.expresion())

    def visitMultiplicacionDivision(self, ctx: MiniLangParser.MultiplicacionDivisionContext):
        line, col = _loc(ctx)
        op = "*" if ctx.MULTIPLICACION() else "/"
        return BinaryExpr(
            op=op,
            left=self.visit(ctx.izq),
            right=self.visit(ctx.der),
            line=line,
            col=col,
        )

    def visitSumaResta(self, ctx: MiniLangParser.SumaRestaContext):
        line, col = _loc(ctx)
        op = "+" if ctx.SUMA() else "-"
        return BinaryExpr(
            op=op,
            left=self.visit(ctx.izq),
            right=self.visit(ctx.der),
            line=line,
            col=col,
        )

    def visitComparacion(self, ctx: MiniLangParser.ComparacionContext):
        line, col = _loc(ctx)
        if ctx.MENOR_QUE():
            op = "<"
        elif ctx.MENOR_IGUAL():
            op = "<="
        elif ctx.MAYOR_QUE():
            op = ">"
        else:
            op = ">="
        return BinaryExpr(
            op=op,
            left=self.visit(ctx.izq),
            right=self.visit(ctx.der),
            line=line,
            col=col,
        )

    def visitIgualdad(self, ctx: MiniLangParser.IgualdadContext):
        line, col = _loc(ctx)
        op = "==" if ctx.IGUAL() else "!="
        return BinaryExpr(
            op=op,
            left=self.visit(ctx.izq),
            right=self.visit(ctx.der),
            line=line,
            col=col,
        )

    def visitYLogico(self, ctx: MiniLangParser.YLogicoContext):
        line, col = _loc(ctx)
        return BinaryExpr(
            op="&&",
            left=self.visit(ctx.izq),
            right=self.visit(ctx.der),
            line=line,
            col=col,
        )

    def visitOLogico(self, ctx: MiniLangParser.OLogicoContext):
        line, col = _loc(ctx)
        return BinaryExpr(
            op="||",
            left=self.visit(ctx.izq),
            right=self.visit(ctx.der),
            line=line,
            col=col,
        )

    def visitLiteralEntero(self, ctx: MiniLangParser.LiteralEnteroContext):
        line, col = _loc(ctx)
        return IntLiteral(value=int(ctx.ENTERO().getText()), line=line, col=col)

    def visitLiteralVerdadero(self, ctx: MiniLangParser.LiteralVerdaderoContext):
        line, col = _loc(ctx)
        return BoolLiteral(value=True, line=line, col=col)

    def visitLiteralFalso(self, ctx: MiniLangParser.LiteralFalsoContext):
        line, col = _loc(ctx)
        return BoolLiteral(value=False, line=line, col=col)

    def visitReferenciaVariable(self, ctx: MiniLangParser.ReferenciaVariableContext):
        line, col = _loc(ctx)
        return VarRef(name=ctx.IDENTIFICADOR().getText(), line=line, col=col)
