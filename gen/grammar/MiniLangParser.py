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
        4,1,43,189,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,5,0,35,8,0,10,0,12,0,38,9,0,1,0,1,0,
        1,0,1,1,1,1,3,1,45,8,1,1,1,1,1,1,1,3,1,50,8,1,1,1,1,1,1,1,1,2,1,
        2,1,2,5,2,58,8,2,10,2,12,2,61,9,2,1,3,1,3,1,3,1,4,1,4,5,4,68,8,4,
        10,4,12,4,71,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,82,8,5,
        1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,3,9,102,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,3,11,
        112,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,3,13,123,8,
        13,1,13,1,13,3,13,127,8,13,1,13,1,13,3,13,131,8,13,1,13,1,13,1,13,
        1,14,1,14,3,14,138,8,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,5,15,162,8,15,10,15,12,15,165,9,15,3,15,167,8,15,1,15,3,15,
        170,8,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,5,15,184,8,15,10,15,12,15,187,9,15,1,15,0,1,30,16,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,0,5,1,0,9,12,1,0,27,28,1,0,25,26,
        1,0,18,23,1,0,15,16,204,0,32,1,0,0,0,2,42,1,0,0,0,4,54,1,0,0,0,6,
        62,1,0,0,0,8,65,1,0,0,0,10,81,1,0,0,0,12,83,1,0,0,0,14,87,1,0,0,
        0,16,89,1,0,0,0,18,94,1,0,0,0,20,103,1,0,0,0,22,111,1,0,0,0,24,113,
        1,0,0,0,26,119,1,0,0,0,28,135,1,0,0,0,30,169,1,0,0,0,32,36,5,1,0,
        0,33,35,3,2,1,0,34,33,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,
        1,0,0,0,37,39,1,0,0,0,38,36,1,0,0,0,39,40,3,8,4,0,40,41,5,0,0,1,
        41,1,1,0,0,0,42,44,5,7,0,0,43,45,3,14,7,0,44,43,1,0,0,0,44,45,1,
        0,0,0,45,46,1,0,0,0,46,47,5,40,0,0,47,49,5,29,0,0,48,50,3,4,2,0,
        49,48,1,0,0,0,49,50,1,0,0,0,50,51,1,0,0,0,51,52,5,30,0,0,52,53,3,
        8,4,0,53,3,1,0,0,0,54,59,3,6,3,0,55,56,5,36,0,0,56,58,3,6,3,0,57,
        55,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,5,1,0,0,
        0,61,59,1,0,0,0,62,63,3,14,7,0,63,64,5,40,0,0,64,7,1,0,0,0,65,69,
        5,31,0,0,66,68,3,10,5,0,67,66,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,
        0,69,70,1,0,0,0,70,72,1,0,0,0,71,69,1,0,0,0,72,73,5,32,0,0,73,9,
        1,0,0,0,74,82,3,12,6,0,75,82,3,16,8,0,76,82,3,18,9,0,77,82,3,20,
        10,0,78,82,3,24,12,0,79,82,3,26,13,0,80,82,3,28,14,0,81,74,1,0,0,
        0,81,75,1,0,0,0,81,76,1,0,0,0,81,77,1,0,0,0,81,78,1,0,0,0,81,79,
        1,0,0,0,81,80,1,0,0,0,82,11,1,0,0,0,83,84,3,14,7,0,84,85,5,40,0,
        0,85,86,5,35,0,0,86,13,1,0,0,0,87,88,7,0,0,0,88,15,1,0,0,0,89,90,
        5,40,0,0,90,91,5,24,0,0,91,92,3,30,15,0,92,93,5,35,0,0,93,17,1,0,
        0,0,94,95,5,2,0,0,95,96,5,29,0,0,96,97,3,30,15,0,97,98,5,30,0,0,
        98,101,3,8,4,0,99,100,5,3,0,0,100,102,3,8,4,0,101,99,1,0,0,0,101,
        102,1,0,0,0,102,19,1,0,0,0,103,104,5,4,0,0,104,105,5,29,0,0,105,
        106,3,30,15,0,106,107,5,30,0,0,107,108,5,35,0,0,108,21,1,0,0,0,109,
        112,3,12,6,0,110,112,3,16,8,0,111,109,1,0,0,0,111,110,1,0,0,0,112,
        23,1,0,0,0,113,114,5,5,0,0,114,115,5,29,0,0,115,116,3,30,15,0,116,
        117,5,30,0,0,117,118,3,8,4,0,118,25,1,0,0,0,119,120,5,6,0,0,120,
        122,5,29,0,0,121,123,3,22,11,0,122,121,1,0,0,0,122,123,1,0,0,0,123,
        124,1,0,0,0,124,126,5,35,0,0,125,127,3,30,15,0,126,125,1,0,0,0,126,
        127,1,0,0,0,127,128,1,0,0,0,128,130,5,35,0,0,129,131,3,16,8,0,130,
        129,1,0,0,0,130,131,1,0,0,0,131,132,1,0,0,0,132,133,5,30,0,0,133,
        134,3,8,4,0,134,27,1,0,0,0,135,137,5,8,0,0,136,138,3,30,15,0,137,
        136,1,0,0,0,137,138,1,0,0,0,138,139,1,0,0,0,139,140,5,35,0,0,140,
        29,1,0,0,0,141,142,6,15,-1,0,142,143,5,17,0,0,143,170,3,30,15,14,
        144,145,5,26,0,0,145,170,3,30,15,13,146,147,5,29,0,0,147,148,3,30,
        15,0,148,149,5,30,0,0,149,170,1,0,0,0,150,170,5,37,0,0,151,170,5,
        38,0,0,152,170,5,39,0,0,153,170,5,13,0,0,154,170,5,14,0,0,155,170,
        5,40,0,0,156,157,5,40,0,0,157,166,5,29,0,0,158,163,3,30,15,0,159,
        160,5,36,0,0,160,162,3,30,15,0,161,159,1,0,0,0,162,165,1,0,0,0,163,
        161,1,0,0,0,163,164,1,0,0,0,164,167,1,0,0,0,165,163,1,0,0,0,166,
        158,1,0,0,0,166,167,1,0,0,0,167,168,1,0,0,0,168,170,5,30,0,0,169,
        141,1,0,0,0,169,144,1,0,0,0,169,146,1,0,0,0,169,150,1,0,0,0,169,
        151,1,0,0,0,169,152,1,0,0,0,169,153,1,0,0,0,169,154,1,0,0,0,169,
        155,1,0,0,0,169,156,1,0,0,0,170,185,1,0,0,0,171,172,10,11,0,0,172,
        173,7,1,0,0,173,184,3,30,15,12,174,175,10,10,0,0,175,176,7,2,0,0,
        176,184,3,30,15,11,177,178,10,9,0,0,178,179,7,3,0,0,179,184,3,30,
        15,10,180,181,10,8,0,0,181,182,7,4,0,0,182,184,3,30,15,9,183,171,
        1,0,0,0,183,174,1,0,0,0,183,177,1,0,0,0,183,180,1,0,0,0,184,187,
        1,0,0,0,185,183,1,0,0,0,185,186,1,0,0,0,186,31,1,0,0,0,187,185,1,
        0,0,0,17,36,44,49,59,69,81,101,111,122,126,130,137,163,166,169,183,
        185
    ]

class MiniLangParser ( Parser ):

    grammarFileName = "MiniLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "'si'", "'sino'", "'imprime'", 
                     "'mientras'", "'para'", "'funcion'", "'retorna'", "'int'", 
                     "'bool'", "'float'", "'string'", "'true'", "'false'", 
                     "'&&'", "'||'", "'!'", "'=='", "<INVALID>", "'<='", 
                     "'>='", "'<'", "'>'", "'='", "'+'", "'-'", "'*'", "'/'", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "PROGRAM", "SI", "SINO", "IMPRIME", "MIENTRAS", 
                      "PARA", "FUNCION", "RETORNA", "INT_T", "BOOL_T", "FLOAT_T", 
                      "STRING_T", "TRUE", "FALSE", "AND", "OR", "NOT", "EQ", 
                      "NEQ", "LE", "GE", "LT", "GT", "ASIGNA", "SUMA", "RESTA", 
                      "MULTI", "DIVIDE", "PARENTESIS_IZQ", "PARENTESIS_DER", 
                      "LLAVE_IZQ", "LLAVE_DER", "CORCHETE_IZQ", "CORCHETE_DER", 
                      "PUNTO_COMA", "COMA", "INT", "FLOAT", "STRING", "ID", 
                      "WS", "LINEA_COMENTARIO", "GRUPO_COMENTARIO" ]

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
    RULE_inicializacion = 11
    RULE_sentenciaMientras = 12
    RULE_sentenciaPara = 13
    RULE_sentenciaRetorna = 14
    RULE_expr = 15

    ruleNames =  [ "program", "funcionDecl", "parametros", "parametro", 
                   "grupo", "sentencia", "declaraVariable", "tipo", "sentenciaAsigna", 
                   "sentenciaSI", "sentenciaImprime", "inicializacion", 
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
    INT_T=9
    BOOL_T=10
    FLOAT_T=11
    STRING_T=12
    TRUE=13
    FALSE=14
    AND=15
    OR=16
    NOT=17
    EQ=18
    NEQ=19
    LE=20
    GE=21
    LT=22
    GT=23
    ASIGNA=24
    SUMA=25
    RESTA=26
    MULTI=27
    DIVIDE=28
    PARENTESIS_IZQ=29
    PARENTESIS_DER=30
    LLAVE_IZQ=31
    LLAVE_DER=32
    CORCHETE_IZQ=33
    CORCHETE_DER=34
    PUNTO_COMA=35
    COMA=36
    INT=37
    FLOAT=38
    STRING=39
    ID=40
    WS=41
    LINEA_COMENTARIO=42
    GRUPO_COMENTARIO=43

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
            self.state = 32
            self.match(MiniLangParser.PROGRAM)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 33
                self.funcionDecl()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
            self.grupo()
            self.state = 40
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
            self.state = 42
            self.match(MiniLangParser.FUNCION)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0):
                self.state = 43
                self.tipo()


            self.state = 46
            self.match(MiniLangParser.ID)
            self.state = 47
            self.match(MiniLangParser.PARENTESIS_IZQ)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0):
                self.state = 48
                self.parametros()


            self.state = 51
            self.match(MiniLangParser.PARENTESIS_DER)
            self.state = 52
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
            self.state = 54
            self.parametro()
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 55
                self.match(MiniLangParser.COMA)
                self.state = 56
                self.parametro()
                self.state = 61
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
            self.state = 62
            self.tipo()
            self.state = 63
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
            self.state = 65
            self.match(MiniLangParser.LLAVE_IZQ)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099511635828) != 0):
                self.state = 66
                self.sentencia()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
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
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 11, 12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.declaraVariable()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.sentenciaAsigna()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.sentenciaSI()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 77
                self.sentenciaImprime()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 78
                self.sentenciaMientras()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 6)
                self.state = 79
                self.sentenciaPara()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 7)
                self.state = 80
                self.sentenciaRetorna()
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
        self.enterRule(localctx, 12, self.RULE_declaraVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.tipo()
            self.state = 84
            self.match(MiniLangParser.ID)
            self.state = 85
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
            self.state = 87
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0)):
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
            self.state = 89
            self.match(MiniLangParser.ID)
            self.state = 90
            self.match(MiniLangParser.ASIGNA)
            self.state = 91
            self.expr(0)
            self.state = 92
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
            self.state = 94
            self.match(MiniLangParser.SI)
            self.state = 95
            self.match(MiniLangParser.PARENTESIS_IZQ)
            self.state = 96
            self.expr(0)
            self.state = 97
            self.match(MiniLangParser.PARENTESIS_DER)
            self.state = 98
            self.grupo()
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 99
                self.match(MiniLangParser.SINO)
                self.state = 100
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
            self.state = 103
            self.match(MiniLangParser.IMPRIME)
            self.state = 104
            self.match(MiniLangParser.PARENTESIS_IZQ)
            self.state = 105
            self.expr(0)
            self.state = 106
            self.match(MiniLangParser.PARENTESIS_DER)
            self.state = 107
            self.match(MiniLangParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InicializacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaraVariable(self):
            return self.getTypedRuleContext(MiniLangParser.DeclaraVariableContext,0)


        def sentenciaAsigna(self):
            return self.getTypedRuleContext(MiniLangParser.SentenciaAsignaContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_inicializacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInicializacion" ):
                listener.enterInicializacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInicializacion" ):
                listener.exitInicializacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInicializacion" ):
                return visitor.visitInicializacion(self)
            else:
                return visitor.visitChildren(self)




    def inicializacion(self):

        localctx = MiniLangParser.InicializacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_inicializacion)
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 11, 12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.declaraVariable()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.sentenciaAsigna()
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
        self.enterRule(localctx, 24, self.RULE_sentenciaMientras)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(MiniLangParser.MIENTRAS)
            self.state = 114
            self.match(MiniLangParser.PARENTESIS_IZQ)
            self.state = 115
            self.expr(0)
            self.state = 116
            self.match(MiniLangParser.PARENTESIS_DER)
            self.state = 117
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
            self.update = None # SentenciaAsignaContext

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


        def inicializacion(self):
            return self.getTypedRuleContext(MiniLangParser.InicializacionContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def sentenciaAsigna(self):
            return self.getTypedRuleContext(MiniLangParser.SentenciaAsignaContext,0)


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
        self.enterRule(localctx, 26, self.RULE_sentenciaPara)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(MiniLangParser.PARA)
            self.state = 120
            self.match(MiniLangParser.PARENTESIS_IZQ)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099511635456) != 0):
                self.state = 121
                self.inicializacion()


            self.state = 124
            self.match(MiniLangParser.PUNTO_COMA)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2062188437504) != 0):
                self.state = 125
                localctx.cond = self.expr(0)


            self.state = 128
            self.match(MiniLangParser.PUNTO_COMA)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 129
                localctx.update = self.sentenciaAsigna()


            self.state = 132
            self.match(MiniLangParser.PARENTESIS_DER)
            self.state = 133
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
        self.enterRule(localctx, 28, self.RULE_sentenciaRetorna)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(MiniLangParser.RETORNA)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2062188437504) != 0):
                self.state = 136
                self.expr(0)


            self.state = 139
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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = MiniLangParser.UnaryNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 142
                self.match(MiniLangParser.NOT)
                self.state = 143
                self.expr(14)
                pass

            elif la_ == 2:
                localctx = MiniLangParser.UnaryMinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 144
                self.match(MiniLangParser.RESTA)
                self.state = 145
                self.expr(13)
                pass

            elif la_ == 3:
                localctx = MiniLangParser.ParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 146
                self.match(MiniLangParser.PARENTESIS_IZQ)
                self.state = 147
                self.expr(0)
                self.state = 148
                self.match(MiniLangParser.PARENTESIS_DER)
                pass

            elif la_ == 4:
                localctx = MiniLangParser.IntLitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 150
                self.match(MiniLangParser.INT)
                pass

            elif la_ == 5:
                localctx = MiniLangParser.FloatLitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 151
                self.match(MiniLangParser.FLOAT)
                pass

            elif la_ == 6:
                localctx = MiniLangParser.StringLitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 152
                self.match(MiniLangParser.STRING)
                pass

            elif la_ == 7:
                localctx = MiniLangParser.TrueLitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 153
                self.match(MiniLangParser.TRUE)
                pass

            elif la_ == 8:
                localctx = MiniLangParser.FalseLitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 154
                self.match(MiniLangParser.FALSE)
                pass

            elif la_ == 9:
                localctx = MiniLangParser.IdRefContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 155
                self.match(MiniLangParser.ID)
                pass

            elif la_ == 10:
                localctx = MiniLangParser.FuncCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 156
                self.match(MiniLangParser.ID)
                self.state = 157
                self.match(MiniLangParser.PARENTESIS_IZQ)
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2062188437504) != 0):
                    self.state = 158
                    self.expr(0)
                    self.state = 163
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==36:
                        self.state = 159
                        self.match(MiniLangParser.COMA)
                        self.state = 160
                        self.expr(0)
                        self.state = 165
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 168
                self.match(MiniLangParser.PARENTESIS_DER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 185
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 183
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = MiniLangParser.MulDivContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 171
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 172
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==27 or _la==28):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 173
                        localctx.right = self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = MiniLangParser.AddSubContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 174
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 175
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==25 or _la==26):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 176
                        localctx.right = self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = MiniLangParser.RelationalContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 177
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 178
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16515072) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 179
                        localctx.right = self.expr(10)
                        pass

                    elif la_ == 4:
                        localctx = MiniLangParser.LogicalContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 180
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 181
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 182
                        localctx.right = self.expr(9)
                        pass

             
                self.state = 187
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        self._predicates[15] = self.expr_sempred
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
         




