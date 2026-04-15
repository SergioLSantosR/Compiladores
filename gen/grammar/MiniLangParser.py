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
        4,1,44,232,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,5,0,40,8,0,
        10,0,12,0,43,9,0,1,0,1,0,1,0,5,0,48,8,0,10,0,12,0,51,9,0,1,0,1,0,
        1,1,1,1,1,1,3,1,58,8,1,1,1,1,1,1,1,3,1,63,8,1,1,1,1,1,1,1,1,2,1,
        2,1,2,5,2,71,8,2,10,2,12,2,74,9,2,1,3,1,3,1,3,1,4,1,4,5,4,81,8,4,
        10,4,12,4,84,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,96,
        8,5,1,6,1,6,1,6,1,6,3,6,102,8,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,
        1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,120,8,9,1,10,1,10,1,10,1,10,
        1,10,1,10,1,11,1,11,1,11,1,11,1,11,5,11,133,8,11,10,11,12,11,136,
        9,11,3,11,138,8,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,13,
        1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,
        1,16,1,16,1,16,1,16,3,16,166,8,16,1,16,1,16,3,16,170,8,16,1,16,1,
        16,3,16,174,8,16,1,16,1,16,1,16,1,17,1,17,3,17,181,8,17,1,17,1,17,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,5,18,205,8,18,10,18,12,18,208,
        9,18,3,18,210,8,18,1,18,3,18,213,8,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,5,18,227,8,18,10,18,12,18,230,9,
        18,1,18,0,1,36,19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,0,5,1,0,10,13,1,0,28,29,1,0,26,27,1,0,19,24,1,0,16,17,249,
        0,41,1,0,0,0,2,54,1,0,0,0,4,67,1,0,0,0,6,75,1,0,0,0,8,78,1,0,0,0,
        10,95,1,0,0,0,12,97,1,0,0,0,14,105,1,0,0,0,16,107,1,0,0,0,18,112,
        1,0,0,0,20,121,1,0,0,0,22,127,1,0,0,0,24,142,1,0,0,0,26,147,1,0,
        0,0,28,151,1,0,0,0,30,155,1,0,0,0,32,161,1,0,0,0,34,178,1,0,0,0,
        36,212,1,0,0,0,38,40,3,2,1,0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,
        0,0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,41,1,0,0,0,44,45,5,1,0,0,45,
        49,3,8,4,0,46,48,3,2,1,0,47,46,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,
        0,49,50,1,0,0,0,50,52,1,0,0,0,51,49,1,0,0,0,52,53,5,0,0,1,53,1,1,
        0,0,0,54,57,5,7,0,0,55,58,3,14,7,0,56,58,5,9,0,0,57,55,1,0,0,0,57,
        56,1,0,0,0,58,59,1,0,0,0,59,60,5,41,0,0,60,62,5,30,0,0,61,63,3,4,
        2,0,62,61,1,0,0,0,62,63,1,0,0,0,63,64,1,0,0,0,64,65,5,31,0,0,65,
        66,3,8,4,0,66,3,1,0,0,0,67,72,3,6,3,0,68,69,5,37,0,0,69,71,3,6,3,
        0,70,68,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,5,1,
        0,0,0,74,72,1,0,0,0,75,76,3,14,7,0,76,77,5,41,0,0,77,7,1,0,0,0,78,
        82,5,32,0,0,79,81,3,10,5,0,80,79,1,0,0,0,81,84,1,0,0,0,82,80,1,0,
        0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,82,1,0,0,0,85,86,5,33,0,0,86,
        9,1,0,0,0,87,96,3,12,6,0,88,96,3,16,8,0,89,96,3,18,9,0,90,96,3,20,
        10,0,91,96,3,30,15,0,92,96,3,32,16,0,93,96,3,34,17,0,94,96,3,22,
        11,0,95,87,1,0,0,0,95,88,1,0,0,0,95,89,1,0,0,0,95,90,1,0,0,0,95,
        91,1,0,0,0,95,92,1,0,0,0,95,93,1,0,0,0,95,94,1,0,0,0,96,11,1,0,0,
        0,97,98,3,14,7,0,98,101,5,41,0,0,99,100,5,25,0,0,100,102,3,36,18,
        0,101,99,1,0,0,0,101,102,1,0,0,0,102,103,1,0,0,0,103,104,5,36,0,
        0,104,13,1,0,0,0,105,106,7,0,0,0,106,15,1,0,0,0,107,108,5,41,0,0,
        108,109,5,25,0,0,109,110,3,36,18,0,110,111,5,36,0,0,111,17,1,0,0,
        0,112,113,5,2,0,0,113,114,5,30,0,0,114,115,3,36,18,0,115,116,5,31,
        0,0,116,119,3,8,4,0,117,118,5,3,0,0,118,120,3,8,4,0,119,117,1,0,
        0,0,119,120,1,0,0,0,120,19,1,0,0,0,121,122,5,4,0,0,122,123,5,30,
        0,0,123,124,3,36,18,0,124,125,5,31,0,0,125,126,5,36,0,0,126,21,1,
        0,0,0,127,128,5,41,0,0,128,137,5,30,0,0,129,134,3,36,18,0,130,131,
        5,37,0,0,131,133,3,36,18,0,132,130,1,0,0,0,133,136,1,0,0,0,134,132,
        1,0,0,0,134,135,1,0,0,0,135,138,1,0,0,0,136,134,1,0,0,0,137,129,
        1,0,0,0,137,138,1,0,0,0,138,139,1,0,0,0,139,140,5,31,0,0,140,141,
        5,36,0,0,141,23,1,0,0,0,142,143,3,14,7,0,143,144,5,41,0,0,144,145,
        5,25,0,0,145,146,3,36,18,0,146,25,1,0,0,0,147,148,5,41,0,0,148,149,
        5,25,0,0,149,150,3,36,18,0,150,27,1,0,0,0,151,152,5,41,0,0,152,153,
        5,25,0,0,153,154,3,36,18,0,154,29,1,0,0,0,155,156,5,5,0,0,156,157,
        5,30,0,0,157,158,3,36,18,0,158,159,5,31,0,0,159,160,3,8,4,0,160,
        31,1,0,0,0,161,162,5,6,0,0,162,165,5,30,0,0,163,166,3,24,12,0,164,
        166,3,26,13,0,165,163,1,0,0,0,165,164,1,0,0,0,165,166,1,0,0,0,166,
        167,1,0,0,0,167,169,5,36,0,0,168,170,3,36,18,0,169,168,1,0,0,0,169,
        170,1,0,0,0,170,171,1,0,0,0,171,173,5,36,0,0,172,174,3,28,14,0,173,
        172,1,0,0,0,173,174,1,0,0,0,174,175,1,0,0,0,175,176,5,31,0,0,176,
        177,3,8,4,0,177,33,1,0,0,0,178,180,5,8,0,0,179,181,3,36,18,0,180,
        179,1,0,0,0,180,181,1,0,0,0,181,182,1,0,0,0,182,183,5,36,0,0,183,
        35,1,0,0,0,184,185,6,18,-1,0,185,186,5,18,0,0,186,213,3,36,18,14,
        187,188,5,27,0,0,188,213,3,36,18,13,189,190,5,30,0,0,190,191,3,36,
        18,0,191,192,5,31,0,0,192,213,1,0,0,0,193,213,5,39,0,0,194,213,5,
        38,0,0,195,213,5,40,0,0,196,213,5,14,0,0,197,213,5,15,0,0,198,213,
        5,41,0,0,199,200,5,41,0,0,200,209,5,30,0,0,201,206,3,36,18,0,202,
        203,5,37,0,0,203,205,3,36,18,0,204,202,1,0,0,0,205,208,1,0,0,0,206,
        204,1,0,0,0,206,207,1,0,0,0,207,210,1,0,0,0,208,206,1,0,0,0,209,
        201,1,0,0,0,209,210,1,0,0,0,210,211,1,0,0,0,211,213,5,31,0,0,212,
        184,1,0,0,0,212,187,1,0,0,0,212,189,1,0,0,0,212,193,1,0,0,0,212,
        194,1,0,0,0,212,195,1,0,0,0,212,196,1,0,0,0,212,197,1,0,0,0,212,
        198,1,0,0,0,212,199,1,0,0,0,213,228,1,0,0,0,214,215,10,11,0,0,215,
        216,7,1,0,0,216,227,3,36,18,12,217,218,10,10,0,0,218,219,7,2,0,0,
        219,227,3,36,18,11,220,221,10,9,0,0,221,222,7,3,0,0,222,227,3,36,
        18,10,223,224,10,8,0,0,224,225,7,4,0,0,225,227,3,36,18,9,226,214,
        1,0,0,0,226,217,1,0,0,0,226,220,1,0,0,0,226,223,1,0,0,0,227,230,
        1,0,0,0,228,226,1,0,0,0,228,229,1,0,0,0,229,37,1,0,0,0,230,228,1,
        0,0,0,20,41,49,57,62,72,82,95,101,119,134,137,165,169,173,180,206,
        209,212,226,228
    ]

class MiniLangParser ( Parser ):

    grammarFileName = "MiniLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'programa'", "'si'", "'sino'", "'imprimir'", 
                     "'mientras'", "'para'", "'funcion'", "'retorna'", "'vacio'", 
                     "'entero'", "'booleano'", "'flotante'", "'cadena'", 
                     "'verdadero'", "'falso'", "'&&'", "'||'", "'!'", "'=='", 
                     "<INVALID>", "'<='", "'>='", "'<'", "'>'", "'='", "'+'", 
                     "'-'", "'*'", "'/'", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "PROGRAMA", "SI", "SINO", "IMPRIMIR", 
                      "MIENTRAS", "PARA", "FUNCION", "RETORNA", "VOID", 
                      "TIPO_ENTERO", "TIPO_BOOL", "TIPO_FLOTANTE", "TIPO_CADENA", 
                      "VERDADERO", "FALSO", "Y_LOGICO", "O_LOGICO", "NEGACION", 
                      "IGUAL", "DIFERENTE", "MENOR_IGUAL", "MAYOR_IGUAL", 
                      "MENOR_QUE", "MAYOR_QUE", "ASIGNACION", "SUMA", "RESTA", 
                      "MULTIPLICACION", "DIVISION", "PAREN_IZQ", "PAREN_DER", 
                      "LLAVE_IZQ", "LLAVE_DER", "CORCHETE_IZQ", "CORCHETE_DER", 
                      "PUNTO_COMA", "COMA", "FLOTANTE", "ENTERO", "CADENA", 
                      "IDENTIFICADOR", "ESPACIO", "COMENTARIO_LINEA", "COMENTARIO_BLOQUE" ]

    RULE_programa = 0
    RULE_funcionDeclaracion = 1
    RULE_parametros = 2
    RULE_parametro = 3
    RULE_bloque = 4
    RULE_sentencia = 5
    RULE_declaracionVariable = 6
    RULE_tipo = 7
    RULE_asignacion = 8
    RULE_condicionalSi = 9
    RULE_impresion = 10
    RULE_llamadaFuncion = 11
    RULE_inicializacionPara = 12
    RULE_asignacionPara = 13
    RULE_actualizacionPara = 14
    RULE_cicloMientras = 15
    RULE_cicloPara = 16
    RULE_sentenciaRetorna = 17
    RULE_expresion = 18

    ruleNames =  [ "programa", "funcionDeclaracion", "parametros", "parametro", 
                   "bloque", "sentencia", "declaracionVariable", "tipo", 
                   "asignacion", "condicionalSi", "impresion", "llamadaFuncion", 
                   "inicializacionPara", "asignacionPara", "actualizacionPara", 
                   "cicloMientras", "cicloPara", "sentenciaRetorna", "expresion" ]

    EOF = Token.EOF
    PROGRAMA=1
    SI=2
    SINO=3
    IMPRIMIR=4
    MIENTRAS=5
    PARA=6
    FUNCION=7
    RETORNA=8
    VOID=9
    TIPO_ENTERO=10
    TIPO_BOOL=11
    TIPO_FLOTANTE=12
    TIPO_CADENA=13
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
    FLOTANTE=38
    ENTERO=39
    CADENA=40
    IDENTIFICADOR=41
    ESPACIO=42
    COMENTARIO_LINEA=43
    COMENTARIO_BLOQUE=44

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

        def funcionDeclaracion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.FuncionDeclaracionContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.FuncionDeclaracionContext,i)


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
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 38
                self.funcionDeclaracion()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(MiniLangParser.PROGRAMA)
            self.state = 45
            self.bloque()
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 46
                self.funcionDeclaracion()
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


    class FuncionDeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCION(self):
            return self.getToken(MiniLangParser.FUNCION, 0)

        def IDENTIFICADOR(self):
            return self.getToken(MiniLangParser.IDENTIFICADOR, 0)

        def PAREN_IZQ(self):
            return self.getToken(MiniLangParser.PAREN_IZQ, 0)

        def PAREN_DER(self):
            return self.getToken(MiniLangParser.PAREN_DER, 0)

        def bloque(self):
            return self.getTypedRuleContext(MiniLangParser.BloqueContext,0)


        def tipo(self):
            return self.getTypedRuleContext(MiniLangParser.TipoContext,0)


        def VOID(self):
            return self.getToken(MiniLangParser.VOID, 0)

        def parametros(self):
            return self.getTypedRuleContext(MiniLangParser.ParametrosContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_funcionDeclaracion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncionDeclaracion" ):
                return visitor.visitFuncionDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def funcionDeclaracion(self):

        localctx = MiniLangParser.FuncionDeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_funcionDeclaracion)
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
            self.match(MiniLangParser.IDENTIFICADOR)
            self.state = 60
            self.match(MiniLangParser.PAREN_IZQ)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 15360) != 0):
                self.state = 61
                self.parametros()


            self.state = 64
            self.match(MiniLangParser.PAREN_DER)
            self.state = 65
            self.bloque()
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
            self.state = 75
            self.tipo()
            self.state = 76
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
        self.enterRule(localctx, 8, self.RULE_bloque)
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

        def declaracionVariable(self):
            return self.getTypedRuleContext(MiniLangParser.DeclaracionVariableContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(MiniLangParser.AsignacionContext,0)


        def condicionalSi(self):
            return self.getTypedRuleContext(MiniLangParser.CondicionalSiContext,0)


        def impresion(self):
            return self.getTypedRuleContext(MiniLangParser.ImpresionContext,0)


        def cicloMientras(self):
            return self.getTypedRuleContext(MiniLangParser.CicloMientrasContext,0)


        def cicloPara(self):
            return self.getTypedRuleContext(MiniLangParser.CicloParaContext,0)


        def sentenciaRetorna(self):
            return self.getTypedRuleContext(MiniLangParser.SentenciaRetornaContext,0)


        def llamadaFuncion(self):
            return self.getTypedRuleContext(MiniLangParser.LlamadaFuncionContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_sentencia

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
                self.declaracionVariable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.asignacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 89
                self.condicionalSi()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 90
                self.impresion()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 91
                self.cicloMientras()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 92
                self.cicloPara()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 93
                self.sentenciaRetorna()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 94
                self.llamadaFuncion()
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
        self.enterRule(localctx, 12, self.RULE_declaracionVariable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.tipo()
            self.state = 98
            self.match(MiniLangParser.IDENTIFICADOR)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 99
                self.match(MiniLangParser.ASIGNACION)
                self.state = 100
                self.expresion(0)


            self.state = 103
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

        def TIPO_FLOTANTE(self):
            return self.getToken(MiniLangParser.TIPO_FLOTANTE, 0)

        def TIPO_CADENA(self):
            return self.getToken(MiniLangParser.TIPO_CADENA, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_tipo

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
            self.state = 105
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
        self.enterRule(localctx, 16, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(MiniLangParser.IDENTIFICADOR)
            self.state = 108
            self.match(MiniLangParser.ASIGNACION)
            self.state = 109
            self.expresion(0)
            self.state = 110
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
        self.enterRule(localctx, 18, self.RULE_condicionalSi)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(MiniLangParser.SI)
            self.state = 113
            self.match(MiniLangParser.PAREN_IZQ)
            self.state = 114
            self.expresion(0)
            self.state = 115
            self.match(MiniLangParser.PAREN_DER)
            self.state = 116
            self.bloque()
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 117
                self.match(MiniLangParser.SINO)
                self.state = 118
                self.bloque()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImpresionContext(ParserRuleContext):
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
            return MiniLangParser.RULE_impresion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImpresion" ):
                return visitor.visitImpresion(self)
            else:
                return visitor.visitChildren(self)




    def impresion(self):

        localctx = MiniLangParser.ImpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_impresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(MiniLangParser.IMPRIMIR)
            self.state = 122
            self.match(MiniLangParser.PAREN_IZQ)
            self.state = 123
            self.expresion(0)
            self.state = 124
            self.match(MiniLangParser.PAREN_DER)
            self.state = 125
            self.match(MiniLangParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlamadaFuncionContext(ParserRuleContext):
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
            return MiniLangParser.RULE_llamadaFuncion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamadaFuncion" ):
                return visitor.visitLlamadaFuncion(self)
            else:
                return visitor.visitChildren(self)




    def llamadaFuncion(self):

        localctx = MiniLangParser.LlamadaFuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_llamadaFuncion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(MiniLangParser.IDENTIFICADOR)
            self.state = 128
            self.match(MiniLangParser.PAREN_IZQ)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4124376875008) != 0):
                self.state = 129
                self.expresion(0)
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==37:
                    self.state = 130
                    self.match(MiniLangParser.COMA)
                    self.state = 131
                    self.expresion(0)
                    self.state = 136
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 139
            self.match(MiniLangParser.PAREN_DER)
            self.state = 140
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


        def IDENTIFICADOR(self):
            return self.getToken(MiniLangParser.IDENTIFICADOR, 0)

        def ASIGNACION(self):
            return self.getToken(MiniLangParser.ASIGNACION, 0)

        def expresion(self):
            return self.getTypedRuleContext(MiniLangParser.ExpresionContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_inicializacionPara

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
            self.state = 142
            self.tipo()
            self.state = 143
            self.match(MiniLangParser.IDENTIFICADOR)
            self.state = 144
            self.match(MiniLangParser.ASIGNACION)
            self.state = 145
            self.expresion(0)
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

        def IDENTIFICADOR(self):
            return self.getToken(MiniLangParser.IDENTIFICADOR, 0)

        def ASIGNACION(self):
            return self.getToken(MiniLangParser.ASIGNACION, 0)

        def expresion(self):
            return self.getTypedRuleContext(MiniLangParser.ExpresionContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_asignacionPara

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
            self.state = 147
            self.match(MiniLangParser.IDENTIFICADOR)
            self.state = 148
            self.match(MiniLangParser.ASIGNACION)
            self.state = 149
            self.expresion(0)
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

        def IDENTIFICADOR(self):
            return self.getToken(MiniLangParser.IDENTIFICADOR, 0)

        def ASIGNACION(self):
            return self.getToken(MiniLangParser.ASIGNACION, 0)

        def expresion(self):
            return self.getTypedRuleContext(MiniLangParser.ExpresionContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_actualizacionPara

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
            self.state = 151
            self.match(MiniLangParser.IDENTIFICADOR)
            self.state = 152
            self.match(MiniLangParser.ASIGNACION)
            self.state = 153
            self.expresion(0)
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
        self.enterRule(localctx, 30, self.RULE_cicloMientras)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(MiniLangParser.MIENTRAS)
            self.state = 156
            self.match(MiniLangParser.PAREN_IZQ)
            self.state = 157
            self.expresion(0)
            self.state = 158
            self.match(MiniLangParser.PAREN_DER)
            self.state = 159
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CicloParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.cond = None # ExpresionContext

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


        def inicializacionPara(self):
            return self.getTypedRuleContext(MiniLangParser.InicializacionParaContext,0)


        def asignacionPara(self):
            return self.getTypedRuleContext(MiniLangParser.AsignacionParaContext,0)


        def actualizacionPara(self):
            return self.getTypedRuleContext(MiniLangParser.ActualizacionParaContext,0)


        def expresion(self):
            return self.getTypedRuleContext(MiniLangParser.ExpresionContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_cicloPara

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCicloPara" ):
                return visitor.visitCicloPara(self)
            else:
                return visitor.visitChildren(self)




    def cicloPara(self):

        localctx = MiniLangParser.CicloParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_cicloPara)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(MiniLangParser.PARA)
            self.state = 162
            self.match(MiniLangParser.PAREN_IZQ)
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11, 12, 13]:
                self.state = 163
                self.inicializacionPara()
                pass
            elif token in [41]:
                self.state = 164
                self.asignacionPara()
                pass
            elif token in [36]:
                pass
            else:
                pass
            self.state = 167
            self.match(MiniLangParser.PUNTO_COMA)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4124376875008) != 0):
                self.state = 168
                localctx.cond = self.expresion(0)


            self.state = 171
            self.match(MiniLangParser.PUNTO_COMA)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 172
                self.actualizacionPara()


            self.state = 175
            self.match(MiniLangParser.PAREN_DER)
            self.state = 176
            self.bloque()
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

        def expresion(self):
            return self.getTypedRuleContext(MiniLangParser.ExpresionContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_sentenciaRetorna

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
            self.state = 178
            self.match(MiniLangParser.RETORNA)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4124376875008) != 0):
                self.state = 179
                self.expresion(0)


            self.state = 182
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


    class LlamadaFuncionExprContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFICADOR(self):
            return self.getToken(MiniLangParser.IDENTIFICADOR, 0)
        def PAREN_IZQ(self):
            return self.getToken(MiniLangParser.PAREN_IZQ, 0)
        def PAREN_DER(self):
            return self.getToken(MiniLangParser.PAREN_DER, 0)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamadaFuncionExpr" ):
                return visitor.visitLlamadaFuncionExpr(self)
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


    class RelacionalContext(ExpresionContext):

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
        def MENOR_QUE(self):
            return self.getToken(MiniLangParser.MENOR_QUE, 0)
        def MENOR_IGUAL(self):
            return self.getToken(MiniLangParser.MENOR_IGUAL, 0)
        def MAYOR_QUE(self):
            return self.getToken(MiniLangParser.MAYOR_QUE, 0)
        def MAYOR_IGUAL(self):
            return self.getToken(MiniLangParser.MAYOR_IGUAL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelacional" ):
                return visitor.visitRelacional(self)
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


    class LogicaContext(ExpresionContext):

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

        def Y_LOGICO(self):
            return self.getToken(MiniLangParser.Y_LOGICO, 0)
        def O_LOGICO(self):
            return self.getToken(MiniLangParser.O_LOGICO, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogica" ):
                return visitor.visitLogica(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniLangParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                localctx = MiniLangParser.NegacionLogicaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 185
                self.match(MiniLangParser.NEGACION)
                self.state = 186
                self.expresion(14)
                pass

            elif la_ == 2:
                localctx = MiniLangParser.MenosUnarioContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 187
                self.match(MiniLangParser.RESTA)
                self.state = 188
                self.expresion(13)
                pass

            elif la_ == 3:
                localctx = MiniLangParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 189
                self.match(MiniLangParser.PAREN_IZQ)
                self.state = 190
                self.expresion(0)
                self.state = 191
                self.match(MiniLangParser.PAREN_DER)
                pass

            elif la_ == 4:
                localctx = MiniLangParser.LiteralEnteroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 193
                self.match(MiniLangParser.ENTERO)
                pass

            elif la_ == 5:
                localctx = MiniLangParser.LiteralFlotanteContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 194
                self.match(MiniLangParser.FLOTANTE)
                pass

            elif la_ == 6:
                localctx = MiniLangParser.LiteralCadenaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 195
                self.match(MiniLangParser.CADENA)
                pass

            elif la_ == 7:
                localctx = MiniLangParser.LiteralVerdaderoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 196
                self.match(MiniLangParser.VERDADERO)
                pass

            elif la_ == 8:
                localctx = MiniLangParser.LiteralFalsoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 197
                self.match(MiniLangParser.FALSO)
                pass

            elif la_ == 9:
                localctx = MiniLangParser.ReferenciaVariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 198
                self.match(MiniLangParser.IDENTIFICADOR)
                pass

            elif la_ == 10:
                localctx = MiniLangParser.LlamadaFuncionExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 199
                self.match(MiniLangParser.IDENTIFICADOR)
                self.state = 200
                self.match(MiniLangParser.PAREN_IZQ)
                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4124376875008) != 0):
                    self.state = 201
                    self.expresion(0)
                    self.state = 206
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==37:
                        self.state = 202
                        self.match(MiniLangParser.COMA)
                        self.state = 203
                        self.expresion(0)
                        self.state = 208
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 211
                self.match(MiniLangParser.PAREN_DER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 226
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = MiniLangParser.MultiplicacionDivisionContext(self, MiniLangParser.ExpresionContext(self, _parentctx, _parentState))
                        localctx.izq = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 214
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 215
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==28 or _la==29):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 216
                        localctx.der = self.expresion(12)
                        pass

                    elif la_ == 2:
                        localctx = MiniLangParser.SumaRestaContext(self, MiniLangParser.ExpresionContext(self, _parentctx, _parentState))
                        localctx.izq = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 217
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 218
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==26 or _la==27):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 219
                        localctx.der = self.expresion(11)
                        pass

                    elif la_ == 3:
                        localctx = MiniLangParser.RelacionalContext(self, MiniLangParser.ExpresionContext(self, _parentctx, _parentState))
                        localctx.izq = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 220
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 221
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33030144) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 222
                        localctx.der = self.expresion(10)
                        pass

                    elif la_ == 4:
                        localctx = MiniLangParser.LogicaContext(self, MiniLangParser.ExpresionContext(self, _parentctx, _parentState))
                        localctx.izq = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 223
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 224
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 225
                        localctx.der = self.expresion(9)
                        pass

             
                self.state = 230
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        self._predicates[18] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         




