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
        4,1,38,178,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,0,1,0,1,1,1,1,5,1,39,8,1,10,1,12,1,
        42,9,1,1,1,5,1,45,8,1,10,1,12,1,48,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,
        2,3,2,57,8,2,1,2,1,2,1,2,1,3,1,3,1,3,5,3,65,8,3,10,3,12,3,68,9,3,
        1,4,1,4,1,4,1,5,1,5,5,5,75,8,5,10,5,12,5,78,9,5,1,5,1,5,1,6,1,6,
        1,6,1,6,1,6,1,6,3,6,88,8,6,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,
        9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,108,8,10,1,11,1,11,
        1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,
        1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,134,8,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,145,8,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,5,14,165,8,14,10,14,12,14,168,9,14,1,15,1,15,1,15,
        5,15,173,8,15,10,15,12,15,176,9,15,1,15,0,1,28,16,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,0,5,1,0,5,6,1,0,24,25,1,0,22,23,1,0,17,
        20,1,0,15,16,187,0,32,1,0,0,0,2,36,1,0,0,0,4,51,1,0,0,0,6,61,1,0,
        0,0,8,69,1,0,0,0,10,72,1,0,0,0,12,87,1,0,0,0,14,89,1,0,0,0,16,93,
        1,0,0,0,18,95,1,0,0,0,20,100,1,0,0,0,22,109,1,0,0,0,24,115,1,0,0,
        0,26,121,1,0,0,0,28,144,1,0,0,0,30,169,1,0,0,0,32,33,5,1,0,0,33,
        34,3,2,1,0,34,35,5,0,0,1,35,1,1,0,0,0,36,40,5,28,0,0,37,39,3,4,2,
        0,38,37,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,46,
        1,0,0,0,42,40,1,0,0,0,43,45,3,12,6,0,44,43,1,0,0,0,45,48,1,0,0,0,
        46,44,1,0,0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,46,1,0,0,0,49,50,5,
        29,0,0,50,3,1,0,0,0,51,52,5,10,0,0,52,53,3,16,8,0,53,54,5,34,0,0,
        54,56,5,26,0,0,55,57,3,6,3,0,56,55,1,0,0,0,56,57,1,0,0,0,57,58,1,
        0,0,0,58,59,5,27,0,0,59,60,3,10,5,0,60,5,1,0,0,0,61,66,3,8,4,0,62,
        63,5,33,0,0,63,65,3,8,4,0,64,62,1,0,0,0,65,68,1,0,0,0,66,64,1,0,
        0,0,66,67,1,0,0,0,67,7,1,0,0,0,68,66,1,0,0,0,69,70,3,16,8,0,70,71,
        5,34,0,0,71,9,1,0,0,0,72,76,5,28,0,0,73,75,3,12,6,0,74,73,1,0,0,
        0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,79,1,0,0,0,78,76,
        1,0,0,0,79,80,5,29,0,0,80,11,1,0,0,0,81,88,3,14,7,0,82,88,3,18,9,
        0,83,88,3,20,10,0,84,88,3,22,11,0,85,88,3,24,12,0,86,88,3,26,13,
        0,87,81,1,0,0,0,87,82,1,0,0,0,87,83,1,0,0,0,87,84,1,0,0,0,87,85,
        1,0,0,0,87,86,1,0,0,0,88,13,1,0,0,0,89,90,3,16,8,0,90,91,5,34,0,
        0,91,92,5,32,0,0,92,15,1,0,0,0,93,94,7,0,0,0,94,17,1,0,0,0,95,96,
        5,34,0,0,96,97,5,21,0,0,97,98,3,28,14,0,98,99,5,32,0,0,99,19,1,0,
        0,0,100,101,5,2,0,0,101,102,5,26,0,0,102,103,3,28,14,0,103,104,5,
        27,0,0,104,107,3,10,5,0,105,106,5,3,0,0,106,108,3,10,5,0,107,105,
        1,0,0,0,107,108,1,0,0,0,108,21,1,0,0,0,109,110,5,9,0,0,110,111,5,
        26,0,0,111,112,3,28,14,0,112,113,5,27,0,0,113,114,3,10,5,0,114,23,
        1,0,0,0,115,116,5,4,0,0,116,117,5,26,0,0,117,118,3,28,14,0,118,119,
        5,27,0,0,119,120,5,32,0,0,120,25,1,0,0,0,121,122,5,11,0,0,122,123,
        3,28,14,0,123,124,5,32,0,0,124,27,1,0,0,0,125,126,6,14,-1,0,126,
        127,5,14,0,0,127,145,3,28,14,14,128,129,5,23,0,0,129,145,3,28,14,
        13,130,131,5,34,0,0,131,133,5,26,0,0,132,134,3,30,15,0,133,132,1,
        0,0,0,133,134,1,0,0,0,134,135,1,0,0,0,135,145,5,27,0,0,136,137,5,
        26,0,0,137,138,3,28,14,0,138,139,5,27,0,0,139,145,1,0,0,0,140,145,
        5,35,0,0,141,145,5,7,0,0,142,145,5,8,0,0,143,145,5,34,0,0,144,125,
        1,0,0,0,144,128,1,0,0,0,144,130,1,0,0,0,144,136,1,0,0,0,144,140,
        1,0,0,0,144,141,1,0,0,0,144,142,1,0,0,0,144,143,1,0,0,0,145,166,
        1,0,0,0,146,147,10,10,0,0,147,148,7,1,0,0,148,165,3,28,14,11,149,
        150,10,9,0,0,150,151,7,2,0,0,151,165,3,28,14,10,152,153,10,8,0,0,
        153,154,7,3,0,0,154,165,3,28,14,9,155,156,10,7,0,0,156,157,7,4,0,
        0,157,165,3,28,14,8,158,159,10,6,0,0,159,160,5,12,0,0,160,165,3,
        28,14,7,161,162,10,5,0,0,162,163,5,13,0,0,163,165,3,28,14,6,164,
        146,1,0,0,0,164,149,1,0,0,0,164,152,1,0,0,0,164,155,1,0,0,0,164,
        158,1,0,0,0,164,161,1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,166,
        167,1,0,0,0,167,29,1,0,0,0,168,166,1,0,0,0,169,174,3,28,14,0,170,
        171,5,33,0,0,171,173,3,28,14,0,172,170,1,0,0,0,173,176,1,0,0,0,174,
        172,1,0,0,0,174,175,1,0,0,0,175,31,1,0,0,0,176,174,1,0,0,0,12,40,
        46,56,66,76,87,107,133,144,164,166,174
    ]

class MiniLangParser ( Parser ):

    grammarFileName = "MiniLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "'if'", "'else'", "'print'", 
                     "'int'", "'bool'", "'true'", "'false'", "'while'", 
                     "'func'", "'return'", "'&&'", "'||'", "'!'", "'=='", 
                     "<INVALID>", "'<='", "'>='", "'<'", "'>'", "'='", "'+'", 
                     "'-'", "'*'", "'/'", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "PROGRAMA", "SI", "SINO", "IMPRIMIR", 
                      "TIPO_ENTERO", "TIPO_BOOL", "VERDADERO", "FALSO", 
                      "MIENTRAS", "FUNC", "RETORNO", "Y_LOGICO", "O_LOGICO", 
                      "NEGACION", "IGUAL", "DIFERENTE", "MENOR_IGUAL", "MAYOR_IGUAL", 
                      "MENOR_QUE", "MAYOR_QUE", "ASIGNACION", "SUMA", "RESTA", 
                      "MULTIPLICACION", "DIVISION", "PAREN_IZQ", "PAREN_DER", 
                      "LLAVE_IZQ", "LLAVE_DER", "CORCHETE_IZQ", "CORCHETE_DER", 
                      "PUNTO_COMA", "COMA", "IDENTIFICADOR", "ENTERO", "ESPACIO", 
                      "COMENTARIO_LINEA", "COMENTARIO_BLOQUE" ]

    RULE_programa = 0
    RULE_cuerpoPrincipal = 1
    RULE_declaracionFuncion = 2
    RULE_listaParametros = 3
    RULE_parametro = 4
    RULE_bloque = 5
    RULE_sentencia = 6
    RULE_declaracionVariable = 7
    RULE_tipo = 8
    RULE_asignacion = 9
    RULE_condicionalSi = 10
    RULE_cicloMientras = 11
    RULE_imprimir = 12
    RULE_retorno = 13
    RULE_expresion = 14
    RULE_listaArgumentos = 15

    ruleNames =  [ "programa", "cuerpoPrincipal", "declaracionFuncion", 
                   "listaParametros", "parametro", "bloque", "sentencia", 
                   "declaracionVariable", "tipo", "asignacion", "condicionalSi", 
                   "cicloMientras", "imprimir", "retorno", "expresion", 
                   "listaArgumentos" ]

    EOF = Token.EOF
    PROGRAMA=1
    SI=2
    SINO=3
    IMPRIMIR=4
    TIPO_ENTERO=5
    TIPO_BOOL=6
    VERDADERO=7
    FALSO=8
    MIENTRAS=9
    FUNC=10
    RETORNO=11
    Y_LOGICO=12
    O_LOGICO=13
    NEGACION=14
    IGUAL=15
    DIFERENTE=16
    MENOR_IGUAL=17
    MAYOR_IGUAL=18
    MENOR_QUE=19
    MAYOR_QUE=20
    ASIGNACION=21
    SUMA=22
    RESTA=23
    MULTIPLICACION=24
    DIVISION=25
    PAREN_IZQ=26
    PAREN_DER=27
    LLAVE_IZQ=28
    LLAVE_DER=29
    CORCHETE_IZQ=30
    CORCHETE_DER=31
    PUNTO_COMA=32
    COMA=33
    IDENTIFICADOR=34
    ENTERO=35
    ESPACIO=36
    COMENTARIO_LINEA=37
    COMENTARIO_BLOQUE=38

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

        def cuerpoPrincipal(self):
            return self.getTypedRuleContext(MiniLangParser.CuerpoPrincipalContext,0)


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
            self.state = 32
            self.match(MiniLangParser.PROGRAMA)
            self.state = 33
            self.cuerpoPrincipal()
            self.state = 34
            self.match(MiniLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CuerpoPrincipalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLAVE_IZQ(self):
            return self.getToken(MiniLangParser.LLAVE_IZQ, 0)

        def LLAVE_DER(self):
            return self.getToken(MiniLangParser.LLAVE_DER, 0)

        def declaracionFuncion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.DeclaracionFuncionContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.DeclaracionFuncionContext,i)


        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.SentenciaContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_cuerpoPrincipal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCuerpoPrincipal" ):
                return visitor.visitCuerpoPrincipal(self)
            else:
                return visitor.visitChildren(self)




    def cuerpoPrincipal(self):

        localctx = MiniLangParser.CuerpoPrincipalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_cuerpoPrincipal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(MiniLangParser.LLAVE_IZQ)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 37
                self.declaracionFuncion()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 17179871860) != 0):
                self.state = 43
                self.sentencia()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self.match(MiniLangParser.LLAVE_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionFuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniLangParser.FUNC, 0)

        def tipo(self):
            return self.getTypedRuleContext(MiniLangParser.TipoContext,0)


        def IDENTIFICADOR(self):
            return self.getToken(MiniLangParser.IDENTIFICADOR, 0)

        def PAREN_IZQ(self):
            return self.getToken(MiniLangParser.PAREN_IZQ, 0)

        def PAREN_DER(self):
            return self.getToken(MiniLangParser.PAREN_DER, 0)

        def bloque(self):
            return self.getTypedRuleContext(MiniLangParser.BloqueContext,0)


        def listaParametros(self):
            return self.getTypedRuleContext(MiniLangParser.ListaParametrosContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_declaracionFuncion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionFuncion" ):
                return visitor.visitDeclaracionFuncion(self)
            else:
                return visitor.visitChildren(self)




    def declaracionFuncion(self):

        localctx = MiniLangParser.DeclaracionFuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracionFuncion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(MiniLangParser.FUNC)
            self.state = 52
            self.tipo()
            self.state = 53
            self.match(MiniLangParser.IDENTIFICADOR)
            self.state = 54
            self.match(MiniLangParser.PAREN_IZQ)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5 or _la==6:
                self.state = 55
                self.listaParametros()


            self.state = 58
            self.match(MiniLangParser.PAREN_DER)
            self.state = 59
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
        self.enterRule(localctx, 6, self.RULE_listaParametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.parametro()
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 62
                self.match(MiniLangParser.COMA)
                self.state = 63
                self.parametro()
                self.state = 68
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
        self.enterRule(localctx, 8, self.RULE_parametro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.tipo()
            self.state = 70
            self.match(MiniLangParser.IDENTIFICADOR)
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
            self.state = 72
            self.match(MiniLangParser.LLAVE_IZQ)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 17179871860) != 0):
                self.state = 73
                self.sentencia()
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
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


        def cicloMientras(self):
            return self.getTypedRuleContext(MiniLangParser.CicloMientrasContext,0)


        def imprimir(self):
            return self.getTypedRuleContext(MiniLangParser.ImprimirContext,0)


        def retorno(self):
            return self.getTypedRuleContext(MiniLangParser.RetornoContext,0)


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
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.declaracionVariable()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.asignacion()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.condicionalSi()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 84
                self.cicloMientras()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 85
                self.imprimir()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 6)
                self.state = 86
                self.retorno()
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
        self.enterRule(localctx, 14, self.RULE_declaracionVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.tipo()
            self.state = 90
            self.match(MiniLangParser.IDENTIFICADOR)
            self.state = 91
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
        self.enterRule(localctx, 16, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
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
        self.enterRule(localctx, 18, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(MiniLangParser.IDENTIFICADOR)
            self.state = 96
            self.match(MiniLangParser.ASIGNACION)
            self.state = 97
            self.expresion(0)
            self.state = 98
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
            self.state = 100
            self.match(MiniLangParser.SI)
            self.state = 101
            self.match(MiniLangParser.PAREN_IZQ)
            self.state = 102
            self.expresion(0)
            self.state = 103
            self.match(MiniLangParser.PAREN_DER)
            self.state = 104
            self.bloque()
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 105
                self.match(MiniLangParser.SINO)
                self.state = 106
                self.bloque()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CicloMientrasContext(ParserRuleContext):
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
            return MiniLangParser.RULE_cicloMientras

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCicloMientras" ):
                return visitor.visitCicloMientras(self)
            else:
                return visitor.visitChildren(self)




    def cicloMientras(self):

        localctx = MiniLangParser.CicloMientrasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_cicloMientras)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(MiniLangParser.MIENTRAS)
            self.state = 110
            self.match(MiniLangParser.PAREN_IZQ)
            self.state = 111
            self.expresion(0)
            self.state = 112
            self.match(MiniLangParser.PAREN_DER)
            self.state = 113
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
        self.enterRule(localctx, 24, self.RULE_imprimir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(MiniLangParser.IMPRIMIR)
            self.state = 116
            self.match(MiniLangParser.PAREN_IZQ)
            self.state = 117
            self.expresion(0)
            self.state = 118
            self.match(MiniLangParser.PAREN_DER)
            self.state = 119
            self.match(MiniLangParser.PUNTO_COMA)
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

        def RETORNO(self):
            return self.getToken(MiniLangParser.RETORNO, 0)

        def expresion(self):
            return self.getTypedRuleContext(MiniLangParser.ExpresionContext,0)


        def PUNTO_COMA(self):
            return self.getToken(MiniLangParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_retorno

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetorno" ):
                return visitor.visitRetorno(self)
            else:
                return visitor.visitChildren(self)




    def retorno(self):

        localctx = MiniLangParser.RetornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_retorno)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(MiniLangParser.RETORNO)
            self.state = 122
            self.expresion(0)
            self.state = 123
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
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = MiniLangParser.NegacionLogicaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 126
                self.match(MiniLangParser.NEGACION)
                self.state = 127
                self.expresion(14)
                pass

            elif la_ == 2:
                localctx = MiniLangParser.MenosUnarioContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 128
                self.match(MiniLangParser.RESTA)
                self.state = 129
                self.expresion(13)
                pass

            elif la_ == 3:
                localctx = MiniLangParser.LlamadaFuncionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 130
                self.match(MiniLangParser.IDENTIFICADOR)
                self.state = 131
                self.match(MiniLangParser.PAREN_IZQ)
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 51615121792) != 0):
                    self.state = 132
                    self.listaArgumentos()


                self.state = 135
                self.match(MiniLangParser.PAREN_DER)
                pass

            elif la_ == 4:
                localctx = MiniLangParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 136
                self.match(MiniLangParser.PAREN_IZQ)
                self.state = 137
                self.expresion(0)
                self.state = 138
                self.match(MiniLangParser.PAREN_DER)
                pass

            elif la_ == 5:
                localctx = MiniLangParser.LiteralEnteroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 140
                self.match(MiniLangParser.ENTERO)
                pass

            elif la_ == 6:
                localctx = MiniLangParser.LiteralVerdaderoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 141
                self.match(MiniLangParser.VERDADERO)
                pass

            elif la_ == 7:
                localctx = MiniLangParser.LiteralFalsoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 142
                self.match(MiniLangParser.FALSO)
                pass

            elif la_ == 8:
                localctx = MiniLangParser.ReferenciaVariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 143
                self.match(MiniLangParser.IDENTIFICADOR)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 166
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 164
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = MiniLangParser.MultiplicacionDivisionContext(self, MiniLangParser.ExpresionContext(self, _parentctx, _parentState))
                        localctx.izq = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 146
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 147
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==24 or _la==25):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 148
                        localctx.der = self.expresion(11)
                        pass

                    elif la_ == 2:
                        localctx = MiniLangParser.SumaRestaContext(self, MiniLangParser.ExpresionContext(self, _parentctx, _parentState))
                        localctx.izq = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 149
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 150
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==22 or _la==23):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 151
                        localctx.der = self.expresion(10)
                        pass

                    elif la_ == 3:
                        localctx = MiniLangParser.ComparacionContext(self, MiniLangParser.ExpresionContext(self, _parentctx, _parentState))
                        localctx.izq = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 152
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 153
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1966080) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 154
                        localctx.der = self.expresion(9)
                        pass

                    elif la_ == 4:
                        localctx = MiniLangParser.IgualdadContext(self, MiniLangParser.ExpresionContext(self, _parentctx, _parentState))
                        localctx.izq = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 155
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 156
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 157
                        localctx.der = self.expresion(8)
                        pass

                    elif la_ == 5:
                        localctx = MiniLangParser.YLogicoContext(self, MiniLangParser.ExpresionContext(self, _parentctx, _parentState))
                        localctx.izq = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 158
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 159
                        self.match(MiniLangParser.Y_LOGICO)
                        self.state = 160
                        localctx.der = self.expresion(7)
                        pass

                    elif la_ == 6:
                        localctx = MiniLangParser.OLogicoContext(self, MiniLangParser.ExpresionContext(self, _parentctx, _parentState))
                        localctx.izq = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 161
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 162
                        self.match(MiniLangParser.O_LOGICO)
                        self.state = 163
                        localctx.der = self.expresion(6)
                        pass

             
                self.state = 168
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 30, self.RULE_listaArgumentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.expresion(0)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 170
                self.match(MiniLangParser.COMA)
                self.state = 171
                self.expresion(0)
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.expresion_sempred
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
         




