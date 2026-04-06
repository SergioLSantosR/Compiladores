# Generated from grammar/MiniLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniLangParser import MiniLangParser
else:
    from MiniLangParser import MiniLangParser

# This class defines a complete generic visitor for a parse tree produced by MiniLangParser.

class MiniLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniLangParser#programa.
    def visitPrograma(self, ctx:MiniLangParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#cuerpoPrincipal.
    def visitCuerpoPrincipal(self, ctx:MiniLangParser.CuerpoPrincipalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#declaracionFuncion.
    def visitDeclaracionFuncion(self, ctx:MiniLangParser.DeclaracionFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#listaParametros.
    def visitListaParametros(self, ctx:MiniLangParser.ListaParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#parametro.
    def visitParametro(self, ctx:MiniLangParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#bloque.
    def visitBloque(self, ctx:MiniLangParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#sentencia.
    def visitSentencia(self, ctx:MiniLangParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#declaracionVariable.
    def visitDeclaracionVariable(self, ctx:MiniLangParser.DeclaracionVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#tipo.
    def visitTipo(self, ctx:MiniLangParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#asignacion.
    def visitAsignacion(self, ctx:MiniLangParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#condicionalSi.
    def visitCondicionalSi(self, ctx:MiniLangParser.CondicionalSiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#cicloMientras.
    def visitCicloMientras(self, ctx:MiniLangParser.CicloMientrasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#imprimir.
    def visitImprimir(self, ctx:MiniLangParser.ImprimirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#retorno.
    def visitRetorno(self, ctx:MiniLangParser.RetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#Comparacion.
    def visitComparacion(self, ctx:MiniLangParser.ComparacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#Parentesis.
    def visitParentesis(self, ctx:MiniLangParser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#MenosUnario.
    def visitMenosUnario(self, ctx:MiniLangParser.MenosUnarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#MultiplicacionDivision.
    def visitMultiplicacionDivision(self, ctx:MiniLangParser.MultiplicacionDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#OLogico.
    def visitOLogico(self, ctx:MiniLangParser.OLogicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#LiteralEntero.
    def visitLiteralEntero(self, ctx:MiniLangParser.LiteralEnteroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#Igualdad.
    def visitIgualdad(self, ctx:MiniLangParser.IgualdadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#YLogico.
    def visitYLogico(self, ctx:MiniLangParser.YLogicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#LiteralVerdadero.
    def visitLiteralVerdadero(self, ctx:MiniLangParser.LiteralVerdaderoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#SumaResta.
    def visitSumaResta(self, ctx:MiniLangParser.SumaRestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#NegacionLogica.
    def visitNegacionLogica(self, ctx:MiniLangParser.NegacionLogicaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#LlamadaFuncion.
    def visitLlamadaFuncion(self, ctx:MiniLangParser.LlamadaFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#ReferenciaVariable.
    def visitReferenciaVariable(self, ctx:MiniLangParser.ReferenciaVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#LiteralFalso.
    def visitLiteralFalso(self, ctx:MiniLangParser.LiteralFalsoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#listaArgumentos.
    def visitListaArgumentos(self, ctx:MiniLangParser.ListaArgumentosContext):
        return self.visitChildren(ctx)



del MiniLangParser