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
        4,1,44,228,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,5,0,40,8,0,
        10,0,12,0,43,9,0,1,0,1,0,1,0,5,0,48,8,0,10,0,12,0,51,9,0,1,0,1,0,
        1,1,1,1,1,1,3,1,58,8,1,1,1,1,1,1,1,3,1,63,8,1,1,1,1,1,1,1,1,2,1,
        2,1,2,5,2,71,8,2,10,2,12,2,74,9,2,1,3,1,3,1,3,1,4,1,4,5,4,81,8,4,
        10,4,12,4,84,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,96,
        8,5,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,3,9,116,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,
        1,11,1,11,1,11,5,11,129,8,11,10,11,12,11,132,9,11,3,11,134,8,11,
        1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,
        1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,
        3,16,162,8,16,1,16,1,16,3,16,166,8,16,1,16,1,16,3,16,170,8,16,1,
        16,1,16,1,16,1,17,1,17,3,17,177,8,17,1,17,1,17,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,5,18,201,8,18,10,18,12,18,204,9,18,3,18,206,8,
        18,1,18,3,18,209,8,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,5,18,223,8,18,10,18,12,18,226,9,18,1,18,0,1,36,
        19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,0,5,1,0,10,
        13,1,0,28,29,1,0,26,27,1,0,19,24,1,0,16,17,244,0,41,1,0,0,0,2,54,
        1,0,0,0,4,67,1,0,0,0,6,75,1,0,0,0,8,78,1,0,0,0,10,95,1,0,0,0,12,
        97,1,0,0,0,14,101,1,0,0,0,16,103,1,0,0,0,18,108,1,0,0,0,20,117,1,
        0,0,0,22,123,1,0,0,0,24,138,1,0,0,0,26,143,1,0,0,0,28,147,1,0,0,
        0,30,151,1,0,0,0,32,157,1,0,0,0,34,174,1,0,0,0,36,208,1,0,0,0,38,
        40,3,2,1,0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,
        0,42,44,1,0,0,0,43,41,1,0,0,0,44,45,5,1,0,0,45,49,3,8,4,0,46,48,
        3,2,1,0,47,46,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,
        50,52,1,0,0,0,51,49,1,0,0,0,52,53,5,0,0,1,53,1,1,0,0,0,54,57,5,7,
        0,0,55,58,3,14,7,0,56,58,5,9,0,0,57,55,1,0,0,0,57,56,1,0,0,0,58,
        59,1,0,0,0,59,60,5,41,0,0,60,62,5,30,0,0,61,63,3,4,2,0,62,61,1,0,
        0,0,62,63,1,0,0,0,63,64,1,0,0,0,64,65,5,31,0,0,65,66,3,8,4,0,66,
        3,1,0,0,0,67,72,3,6,3,0,68,69,5,37,0,0,69,71,3,6,3,0,70,68,1,0,0,
        0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,5,1,0,0,0,74,72,1,
        0,0,0,75,76,3,14,7,0,76,77,5,41,0,0,77,7,1,0,0,0,78,82,5,32,0,0,
        79,81,3,10,5,0,80,79,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,
        0,0,0,83,85,1,0,0,0,84,82,1,0,0,0,85,86,5,33,0,0,86,9,1,0,0,0,87,
        96,3,12,6,0,88,96,3,16,8,0,89,96,3,18,9,0,90,96,3,20,10,0,91,96,
        3,30,15,0,92,96,3,32,16,0,93,96,3,34,17,0,94,96,3,22,11,0,95,87,
        1,0,0,0,95,88,1,0,0,0,95,89,1,0,0,0,95,90,1,0,0,0,95,91,1,0,0,0,
        95,92,1,0,0,0,95,93,1,0,0,0,95,94,1,0,0,0,96,11,1,0,0,0,97,98,3,
        14,7,0,98,99,5,41,0,0,99,100,5,36,0,0,100,13,1,0,0,0,101,102,7,0,
        0,0,102,15,1,0,0,0,103,104,5,41,0,0,104,105,5,25,0,0,105,106,3,36,
        18,0,106,107,5,36,0,0,107,17,1,0,0,0,108,109,5,2,0,0,109,110,5,30,
        0,0,110,111,3,36,18,0,111,112,5,31,0,0,112,115,3,8,4,0,113,114,5,
        3,0,0,114,116,3,8,4,0,115,113,1,0,0,0,115,116,1,0,0,0,116,19,1,0,
        0,0,117,118,5,4,0,0,118,119,5,30,0,0,119,120,3,36,18,0,120,121,5,
        31,0,0,121,122,5,36,0,0,122,21,1,0,0,0,123,124,5,41,0,0,124,133,
        5,30,0,0,125,130,3,36,18,0,126,127,5,37,0,0,127,129,3,36,18,0,128,
        126,1,0,0,0,129,132,1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,
        134,1,0,0,0,132,130,1,0,0,0,133,125,1,0,0,0,133,134,1,0,0,0,134,
        135,1,0,0,0,135,136,5,31,0,0,136,137,5,36,0,0,137,23,1,0,0,0,138,
        139,3,14,7,0,139,140,5,41,0,0,140,141,5,25,0,0,141,142,3,36,18,0,
        142,25,1,0,0,0,143,144,5,41,0,0,144,145,5,25,0,0,145,146,3,36,18,
        0,146,27,1,0,0,0,147,148,5,41,0,0,148,149,5,25,0,0,149,150,3,36,
        18,0,150,29,1,0,0,0,151,152,5,5,0,0,152,153,5,30,0,0,153,154,3,36,
        18,0,154,155,5,31,0,0,155,156,3,8,4,0,156,31,1,0,0,0,157,158,5,6,
        0,0,158,161,5,30,0,0,159,162,3,24,12,0,160,162,3,26,13,0,161,159,
        1,0,0,0,161,160,1,0,0,0,161,162,1,0,0,0,162,163,1,0,0,0,163,165,
        5,36,0,0,164,166,3,36,18,0,165,164,1,0,0,0,165,166,1,0,0,0,166,167,
        1,0,0,0,167,169,5,36,0,0,168,170,3,28,14,0,169,168,1,0,0,0,169,170,
        1,0,0,0,170,171,1,0,0,0,171,172,5,31,0,0,172,173,3,8,4,0,173,33,
        1,0,0,0,174,176,5,8,0,0,175,177,3,36,18,0,176,175,1,0,0,0,176,177,
        1,0,0,0,177,178,1,0,0,0,178,179,5,36,0,0,179,35,1,0,0,0,180,181,
        6,18,-1,0,181,182,5,18,0,0,182,209,3,36,18,14,183,184,5,27,0,0,184,
        209,3,36,18,13,185,186,5,30,0,0,186,187,3,36,18,0,187,188,5,31,0,
        0,188,209,1,0,0,0,189,209,5,38,0,0,190,209,5,39,0,0,191,209,5,40,
        0,0,192,209,5,14,0,0,193,209,5,15,0,0,194,209,5,41,0,0,195,196,5,
        41,0,0,196,205,5,30,0,0,197,202,3,36,18,0,198,199,5,37,0,0,199,201,
        3,36,18,0,200,198,1,0,0,0,201,204,1,0,0,0,202,200,1,0,0,0,202,203,
        1,0,0,0,203,206,1,0,0,0,204,202,1,0,0,0,205,197,1,0,0,0,205,206,
        1,0,0,0,206,207,1,0,0,0,207,209,5,31,0,0,208,180,1,0,0,0,208,183,
        1,0,0,0,208,185,1,0,0,0,208,189,1,0,0,0,208,190,1,0,0,0,208,191,
        1,0,0,0,208,192,1,0,0,0,208,193,1,0,0,0,208,194,1,0,0,0,208,195,
        1,0,0,0,209,224,1,0,0,0,210,211,10,11,0,0,211,212,7,1,0,0,212,223,
        3,36,18,12,213,214,10,10,0,0,214,215,7,2,0,0,215,223,3,36,18,11,
        216,217,10,9,0,0,217,218,7,3,0,0,218,223,3,36,18,10,219,220,10,8,
        0,0,220,221,7,4,0,0,221,223,3,36,18,9,222,210,1,0,0,0,222,213,1,
        0,0,0,222,216,1,0,0,0,222,219,1,0,0,0,223,226,1,0,0,0,224,222,1,
        0,0,0,224,225,1,0,0,0,225,37,1,0,0,0,226,224,1,0,0,0,19,41,49,57,
        62,72,82,95,115,130,133,161,165,169,176,202,205,208,222,224
    ]

class MiniLangParser ( Parser ):

    grammarFileName = "MiniLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "'si'", "'sino'", "'imprime'", 
                     "'mientras'", "'para'", "'funcion'", "'retorna'", "'void'", 
                     "'int'", "'bool'", "'float'", "'string'", "'true'", 
                     "'false'", "'&&'", "'||'", "'!'", "'=='", "<INVALID>", 
                     "'<='", "'>='", "'<'", "'>'", "'='", "'+'", "'-'", 
                     "'*'", "'/'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "';'", "','" ]

    symbolicNames = [ "<INVALID>", "PROGRAM", "SI", "SINO", "IMPRIME", "MIENTRAS", 
                      "PARA", "FUNCION", "RETORNA", "VOID", "INT_T", "BOOL_T", 
                      "FLOAT_T", "STRING_T", "TRUE", "FALSE", "AND", "OR", 
                      "NOT", "EQ", "NEQ", "LE", "GE", "LT", "GT", "ASIGNA", 
                      "SUMA", "RESTA", "MULTI", "DIVIDE", "PARENTESIS_IZQ", 
                      "PARENTESIS_DER", "LLAVE_IZQ", "LLAVE_DER", "CORCHETE_IZQ", 
                      "CORCHETE_DER", "PUNTO_COMA", "COMA", "INT", "FLOAT", 
                      "STRING", "ID", "WS", "LINEA_COMENTARIO", "GRUPO_COMENTARIO" ]

    RULE_program = 0
    RULE_funcionDecl = 1
    RULE_parametros = 2
    RULE_parametro = 3
    RULE_grupo = 4
    RULE_sentencia = 5
    RULE_declaraVariable = 6
    RULE_tipo = 7
    RULE_sentenciaAsigna = 8
    RULE_sentenciaSI = 9
    RULE_sentenciaImprime = 10
    RULE_sentenciaLlamada = 11
    RULE_inicializacionPara = 12
    RULE_asignacionPara = 13
    RULE_actualizacionPara = 14
    RULE_sentenciaMientras = 15
    RULE_sentenciaPara = 16
    RULE_sentenciaRetorna = 17
    RULE_expr = 18

    ruleNames =  [ "program", "funcionDecl", "parametros", "parametro", 
                   "grupo", "sentencia", "declaraVariable", "tipo", "sentenciaAsigna", 
                   "sentenciaSI", "sentenciaImprime", "sentenciaLlamada", 
                   "inicializacionPara", "asignacionPara", "actualizacionPara", 
                   "sentenciaMientras", "sentenciaPara", "sentenciaRetorna", 
                   "expr" ]

    EOF = Token.EOF
    PROGRAM=1
    SI=2
    SINO=3
    IMPRIME=4
    MIENTRAS=5
    PARA=6
    FUNCION=7
    RETORNA=8
    VOID=9
    INT_T=10
    BOOL_T=11
    FLOAT_T=12
    STRING_T=13
    TRUE=14
    FALSE=15
    AND=16
    OR=17
    NOT=18
    EQ=19
    NEQ=20
    LE=21
    GE=22
    LT=23
    GT=24
    ASIGNA=25
    SUMA=26
    RESTA=27
    MULTI=28
    DIVIDE=29
    PARENTESIS_IZQ=30
    PARENTESIS_DER=31
    LLAVE_IZQ=32
    LLAVE_DER=33
    CORCHETE_IZQ=34
    CORCHETE_DER=35
    PUNTO_COMA=36
    COMA=37
    INT=38
    FLOAT=39
    STRING=40
    ID=41
    WS=42
    LINEA_COMENTARIO=43
    GRUPO_COMENTARIO=44

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

        def funcionDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.FuncionDeclContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.FuncionDeclContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 38
                self.funcionDecl()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(MiniLangParser.PROGRAM)
            self.state = 45
            self.grupo()
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 46
                self.funcionDecl()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(MiniLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCION(self):
            return self.getToken(MiniLangParser.FUNCION, 0)

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def PARENTESIS_IZQ(self):
            return self.getToken(MiniLangParser.PARENTESIS_IZQ, 0)

        def PARENTESIS_DER(self):
            return self.getToken(MiniLangParser.PARENTESIS_DER, 0)

        def grupo(self):
            return self.getTypedRuleContext(MiniLangParser.GrupoContext,0)


        def tipo(self):
            return self.getTypedRuleContext(MiniLangParser.TipoContext,0)


        def VOID(self):
            return self.getToken(MiniLangParser.VOID, 0)

        def parametros(self):
            return self.getTypedRuleContext(MiniLangParser.ParametrosContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_funcionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncionDecl" ):
                listener.enterFuncionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncionDecl" ):
                listener.exitFuncionDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncionDecl" ):
                return visitor.visitFuncionDecl(self)
            else:
                return visitor.visitChildren(self)




    def funcionDecl(self):

        localctx = MiniLangParser.FuncionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_funcionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(MiniLangParser.FUNCION)
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11, 12, 13]:
                self.state = 55
                self.tipo()
                pass
            elif token in [9]:
                self.state = 56
                self.match(MiniLangParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 59
            self.match(MiniLangParser.ID)
            self.state = 60
            self.match(MiniLangParser.PARENTESIS_IZQ)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 15360) != 0):
                self.state = 61
                self.parametros()


            self.state = 64
            self.match(MiniLangParser.PARENTESIS_DER)
            self.state = 65
            self.grupo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ParametroContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ParametroContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.COMA)
            else:
                return self.getToken(MiniLangParser.COMA, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros" ):
                return visitor.visitParametros(self)
            else:
                return visitor.visitChildren(self)




    def parametros(self):

        localctx = MiniLangParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.parametro()
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 68
                self.match(MiniLangParser.COMA)
                self.state = 69
                self.parametro()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(MiniLangParser.TipoContext,0)


        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_parametro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametro" ):
                listener.enterParametro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametro" ):
                listener.exitParametro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametro" ):
                return visitor.visitParametro(self)
            else:
                return visitor.visitChildren(self)




    def parametro(self):

        localctx = MiniLangParser.ParametroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parametro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.tipo()
            self.state = 76
            self.match(MiniLangParser.ID)
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
        self.enterRule(localctx, 8, self.RULE_grupo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(MiniLangParser.LLAVE_IZQ)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2199023271284) != 0):
                self.state = 79
                self.sentencia()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
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


        def sentenciaMientras(self):
            return self.getTypedRuleContext(MiniLangParser.SentenciaMientrasContext,0)


        def sentenciaPara(self):
            return self.getTypedRuleContext(MiniLangParser.SentenciaParaContext,0)


        def sentenciaRetorna(self):
            return self.getTypedRuleContext(MiniLangParser.SentenciaRetornaContext,0)


        def sentenciaLlamada(self):
            return self.getTypedRuleContext(MiniLangParser.SentenciaLlamadaContext,0)


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
        self.enterRule(localctx, 10, self.RULE_sentencia)
        try:
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.declaraVariable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.sentenciaAsigna()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 89
                self.sentenciaSI()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 90
                self.sentenciaImprime()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 91
                self.sentenciaMientras()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 92
                self.sentenciaPara()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 93
                self.sentenciaRetorna()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 94
                self.sentenciaLlamada()
                pass


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
        self.enterRule(localctx, 12, self.RULE_declaraVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.tipo()
            self.state = 98
            self.match(MiniLangParser.ID)
            self.state = 99
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

        def FLOAT_T(self):
            return self.getToken(MiniLangParser.FLOAT_T, 0)

        def STRING_T(self):
            return self.getToken(MiniLangParser.STRING_T, 0)

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
        self.enterRule(localctx, 14, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15360) != 0)):
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
        self.enterRule(localctx, 16, self.RULE_sentenciaAsigna)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(MiniLangParser.ID)
            self.state = 104
            self.match(MiniLangParser.ASIGNA)
            self.state = 105
            self.expr(0)
            self.state = 106
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
        self.enterRule(localctx, 18, self.RULE_sentenciaSI)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(MiniLangParser.SI)
            self.state = 109
            self.match(MiniLangParser.PARENTESIS_IZQ)
            self.state = 110
            self.expr(0)
            self.state = 111
            self.match(MiniLangParser.PARENTESIS_DER)
            self.state = 112
            self.grupo()
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 113
                self.match(MiniLangParser.SINO)
                self.state = 114
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
        self.enterRule(localctx, 20, self.RULE_sentenciaImprime)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(MiniLangParser.IMPRIME)
            self.state = 118
            self.match(MiniLangParser.PARENTESIS_IZQ)
            self.state = 119
            self.expr(0)
            self.state = 120
            self.match(MiniLangParser.PARENTESIS_DER)
            self.state = 121
            self.match(MiniLangParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaLlamadaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def PARENTESIS_IZQ(self):
            return self.getToken(MiniLangParser.PARENTESIS_IZQ, 0)

        def PARENTESIS_DER(self):
            return self.getToken(MiniLangParser.PARENTESIS_DER, 0)

        def PUNTO_COMA(self):
            return self.getToken(MiniLangParser.PUNTO_COMA, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.COMA)
            else:
                return self.getToken(MiniLangParser.COMA, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_sentenciaLlamada

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaLlamada" ):
                listener.enterSentenciaLlamada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaLlamada" ):
                listener.exitSentenciaLlamada(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaLlamada" ):
                return visitor.visitSentenciaLlamada(self)
            else:
                return visitor.visitChildren(self)




    def sentenciaLlamada(self):

        localctx = MiniLangParser.SentenciaLlamadaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_sentenciaLlamada)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(MiniLangParser.ID)
            self.state = 124
            self.match(MiniLangParser.PARENTESIS_IZQ)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4124376875008) != 0):
                self.state = 125
                self.expr(0)
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==37:
                    self.state = 126
                    self.match(MiniLangParser.COMA)
                    self.state = 127
                    self.expr(0)
                    self.state = 132
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 135
            self.match(MiniLangParser.PARENTESIS_DER)
            self.state = 136
            self.match(MiniLangParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InicializacionParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(MiniLangParser.TipoContext,0)


        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def ASIGNA(self):
            return self.getToken(MiniLangParser.ASIGNA, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_inicializacionPara

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInicializacionPara" ):
                listener.enterInicializacionPara(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInicializacionPara" ):
                listener.exitInicializacionPara(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInicializacionPara" ):
                return visitor.visitInicializacionPara(self)
            else:
                return visitor.visitChildren(self)




    def inicializacionPara(self):

        localctx = MiniLangParser.InicializacionParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_inicializacionPara)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.tipo()
            self.state = 139
            self.match(MiniLangParser.ID)
            self.state = 140
            self.match(MiniLangParser.ASIGNA)
            self.state = 141
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionParaContext(ParserRuleContext):
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


        def getRuleIndex(self):
            return MiniLangParser.RULE_asignacionPara

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacionPara" ):
                listener.enterAsignacionPara(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacionPara" ):
                listener.exitAsignacionPara(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacionPara" ):
                return visitor.visitAsignacionPara(self)
            else:
                return visitor.visitChildren(self)




    def asignacionPara(self):

        localctx = MiniLangParser.AsignacionParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_asignacionPara)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(MiniLangParser.ID)
            self.state = 144
            self.match(MiniLangParser.ASIGNA)
            self.state = 145
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActualizacionParaContext(ParserRuleContext):
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


        def getRuleIndex(self):
            return MiniLangParser.RULE_actualizacionPara

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActualizacionPara" ):
                listener.enterActualizacionPara(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActualizacionPara" ):
                listener.exitActualizacionPara(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActualizacionPara" ):
                return visitor.visitActualizacionPara(self)
            else:
                return visitor.visitChildren(self)




    def actualizacionPara(self):

        localctx = MiniLangParser.ActualizacionParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_actualizacionPara)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(MiniLangParser.ID)
            self.state = 148
            self.match(MiniLangParser.ASIGNA)
            self.state = 149
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaMientrasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIENTRAS(self):
            return self.getToken(MiniLangParser.MIENTRAS, 0)

        def PARENTESIS_IZQ(self):
            return self.getToken(MiniLangParser.PARENTESIS_IZQ, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def PARENTESIS_DER(self):
            return self.getToken(MiniLangParser.PARENTESIS_DER, 0)

        def grupo(self):
            return self.getTypedRuleContext(MiniLangParser.GrupoContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_sentenciaMientras

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaMientras" ):
                listener.enterSentenciaMientras(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaMientras" ):
                listener.exitSentenciaMientras(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaMientras" ):
                return visitor.visitSentenciaMientras(self)
            else:
                return visitor.visitChildren(self)




    def sentenciaMientras(self):

        localctx = MiniLangParser.SentenciaMientrasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_sentenciaMientras)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(MiniLangParser.MIENTRAS)
            self.state = 152
            self.match(MiniLangParser.PARENTESIS_IZQ)
            self.state = 153
            self.expr(0)
            self.state = 154
            self.match(MiniLangParser.PARENTESIS_DER)
            self.state = 155
            self.grupo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.cond = None # ExprContext

        def PARA(self):
            return self.getToken(MiniLangParser.PARA, 0)

        def PARENTESIS_IZQ(self):
            return self.getToken(MiniLangParser.PARENTESIS_IZQ, 0)

        def PUNTO_COMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.PUNTO_COMA)
            else:
                return self.getToken(MiniLangParser.PUNTO_COMA, i)

        def PARENTESIS_DER(self):
            return self.getToken(MiniLangParser.PARENTESIS_DER, 0)

        def grupo(self):
            return self.getTypedRuleContext(MiniLangParser.GrupoContext,0)


        def inicializacionPara(self):
            return self.getTypedRuleContext(MiniLangParser.InicializacionParaContext,0)


        def asignacionPara(self):
            return self.getTypedRuleContext(MiniLangParser.AsignacionParaContext,0)


        def actualizacionPara(self):
            return self.getTypedRuleContext(MiniLangParser.ActualizacionParaContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_sentenciaPara

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaPara" ):
                listener.enterSentenciaPara(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaPara" ):
                listener.exitSentenciaPara(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaPara" ):
                return visitor.visitSentenciaPara(self)
            else:
                return visitor.visitChildren(self)




    def sentenciaPara(self):

        localctx = MiniLangParser.SentenciaParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_sentenciaPara)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(MiniLangParser.PARA)
            self.state = 158
            self.match(MiniLangParser.PARENTESIS_IZQ)
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11, 12, 13]:
                self.state = 159
                self.inicializacionPara()
                pass
            elif token in [41]:
                self.state = 160
                self.asignacionPara()
                pass
            elif token in [36]:
                pass
            else:
                pass
            self.state = 163
            self.match(MiniLangParser.PUNTO_COMA)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4124376875008) != 0):
                self.state = 164
                localctx.cond = self.expr(0)


            self.state = 167
            self.match(MiniLangParser.PUNTO_COMA)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 168
                self.actualizacionPara()


            self.state = 171
            self.match(MiniLangParser.PARENTESIS_DER)
            self.state = 172
            self.grupo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaRetornaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETORNA(self):
            return self.getToken(MiniLangParser.RETORNA, 0)

        def PUNTO_COMA(self):
            return self.getToken(MiniLangParser.PUNTO_COMA, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_sentenciaRetorna

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaRetorna" ):
                listener.enterSentenciaRetorna(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaRetorna" ):
                listener.exitSentenciaRetorna(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaRetorna" ):
                return visitor.visitSentenciaRetorna(self)
            else:
                return visitor.visitChildren(self)




    def sentenciaRetorna(self):

        localctx = MiniLangParser.SentenciaRetornaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_sentenciaRetorna)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(MiniLangParser.RETORNA)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4124376875008) != 0):
                self.state = 175
                self.expr(0)


            self.state = 178
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


    class StringLitContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(MiniLangParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLit" ):
                listener.enterStringLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLit" ):
                listener.exitStringLit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLit" ):
                return visitor.visitStringLit(self)
            else:
                return visitor.visitChildren(self)


    class FuncCallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)
        def PARENTESIS_IZQ(self):
            return self.getToken(MiniLangParser.PARENTESIS_IZQ, 0)
        def PARENTESIS_DER(self):
            return self.getToken(MiniLangParser.PARENTESIS_DER, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.COMA)
            else:
                return self.getToken(MiniLangParser.COMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCall" ):
                listener.enterFuncCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCall" ):
                listener.exitFuncCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCall" ):
                return visitor.visitFuncCall(self)
            else:
                return visitor.visitChildren(self)


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


    class FloatLitContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(MiniLangParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatLit" ):
                listener.enterFloatLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatLit" ):
                listener.exitFloatLit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatLit" ):
                return visitor.visitFloatLit(self)
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
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                localctx = MiniLangParser.UnaryNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 181
                self.match(MiniLangParser.NOT)
                self.state = 182
                self.expr(14)
                pass

            elif la_ == 2:
                localctx = MiniLangParser.UnaryMinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 183
                self.match(MiniLangParser.RESTA)
                self.state = 184
                self.expr(13)
                pass

            elif la_ == 3:
                localctx = MiniLangParser.ParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 185
                self.match(MiniLangParser.PARENTESIS_IZQ)
                self.state = 186
                self.expr(0)
                self.state = 187
                self.match(MiniLangParser.PARENTESIS_DER)
                pass

            elif la_ == 4:
                localctx = MiniLangParser.IntLitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 189
                self.match(MiniLangParser.INT)
                pass

            elif la_ == 5:
                localctx = MiniLangParser.FloatLitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 190
                self.match(MiniLangParser.FLOAT)
                pass

            elif la_ == 6:
                localctx = MiniLangParser.StringLitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 191
                self.match(MiniLangParser.STRING)
                pass

            elif la_ == 7:
                localctx = MiniLangParser.TrueLitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 192
                self.match(MiniLangParser.TRUE)
                pass

            elif la_ == 8:
                localctx = MiniLangParser.FalseLitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 193
                self.match(MiniLangParser.FALSE)
                pass

            elif la_ == 9:
                localctx = MiniLangParser.IdRefContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 194
                self.match(MiniLangParser.ID)
                pass

            elif la_ == 10:
                localctx = MiniLangParser.FuncCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 195
                self.match(MiniLangParser.ID)
                self.state = 196
                self.match(MiniLangParser.PARENTESIS_IZQ)
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4124376875008) != 0):
                    self.state = 197
                    self.expr(0)
                    self.state = 202
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==37:
                        self.state = 198
                        self.match(MiniLangParser.COMA)
                        self.state = 199
                        self.expr(0)
                        self.state = 204
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 207
                self.match(MiniLangParser.PARENTESIS_DER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 224
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 222
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = MiniLangParser.MulDivContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 210
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 211
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==28 or _la==29):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 212
                        localctx.right = self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = MiniLangParser.AddSubContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 213
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 214
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==26 or _la==27):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 215
                        localctx.right = self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = MiniLangParser.RelationalContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 216
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 217
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33030144) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 218
                        localctx.right = self.expr(10)
                        pass

                    elif la_ == 4:
                        localctx = MiniLangParser.LogicalContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 219
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 220
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 221
                        localctx.right = self.expr(9)
                        pass

             
                self.state = 226
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
        self._predicates[18] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         




