# Generated from gramatica_v3.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramatica_v3Parser import gramatica_v3Parser
else:
    from gramatica_v3Parser import gramatica_v3Parser

# This class defines a complete generic visitor for a parse tree produced by gramatica_v3Parser.

class gramatica_v3Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramatica_v3Parser#programa.
    def visitPrograma(self, ctx:gramatica_v3Parser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#funcionDeclaracion.
    def visitFuncionDeclaracion(self, ctx:gramatica_v3Parser.FuncionDeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#parametros.
    def visitParametros(self, ctx:gramatica_v3Parser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#parametro.
    def visitParametro(self, ctx:gramatica_v3Parser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#bloque.
    def visitBloque(self, ctx:gramatica_v3Parser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#sentencia.
    def visitSentencia(self, ctx:gramatica_v3Parser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#declaracionVariable.
    def visitDeclaracionVariable(self, ctx:gramatica_v3Parser.DeclaracionVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#literalArreglo.
    def visitLiteralArreglo(self, ctx:gramatica_v3Parser.LiteralArregloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#accesoArreglo.
    def visitAccesoArreglo(self, ctx:gramatica_v3Parser.AccesoArregloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#asignacionArreglo.
    def visitAsignacionArreglo(self, ctx:gramatica_v3Parser.AsignacionArregloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#tipo.
    def visitTipo(self, ctx:gramatica_v3Parser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#asignacion.
    def visitAsignacion(self, ctx:gramatica_v3Parser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#condicionalSi.
    def visitCondicionalSi(self, ctx:gramatica_v3Parser.CondicionalSiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#impresion.
    def visitImpresion(self, ctx:gramatica_v3Parser.ImpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#llamadaFuncion.
    def visitLlamadaFuncion(self, ctx:gramatica_v3Parser.LlamadaFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#inicializacionPara.
    def visitInicializacionPara(self, ctx:gramatica_v3Parser.InicializacionParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#asignacionPara.
    def visitAsignacionPara(self, ctx:gramatica_v3Parser.AsignacionParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#actualizacionPara.
    def visitActualizacionPara(self, ctx:gramatica_v3Parser.ActualizacionParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#cicloMientras.
    def visitCicloMientras(self, ctx:gramatica_v3Parser.CicloMientrasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#cicloPara.
    def visitCicloPara(self, ctx:gramatica_v3Parser.CicloParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#sentenciaRetorna.
    def visitSentenciaRetorna(self, ctx:gramatica_v3Parser.SentenciaRetornaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#sentenciaBreak.
    def visitSentenciaBreak(self, ctx:gramatica_v3Parser.SentenciaBreakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#sentenciaContinue.
    def visitSentenciaContinue(self, ctx:gramatica_v3Parser.SentenciaContinueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#sentenciaImportar.
    def visitSentenciaImportar(self, ctx:gramatica_v3Parser.SentenciaImportarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#LiteralCadena.
    def visitLiteralCadena(self, ctx:gramatica_v3Parser.LiteralCadenaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#Parentesis.
    def visitParentesis(self, ctx:gramatica_v3Parser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#MenosUnario.
    def visitMenosUnario(self, ctx:gramatica_v3Parser.MenosUnarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#LlamadaFuncionExpr.
    def visitLlamadaFuncionExpr(self, ctx:gramatica_v3Parser.LlamadaFuncionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#LiteralEntero.
    def visitLiteralEntero(self, ctx:gramatica_v3Parser.LiteralEnteroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#LiteralVerdadero.
    def visitLiteralVerdadero(self, ctx:gramatica_v3Parser.LiteralVerdaderoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#SumaResta.
    def visitSumaResta(self, ctx:gramatica_v3Parser.SumaRestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#LiteralFlotante.
    def visitLiteralFlotante(self, ctx:gramatica_v3Parser.LiteralFlotanteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#NegacionLogica.
    def visitNegacionLogica(self, ctx:gramatica_v3Parser.NegacionLogicaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#Relacional.
    def visitRelacional(self, ctx:gramatica_v3Parser.RelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#ReferenciaVariable.
    def visitReferenciaVariable(self, ctx:gramatica_v3Parser.ReferenciaVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#LiteralFalso.
    def visitLiteralFalso(self, ctx:gramatica_v3Parser.LiteralFalsoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#AccesoArregloExpr.
    def visitAccesoArregloExpr(self, ctx:gramatica_v3Parser.AccesoArregloExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#MultiplicacionDivisionModulo.
    def visitMultiplicacionDivisionModulo(self, ctx:gramatica_v3Parser.MultiplicacionDivisionModuloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#Logica.
    def visitLogica(self, ctx:gramatica_v3Parser.LogicaContext):
        return self.visitChildren(ctx)



del gramatica_v3Parser