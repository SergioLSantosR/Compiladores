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


    # Visit a parse tree produced by MiniLangParser#funcionDeclaracion.
    def visitFuncionDeclaracion(self, ctx:MiniLangParser.FuncionDeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#parametros.
    def visitParametros(self, ctx:MiniLangParser.ParametrosContext):
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


    # Visit a parse tree produced by MiniLangParser#literalArreglo.
    def visitLiteralArreglo(self, ctx:MiniLangParser.LiteralArregloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#accesoArreglo.
    def visitAccesoArreglo(self, ctx:MiniLangParser.AccesoArregloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#asignacionArreglo.
    def visitAsignacionArreglo(self, ctx:MiniLangParser.AsignacionArregloContext):
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


    # Visit a parse tree produced by MiniLangParser#impresion.
    def visitImpresion(self, ctx:MiniLangParser.ImpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#llamadaFuncion.
    def visitLlamadaFuncion(self, ctx:MiniLangParser.LlamadaFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#inicializacionPara.
    def visitInicializacionPara(self, ctx:MiniLangParser.InicializacionParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#asignacionPara.
    def visitAsignacionPara(self, ctx:MiniLangParser.AsignacionParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#actualizacionPara.
    def visitActualizacionPara(self, ctx:MiniLangParser.ActualizacionParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#cicloMientras.
    def visitCicloMientras(self, ctx:MiniLangParser.CicloMientrasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#cicloPara.
    def visitCicloPara(self, ctx:MiniLangParser.CicloParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#sentenciaRetorna.
    def visitSentenciaRetorna(self, ctx:MiniLangParser.SentenciaRetornaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#sentenciaBreak.
    def visitSentenciaBreak(self, ctx:MiniLangParser.SentenciaBreakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#sentenciaContinue.
    def visitSentenciaContinue(self, ctx:MiniLangParser.SentenciaContinueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#sentenciaImportar.
    def visitSentenciaImportar(self, ctx:MiniLangParser.SentenciaImportarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#LiteralCadena.
    def visitLiteralCadena(self, ctx:MiniLangParser.LiteralCadenaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#Parentesis.
    def visitParentesis(self, ctx:MiniLangParser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#MenosUnario.
    def visitMenosUnario(self, ctx:MiniLangParser.MenosUnarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#LlamadaFuncionExpr.
    def visitLlamadaFuncionExpr(self, ctx:MiniLangParser.LlamadaFuncionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#LiteralEntero.
    def visitLiteralEntero(self, ctx:MiniLangParser.LiteralEnteroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#LiteralVerdadero.
    def visitLiteralVerdadero(self, ctx:MiniLangParser.LiteralVerdaderoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#SumaResta.
    def visitSumaResta(self, ctx:MiniLangParser.SumaRestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#LiteralFlotante.
    def visitLiteralFlotante(self, ctx:MiniLangParser.LiteralFlotanteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#NegacionLogica.
    def visitNegacionLogica(self, ctx:MiniLangParser.NegacionLogicaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#Relacional.
    def visitRelacional(self, ctx:MiniLangParser.RelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#ReferenciaVariable.
    def visitReferenciaVariable(self, ctx:MiniLangParser.ReferenciaVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#LiteralFalso.
    def visitLiteralFalso(self, ctx:MiniLangParser.LiteralFalsoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#AccesoArregloExpr.
    def visitAccesoArregloExpr(self, ctx:MiniLangParser.AccesoArregloExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#MultiplicacionDivisionModulo.
    def visitMultiplicacionDivisionModulo(self, ctx:MiniLangParser.MultiplicacionDivisionModuloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#Logica.
    def visitLogica(self, ctx:MiniLangParser.LogicaContext):
        return self.visitChildren(ctx)



del MiniLangParser