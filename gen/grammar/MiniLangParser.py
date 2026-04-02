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
        4,1,35,96,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,0,1,1,1,1,5,1,25,8,1,10,1,12,1,28,
        9,1,1,1,1,1,1,2,1,2,1,2,1,2,3,2,36,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,
        5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,56,8,6,1,7,1,7,
        1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,3,8,77,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,
        8,91,8,8,10,8,12,8,94,9,8,1,8,0,1,16,9,0,2,4,6,8,10,12,14,16,0,5,
        1,0,5,6,1,0,21,22,1,0,19,20,1,0,12,17,1,0,9,10,101,0,18,1,0,0,0,
        2,22,1,0,0,0,4,35,1,0,0,0,6,37,1,0,0,0,8,41,1,0,0,0,10,43,1,0,0,
        0,12,48,1,0,0,0,14,57,1,0,0,0,16,76,1,0,0,0,18,19,5,1,0,0,19,20,
        3,2,1,0,20,21,5,0,0,1,21,1,1,0,0,0,22,26,5,25,0,0,23,25,3,4,2,0,
        24,23,1,0,0,0,25,28,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,29,1,
        0,0,0,28,26,1,0,0,0,29,30,5,26,0,0,30,3,1,0,0,0,31,36,3,6,3,0,32,
        36,3,10,5,0,33,36,3,12,6,0,34,36,3,14,7,0,35,31,1,0,0,0,35,32,1,
        0,0,0,35,33,1,0,0,0,35,34,1,0,0,0,36,5,1,0,0,0,37,38,3,8,4,0,38,
        39,5,31,0,0,39,40,5,29,0,0,40,7,1,0,0,0,41,42,7,0,0,0,42,9,1,0,0,
        0,43,44,5,31,0,0,44,45,5,18,0,0,45,46,3,16,8,0,46,47,5,29,0,0,47,
        11,1,0,0,0,48,49,5,2,0,0,49,50,5,23,0,0,50,51,3,16,8,0,51,52,5,24,
        0,0,52,55,3,2,1,0,53,54,5,3,0,0,54,56,3,2,1,0,55,53,1,0,0,0,55,56,
        1,0,0,0,56,13,1,0,0,0,57,58,5,4,0,0,58,59,5,23,0,0,59,60,3,16,8,
        0,60,61,5,24,0,0,61,62,5,29,0,0,62,15,1,0,0,0,63,64,6,8,-1,0,64,
        65,5,11,0,0,65,77,3,16,8,11,66,67,5,20,0,0,67,77,3,16,8,10,68,69,
        5,23,0,0,69,70,3,16,8,0,70,71,5,24,0,0,71,77,1,0,0,0,72,77,5,32,
        0,0,73,77,5,7,0,0,74,77,5,8,0,0,75,77,5,31,0,0,76,63,1,0,0,0,76,
        66,1,0,0,0,76,68,1,0,0,0,76,72,1,0,0,0,76,73,1,0,0,0,76,74,1,0,0,
        0,76,75,1,0,0,0,77,92,1,0,0,0,78,79,10,8,0,0,79,80,7,1,0,0,80,91,
        3,16,8,9,81,82,10,7,0,0,82,83,7,2,0,0,83,91,3,16,8,8,84,85,10,6,
        0,0,85,86,7,3,0,0,86,91,3,16,8,7,87,88,10,5,0,0,88,89,7,4,0,0,89,
        91,3,16,8,6,90,78,1,0,0,0,90,81,1,0,0,0,90,84,1,0,0,0,90,87,1,0,
        0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,17,1,0,0,0,94,92,
        1,0,0,0,6,26,35,55,76,90,92
    ]

class MiniLangParser ( Parser ):

    grammarFileName = "MiniLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "'si'", "'sino'", "'imprime'", 
                     "'int'", "'bool'", "'true'", "'false'", "'&&'", "'||'", 
                     "'!'", "'=='", "<INVALID>", "'<='", "'>='", "'<'", 
                     "'>'", "'='", "'+'", "'-'", "'*'", "'/'", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "PROGRAM", "SI", "SINO", "IMPRIME", "INT_T", 
                      "BOOL_T", "TRUE", "FALSE", "AND", "OR", "NOT", "EQ", 
                      "NEQ", "LE", "GE", "LT", "GT", "ASIGNA", "SUMA", "RESTA", 
                      "MULTI", "DIVIDE", "PARENTESIS_IZQ", "PARENTESIS_DER", 
                      "LLAVE_IZQ", "LLAVE_DER", "CORCHETE_IZQ", "CORCHETE_DER", 
                      "PUNTO_COMA", "COMA", "ID", "INT", "WS", "LINEA_COMENTARIO", 
                      "GRUPO_COMENTARIO" ]

    RULE_program = 0
    RULE_grupo = 1
    RULE_sentencia = 2
    RULE_declaraVariable = 3
    RULE_tipo = 4
    RULE_sentenciaAsigna = 5
    RULE_sentenciaSI = 6
    RULE_sentenciaImprime = 7
    RULE_expr = 8

    ruleNames =  [ "program", "grupo", "sentencia", "declaraVariable", "tipo", 
                   "sentenciaAsigna", "sentenciaSI", "sentenciaImprime", 
                   "expr" ]

    EOF = Token.EOF
    PROGRAM=1
    SI=2
    SINO=3
    IMPRIME=4
    INT_T=5
    BOOL_T=6
    TRUE=7
    FALSE=8
    AND=9
    OR=10
    NOT=11
    EQ=12
    NEQ=13
    LE=14
    GE=15
    LT=16
    GT=17
    ASIGNA=18
    SUMA=19
    RESTA=20
    MULTI=21
    DIVIDE=22
    PARENTESIS_IZQ=23
    PARENTESIS_DER=24
    LLAVE_IZQ=25
    LLAVE_DER=26
    CORCHETE_IZQ=27
    CORCHETE_DER=28
    PUNTO_COMA=29
    COMA=30
    ID=31
    INT=32
    WS=33
    LINEA_COMENTARIO=34
    GRUPO_COMENTARIO=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM(self):
            return self.getToken(MiniLangParser.PROGRAM, 0)

        def grupo(self):
            return self.getTypedRuleContext(MiniLangParser.GrupoContext,0)


        def EOF(self):
            return self.getToken(MiniLangParser.EOF, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(MiniLangParser.PROGRAM)
            self.state = 19
            self.grupo()
            self.state = 20
            self.match(MiniLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GrupoContext(ParserRuleContext):
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
            return MiniLangParser.RULE_grupo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGrupo" ):
                listener.enterGrupo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGrupo" ):
                listener.exitGrupo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrupo" ):
                return visitor.visitGrupo(self)
            else:
                return visitor.visitChildren(self)




    def grupo(self):

        localctx = MiniLangParser.GrupoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_grupo)
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

        def declaraVariable(self):
            return self.getTypedRuleContext(MiniLangParser.DeclaraVariableContext,0)


        def sentenciaAsigna(self):
            return self.getTypedRuleContext(MiniLangParser.SentenciaAsignaContext,0)


        def sentenciaSI(self):
            return self.getTypedRuleContext(MiniLangParser.SentenciaSIContext,0)


        def sentenciaImprime(self):
            return self.getTypedRuleContext(MiniLangParser.SentenciaImprimeContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)

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
                self.declaraVariable()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.sentenciaAsigna()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.sentenciaSI()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 34
                self.sentenciaImprime()
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


    class DeclaraVariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(MiniLangParser.TipoContext,0)


        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def PUNTO_COMA(self):
            return self.getToken(MiniLangParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_declaraVariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaraVariable" ):
                listener.enterDeclaraVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaraVariable" ):
                listener.exitDeclaraVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaraVariable" ):
                return visitor.visitDeclaraVariable(self)
            else:
                return visitor.visitChildren(self)




    def declaraVariable(self):

        localctx = MiniLangParser.DeclaraVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaraVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.tipo()
            self.state = 38
            self.match(MiniLangParser.ID)
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

        def INT_T(self):
            return self.getToken(MiniLangParser.INT_T, 0)

        def BOOL_T(self):
            return self.getToken(MiniLangParser.BOOL_T, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

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


    class SentenciaAsignaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def ASIGNA(self):
            return self.getToken(MiniLangParser.ASIGNA, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def PUNTO_COMA(self):
            return self.getToken(MiniLangParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_sentenciaAsigna

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaAsigna" ):
                listener.enterSentenciaAsigna(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaAsigna" ):
                listener.exitSentenciaAsigna(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaAsigna" ):
                return visitor.visitSentenciaAsigna(self)
            else:
                return visitor.visitChildren(self)




    def sentenciaAsigna(self):

        localctx = MiniLangParser.SentenciaAsignaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_sentenciaAsigna)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(MiniLangParser.ID)
            self.state = 44
            self.match(MiniLangParser.ASIGNA)
            self.state = 45
            self.expr(0)
            self.state = 46
            self.match(MiniLangParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaSIContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(MiniLangParser.SI, 0)

        def PARENTESIS_IZQ(self):
            return self.getToken(MiniLangParser.PARENTESIS_IZQ, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def PARENTESIS_DER(self):
            return self.getToken(MiniLangParser.PARENTESIS_DER, 0)

        def grupo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.GrupoContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.GrupoContext,i)


        def SINO(self):
            return self.getToken(MiniLangParser.SINO, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_sentenciaSI

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaSI" ):
                listener.enterSentenciaSI(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaSI" ):
                listener.exitSentenciaSI(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaSI" ):
                return visitor.visitSentenciaSI(self)
            else:
                return visitor.visitChildren(self)




    def sentenciaSI(self):

        localctx = MiniLangParser.SentenciaSIContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_sentenciaSI)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(MiniLangParser.SI)
            self.state = 49
            self.match(MiniLangParser.PARENTESIS_IZQ)
            self.state = 50
            self.expr(0)
            self.state = 51
            self.match(MiniLangParser.PARENTESIS_DER)
            self.state = 52
            self.grupo()
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 53
                self.match(MiniLangParser.SINO)
                self.state = 54
                self.grupo()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaImprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPRIME(self):
            return self.getToken(MiniLangParser.IMPRIME, 0)

        def PARENTESIS_IZQ(self):
            return self.getToken(MiniLangParser.PARENTESIS_IZQ, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def PARENTESIS_DER(self):
            return self.getToken(MiniLangParser.PARENTESIS_DER, 0)

        def PUNTO_COMA(self):
            return self.getToken(MiniLangParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_sentenciaImprime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaImprime" ):
                listener.enterSentenciaImprime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaImprime" ):
                listener.exitSentenciaImprime(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaImprime" ):
                return visitor.visitSentenciaImprime(self)
            else:
                return visitor.visitChildren(self)




    def sentenciaImprime(self):

        localctx = MiniLangParser.SentenciaImprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_sentenciaImprime)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(MiniLangParser.IMPRIME)
            self.state = 58
            self.match(MiniLangParser.PARENTESIS_IZQ)
            self.state = 59
            self.expr(0)
            self.state = 60
            self.match(MiniLangParser.PARENTESIS_DER)
            self.state = 61
            self.match(MiniLangParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class UnaryNotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(MiniLangParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryNot" ):
                listener.enterUnaryNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryNot" ):
                listener.exitUnaryNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryNot" ):
                return visitor.visitUnaryNot(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)

        def MULTI(self):
            return self.getToken(MiniLangParser.MULTI, 0)
        def DIVIDE(self):
            return self.getToken(MiniLangParser.DIVIDE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)

        def SUMA(self):
            return self.getToken(MiniLangParser.SUMA, 0)
        def RESTA(self):
            return self.getToken(MiniLangParser.RESTA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class RelationalContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)

        def EQ(self):
            return self.getToken(MiniLangParser.EQ, 0)
        def NEQ(self):
            return self.getToken(MiniLangParser.NEQ, 0)
        def LT(self):
            return self.getToken(MiniLangParser.LT, 0)
        def LE(self):
            return self.getToken(MiniLangParser.LE, 0)
        def GT(self):
            return self.getToken(MiniLangParser.GT, 0)
        def GE(self):
            return self.getToken(MiniLangParser.GE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational" ):
                listener.enterRelational(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational" ):
                listener.exitRelational(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational" ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)


    class FalseLitContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(MiniLangParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFalseLit" ):
                listener.enterFalseLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFalseLit" ):
                listener.exitFalseLit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFalseLit" ):
                return visitor.visitFalseLit(self)
            else:
                return visitor.visitChildren(self)


    class LogicalContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)

        def AND(self):
            return self.getToken(MiniLangParser.AND, 0)
        def OR(self):
            return self.getToken(MiniLangParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical" ):
                listener.enterLogical(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical" ):
                listener.exitLogical(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical" ):
                return visitor.visitLogical(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RESTA(self):
            return self.getToken(MiniLangParser.RESTA, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinus" ):
                listener.enterUnaryMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinus" ):
                listener.exitUnaryMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinus" ):
                return visitor.visitUnaryMinus(self)
            else:
                return visitor.visitChildren(self)


    class TrueLitContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(MiniLangParser.TRUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrueLit" ):
                listener.enterTrueLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrueLit" ):
                listener.exitTrueLit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrueLit" ):
                return visitor.visitTrueLit(self)
            else:
                return visitor.visitChildren(self)


    class IdRefContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdRef" ):
                listener.enterIdRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdRef" ):
                listener.exitIdRef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdRef" ):
                return visitor.visitIdRef(self)
            else:
                return visitor.visitChildren(self)


    class IntLitContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(MiniLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntLit" ):
                listener.enterIntLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntLit" ):
                listener.exitIntLit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntLit" ):
                return visitor.visitIntLit(self)
            else:
                return visitor.visitChildren(self)


    class ParenContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PARENTESIS_IZQ(self):
            return self.getToken(MiniLangParser.PARENTESIS_IZQ, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)

        def PARENTESIS_DER(self):
            return self.getToken(MiniLangParser.PARENTESIS_DER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParen" ):
                listener.enterParen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParen" ):
                listener.exitParen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParen" ):
                return visitor.visitParen(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                localctx = MiniLangParser.UnaryNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 64
                self.match(MiniLangParser.NOT)
                self.state = 65
                self.expr(11)
                pass
            elif token in [20]:
                localctx = MiniLangParser.UnaryMinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 66
                self.match(MiniLangParser.RESTA)
                self.state = 67
                self.expr(10)
                pass
            elif token in [23]:
                localctx = MiniLangParser.ParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 68
                self.match(MiniLangParser.PARENTESIS_IZQ)
                self.state = 69
                self.expr(0)
                self.state = 70
                self.match(MiniLangParser.PARENTESIS_DER)
                pass
            elif token in [32]:
                localctx = MiniLangParser.IntLitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 72
                self.match(MiniLangParser.INT)
                pass
            elif token in [7]:
                localctx = MiniLangParser.TrueLitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 73
                self.match(MiniLangParser.TRUE)
                pass
            elif token in [8]:
                localctx = MiniLangParser.FalseLitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 74
                self.match(MiniLangParser.FALSE)
                pass
            elif token in [31]:
                localctx = MiniLangParser.IdRefContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 75
                self.match(MiniLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 92
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 90
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = MiniLangParser.MulDivContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 78
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 79
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 80
                        localctx.right = self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = MiniLangParser.AddSubContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 81
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 82
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 83
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = MiniLangParser.RelationalContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 84
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 85
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 258048) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 86
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = MiniLangParser.LogicalContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 87
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 88
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 89
                        localctx.right = self.expr(6)
                        pass

             
                self.state = 94
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
        self._predicates[8] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         




