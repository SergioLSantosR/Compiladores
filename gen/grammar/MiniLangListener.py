# Generated from grammar/MiniLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniLangParser import MiniLangParser
else:
    from MiniLangParser import MiniLangParser

# This class defines a complete listener for a parse tree produced by MiniLangParser.
class MiniLangListener(ParseTreeListener):

    # Enter a parse tree produced by MiniLangParser#program.
    def enterProgram(self, ctx:MiniLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniLangParser#program.
    def exitProgram(self, ctx:MiniLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniLangParser#grupo.
    def enterGrupo(self, ctx:MiniLangParser.GrupoContext):
        pass

    # Exit a parse tree produced by MiniLangParser#grupo.
    def exitGrupo(self, ctx:MiniLangParser.GrupoContext):
        pass


    # Enter a parse tree produced by MiniLangParser#sentencia.
    def enterSentencia(self, ctx:MiniLangParser.SentenciaContext):
        pass

    # Exit a parse tree produced by MiniLangParser#sentencia.
    def exitSentencia(self, ctx:MiniLangParser.SentenciaContext):
        pass


    # Enter a parse tree produced by MiniLangParser#declaraVariable.
    def enterDeclaraVariable(self, ctx:MiniLangParser.DeclaraVariableContext):
        pass

    # Exit a parse tree produced by MiniLangParser#declaraVariable.
    def exitDeclaraVariable(self, ctx:MiniLangParser.DeclaraVariableContext):
        pass


    # Enter a parse tree produced by MiniLangParser#tipo.
    def enterTipo(self, ctx:MiniLangParser.TipoContext):
        pass

    # Exit a parse tree produced by MiniLangParser#tipo.
    def exitTipo(self, ctx:MiniLangParser.TipoContext):
        pass


    # Enter a parse tree produced by MiniLangParser#sentenciaAsigna.
    def enterSentenciaAsigna(self, ctx:MiniLangParser.SentenciaAsignaContext):
        pass

    # Exit a parse tree produced by MiniLangParser#sentenciaAsigna.
    def exitSentenciaAsigna(self, ctx:MiniLangParser.SentenciaAsignaContext):
        pass


    # Enter a parse tree produced by MiniLangParser#sentenciaSI.
    def enterSentenciaSI(self, ctx:MiniLangParser.SentenciaSIContext):
        pass

    # Exit a parse tree produced by MiniLangParser#sentenciaSI.
    def exitSentenciaSI(self, ctx:MiniLangParser.SentenciaSIContext):
        pass


    # Enter a parse tree produced by MiniLangParser#sentenciaImprime.
    def enterSentenciaImprime(self, ctx:MiniLangParser.SentenciaImprimeContext):
        pass

    # Exit a parse tree produced by MiniLangParser#sentenciaImprime.
    def exitSentenciaImprime(self, ctx:MiniLangParser.SentenciaImprimeContext):
        pass


    # Enter a parse tree produced by MiniLangParser#UnaryNot.
    def enterUnaryNot(self, ctx:MiniLangParser.UnaryNotContext):
        pass

    # Exit a parse tree produced by MiniLangParser#UnaryNot.
    def exitUnaryNot(self, ctx:MiniLangParser.UnaryNotContext):
        pass


    # Enter a parse tree produced by MiniLangParser#MulDiv.
    def enterMulDiv(self, ctx:MiniLangParser.MulDivContext):
        pass

    # Exit a parse tree produced by MiniLangParser#MulDiv.
    def exitMulDiv(self, ctx:MiniLangParser.MulDivContext):
        pass


    # Enter a parse tree produced by MiniLangParser#AddSub.
    def enterAddSub(self, ctx:MiniLangParser.AddSubContext):
        pass

    # Exit a parse tree produced by MiniLangParser#AddSub.
    def exitAddSub(self, ctx:MiniLangParser.AddSubContext):
        pass


    # Enter a parse tree produced by MiniLangParser#Relational.
    def enterRelational(self, ctx:MiniLangParser.RelationalContext):
        pass

    # Exit a parse tree produced by MiniLangParser#Relational.
    def exitRelational(self, ctx:MiniLangParser.RelationalContext):
        pass


    # Enter a parse tree produced by MiniLangParser#FalseLit.
    def enterFalseLit(self, ctx:MiniLangParser.FalseLitContext):
        pass

    # Exit a parse tree produced by MiniLangParser#FalseLit.
    def exitFalseLit(self, ctx:MiniLangParser.FalseLitContext):
        pass


    # Enter a parse tree produced by MiniLangParser#Logical.
    def enterLogical(self, ctx:MiniLangParser.LogicalContext):
        pass

    # Exit a parse tree produced by MiniLangParser#Logical.
    def exitLogical(self, ctx:MiniLangParser.LogicalContext):
        pass


    # Enter a parse tree produced by MiniLangParser#UnaryMinus.
    def enterUnaryMinus(self, ctx:MiniLangParser.UnaryMinusContext):
        pass

    # Exit a parse tree produced by MiniLangParser#UnaryMinus.
    def exitUnaryMinus(self, ctx:MiniLangParser.UnaryMinusContext):
        pass


    # Enter a parse tree produced by MiniLangParser#TrueLit.
    def enterTrueLit(self, ctx:MiniLangParser.TrueLitContext):
        pass

    # Exit a parse tree produced by MiniLangParser#TrueLit.
    def exitTrueLit(self, ctx:MiniLangParser.TrueLitContext):
        pass


    # Enter a parse tree produced by MiniLangParser#IdRef.
    def enterIdRef(self, ctx:MiniLangParser.IdRefContext):
        pass

    # Exit a parse tree produced by MiniLangParser#IdRef.
    def exitIdRef(self, ctx:MiniLangParser.IdRefContext):
        pass


    # Enter a parse tree produced by MiniLangParser#IntLit.
    def enterIntLit(self, ctx:MiniLangParser.IntLitContext):
        pass

    # Exit a parse tree produced by MiniLangParser#IntLit.
    def exitIntLit(self, ctx:MiniLangParser.IntLitContext):
        pass


    # Enter a parse tree produced by MiniLangParser#Paren.
    def enterParen(self, ctx:MiniLangParser.ParenContext):
        pass

    # Exit a parse tree produced by MiniLangParser#Paren.
    def exitParen(self, ctx:MiniLangParser.ParenContext):
        pass



del MiniLangParser