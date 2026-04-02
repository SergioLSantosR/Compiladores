# Generated from grammar/MiniLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniLangParser import MiniLangParser
else:
    from MiniLangParser import MiniLangParser

# This class defines a complete generic visitor for a parse tree produced by MiniLangParser.

class MiniLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniLangParser#program.
    def visitProgram(self, ctx:MiniLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#grupo.
    def visitGrupo(self, ctx:MiniLangParser.GrupoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#sentencia.
    def visitSentencia(self, ctx:MiniLangParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#declaraVariable.
    def visitDeclaraVariable(self, ctx:MiniLangParser.DeclaraVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#tipo.
    def visitTipo(self, ctx:MiniLangParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#sentenciaAsigna.
    def visitSentenciaAsigna(self, ctx:MiniLangParser.SentenciaAsignaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#sentenciaSI.
    def visitSentenciaSI(self, ctx:MiniLangParser.SentenciaSIContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#sentenciaImprime.
    def visitSentenciaImprime(self, ctx:MiniLangParser.SentenciaImprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#UnaryNot.
    def visitUnaryNot(self, ctx:MiniLangParser.UnaryNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#MulDiv.
    def visitMulDiv(self, ctx:MiniLangParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#AddSub.
    def visitAddSub(self, ctx:MiniLangParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#Relational.
    def visitRelational(self, ctx:MiniLangParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#FalseLit.
    def visitFalseLit(self, ctx:MiniLangParser.FalseLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#Logical.
    def visitLogical(self, ctx:MiniLangParser.LogicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#UnaryMinus.
    def visitUnaryMinus(self, ctx:MiniLangParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#TrueLit.
    def visitTrueLit(self, ctx:MiniLangParser.TrueLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#IdRef.
    def visitIdRef(self, ctx:MiniLangParser.IdRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#IntLit.
    def visitIntLit(self, ctx:MiniLangParser.IntLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#Paren.
    def visitParen(self, ctx:MiniLangParser.ParenContext):
        return self.visitChildren(ctx)



del MiniLangParser