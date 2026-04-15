# Generated from grammar/MiniLang.g4 by ANTLR 4.13.2
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
        4,1,44,229,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        5,0,42,8,0,10,0,12,0,45,9,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,
        55,8,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,5,2,64,8,2,10,2,12,2,67,9,2,1,
        3,1,3,1,3,1,4,1,4,3,4,74,8,4,1,5,1,5,5,5,78,8,5,10,5,12,5,81,9,5,
        1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,93,8,6,1,7,1,7,1,7,1,
        7,3,7,99,8,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,3,10,117,8,10,1,11,1,11,1,11,1,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,3,13,134,8,13,1,13,
        1,13,3,13,138,8,13,1,13,1,13,3,13,142,8,13,1,13,1,13,1,13,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,155,8,14,1,15,1,15,1,15,1,
        15,1,16,1,16,3,16,163,8,16,1,16,1,16,1,17,1,17,1,17,3,17,170,8,17,
        1,17,1,17,1,17,1,18,1,18,1,18,5,18,178,8,18,10,18,12,18,181,9,18,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,3,19,200,8,19,1,19,1,19,3,19,204,8,19,1,19,1,
        19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,
        19,1,19,1,19,1,19,5,19,224,8,19,10,19,12,19,227,9,19,1,19,0,1,38,
        20,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,0,5,1,
        0,10,13,1,0,28,29,1,0,26,27,1,0,21,24,1,0,19,20,245,0,43,1,0,0,0,
        2,50,1,0,0,0,4,60,1,0,0,0,6,68,1,0,0,0,8,73,1,0,0,0,10,75,1,0,0,
        0,12,92,1,0,0,0,14,94,1,0,0,0,16,102,1,0,0,0,18,104,1,0,0,0,20,109,
        1,0,0,0,22,118,1,0,0,0,24,124,1,0,0,0,26,130,1,0,0,0,28,154,1,0,
        0,0,30,156,1,0,0,0,32,160,1,0,0,0,34,166,1,0,0,0,36,174,1,0,0,0,
        38,203,1,0,0,0,40,42,3,2,1,0,41,40,1,0,0,0,42,45,1,0,0,0,43,41,1,
        0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,45,43,1,0,0,0,46,47,5,6,0,0,47,
        48,3,10,5,0,48,49,5,0,0,1,49,1,1,0,0,0,50,51,5,1,0,0,51,52,5,38,
        0,0,52,54,5,30,0,0,53,55,3,4,2,0,54,53,1,0,0,0,54,55,1,0,0,0,55,
        56,1,0,0,0,56,57,5,31,0,0,57,58,3,8,4,0,58,59,3,10,5,0,59,3,1,0,
        0,0,60,65,3,6,3,0,61,62,5,37,0,0,62,64,3,6,3,0,63,61,1,0,0,0,64,
        67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,5,1,0,0,0,67,65,1,0,0,
        0,68,69,3,16,8,0,69,70,5,38,0,0,70,7,1,0,0,0,71,74,3,16,8,0,72,74,
        5,5,0,0,73,71,1,0,0,0,73,72,1,0,0,0,74,9,1,0,0,0,75,79,5,32,0,0,
        76,78,3,12,6,0,77,76,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,1,
        0,0,0,80,82,1,0,0,0,81,79,1,0,0,0,82,83,5,33,0,0,83,11,1,0,0,0,84,
        93,3,14,7,0,85,93,3,18,9,0,86,93,3,20,10,0,87,93,3,22,11,0,88,93,
        3,24,12,0,89,93,3,26,13,0,90,93,3,32,16,0,91,93,3,34,17,0,92,84,
        1,0,0,0,92,85,1,0,0,0,92,86,1,0,0,0,92,87,1,0,0,0,92,88,1,0,0,0,
        92,89,1,0,0,0,92,90,1,0,0,0,92,91,1,0,0,0,93,13,1,0,0,0,94,95,3,
        16,8,0,95,98,5,38,0,0,96,97,5,25,0,0,97,99,3,38,19,0,98,96,1,0,0,
        0,98,99,1,0,0,0,99,100,1,0,0,0,100,101,5,36,0,0,101,15,1,0,0,0,102,
        103,7,0,0,0,103,17,1,0,0,0,104,105,5,38,0,0,105,106,5,25,0,0,106,
        107,3,38,19,0,107,108,5,36,0,0,108,19,1,0,0,0,109,110,5,7,0,0,110,
        111,5,30,0,0,111,112,3,38,19,0,112,113,5,31,0,0,113,116,3,10,5,0,
        114,115,5,8,0,0,115,117,3,10,5,0,116,114,1,0,0,0,116,117,1,0,0,0,
        117,21,1,0,0,0,118,119,5,9,0,0,119,120,5,30,0,0,120,121,3,38,19,
        0,121,122,5,31,0,0,122,123,5,36,0,0,123,23,1,0,0,0,124,125,5,2,0,
        0,125,126,5,30,0,0,126,127,3,38,19,0,127,128,5,31,0,0,128,129,3,
        10,5,0,129,25,1,0,0,0,130,131,5,3,0,0,131,133,5,30,0,0,132,134,3,
        28,14,0,133,132,1,0,0,0,133,134,1,0,0,0,134,135,1,0,0,0,135,137,
        5,36,0,0,136,138,3,38,19,0,137,136,1,0,0,0,137,138,1,0,0,0,138,139,
        1,0,0,0,139,141,5,36,0,0,140,142,3,30,15,0,141,140,1,0,0,0,141,142,
        1,0,0,0,142,143,1,0,0,0,143,144,5,31,0,0,144,145,3,10,5,0,145,27,
        1,0,0,0,146,147,3,16,8,0,147,148,5,38,0,0,148,149,5,25,0,0,149,150,
        3,38,19,0,150,155,1,0,0,0,151,152,5,38,0,0,152,153,5,25,0,0,153,
        155,3,38,19,0,154,146,1,0,0,0,154,151,1,0,0,0,155,29,1,0,0,0,156,
        157,5,38,0,0,157,158,5,25,0,0,158,159,3,38,19,0,159,31,1,0,0,0,160,
        162,5,4,0,0,161,163,3,38,19,0,162,161,1,0,0,0,162,163,1,0,0,0,163,
        164,1,0,0,0,164,165,5,36,0,0,165,33,1,0,0,0,166,167,5,38,0,0,167,
        169,5,30,0,0,168,170,3,36,18,0,169,168,1,0,0,0,169,170,1,0,0,0,170,
        171,1,0,0,0,171,172,5,31,0,0,172,173,5,36,0,0,173,35,1,0,0,0,174,
        179,3,38,19,0,175,176,5,37,0,0,176,178,3,38,19,0,177,175,1,0,0,0,
        178,181,1,0,0,0,179,177,1,0,0,0,179,180,1,0,0,0,180,37,1,0,0,0,181,
        179,1,0,0,0,182,183,6,19,-1,0,183,184,5,18,0,0,184,204,3,38,19,16,
        185,186,5,27,0,0,186,204,3,38,19,15,187,188,5,30,0,0,188,189,3,38,
        19,0,189,190,5,31,0,0,190,204,1,0,0,0,191,204,5,40,0,0,192,204,5,
        39,0,0,193,204,5,41,0,0,194,204,5,14,0,0,195,204,5,15,0,0,196,197,
        5,38,0,0,197,199,5,30,0,0,198,200,3,36,18,0,199,198,1,0,0,0,199,
        200,1,0,0,0,200,201,1,0,0,0,201,204,5,31,0,0,202,204,5,38,0,0,203,
        182,1,0,0,0,203,185,1,0,0,0,203,187,1,0,0,0,203,191,1,0,0,0,203,
        192,1,0,0,0,203,193,1,0,0,0,203,194,1,0,0,0,203,195,1,0,0,0,203,
        196,1,0,0,0,203,202,1,0,0,0,204,225,1,0,0,0,205,206,10,13,0,0,206,
        207,7,1,0,0,207,224,3,38,19,14,208,209,10,12,0,0,209,210,7,2,0,0,
        210,224,3,38,19,13,211,212,10,11,0,0,212,213,7,3,0,0,213,224,3,38,
        19,12,214,215,10,10,0,0,215,216,7,4,0,0,216,224,3,38,19,11,217,218,
        10,9,0,0,218,219,5,16,0,0,219,224,3,38,19,10,220,221,10,8,0,0,221,
        222,5,17,0,0,222,224,3,38,19,9,223,205,1,0,0,0,223,208,1,0,0,0,223,
        211,1,0,0,0,223,214,1,0,0,0,223,217,1,0,0,0,223,220,1,0,0,0,224,
        227,1,0,0,0,225,223,1,0,0,0,225,226,1,0,0,0,226,39,1,0,0,0,227,225,
        1,0,0,0,19,43,54,65,73,79,92,98,116,133,137,141,154,162,169,179,
        199,203,223,225
    ]

class MiniLangParser ( Parser ):

    grammarFileName = "MiniLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'func'", "'while'", "'for'", "'return'", 
                     "'void'", "'program'", "'if'", "'else'", "'print'", 
                     "'int'", "'bool'", "'float'", "'string'", "'true'", 
                     "'false'", "'&&'", "'||'", "'!'", "'=='", "<INVALID>", 
                     "'<='", "'>='", "'<'", "'>'", "'='", "'+'", "'-'", 
                     "'*'", "'/'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "';'", "','" ]

    symbolicNames = [ "<INVALID>", "FUNC", "MIENTRAS", "PARA", "RETORNAR", 
                      "VOID", "PROGRAMA", "SI", "SINO", "IMPRIMIR", "TIPO_ENTERO", 
                      "TIPO_BOOL", "TIPO_FLOAT", "TIPO_STRING", "VERDADERO", 
                      "FALSO", "Y_LOGICO", "O_LOGICO", "NEGACION", "IGUAL", 
                      "DIFERENTE", "MENOR_IGUAL", "MAYOR_IGUAL", "MENOR_QUE", 
                      "MAYOR_QUE", "ASIGNACION", "SUMA", "RESTA", "MULTIPLICACION", 
                      "DIVISION", "PAREN_IZQ", "PAREN_DER", "LLAVE_IZQ", 
                      "LLAVE_DER", "CORCHETE_IZQ", "CORCHETE_DER", "PUNTO_COMA", 
                      "COMA", "IDENTIFICADOR", "FLOTANTE", "ENTERO", "CADENA", 
                      "ESPACIO", "COMENTARIO_LINEA", "COMENTARIO_BLOQUE" ]

    RULE_programa = 0
    RULE_funcion = 1
    RULE_listaParametros = 2
    RULE_parametro = 3
    RULE_tipoRetorno = 4
    RULE_bloque = 5
    RULE_sentencia = 6
    RULE_declaracionVariable = 7
    RULE_tipo = 8
    RULE_asignacion = 9
    RULE_condicionalSi = 10
    RULE_imprimir = 11
    RULE_mientras = 12
    RULE_para = 13
    RULE_paraInicio = 14
    RULE_paraActualizacion = 15
    RULE_retorno = 16
    RULE_llamadaFuncionStmt = 17
    RULE_listaArgumentos = 18
    RULE_expresion = 19

    ruleNames =  [ "programa", "funcion", "listaParametros", "parametro", 
                   "tipoRetorno", "bloque", "sentencia", "declaracionVariable", 
                   "tipo", "asignacion", "condicionalSi", "imprimir", "mientras", 
                   "para", "paraInicio", "paraActualizacion", "retorno", 
                   "llamadaFuncionStmt", "listaArgumentos", "expresion" ]

    EOF = Token.EOF
    FUNC=1
    MIENTRAS=2
    PARA=3
    RETORNAR=4
    VOID=5
    PROGRAMA=6
    SI=7
    SINO=8
    IMPRIMIR=9
    TIPO_ENTERO=10
    TIPO_BOOL=11
    TIPO_FLOAT=12
    TIPO_STRING=13
    VERDADERO=14
    FALSO=15
    Y_LOGICO=16
    O_LOGICO=17
    NEGACION=18
    IGUAL=19
    DIFERENTE=20
    MENOR_IGUAL=21
    MAYOR_IGUAL=22
    MENOR_QUE=23
    MAYOR_QUE=24
    ASIGNACION=25
    SUMA=26
    RESTA=27
    MULTIPLICACION=28
    DIVISION=29
    PAREN_IZQ=30
    PAREN_DER=31
    LLAVE_IZQ=32
    LLAVE_DER=33
    CORCHETE_IZQ=34
    CORCHETE_DER=35
    PUNTO_COMA=36
    COMA=37
    IDENTIFICADOR=38
    FLOTANTE=39
    ENTERO=40
    CADENA=41
    ESPACIO=42
    COMENTARIO_LINEA=43
    COMENTARIO_BLOQUE=44

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
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

        def funcion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.FuncionContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.FuncionContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 40
                self.funcion()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self.match(MiniLangParser.PROGRAMA)
            self.state = 47
            self.bloque()
            self.state = 48
            self.match(MiniLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniLangParser.FUNC, 0)

        def IDENTIFICADOR(self):
            return self.getToken(MiniLangParser.IDENTIFICADOR, 0)

        def PAREN_IZQ(self):
            return self.getToken(MiniLangParser.PAREN_IZQ, 0)

        def PAREN_DER(self):
            return self.getToken(MiniLangParser.PAREN_DER, 0)

        def tipoRetorno(self):
            return self.getTypedRuleContext(MiniLangParser.TipoRetornoContext,0)


        def bloque(self):
            return self.getTypedRuleContext(MiniLangParser.BloqueContext,0)


        def listaParametros(self):
            return self.getTypedRuleContext(MiniLangParser.ListaParametrosContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_funcion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncion" ):
                return visitor.visitFuncion(self)
            else:
                return visitor.visitChildren(self)




    def funcion(self):

        localctx = MiniLangParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_funcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(MiniLangParser.FUNC)
            self.state = 51
            self.match(MiniLangParser.IDENTIFICADOR)
            self.state = 52
            self.match(MiniLangParser.PAREN_IZQ)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 15360) != 0):
                self.state = 53
                self.listaParametros()


            self.state = 56
            self.match(MiniLangParser.PAREN_DER)
            self.state = 57
            self.tipoRetorno()
            self.state = 58
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaParametrosContext(ParserRuleContext):
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
            return MiniLangParser.RULE_listaParametros

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaParametros" ):
                return visitor.visitListaParametros(self)
            else:
                return visitor.visitChildren(self)




    def listaParametros(self):

        localctx = MiniLangParser.ListaParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_listaParametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.parametro()
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 61
                self.match(MiniLangParser.COMA)
                self.state = 62
                self.parametro()
                self.state = 67
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


        def IDENTIFICADOR(self):
            return self.getToken(MiniLangParser.IDENTIFICADOR, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_parametro

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
            self.state = 68
            self.tipo()
            self.state = 69
            self.match(MiniLangParser.IDENTIFICADOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoRetornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(MiniLangParser.TipoContext,0)


        def VOID(self):
            return self.getToken(MiniLangParser.VOID, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_tipoRetorno

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoRetorno" ):
                return visitor.visitTipoRetorno(self)
            else:
                return visitor.visitChildren(self)




    def tipoRetorno(self):

        localctx = MiniLangParser.TipoRetornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tipoRetorno)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11, 12, 13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.tipo()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.match(MiniLangParser.VOID)
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
        self.enterRule(localctx, 10, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(MiniLangParser.LLAVE_IZQ)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274877922972) != 0):
                self.state = 76
                self.sentencia()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 82
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


        def mientras(self):
            return self.getTypedRuleContext(MiniLangParser.MientrasContext,0)


        def para(self):
            return self.getTypedRuleContext(MiniLangParser.ParaContext,0)


        def retorno(self):
            return self.getTypedRuleContext(MiniLangParser.RetornoContext,0)


        def llamadaFuncionStmt(self):
            return self.getTypedRuleContext(MiniLangParser.LlamadaFuncionStmtContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_sentencia

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = MiniLangParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_sentencia)
        try:
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.declaracionVariable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.asignacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.condicionalSi()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 87
                self.imprimir()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 88
                self.mientras()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 89
                self.para()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 90
                self.retorno()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 91
                self.llamadaFuncionStmt()
                pass


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

        def ASIGNACION(self):
            return self.getToken(MiniLangParser.ASIGNACION, 0)

        def expresion(self):
            return self.getTypedRuleContext(MiniLangParser.ExpresionContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_declaracionVariable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionVariable" ):
                return visitor.visitDeclaracionVariable(self)
            else:
                return visitor.visitChildren(self)




    def declaracionVariable(self):

        localctx = MiniLangParser.DeclaracionVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_declaracionVariable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.tipo()
            self.state = 95
            self.match(MiniLangParser.IDENTIFICADOR)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 96
                self.match(MiniLangParser.ASIGNACION)
                self.state = 97
                self.expresion(0)


            self.state = 100
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

        def TIPO_FLOAT(self):
            return self.getToken(MiniLangParser.TIPO_FLOAT, 0)

        def TIPO_STRING(self):
            return self.getToken(MiniLangParser.TIPO_STRING, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_tipo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = MiniLangParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
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
        self.enterRule(localctx, 18, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(MiniLangParser.IDENTIFICADOR)
            self.state = 105
            self.match(MiniLangParser.ASIGNACION)
            self.state = 106
            self.expresion(0)
            self.state = 107
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
        self.enterRule(localctx, 20, self.RULE_condicionalSi)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(MiniLangParser.SI)
            self.state = 110
            self.match(MiniLangParser.PAREN_IZQ)
            self.state = 111
            self.expresion(0)
            self.state = 112
            self.match(MiniLangParser.PAREN_DER)
            self.state = 113
            self.bloque()
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 114
                self.match(MiniLangParser.SINO)
                self.state = 115
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
        self.enterRule(localctx, 22, self.RULE_imprimir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(MiniLangParser.IMPRIMIR)
            self.state = 119
            self.match(MiniLangParser.PAREN_IZQ)
            self.state = 120
            self.expresion(0)
            self.state = 121
            self.match(MiniLangParser.PAREN_DER)
            self.state = 122
            self.match(MiniLangParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MientrasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIENTRAS(self):
            return self.getToken(MiniLangParser.MIENTRAS, 0)

        def PAREN_IZQ(self):
            return self.getToken(MiniLangParser.PAREN_IZQ, 0)

        def expresion(self):
            return self.getTypedRuleContext(MiniLangParser.ExpresionContext,0)


        def PAREN_DER(self):
            return self.getToken(MiniLangParser.PAREN_DER, 0)

        def bloque(self):
            return self.getTypedRuleContext(MiniLangParser.BloqueContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_mientras

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMientras" ):
                return visitor.visitMientras(self)
            else:
                return visitor.visitChildren(self)




    def mientras(self):

        localctx = MiniLangParser.MientrasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_mientras)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(MiniLangParser.MIENTRAS)
            self.state = 125
            self.match(MiniLangParser.PAREN_IZQ)
            self.state = 126
            self.expresion(0)
            self.state = 127
            self.match(MiniLangParser.PAREN_DER)
            self.state = 128
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARA(self):
            return self.getToken(MiniLangParser.PARA, 0)

        def PAREN_IZQ(self):
            return self.getToken(MiniLangParser.PAREN_IZQ, 0)

        def PUNTO_COMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.PUNTO_COMA)
            else:
                return self.getToken(MiniLangParser.PUNTO_COMA, i)

        def PAREN_DER(self):
            return self.getToken(MiniLangParser.PAREN_DER, 0)

        def bloque(self):
            return self.getTypedRuleContext(MiniLangParser.BloqueContext,0)


        def paraInicio(self):
            return self.getTypedRuleContext(MiniLangParser.ParaInicioContext,0)


        def expresion(self):
            return self.getTypedRuleContext(MiniLangParser.ExpresionContext,0)


        def paraActualizacion(self):
            return self.getTypedRuleContext(MiniLangParser.ParaActualizacionContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = MiniLangParser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_para)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(MiniLangParser.PARA)
            self.state = 131
            self.match(MiniLangParser.PAREN_IZQ)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 274877922304) != 0):
                self.state = 132
                self.paraInicio()


            self.state = 135
            self.match(MiniLangParser.PUNTO_COMA)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4124376875008) != 0):
                self.state = 136
                self.expresion(0)


            self.state = 139
            self.match(MiniLangParser.PUNTO_COMA)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 140
                self.paraActualizacion()


            self.state = 143
            self.match(MiniLangParser.PAREN_DER)
            self.state = 144
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaInicioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(MiniLangParser.TipoContext,0)


        def IDENTIFICADOR(self):
            return self.getToken(MiniLangParser.IDENTIFICADOR, 0)

        def ASIGNACION(self):
            return self.getToken(MiniLangParser.ASIGNACION, 0)

        def expresion(self):
            return self.getTypedRuleContext(MiniLangParser.ExpresionContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_paraInicio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParaInicio" ):
                return visitor.visitParaInicio(self)
            else:
                return visitor.visitChildren(self)




    def paraInicio(self):

        localctx = MiniLangParser.ParaInicioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_paraInicio)
        try:
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11, 12, 13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.tipo()
                self.state = 147
                self.match(MiniLangParser.IDENTIFICADOR)
                self.state = 148
                self.match(MiniLangParser.ASIGNACION)
                self.state = 149
                self.expresion(0)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.match(MiniLangParser.IDENTIFICADOR)
                self.state = 152
                self.match(MiniLangParser.ASIGNACION)
                self.state = 153
                self.expresion(0)
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


    class ParaActualizacionContext(ParserRuleContext):
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


        def getRuleIndex(self):
            return MiniLangParser.RULE_paraActualizacion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParaActualizacion" ):
                return visitor.visitParaActualizacion(self)
            else:
                return visitor.visitChildren(self)




    def paraActualizacion(self):

        localctx = MiniLangParser.ParaActualizacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_paraActualizacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(MiniLangParser.IDENTIFICADOR)
            self.state = 157
            self.match(MiniLangParser.ASIGNACION)
            self.state = 158
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETORNAR(self):
            return self.getToken(MiniLangParser.RETORNAR, 0)

        def PUNTO_COMA(self):
            return self.getToken(MiniLangParser.PUNTO_COMA, 0)

        def expresion(self):
            return self.getTypedRuleContext(MiniLangParser.ExpresionContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_retorno

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetorno" ):
                return visitor.visitRetorno(self)
            else:
                return visitor.visitChildren(self)




    def retorno(self):

        localctx = MiniLangParser.RetornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_retorno)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(MiniLangParser.RETORNAR)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4124376875008) != 0):
                self.state = 161
                self.expresion(0)


            self.state = 164
            self.match(MiniLangParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlamadaFuncionStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(MiniLangParser.IDENTIFICADOR, 0)

        def PAREN_IZQ(self):
            return self.getToken(MiniLangParser.PAREN_IZQ, 0)

        def PAREN_DER(self):
            return self.getToken(MiniLangParser.PAREN_DER, 0)

        def PUNTO_COMA(self):
            return self.getToken(MiniLangParser.PUNTO_COMA, 0)

        def listaArgumentos(self):
            return self.getTypedRuleContext(MiniLangParser.ListaArgumentosContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_llamadaFuncionStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamadaFuncionStmt" ):
                return visitor.visitLlamadaFuncionStmt(self)
            else:
                return visitor.visitChildren(self)




    def llamadaFuncionStmt(self):

        localctx = MiniLangParser.LlamadaFuncionStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_llamadaFuncionStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(MiniLangParser.IDENTIFICADOR)
            self.state = 167
            self.match(MiniLangParser.PAREN_IZQ)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4124376875008) != 0):
                self.state = 168
                self.listaArgumentos()


            self.state = 171
            self.match(MiniLangParser.PAREN_DER)
            self.state = 172
            self.match(MiniLangParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExpresionContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.COMA)
            else:
                return self.getToken(MiniLangParser.COMA, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_listaArgumentos

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaArgumentos" ):
                return visitor.visitListaArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def listaArgumentos(self):

        localctx = MiniLangParser.ListaArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_listaArgumentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.expresion(0)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 175
                self.match(MiniLangParser.COMA)
                self.state = 176
                self.expresion(0)
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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


    class LiteralCadenaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CADENA(self):
            return self.getToken(MiniLangParser.CADENA, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralCadena" ):
                return visitor.visitLiteralCadena(self)
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


    class LiteralFlotanteContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOTANTE(self):
            return self.getToken(MiniLangParser.FLOTANTE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralFlotante" ):
                return visitor.visitLiteralFlotante(self)
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


    class LlamadaFuncionContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFICADOR(self):
            return self.getToken(MiniLangParser.IDENTIFICADOR, 0)
        def PAREN_IZQ(self):
            return self.getToken(MiniLangParser.PAREN_IZQ, 0)
        def PAREN_DER(self):
            return self.getToken(MiniLangParser.PAREN_DER, 0)
        def listaArgumentos(self):
            return self.getTypedRuleContext(MiniLangParser.ListaArgumentosContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamadaFuncion" ):
                return visitor.visitLlamadaFuncion(self)
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
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                localctx = MiniLangParser.NegacionLogicaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 183
                self.match(MiniLangParser.NEGACION)
                self.state = 184
                self.expresion(16)
                pass

            elif la_ == 2:
                localctx = MiniLangParser.MenosUnarioContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 185
                self.match(MiniLangParser.RESTA)
                self.state = 186
                self.expresion(15)
                pass

            elif la_ == 3:
                localctx = MiniLangParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 187
                self.match(MiniLangParser.PAREN_IZQ)
                self.state = 188
                self.expresion(0)
                self.state = 189
                self.match(MiniLangParser.PAREN_DER)
                pass

            elif la_ == 4:
                localctx = MiniLangParser.LiteralEnteroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 191
                self.match(MiniLangParser.ENTERO)
                pass

            elif la_ == 5:
                localctx = MiniLangParser.LiteralFlotanteContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 192
                self.match(MiniLangParser.FLOTANTE)
                pass

            elif la_ == 6:
                localctx = MiniLangParser.LiteralCadenaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 193
                self.match(MiniLangParser.CADENA)
                pass

            elif la_ == 7:
                localctx = MiniLangParser.LiteralVerdaderoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 194
                self.match(MiniLangParser.VERDADERO)
                pass

            elif la_ == 8:
                localctx = MiniLangParser.LiteralFalsoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 195
                self.match(MiniLangParser.FALSO)
                pass

            elif la_ == 9:
                localctx = MiniLangParser.LlamadaFuncionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 196
                self.match(MiniLangParser.IDENTIFICADOR)
                self.state = 197
                self.match(MiniLangParser.PAREN_IZQ)
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4124376875008) != 0):
                    self.state = 198
                    self.listaArgumentos()


                self.state = 201
                self.match(MiniLangParser.PAREN_DER)
                pass

            elif la_ == 10:
                localctx = MiniLangParser.ReferenciaVariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 202
                self.match(MiniLangParser.IDENTIFICADOR)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 225
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 223
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = MiniLangParser.MultiplicacionDivisionContext(self, MiniLangParser.ExpresionContext(self, _parentctx, _parentState))
                        localctx.izq = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 205
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 206
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==28 or _la==29):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 207
                        localctx.der = self.expresion(14)
                        pass

                    elif la_ == 2:
                        localctx = MiniLangParser.SumaRestaContext(self, MiniLangParser.ExpresionContext(self, _parentctx, _parentState))
                        localctx.izq = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 208
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 209
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==26 or _la==27):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 210
                        localctx.der = self.expresion(13)
                        pass

                    elif la_ == 3:
                        localctx = MiniLangParser.ComparacionContext(self, MiniLangParser.ExpresionContext(self, _parentctx, _parentState))
                        localctx.izq = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 211
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 212
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31457280) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 213
                        localctx.der = self.expresion(12)
                        pass

                    elif la_ == 4:
                        localctx = MiniLangParser.IgualdadContext(self, MiniLangParser.ExpresionContext(self, _parentctx, _parentState))
                        localctx.izq = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 214
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 215
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 216
                        localctx.der = self.expresion(11)
                        pass

                    elif la_ == 5:
                        localctx = MiniLangParser.YLogicoContext(self, MiniLangParser.ExpresionContext(self, _parentctx, _parentState))
                        localctx.izq = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 217
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 218
                        self.match(MiniLangParser.Y_LOGICO)
                        self.state = 219
                        localctx.der = self.expresion(10)
                        pass

                    elif la_ == 6:
                        localctx = MiniLangParser.OLogicoContext(self, MiniLangParser.ExpresionContext(self, _parentctx, _parentState))
                        localctx.izq = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 220
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 221
                        self.match(MiniLangParser.O_LOGICO)
                        self.state = 222
                        localctx.der = self.expresion(9)
                        pass

             
                self.state = 227
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
        self._predicates[19] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 8)
         




