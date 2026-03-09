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


    # Enter a parse tree produced by MiniLangParser#block.
    def enterBlock(self, ctx:MiniLangParser.BlockContext):
        pass

    # Exit a parse tree produced by MiniLangParser#block.
    def exitBlock(self, ctx:MiniLangParser.BlockContext):
        pass


    # Enter a parse tree produced by MiniLangParser#stmt.
    def enterStmt(self, ctx:MiniLangParser.StmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#stmt.
    def exitStmt(self, ctx:MiniLangParser.StmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#varDecl.
    def enterVarDecl(self, ctx:MiniLangParser.VarDeclContext):
        pass

    # Exit a parse tree produced by MiniLangParser#varDecl.
    def exitVarDecl(self, ctx:MiniLangParser.VarDeclContext):
        pass


    # Enter a parse tree produced by MiniLangParser#type.
    def enterType(self, ctx:MiniLangParser.TypeContext):
        pass

    # Exit a parse tree produced by MiniLangParser#type.
    def exitType(self, ctx:MiniLangParser.TypeContext):
        pass


    # Enter a parse tree produced by MiniLangParser#assignStmt.
    def enterAssignStmt(self, ctx:MiniLangParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#assignStmt.
    def exitAssignStmt(self, ctx:MiniLangParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#ifStmt.
    def enterIfStmt(self, ctx:MiniLangParser.IfStmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#ifStmt.
    def exitIfStmt(self, ctx:MiniLangParser.IfStmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#printStmt.
    def enterPrintStmt(self, ctx:MiniLangParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#printStmt.
    def exitPrintStmt(self, ctx:MiniLangParser.PrintStmtContext):
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