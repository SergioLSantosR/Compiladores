# Generated from grammar/MiniLang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,35,102,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,0,1,1,1,1,5,1,25,8,1,10,1,12,1,28,
        9,1,1,1,1,1,1,2,1,2,1,2,1,2,3,2,36,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,
        5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,56,8,6,1,7,1,7,
        1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,3,8,77,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,5,8,97,8,8,10,8,12,8,100,9,8,1,8,0,1,16,9,
        0,2,4,6,8,10,12,14,16,0,5,1,0,5,6,1,0,21,22,1,0,19,20,1,0,14,17,
        1,0,12,13,109,0,18,1,0,0,0,2,22,1,0,0,0,4,35,1,0,0,0,6,37,1,0,0,
        0,8,41,1,0,0,0,10,43,1,0,0,0,12,48,1,0,0,0,14,57,1,0,0,0,16,76,1,
        0,0,0,18,19,5,1,0,0,19,20,3,2,1,0,20,21,5,0,0,1,21,1,1,0,0,0,22,
        26,5,25,0,0,23,25,3,4,2,0,24,23,1,0,0,0,25,28,1,0,0,0,26,24,1,0,
        0,0,26,27,1,0,0,0,27,29,1,0,0,0,28,26,1,0,0,0,29,30,5,26,0,0,30,
        3,1,0,0,0,31,36,3,6,3,0,32,36,3,10,5,0,33,36,3,12,6,0,34,36,3,14,
        7,0,35,31,1,0,0,0,35,32,1,0,0,0,35,33,1,0,0,0,35,34,1,0,0,0,36,5,
        1,0,0,0,37,38,3,8,4,0,38,39,5,31,0,0,39,40,5,29,0,0,40,7,1,0,0,0,
        41,42,7,0,0,0,42,9,1,0,0,0,43,44,5,31,0,0,44,45,5,18,0,0,45,46,3,
        16,8,0,46,47,5,29,0,0,47,11,1,0,0,0,48,49,5,2,0,0,49,50,5,23,0,0,
        50,51,3,16,8,0,51,52,5,24,0,0,52,55,3,2,1,0,53,54,5,3,0,0,54,56,
        3,2,1,0,55,53,1,0,0,0,55,56,1,0,0,0,56,13,1,0,0,0,57,58,5,4,0,0,
        58,59,5,23,0,0,59,60,3,16,8,0,60,61,5,24,0,0,61,62,5,29,0,0,62,15,
        1,0,0,0,63,64,6,8,-1,0,64,65,5,11,0,0,65,77,3,16,8,13,66,67,5,20,
        0,0,67,77,3,16,8,12,68,69,5,23,0,0,69,70,3,16,8,0,70,71,5,24,0,0,
        71,77,1,0,0,0,72,77,5,32,0,0,73,77,5,7,0,0,74,77,5,8,0,0,75,77,5,
        31,0,0,76,63,1,0,0,0,76,66,1,0,0,0,76,68,1,0,0,0,76,72,1,0,0,0,76,
        73,1,0,0,0,76,74,1,0,0,0,76,75,1,0,0,0,77,98,1,0,0,0,78,79,10,10,
        0,0,79,80,7,1,0,0,80,97,3,16,8,11,81,82,10,9,0,0,82,83,7,2,0,0,83,
        97,3,16,8,10,84,85,10,8,0,0,85,86,7,3,0,0,86,97,3,16,8,9,87,88,10,
        7,0,0,88,89,7,4,0,0,89,97,3,16,8,8,90,91,10,6,0,0,91,92,5,9,0,0,
        92,97,3,16,8,7,93,94,10,5,0,0,94,95,5,10,0,0,95,97,3,16,8,6,96,78,
        1,0,0,0,96,81,1,0,0,0,96,84,1,0,0,0,96,87,1,0,0,0,96,90,1,0,0,0,
        96,93,1,0,0,0,97,100,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,17,1,
        0,0,0,100,98,1,0,0,0,6,26,35,55,76,96,98
    ]

class MiniLangParser ( Parser ):

    grammarFileName = "MiniLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "'if'", "'else'", "'print'", 
                     "'int'", "'bool'", "'true'", "'false'", "'&&'", "'||'", 
                     "'!'", "'=='", "<INVALID>", "'<='", "'>='", "'<'", 
                     "'>'", "'='", "'+'", "'-'", "'*'", "'/'", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "PROGRAMA", "SI", "SINO", "IMPRIMIR", 
                      "TIPO_ENTERO", "TIPO_BOOL", "VERDADERO", "FALSO", 
                      "Y_LOGICO", "O_LOGICO", "NEGACION", "IGUAL", "DIFERENTE", 
                      "MENOR_IGUAL", "MAYOR_IGUAL", "MENOR_QUE", "MAYOR_QUE", 
                      "ASIGNACION", "SUMA", "RESTA", "MULTIPLICACION", "DIVISION", 
                      "PAREN_IZQ", "PAREN_DER", "LLAVE_IZQ", "LLAVE_DER", 
                      "CORCHETE_IZQ", "CORCHETE_DER", "PUNTO_COMA", "COMA", 
                      "IDENTIFICADOR", "ENTERO", "ESPACIO", "COMENTARIO_LINEA", 
                      "COMENTARIO_BLOQUE" ]

    RULE_programa = 0
    RULE_bloque = 1
    RULE_sentencia = 2
    RULE_declaracionVariable = 3
    RULE_tipo = 4
    RULE_asignacion = 5
    RULE_condicionalSi = 6
    RULE_imprimir = 7
    RULE_expresion = 8

    ruleNames =  [ "programa", "bloque", "sentencia", "declaracionVariable", 
                   "tipo", "asignacion", "condicionalSi", "imprimir", "expresion" ]

    EOF = Token.EOF
    PROGRAMA=1
    SI=2
    SINO=3
    IMPRIMIR=4
    TIPO_ENTERO=5
    TIPO_BOOL=6
    VERDADERO=7
    FALSO=8
    Y_LOGICO=9
    O_LOGICO=10
    NEGACION=11
    IGUAL=12
    DIFERENTE=13
    MENOR_IGUAL=14
    MAYOR_IGUAL=15
    MENOR_QUE=16
    MAYOR_QUE=17
    ASIGNACION=18
    SUMA=19
    RESTA=20
    MULTIPLICACION=21
    DIVISION=22
    PAREN_IZQ=23
    PAREN_DER=24
    LLAVE_IZQ=25
    LLAVE_DER=26
    CORCHETE_IZQ=27
    CORCHETE_DER=28
    PUNTO_COMA=29
    COMA=30
    IDENTIFICADOR=31
    ENTERO=32
    ESPACIO=33
    COMENTARIO_LINEA=34
    COMENTARIO_BLOQUE=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAMA(self):
            return self.getToken(MiniLangParser.PROGRAMA, 0)

        def bloque(self):
            return self.getTypedRuleContext(MiniLangParser.BloqueContext,0)


        def EOF(self):
            return self.getToken(MiniLangParser.EOF, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_programa

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = MiniLangParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(MiniLangParser.PROGRAMA)
            self.state = 19
            self.bloque()
            self.state = 20
            self.match(MiniLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLAVE_IZQ(self):
            return self.getToken(MiniLangParser.LLAVE_IZQ, 0)

        def LLAVE_DER(self):
            return self.getToken(MiniLangParser.LLAVE_DER, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.SentenciaContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_bloque

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = MiniLangParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(MiniLangParser.LLAVE_IZQ)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2147483764) != 0):
                self.state = 23
                self.sentencia()
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self.match(MiniLangParser.LLAVE_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracionVariable(self):
            return self.getTypedRuleContext(MiniLangParser.DeclaracionVariableContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(MiniLangParser.AsignacionContext,0)


        def condicionalSi(self):
            return self.getTypedRuleContext(MiniLangParser.CondicionalSiContext,0)


        def imprimir(self):
            return self.getTypedRuleContext(MiniLangParser.ImprimirContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_sentencia

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = MiniLangParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sentencia)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.declaracionVariable()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.asignacion()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.condicionalSi()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 34
                self.imprimir()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionVariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(MiniLangParser.TipoContext,0)


        def IDENTIFICADOR(self):
            return self.getToken(MiniLangParser.IDENTIFICADOR, 0)

        def PUNTO_COMA(self):
            return self.getToken(MiniLangParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_declaracionVariable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionVariable" ):
                return visitor.visitDeclaracionVariable(self)
            else:
                return visitor.visitChildren(self)




    def declaracionVariable(self):

        localctx = MiniLangParser.DeclaracionVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracionVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.tipo()
            self.state = 38
            self.match(MiniLangParser.IDENTIFICADOR)
            self.state = 39
            self.match(MiniLangParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIPO_ENTERO(self):
            return self.getToken(MiniLangParser.TIPO_ENTERO, 0)

        def TIPO_BOOL(self):
            return self.getToken(MiniLangParser.TIPO_BOOL, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_tipo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = MiniLangParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(MiniLangParser.IDENTIFICADOR, 0)

        def ASIGNACION(self):
            return self.getToken(MiniLangParser.ASIGNACION, 0)

        def expresion(self):
            return self.getTypedRuleContext(MiniLangParser.ExpresionContext,0)


        def PUNTO_COMA(self):
            return self.getToken(MiniLangParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_asignacion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = MiniLangParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(MiniLangParser.IDENTIFICADOR)
            self.state = 44
            self.match(MiniLangParser.ASIGNACION)
            self.state = 45
            self.expresion(0)
            self.state = 46
            self.match(MiniLangParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalSiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(MiniLangParser.SI, 0)

        def PAREN_IZQ(self):
            return self.getToken(MiniLangParser.PAREN_IZQ, 0)

        def expresion(self):
            return self.getTypedRuleContext(MiniLangParser.ExpresionContext,0)


        def PAREN_DER(self):
            return self.getToken(MiniLangParser.PAREN_DER, 0)

        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.BloqueContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.BloqueContext,i)


        def SINO(self):
            return self.getToken(MiniLangParser.SINO, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_condicionalSi

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicionalSi" ):
                return visitor.visitCondicionalSi(self)
            else:
                return visitor.visitChildren(self)




    def condicionalSi(self):

        localctx = MiniLangParser.CondicionalSiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condicionalSi)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(MiniLangParser.SI)
            self.state = 49
            self.match(MiniLangParser.PAREN_IZQ)
            self.state = 50
            self.expresion(0)
            self.state = 51
            self.match(MiniLangParser.PAREN_DER)
            self.state = 52
            self.bloque()
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 53
                self.match(MiniLangParser.SINO)
                self.state = 54
                self.bloque()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImprimirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPRIMIR(self):
            return self.getToken(MiniLangParser.IMPRIMIR, 0)

        def PAREN_IZQ(self):
            return self.getToken(MiniLangParser.PAREN_IZQ, 0)

        def expresion(self):
            return self.getTypedRuleContext(MiniLangParser.ExpresionContext,0)


        def PAREN_DER(self):
            return self.getToken(MiniLangParser.PAREN_DER, 0)

        def PUNTO_COMA(self):
            return self.getToken(MiniLangParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_imprimir

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImprimir" ):
                return visitor.visitImprimir(self)
            else:
                return visitor.visitChildren(self)




    def imprimir(self):

        localctx = MiniLangParser.ImprimirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_imprimir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(MiniLangParser.IMPRIMIR)
            self.state = 58
            self.match(MiniLangParser.PAREN_IZQ)
            self.state = 59
            self.expresion(0)
            self.state = 60
            self.match(MiniLangParser.PAREN_DER)
            self.state = 61
            self.match(MiniLangParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLangParser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ComparacionContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExpresionContext
            super().__init__(parser)
            self.izq = None # ExpresionContext
            self.op = None # Token
            self.der = None # ExpresionContext
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExpresionContext,i)

        def MENOR_QUE(self):
            return self.getToken(MiniLangParser.MENOR_QUE, 0)
        def MENOR_IGUAL(self):
            return self.getToken(MiniLangParser.MENOR_IGUAL, 0)
        def MAYOR_QUE(self):
            return self.getToken(MiniLangParser.MAYOR_QUE, 0)
        def MAYOR_IGUAL(self):
            return self.getToken(MiniLangParser.MAYOR_IGUAL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparacion" ):
                return visitor.visitComparacion(self)
            else:
                return visitor.visitChildren(self)


    class ParentesisContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PAREN_IZQ(self):
            return self.getToken(MiniLangParser.PAREN_IZQ, 0)
        def expresion(self):
            return self.getTypedRuleContext(MiniLangParser.ExpresionContext,0)

        def PAREN_DER(self):
            return self.getToken(MiniLangParser.PAREN_DER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentesis" ):
                return visitor.visitParentesis(self)
            else:
                return visitor.visitChildren(self)


    class MenosUnarioContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RESTA(self):
            return self.getToken(MiniLangParser.RESTA, 0)
        def expresion(self):
            return self.getTypedRuleContext(MiniLangParser.ExpresionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMenosUnario" ):
                return visitor.visitMenosUnario(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicacionDivisionContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExpresionContext
            super().__init__(parser)
            self.izq = None # ExpresionContext
            self.op = None # Token
            self.der = None # ExpresionContext
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExpresionContext,i)

        def MULTIPLICACION(self):
            return self.getToken(MiniLangParser.MULTIPLICACION, 0)
        def DIVISION(self):
            return self.getToken(MiniLangParser.DIVISION, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicacionDivision" ):
                return visitor.visitMultiplicacionDivision(self)
            else:
                return visitor.visitChildren(self)


    class OLogicoContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExpresionContext
            super().__init__(parser)
            self.izq = None # ExpresionContext
            self.der = None # ExpresionContext
            self.copyFrom(ctx)

        def O_LOGICO(self):
            return self.getToken(MiniLangParser.O_LOGICO, 0)
        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExpresionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOLogico" ):
                return visitor.visitOLogico(self)
            else:
                return visitor.visitChildren(self)


    class LiteralEnteroContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ENTERO(self):
            return self.getToken(MiniLangParser.ENTERO, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralEntero" ):
                return visitor.visitLiteralEntero(self)
            else:
                return visitor.visitChildren(self)


    class IgualdadContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExpresionContext
            super().__init__(parser)
            self.izq = None # ExpresionContext
            self.op = None # Token
            self.der = None # ExpresionContext
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExpresionContext,i)

        def IGUAL(self):
            return self.getToken(MiniLangParser.IGUAL, 0)
        def DIFERENTE(self):
            return self.getToken(MiniLangParser.DIFERENTE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgualdad" ):
                return visitor.visitIgualdad(self)
            else:
                return visitor.visitChildren(self)


    class YLogicoContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExpresionContext
            super().__init__(parser)
            self.izq = None # ExpresionContext
            self.der = None # ExpresionContext
            self.copyFrom(ctx)

        def Y_LOGICO(self):
            return self.getToken(MiniLangParser.Y_LOGICO, 0)
        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExpresionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitYLogico" ):
                return visitor.visitYLogico(self)
            else:
                return visitor.visitChildren(self)


    class LiteralVerdaderoContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VERDADERO(self):
            return self.getToken(MiniLangParser.VERDADERO, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralVerdadero" ):
                return visitor.visitLiteralVerdadero(self)
            else:
                return visitor.visitChildren(self)


    class SumaRestaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExpresionContext
            super().__init__(parser)
            self.izq = None # ExpresionContext
            self.op = None # Token
            self.der = None # ExpresionContext
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExpresionContext,i)

        def SUMA(self):
            return self.getToken(MiniLangParser.SUMA, 0)
        def RESTA(self):
            return self.getToken(MiniLangParser.RESTA, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumaResta" ):
                return visitor.visitSumaResta(self)
            else:
                return visitor.visitChildren(self)


    class NegacionLogicaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEGACION(self):
            return self.getToken(MiniLangParser.NEGACION, 0)
        def expresion(self):
            return self.getTypedRuleContext(MiniLangParser.ExpresionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegacionLogica" ):
                return visitor.visitNegacionLogica(self)
            else:
                return visitor.visitChildren(self)


    class ReferenciaVariableContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFICADOR(self):
            return self.getToken(MiniLangParser.IDENTIFICADOR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReferenciaVariable" ):
                return visitor.visitReferenciaVariable(self)
            else:
                return visitor.visitChildren(self)


    class LiteralFalsoContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSO(self):
            return self.getToken(MiniLangParser.FALSO, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralFalso" ):
                return visitor.visitLiteralFalso(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniLangParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                localctx = MiniLangParser.NegacionLogicaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 64
                self.match(MiniLangParser.NEGACION)
                self.state = 65
                self.expresion(13)
                pass
            elif token in [20]:
                localctx = MiniLangParser.MenosUnarioContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 66
                self.match(MiniLangParser.RESTA)
                self.state = 67
                self.expresion(12)
                pass
            elif token in [23]:
                localctx = MiniLangParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 68
                self.match(MiniLangParser.PAREN_IZQ)
                self.state = 69
                self.expresion(0)
                self.state = 70
                self.match(MiniLangParser.PAREN_DER)
                pass
            elif token in [32]:
                localctx = MiniLangParser.LiteralEnteroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 72
                self.match(MiniLangParser.ENTERO)
                pass
            elif token in [7]:
                localctx = MiniLangParser.LiteralVerdaderoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 73
                self.match(MiniLangParser.VERDADERO)
                pass
            elif token in [8]:
                localctx = MiniLangParser.LiteralFalsoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 74
                self.match(MiniLangParser.FALSO)
                pass
            elif token in [31]:
                localctx = MiniLangParser.ReferenciaVariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 75
                self.match(MiniLangParser.IDENTIFICADOR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 98
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 96
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = MiniLangParser.MultiplicacionDivisionContext(self, MiniLangParser.ExpresionContext(self, _parentctx, _parentState))
                        localctx.izq = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 78
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 79
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 80
                        localctx.der = self.expresion(11)
                        pass

                    elif la_ == 2:
                        localctx = MiniLangParser.SumaRestaContext(self, MiniLangParser.ExpresionContext(self, _parentctx, _parentState))
                        localctx.izq = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 81
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 82
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 83
                        localctx.der = self.expresion(10)
                        pass

                    elif la_ == 3:
                        localctx = MiniLangParser.ComparacionContext(self, MiniLangParser.ExpresionContext(self, _parentctx, _parentState))
                        localctx.izq = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 84
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 85
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 86
                        localctx.der = self.expresion(9)
                        pass

                    elif la_ == 4:
                        localctx = MiniLangParser.IgualdadContext(self, MiniLangParser.ExpresionContext(self, _parentctx, _parentState))
                        localctx.izq = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 87
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 88
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 89
                        localctx.der = self.expresion(8)
                        pass

                    elif la_ == 5:
                        localctx = MiniLangParser.YLogicoContext(self, MiniLangParser.ExpresionContext(self, _parentctx, _parentState))
                        localctx.izq = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 90
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 91
                        self.match(MiniLangParser.Y_LOGICO)
                        self.state = 92
                        localctx.der = self.expresion(7)
                        pass

                    elif la_ == 6:
                        localctx = MiniLangParser.OLogicoContext(self, MiniLangParser.ExpresionContext(self, _parentctx, _parentState))
                        localctx.izq = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 93
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 94
                        self.match(MiniLangParser.O_LOGICO)
                        self.state = 95
                        localctx.der = self.expresion(6)
                        pass

             
                self.state = 100
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         




