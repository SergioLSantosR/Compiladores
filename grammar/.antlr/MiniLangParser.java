// Generated from /home/sergio/Compiladores/grammar/MiniLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class MiniLangParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PROGRAMA=1, SI=2, SINO=3, IMPRIMIR=4, MIENTRAS=5, PARA=6, FUNCION=7, RETORNA=8, 
		VOID=9, TIPO_ENTERO=10, TIPO_BOOL=11, TIPO_FLOTANTE=12, TIPO_CADENA=13, 
		VERDADERO=14, FALSO=15, ROMPER=16, CONTINUAR=17, IMPORTAR=18, Y_LOGICO=19, 
		O_LOGICO=20, NEGACION=21, IGUAL=22, DIFERENTE=23, MENOR_IGUAL=24, MAYOR_IGUAL=25, 
		MENOR_QUE=26, MAYOR_QUE=27, ASIGNACION=28, SUMA=29, RESTA=30, MULTIPLICACION=31, 
		DIVISION=32, MODULO=33, PAREN_IZQ=34, PAREN_DER=35, LLAVE_IZQ=36, LLAVE_DER=37, 
		CORCHETE_IZQ=38, CORCHETE_DER=39, PUNTO_COMA=40, COMA=41, FLOTANTE=42, 
		ENTERO=43, CADENA=44, IDENTIFICADOR=45, ESPACIO=46, COMENTARIO_LINEA=47, 
		COMENTARIO_BLOQUE=48;
	public static final int
		RULE_programa = 0, RULE_funcionDeclaracion = 1, RULE_parametros = 2, RULE_parametro = 3, 
		RULE_bloque = 4, RULE_sentencia = 5, RULE_declaracionVariable = 6, RULE_literalArreglo = 7, 
		RULE_accesoArreglo = 8, RULE_asignacionArreglo = 9, RULE_tipo = 10, RULE_asignacion = 11, 
		RULE_condicionalSi = 12, RULE_impresion = 13, RULE_llamadaFuncion = 14, 
		RULE_inicializacionPara = 15, RULE_asignacionPara = 16, RULE_actualizacionPara = 17, 
		RULE_cicloMientras = 18, RULE_cicloPara = 19, RULE_sentenciaRetorna = 20, 
		RULE_sentenciaBreak = 21, RULE_sentenciaContinue = 22, RULE_sentenciaImportar = 23, 
		RULE_expresion = 24;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "funcionDeclaracion", "parametros", "parametro", "bloque", 
			"sentencia", "declaracionVariable", "literalArreglo", "accesoArreglo", 
			"asignacionArreglo", "tipo", "asignacion", "condicionalSi", "impresion", 
			"llamadaFuncion", "inicializacionPara", "asignacionPara", "actualizacionPara", 
			"cicloMientras", "cicloPara", "sentenciaRetorna", "sentenciaBreak", "sentenciaContinue", 
			"sentenciaImportar", "expresion"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'programa'", "'si'", "'sino'", "'imprimir'", "'mientras'", "'para'", 
			"'funcion'", "'retorna'", "'vacio'", "'entero'", "'booleano'", "'flotante'", 
			"'cadena'", "'verdadero'", "'falso'", "'romper'", "'continuar'", "'importar'", 
			"'&&'", "'||'", "'!'", "'=='", null, "'<='", "'>='", "'<'", "'>'", "'='", 
			"'+'", "'-'", "'*'", "'/'", "'%'", "'('", "')'", "'{'", "'}'", "'['", 
			"']'", "';'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PROGRAMA", "SI", "SINO", "IMPRIMIR", "MIENTRAS", "PARA", "FUNCION", 
			"RETORNA", "VOID", "TIPO_ENTERO", "TIPO_BOOL", "TIPO_FLOTANTE", "TIPO_CADENA", 
			"VERDADERO", "FALSO", "ROMPER", "CONTINUAR", "IMPORTAR", "Y_LOGICO", 
			"O_LOGICO", "NEGACION", "IGUAL", "DIFERENTE", "MENOR_IGUAL", "MAYOR_IGUAL", 
			"MENOR_QUE", "MAYOR_QUE", "ASIGNACION", "SUMA", "RESTA", "MULTIPLICACION", 
			"DIVISION", "MODULO", "PAREN_IZQ", "PAREN_DER", "LLAVE_IZQ", "LLAVE_DER", 
			"CORCHETE_IZQ", "CORCHETE_DER", "PUNTO_COMA", "COMA", "FLOTANTE", "ENTERO", 
			"CADENA", "IDENTIFICADOR", "ESPACIO", "COMENTARIO_LINEA", "COMENTARIO_BLOQUE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "MiniLang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MiniLangParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
		public TerminalNode PROGRAMA() { return getToken(MiniLangParser.PROGRAMA, 0); }
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public TerminalNode EOF() { return getToken(MiniLangParser.EOF, 0); }
		public List<FuncionDeclaracionContext> funcionDeclaracion() {
			return getRuleContexts(FuncionDeclaracionContext.class);
		}
		public FuncionDeclaracionContext funcionDeclaracion(int i) {
			return getRuleContext(FuncionDeclaracionContext.class,i);
		}
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programa);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNCION) {
				{
				{
				setState(50);
				funcionDeclaracion();
				}
				}
				setState(55);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(56);
			match(PROGRAMA);
			setState(57);
			bloque();
			setState(61);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNCION) {
				{
				{
				setState(58);
				funcionDeclaracion();
				}
				}
				setState(63);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(64);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FuncionDeclaracionContext extends ParserRuleContext {
		public TerminalNode FUNCION() { return getToken(MiniLangParser.FUNCION, 0); }
		public TerminalNode IDENTIFICADOR() { return getToken(MiniLangParser.IDENTIFICADOR, 0); }
		public TerminalNode PAREN_IZQ() { return getToken(MiniLangParser.PAREN_IZQ, 0); }
		public TerminalNode PAREN_DER() { return getToken(MiniLangParser.PAREN_DER, 0); }
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode VOID() { return getToken(MiniLangParser.VOID, 0); }
		public ParametrosContext parametros() {
			return getRuleContext(ParametrosContext.class,0);
		}
		public FuncionDeclaracionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcionDeclaracion; }
	}

	public final FuncionDeclaracionContext funcionDeclaracion() throws RecognitionException {
		FuncionDeclaracionContext _localctx = new FuncionDeclaracionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_funcionDeclaracion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			match(FUNCION);
			setState(69);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TIPO_ENTERO:
			case TIPO_BOOL:
			case TIPO_FLOTANTE:
			case TIPO_CADENA:
				{
				setState(67);
				tipo();
				}
				break;
			case VOID:
				{
				setState(68);
				match(VOID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(71);
			match(IDENTIFICADOR);
			setState(72);
			match(PAREN_IZQ);
			setState(74);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 15360L) != 0)) {
				{
				setState(73);
				parametros();
				}
			}

			setState(76);
			match(PAREN_DER);
			setState(77);
			bloque();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParametrosContext extends ParserRuleContext {
		public List<ParametroContext> parametro() {
			return getRuleContexts(ParametroContext.class);
		}
		public ParametroContext parametro(int i) {
			return getRuleContext(ParametroContext.class,i);
		}
		public List<TerminalNode> COMA() { return getTokens(MiniLangParser.COMA); }
		public TerminalNode COMA(int i) {
			return getToken(MiniLangParser.COMA, i);
		}
		public ParametrosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parametros; }
	}

	public final ParametrosContext parametros() throws RecognitionException {
		ParametrosContext _localctx = new ParametrosContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_parametros);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(79);
			parametro();
			setState(84);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMA) {
				{
				{
				setState(80);
				match(COMA);
				setState(81);
				parametro();
				}
				}
				setState(86);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParametroContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode IDENTIFICADOR() { return getToken(MiniLangParser.IDENTIFICADOR, 0); }
		public ParametroContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parametro; }
	}

	public final ParametroContext parametro() throws RecognitionException {
		ParametroContext _localctx = new ParametroContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_parametro);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			tipo();
			setState(88);
			match(IDENTIFICADOR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BloqueContext extends ParserRuleContext {
		public TerminalNode LLAVE_IZQ() { return getToken(MiniLangParser.LLAVE_IZQ, 0); }
		public TerminalNode LLAVE_DER() { return getToken(MiniLangParser.LLAVE_DER, 0); }
		public List<SentenciaContext> sentencia() {
			return getRuleContexts(SentenciaContext.class);
		}
		public SentenciaContext sentencia(int i) {
			return getRuleContext(SentenciaContext.class,i);
		}
		public BloqueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloque; }
	}

	public final BloqueContext bloque() throws RecognitionException {
		BloqueContext _localctx = new BloqueContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_bloque);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			match(LLAVE_IZQ);
			setState(94);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 35184372563316L) != 0)) {
				{
				{
				setState(91);
				sentencia();
				}
				}
				setState(96);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(97);
			match(LLAVE_DER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SentenciaContext extends ParserRuleContext {
		public DeclaracionVariableContext declaracionVariable() {
			return getRuleContext(DeclaracionVariableContext.class,0);
		}
		public AsignacionContext asignacion() {
			return getRuleContext(AsignacionContext.class,0);
		}
		public AsignacionArregloContext asignacionArreglo() {
			return getRuleContext(AsignacionArregloContext.class,0);
		}
		public CondicionalSiContext condicionalSi() {
			return getRuleContext(CondicionalSiContext.class,0);
		}
		public ImpresionContext impresion() {
			return getRuleContext(ImpresionContext.class,0);
		}
		public CicloMientrasContext cicloMientras() {
			return getRuleContext(CicloMientrasContext.class,0);
		}
		public CicloParaContext cicloPara() {
			return getRuleContext(CicloParaContext.class,0);
		}
		public SentenciaRetornaContext sentenciaRetorna() {
			return getRuleContext(SentenciaRetornaContext.class,0);
		}
		public LlamadaFuncionContext llamadaFuncion() {
			return getRuleContext(LlamadaFuncionContext.class,0);
		}
		public SentenciaBreakContext sentenciaBreak() {
			return getRuleContext(SentenciaBreakContext.class,0);
		}
		public SentenciaContinueContext sentenciaContinue() {
			return getRuleContext(SentenciaContinueContext.class,0);
		}
		public SentenciaImportarContext sentenciaImportar() {
			return getRuleContext(SentenciaImportarContext.class,0);
		}
		public SentenciaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentencia; }
	}

	public final SentenciaContext sentencia() throws RecognitionException {
		SentenciaContext _localctx = new SentenciaContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_sentencia);
		try {
			setState(111);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(99);
				declaracionVariable();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(100);
				asignacion();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(101);
				asignacionArreglo();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(102);
				condicionalSi();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(103);
				impresion();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(104);
				cicloMientras();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(105);
				cicloPara();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(106);
				sentenciaRetorna();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(107);
				llamadaFuncion();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(108);
				sentenciaBreak();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(109);
				sentenciaContinue();
				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(110);
				sentenciaImportar();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracionVariableContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode IDENTIFICADOR() { return getToken(MiniLangParser.IDENTIFICADOR, 0); }
		public TerminalNode PUNTO_COMA() { return getToken(MiniLangParser.PUNTO_COMA, 0); }
		public TerminalNode ASIGNACION() { return getToken(MiniLangParser.ASIGNACION, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode CORCHETE_IZQ() { return getToken(MiniLangParser.CORCHETE_IZQ, 0); }
		public TerminalNode CORCHETE_DER() { return getToken(MiniLangParser.CORCHETE_DER, 0); }
		public LiteralArregloContext literalArreglo() {
			return getRuleContext(LiteralArregloContext.class,0);
		}
		public DeclaracionVariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracionVariable; }
	}

	public final DeclaracionVariableContext declaracionVariable() throws RecognitionException {
		DeclaracionVariableContext _localctx = new DeclaracionVariableContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_declaracionVariable);
		int _la;
		try {
			setState(131);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(113);
				tipo();
				setState(114);
				match(IDENTIFICADOR);
				setState(117);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASIGNACION) {
					{
					setState(115);
					match(ASIGNACION);
					setState(116);
					expresion(0);
					}
				}

				setState(119);
				match(PUNTO_COMA);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(121);
				tipo();
				setState(122);
				match(CORCHETE_IZQ);
				setState(123);
				match(CORCHETE_DER);
				setState(124);
				match(IDENTIFICADOR);
				setState(127);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASIGNACION) {
					{
					setState(125);
					match(ASIGNACION);
					setState(126);
					literalArreglo();
					}
				}

				setState(129);
				match(PUNTO_COMA);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LiteralArregloContext extends ParserRuleContext {
		public TerminalNode CORCHETE_IZQ() { return getToken(MiniLangParser.CORCHETE_IZQ, 0); }
		public TerminalNode CORCHETE_DER() { return getToken(MiniLangParser.CORCHETE_DER, 0); }
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public List<TerminalNode> COMA() { return getTokens(MiniLangParser.COMA); }
		public TerminalNode COMA(int i) {
			return getToken(MiniLangParser.COMA, i);
		}
		public LiteralArregloContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literalArreglo; }
	}

	public final LiteralArregloContext literalArreglo() throws RecognitionException {
		LiteralArregloContext _localctx = new LiteralArregloContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_literalArreglo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(133);
			match(CORCHETE_IZQ);
			setState(142);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 65988953423872L) != 0)) {
				{
				setState(134);
				expresion(0);
				setState(139);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMA) {
					{
					{
					setState(135);
					match(COMA);
					setState(136);
					expresion(0);
					}
					}
					setState(141);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(144);
			match(CORCHETE_DER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AccesoArregloContext extends ParserRuleContext {
		public TerminalNode IDENTIFICADOR() { return getToken(MiniLangParser.IDENTIFICADOR, 0); }
		public TerminalNode CORCHETE_IZQ() { return getToken(MiniLangParser.CORCHETE_IZQ, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode CORCHETE_DER() { return getToken(MiniLangParser.CORCHETE_DER, 0); }
		public AccesoArregloContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_accesoArreglo; }
	}

	public final AccesoArregloContext accesoArreglo() throws RecognitionException {
		AccesoArregloContext _localctx = new AccesoArregloContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_accesoArreglo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(146);
			match(IDENTIFICADOR);
			setState(147);
			match(CORCHETE_IZQ);
			setState(148);
			expresion(0);
			setState(149);
			match(CORCHETE_DER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AsignacionArregloContext extends ParserRuleContext {
		public AccesoArregloContext accesoArreglo() {
			return getRuleContext(AccesoArregloContext.class,0);
		}
		public TerminalNode ASIGNACION() { return getToken(MiniLangParser.ASIGNACION, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode PUNTO_COMA() { return getToken(MiniLangParser.PUNTO_COMA, 0); }
		public AsignacionArregloContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacionArreglo; }
	}

	public final AsignacionArregloContext asignacionArreglo() throws RecognitionException {
		AsignacionArregloContext _localctx = new AsignacionArregloContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_asignacionArreglo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(151);
			accesoArreglo();
			setState(152);
			match(ASIGNACION);
			setState(153);
			expresion(0);
			setState(154);
			match(PUNTO_COMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TipoContext extends ParserRuleContext {
		public TerminalNode TIPO_ENTERO() { return getToken(MiniLangParser.TIPO_ENTERO, 0); }
		public TerminalNode TIPO_BOOL() { return getToken(MiniLangParser.TIPO_BOOL, 0); }
		public TerminalNode TIPO_FLOTANTE() { return getToken(MiniLangParser.TIPO_FLOTANTE, 0); }
		public TerminalNode TIPO_CADENA() { return getToken(MiniLangParser.TIPO_CADENA, 0); }
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(156);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 15360L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AsignacionContext extends ParserRuleContext {
		public TerminalNode IDENTIFICADOR() { return getToken(MiniLangParser.IDENTIFICADOR, 0); }
		public TerminalNode ASIGNACION() { return getToken(MiniLangParser.ASIGNACION, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode PUNTO_COMA() { return getToken(MiniLangParser.PUNTO_COMA, 0); }
		public AsignacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacion; }
	}

	public final AsignacionContext asignacion() throws RecognitionException {
		AsignacionContext _localctx = new AsignacionContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_asignacion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(158);
			match(IDENTIFICADOR);
			setState(159);
			match(ASIGNACION);
			setState(160);
			expresion(0);
			setState(161);
			match(PUNTO_COMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CondicionalSiContext extends ParserRuleContext {
		public TerminalNode SI() { return getToken(MiniLangParser.SI, 0); }
		public TerminalNode PAREN_IZQ() { return getToken(MiniLangParser.PAREN_IZQ, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode PAREN_DER() { return getToken(MiniLangParser.PAREN_DER, 0); }
		public List<BloqueContext> bloque() {
			return getRuleContexts(BloqueContext.class);
		}
		public BloqueContext bloque(int i) {
			return getRuleContext(BloqueContext.class,i);
		}
		public TerminalNode SINO() { return getToken(MiniLangParser.SINO, 0); }
		public CondicionalSiContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicionalSi; }
	}

	public final CondicionalSiContext condicionalSi() throws RecognitionException {
		CondicionalSiContext _localctx = new CondicionalSiContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_condicionalSi);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(163);
			match(SI);
			setState(164);
			match(PAREN_IZQ);
			setState(165);
			expresion(0);
			setState(166);
			match(PAREN_DER);
			setState(167);
			bloque();
			setState(170);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SINO) {
				{
				setState(168);
				match(SINO);
				setState(169);
				bloque();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ImpresionContext extends ParserRuleContext {
		public TerminalNode IMPRIMIR() { return getToken(MiniLangParser.IMPRIMIR, 0); }
		public TerminalNode PAREN_IZQ() { return getToken(MiniLangParser.PAREN_IZQ, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode PAREN_DER() { return getToken(MiniLangParser.PAREN_DER, 0); }
		public TerminalNode PUNTO_COMA() { return getToken(MiniLangParser.PUNTO_COMA, 0); }
		public ImpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_impresion; }
	}

	public final ImpresionContext impresion() throws RecognitionException {
		ImpresionContext _localctx = new ImpresionContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_impresion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(172);
			match(IMPRIMIR);
			setState(173);
			match(PAREN_IZQ);
			setState(174);
			expresion(0);
			setState(175);
			match(PAREN_DER);
			setState(176);
			match(PUNTO_COMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LlamadaFuncionContext extends ParserRuleContext {
		public TerminalNode IDENTIFICADOR() { return getToken(MiniLangParser.IDENTIFICADOR, 0); }
		public TerminalNode PAREN_IZQ() { return getToken(MiniLangParser.PAREN_IZQ, 0); }
		public TerminalNode PAREN_DER() { return getToken(MiniLangParser.PAREN_DER, 0); }
		public TerminalNode PUNTO_COMA() { return getToken(MiniLangParser.PUNTO_COMA, 0); }
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public List<TerminalNode> COMA() { return getTokens(MiniLangParser.COMA); }
		public TerminalNode COMA(int i) {
			return getToken(MiniLangParser.COMA, i);
		}
		public LlamadaFuncionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_llamadaFuncion; }
	}

	public final LlamadaFuncionContext llamadaFuncion() throws RecognitionException {
		LlamadaFuncionContext _localctx = new LlamadaFuncionContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_llamadaFuncion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(178);
			match(IDENTIFICADOR);
			setState(179);
			match(PAREN_IZQ);
			setState(188);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 65988953423872L) != 0)) {
				{
				setState(180);
				expresion(0);
				setState(185);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMA) {
					{
					{
					setState(181);
					match(COMA);
					setState(182);
					expresion(0);
					}
					}
					setState(187);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(190);
			match(PAREN_DER);
			setState(191);
			match(PUNTO_COMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InicializacionParaContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode IDENTIFICADOR() { return getToken(MiniLangParser.IDENTIFICADOR, 0); }
		public TerminalNode ASIGNACION() { return getToken(MiniLangParser.ASIGNACION, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public InicializacionParaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inicializacionPara; }
	}

	public final InicializacionParaContext inicializacionPara() throws RecognitionException {
		InicializacionParaContext _localctx = new InicializacionParaContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_inicializacionPara);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(193);
			tipo();
			setState(194);
			match(IDENTIFICADOR);
			setState(195);
			match(ASIGNACION);
			setState(196);
			expresion(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AsignacionParaContext extends ParserRuleContext {
		public TerminalNode IDENTIFICADOR() { return getToken(MiniLangParser.IDENTIFICADOR, 0); }
		public TerminalNode ASIGNACION() { return getToken(MiniLangParser.ASIGNACION, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public AsignacionParaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacionPara; }
	}

	public final AsignacionParaContext asignacionPara() throws RecognitionException {
		AsignacionParaContext _localctx = new AsignacionParaContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_asignacionPara);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(198);
			match(IDENTIFICADOR);
			setState(199);
			match(ASIGNACION);
			setState(200);
			expresion(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ActualizacionParaContext extends ParserRuleContext {
		public TerminalNode IDENTIFICADOR() { return getToken(MiniLangParser.IDENTIFICADOR, 0); }
		public TerminalNode ASIGNACION() { return getToken(MiniLangParser.ASIGNACION, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public ActualizacionParaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_actualizacionPara; }
	}

	public final ActualizacionParaContext actualizacionPara() throws RecognitionException {
		ActualizacionParaContext _localctx = new ActualizacionParaContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_actualizacionPara);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(202);
			match(IDENTIFICADOR);
			setState(203);
			match(ASIGNACION);
			setState(204);
			expresion(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CicloMientrasContext extends ParserRuleContext {
		public TerminalNode MIENTRAS() { return getToken(MiniLangParser.MIENTRAS, 0); }
		public TerminalNode PAREN_IZQ() { return getToken(MiniLangParser.PAREN_IZQ, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode PAREN_DER() { return getToken(MiniLangParser.PAREN_DER, 0); }
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public CicloMientrasContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cicloMientras; }
	}

	public final CicloMientrasContext cicloMientras() throws RecognitionException {
		CicloMientrasContext _localctx = new CicloMientrasContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_cicloMientras);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(206);
			match(MIENTRAS);
			setState(207);
			match(PAREN_IZQ);
			setState(208);
			expresion(0);
			setState(209);
			match(PAREN_DER);
			setState(210);
			bloque();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CicloParaContext extends ParserRuleContext {
		public ExpresionContext cond;
		public TerminalNode PARA() { return getToken(MiniLangParser.PARA, 0); }
		public TerminalNode PAREN_IZQ() { return getToken(MiniLangParser.PAREN_IZQ, 0); }
		public List<TerminalNode> PUNTO_COMA() { return getTokens(MiniLangParser.PUNTO_COMA); }
		public TerminalNode PUNTO_COMA(int i) {
			return getToken(MiniLangParser.PUNTO_COMA, i);
		}
		public TerminalNode PAREN_DER() { return getToken(MiniLangParser.PAREN_DER, 0); }
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public InicializacionParaContext inicializacionPara() {
			return getRuleContext(InicializacionParaContext.class,0);
		}
		public AsignacionParaContext asignacionPara() {
			return getRuleContext(AsignacionParaContext.class,0);
		}
		public ActualizacionParaContext actualizacionPara() {
			return getRuleContext(ActualizacionParaContext.class,0);
		}
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public CicloParaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cicloPara; }
	}

	public final CicloParaContext cicloPara() throws RecognitionException {
		CicloParaContext _localctx = new CicloParaContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_cicloPara);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(212);
			match(PARA);
			setState(213);
			match(PAREN_IZQ);
			setState(216);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TIPO_ENTERO:
			case TIPO_BOOL:
			case TIPO_FLOTANTE:
			case TIPO_CADENA:
				{
				setState(214);
				inicializacionPara();
				}
				break;
			case IDENTIFICADOR:
				{
				setState(215);
				asignacionPara();
				}
				break;
			case PUNTO_COMA:
				break;
			default:
				break;
			}
			setState(218);
			match(PUNTO_COMA);
			setState(220);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 65988953423872L) != 0)) {
				{
				setState(219);
				((CicloParaContext)_localctx).cond = expresion(0);
				}
			}

			setState(222);
			match(PUNTO_COMA);
			setState(224);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==IDENTIFICADOR) {
				{
				setState(223);
				actualizacionPara();
				}
			}

			setState(226);
			match(PAREN_DER);
			setState(227);
			bloque();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SentenciaRetornaContext extends ParserRuleContext {
		public TerminalNode RETORNA() { return getToken(MiniLangParser.RETORNA, 0); }
		public TerminalNode PUNTO_COMA() { return getToken(MiniLangParser.PUNTO_COMA, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public SentenciaRetornaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentenciaRetorna; }
	}

	public final SentenciaRetornaContext sentenciaRetorna() throws RecognitionException {
		SentenciaRetornaContext _localctx = new SentenciaRetornaContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_sentenciaRetorna);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(229);
			match(RETORNA);
			setState(231);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 65988953423872L) != 0)) {
				{
				setState(230);
				expresion(0);
				}
			}

			setState(233);
			match(PUNTO_COMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SentenciaBreakContext extends ParserRuleContext {
		public TerminalNode ROMPER() { return getToken(MiniLangParser.ROMPER, 0); }
		public TerminalNode PUNTO_COMA() { return getToken(MiniLangParser.PUNTO_COMA, 0); }
		public SentenciaBreakContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentenciaBreak; }
	}

	public final SentenciaBreakContext sentenciaBreak() throws RecognitionException {
		SentenciaBreakContext _localctx = new SentenciaBreakContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_sentenciaBreak);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(235);
			match(ROMPER);
			setState(236);
			match(PUNTO_COMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SentenciaContinueContext extends ParserRuleContext {
		public TerminalNode CONTINUAR() { return getToken(MiniLangParser.CONTINUAR, 0); }
		public TerminalNode PUNTO_COMA() { return getToken(MiniLangParser.PUNTO_COMA, 0); }
		public SentenciaContinueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentenciaContinue; }
	}

	public final SentenciaContinueContext sentenciaContinue() throws RecognitionException {
		SentenciaContinueContext _localctx = new SentenciaContinueContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_sentenciaContinue);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(238);
			match(CONTINUAR);
			setState(239);
			match(PUNTO_COMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SentenciaImportarContext extends ParserRuleContext {
		public TerminalNode IMPORTAR() { return getToken(MiniLangParser.IMPORTAR, 0); }
		public TerminalNode CADENA() { return getToken(MiniLangParser.CADENA, 0); }
		public TerminalNode PUNTO_COMA() { return getToken(MiniLangParser.PUNTO_COMA, 0); }
		public SentenciaImportarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentenciaImportar; }
	}

	public final SentenciaImportarContext sentenciaImportar() throws RecognitionException {
		SentenciaImportarContext _localctx = new SentenciaImportarContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_sentenciaImportar);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(241);
			match(IMPORTAR);
			setState(242);
			match(CADENA);
			setState(243);
			match(PUNTO_COMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpresionContext extends ParserRuleContext {
		public ExpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion; }
	 
		public ExpresionContext() { }
		public void copyFrom(ExpresionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LiteralCadenaContext extends ExpresionContext {
		public TerminalNode CADENA() { return getToken(MiniLangParser.CADENA, 0); }
		public LiteralCadenaContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParentesisContext extends ExpresionContext {
		public TerminalNode PAREN_IZQ() { return getToken(MiniLangParser.PAREN_IZQ, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode PAREN_DER() { return getToken(MiniLangParser.PAREN_DER, 0); }
		public ParentesisContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MenosUnarioContext extends ExpresionContext {
		public TerminalNode RESTA() { return getToken(MiniLangParser.RESTA, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public MenosUnarioContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LlamadaFuncionExprContext extends ExpresionContext {
		public TerminalNode IDENTIFICADOR() { return getToken(MiniLangParser.IDENTIFICADOR, 0); }
		public TerminalNode PAREN_IZQ() { return getToken(MiniLangParser.PAREN_IZQ, 0); }
		public TerminalNode PAREN_DER() { return getToken(MiniLangParser.PAREN_DER, 0); }
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public List<TerminalNode> COMA() { return getTokens(MiniLangParser.COMA); }
		public TerminalNode COMA(int i) {
			return getToken(MiniLangParser.COMA, i);
		}
		public LlamadaFuncionExprContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LiteralEnteroContext extends ExpresionContext {
		public TerminalNode ENTERO() { return getToken(MiniLangParser.ENTERO, 0); }
		public LiteralEnteroContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LiteralVerdaderoContext extends ExpresionContext {
		public TerminalNode VERDADERO() { return getToken(MiniLangParser.VERDADERO, 0); }
		public LiteralVerdaderoContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class SumaRestaContext extends ExpresionContext {
		public ExpresionContext izq;
		public Token op;
		public ExpresionContext der;
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public TerminalNode SUMA() { return getToken(MiniLangParser.SUMA, 0); }
		public TerminalNode RESTA() { return getToken(MiniLangParser.RESTA, 0); }
		public SumaRestaContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LiteralFlotanteContext extends ExpresionContext {
		public TerminalNode FLOTANTE() { return getToken(MiniLangParser.FLOTANTE, 0); }
		public LiteralFlotanteContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NegacionLogicaContext extends ExpresionContext {
		public TerminalNode NEGACION() { return getToken(MiniLangParser.NEGACION, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public NegacionLogicaContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class RelacionalContext extends ExpresionContext {
		public ExpresionContext izq;
		public Token op;
		public ExpresionContext der;
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public TerminalNode IGUAL() { return getToken(MiniLangParser.IGUAL, 0); }
		public TerminalNode DIFERENTE() { return getToken(MiniLangParser.DIFERENTE, 0); }
		public TerminalNode MENOR_QUE() { return getToken(MiniLangParser.MENOR_QUE, 0); }
		public TerminalNode MENOR_IGUAL() { return getToken(MiniLangParser.MENOR_IGUAL, 0); }
		public TerminalNode MAYOR_QUE() { return getToken(MiniLangParser.MAYOR_QUE, 0); }
		public TerminalNode MAYOR_IGUAL() { return getToken(MiniLangParser.MAYOR_IGUAL, 0); }
		public RelacionalContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ReferenciaVariableContext extends ExpresionContext {
		public TerminalNode IDENTIFICADOR() { return getToken(MiniLangParser.IDENTIFICADOR, 0); }
		public ReferenciaVariableContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LiteralFalsoContext extends ExpresionContext {
		public TerminalNode FALSO() { return getToken(MiniLangParser.FALSO, 0); }
		public LiteralFalsoContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AccesoArregloExprContext extends ExpresionContext {
		public AccesoArregloContext accesoArreglo() {
			return getRuleContext(AccesoArregloContext.class,0);
		}
		public AccesoArregloExprContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MultiplicacionDivisionModuloContext extends ExpresionContext {
		public ExpresionContext izq;
		public Token op;
		public ExpresionContext der;
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public TerminalNode MULTIPLICACION() { return getToken(MiniLangParser.MULTIPLICACION, 0); }
		public TerminalNode DIVISION() { return getToken(MiniLangParser.DIVISION, 0); }
		public TerminalNode MODULO() { return getToken(MiniLangParser.MODULO, 0); }
		public MultiplicacionDivisionModuloContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LogicaContext extends ExpresionContext {
		public ExpresionContext izq;
		public Token op;
		public ExpresionContext der;
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public TerminalNode Y_LOGICO() { return getToken(MiniLangParser.Y_LOGICO, 0); }
		public TerminalNode O_LOGICO() { return getToken(MiniLangParser.O_LOGICO, 0); }
		public LogicaContext(ExpresionContext ctx) { copyFrom(ctx); }
	}

	public final ExpresionContext expresion() throws RecognitionException {
		return expresion(0);
	}

	private ExpresionContext expresion(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpresionContext _localctx = new ExpresionContext(_ctx, _parentState);
		ExpresionContext _prevctx = _localctx;
		int _startState = 48;
		enterRecursionRule(_localctx, 48, RULE_expresion, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(274);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				{
				_localctx = new NegacionLogicaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(246);
				match(NEGACION);
				setState(247);
				expresion(15);
				}
				break;
			case 2:
				{
				_localctx = new MenosUnarioContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(248);
				match(RESTA);
				setState(249);
				expresion(14);
				}
				break;
			case 3:
				{
				_localctx = new ParentesisContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(250);
				match(PAREN_IZQ);
				setState(251);
				expresion(0);
				setState(252);
				match(PAREN_DER);
				}
				break;
			case 4:
				{
				_localctx = new LiteralEnteroContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(254);
				match(ENTERO);
				}
				break;
			case 5:
				{
				_localctx = new LiteralFlotanteContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(255);
				match(FLOTANTE);
				}
				break;
			case 6:
				{
				_localctx = new LiteralCadenaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(256);
				match(CADENA);
				}
				break;
			case 7:
				{
				_localctx = new LiteralVerdaderoContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(257);
				match(VERDADERO);
				}
				break;
			case 8:
				{
				_localctx = new LiteralFalsoContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(258);
				match(FALSO);
				}
				break;
			case 9:
				{
				_localctx = new ReferenciaVariableContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(259);
				match(IDENTIFICADOR);
				}
				break;
			case 10:
				{
				_localctx = new AccesoArregloExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(260);
				accesoArreglo();
				}
				break;
			case 11:
				{
				_localctx = new LlamadaFuncionExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(261);
				match(IDENTIFICADOR);
				setState(262);
				match(PAREN_IZQ);
				setState(271);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 65988953423872L) != 0)) {
					{
					setState(263);
					expresion(0);
					setState(268);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMA) {
						{
						{
						setState(264);
						match(COMA);
						setState(265);
						expresion(0);
						}
						}
						setState(270);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(273);
				match(PAREN_DER);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(290);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(288);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
					case 1:
						{
						_localctx = new MultiplicacionDivisionModuloContext(new ExpresionContext(_parentctx, _parentState));
						((MultiplicacionDivisionModuloContext)_localctx).izq = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expresion);
						setState(276);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(277);
						((MultiplicacionDivisionModuloContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 15032385536L) != 0)) ) {
							((MultiplicacionDivisionModuloContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(278);
						((MultiplicacionDivisionModuloContext)_localctx).der = expresion(13);
						}
						break;
					case 2:
						{
						_localctx = new SumaRestaContext(new ExpresionContext(_parentctx, _parentState));
						((SumaRestaContext)_localctx).izq = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expresion);
						setState(279);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(280);
						((SumaRestaContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==SUMA || _la==RESTA) ) {
							((SumaRestaContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(281);
						((SumaRestaContext)_localctx).der = expresion(12);
						}
						break;
					case 3:
						{
						_localctx = new RelacionalContext(new ExpresionContext(_parentctx, _parentState));
						((RelacionalContext)_localctx).izq = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expresion);
						setState(282);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(283);
						((RelacionalContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 264241152L) != 0)) ) {
							((RelacionalContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(284);
						((RelacionalContext)_localctx).der = expresion(11);
						}
						break;
					case 4:
						{
						_localctx = new LogicaContext(new ExpresionContext(_parentctx, _parentState));
						((LogicaContext)_localctx).izq = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expresion);
						setState(285);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(286);
						((LogicaContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==Y_LOGICO || _la==O_LOGICO) ) {
							((LogicaContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(287);
						((LogicaContext)_localctx).der = expresion(10);
						}
						break;
					}
					} 
				}
				setState(292);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 24:
			return expresion_sempred((ExpresionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expresion_sempred(ExpresionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 12);
		case 1:
			return precpred(_ctx, 11);
		case 2:
			return precpred(_ctx, 10);
		case 3:
			return precpred(_ctx, 9);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u00010\u0126\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0001\u0000\u0005\u00004\b\u0000\n\u0000\f\u00007\t\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0005\u0000<\b\u0000\n\u0000\f\u0000?\t\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001"+
		"F\b\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001K\b\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0005"+
		"\u0002S\b\u0002\n\u0002\f\u0002V\t\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0005\u0004]\b\u0004\n\u0004\f\u0004`\t"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0003\u0005p\b\u0005\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0003\u0006v\b\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0003\u0006\u0080\b\u0006\u0001\u0006\u0001\u0006\u0003\u0006\u0084"+
		"\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0005\u0007\u008a"+
		"\b\u0007\n\u0007\f\u0007\u008d\t\u0007\u0003\u0007\u008f\b\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f"+
		"\u0001\f\u0001\f\u0003\f\u00ab\b\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0005\u000e\u00b8\b\u000e\n\u000e\f\u000e\u00bb\t\u000e\u0003\u000e\u00bd"+
		"\b\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001"+
		"\u0013\u0001\u0013\u0001\u0013\u0003\u0013\u00d9\b\u0013\u0001\u0013\u0001"+
		"\u0013\u0003\u0013\u00dd\b\u0013\u0001\u0013\u0001\u0013\u0003\u0013\u00e1"+
		"\b\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0003"+
		"\u0014\u00e8\b\u0014\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001"+
		"\u0017\u0001\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0005\u0018\u010b"+
		"\b\u0018\n\u0018\f\u0018\u010e\t\u0018\u0003\u0018\u0110\b\u0018\u0001"+
		"\u0018\u0003\u0018\u0113\b\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0005\u0018\u0121\b\u0018\n\u0018\f\u0018"+
		"\u0124\t\u0018\u0001\u0018\u0000\u00010\u0019\u0000\u0002\u0004\u0006"+
		"\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,."+
		"0\u0000\u0005\u0001\u0000\n\r\u0001\u0000\u001f!\u0001\u0000\u001d\u001e"+
		"\u0001\u0000\u0016\u001b\u0001\u0000\u0013\u0014\u013a\u00005\u0001\u0000"+
		"\u0000\u0000\u0002B\u0001\u0000\u0000\u0000\u0004O\u0001\u0000\u0000\u0000"+
		"\u0006W\u0001\u0000\u0000\u0000\bZ\u0001\u0000\u0000\u0000\no\u0001\u0000"+
		"\u0000\u0000\f\u0083\u0001\u0000\u0000\u0000\u000e\u0085\u0001\u0000\u0000"+
		"\u0000\u0010\u0092\u0001\u0000\u0000\u0000\u0012\u0097\u0001\u0000\u0000"+
		"\u0000\u0014\u009c\u0001\u0000\u0000\u0000\u0016\u009e\u0001\u0000\u0000"+
		"\u0000\u0018\u00a3\u0001\u0000\u0000\u0000\u001a\u00ac\u0001\u0000\u0000"+
		"\u0000\u001c\u00b2\u0001\u0000\u0000\u0000\u001e\u00c1\u0001\u0000\u0000"+
		"\u0000 \u00c6\u0001\u0000\u0000\u0000\"\u00ca\u0001\u0000\u0000\u0000"+
		"$\u00ce\u0001\u0000\u0000\u0000&\u00d4\u0001\u0000\u0000\u0000(\u00e5"+
		"\u0001\u0000\u0000\u0000*\u00eb\u0001\u0000\u0000\u0000,\u00ee\u0001\u0000"+
		"\u0000\u0000.\u00f1\u0001\u0000\u0000\u00000\u0112\u0001\u0000\u0000\u0000"+
		"24\u0003\u0002\u0001\u000032\u0001\u0000\u0000\u000047\u0001\u0000\u0000"+
		"\u000053\u0001\u0000\u0000\u000056\u0001\u0000\u0000\u000068\u0001\u0000"+
		"\u0000\u000075\u0001\u0000\u0000\u000089\u0005\u0001\u0000\u00009=\u0003"+
		"\b\u0004\u0000:<\u0003\u0002\u0001\u0000;:\u0001\u0000\u0000\u0000<?\u0001"+
		"\u0000\u0000\u0000=;\u0001\u0000\u0000\u0000=>\u0001\u0000\u0000\u0000"+
		">@\u0001\u0000\u0000\u0000?=\u0001\u0000\u0000\u0000@A\u0005\u0000\u0000"+
		"\u0001A\u0001\u0001\u0000\u0000\u0000BE\u0005\u0007\u0000\u0000CF\u0003"+
		"\u0014\n\u0000DF\u0005\t\u0000\u0000EC\u0001\u0000\u0000\u0000ED\u0001"+
		"\u0000\u0000\u0000FG\u0001\u0000\u0000\u0000GH\u0005-\u0000\u0000HJ\u0005"+
		"\"\u0000\u0000IK\u0003\u0004\u0002\u0000JI\u0001\u0000\u0000\u0000JK\u0001"+
		"\u0000\u0000\u0000KL\u0001\u0000\u0000\u0000LM\u0005#\u0000\u0000MN\u0003"+
		"\b\u0004\u0000N\u0003\u0001\u0000\u0000\u0000OT\u0003\u0006\u0003\u0000"+
		"PQ\u0005)\u0000\u0000QS\u0003\u0006\u0003\u0000RP\u0001\u0000\u0000\u0000"+
		"SV\u0001\u0000\u0000\u0000TR\u0001\u0000\u0000\u0000TU\u0001\u0000\u0000"+
		"\u0000U\u0005\u0001\u0000\u0000\u0000VT\u0001\u0000\u0000\u0000WX\u0003"+
		"\u0014\n\u0000XY\u0005-\u0000\u0000Y\u0007\u0001\u0000\u0000\u0000Z^\u0005"+
		"$\u0000\u0000[]\u0003\n\u0005\u0000\\[\u0001\u0000\u0000\u0000]`\u0001"+
		"\u0000\u0000\u0000^\\\u0001\u0000\u0000\u0000^_\u0001\u0000\u0000\u0000"+
		"_a\u0001\u0000\u0000\u0000`^\u0001\u0000\u0000\u0000ab\u0005%\u0000\u0000"+
		"b\t\u0001\u0000\u0000\u0000cp\u0003\f\u0006\u0000dp\u0003\u0016\u000b"+
		"\u0000ep\u0003\u0012\t\u0000fp\u0003\u0018\f\u0000gp\u0003\u001a\r\u0000"+
		"hp\u0003$\u0012\u0000ip\u0003&\u0013\u0000jp\u0003(\u0014\u0000kp\u0003"+
		"\u001c\u000e\u0000lp\u0003*\u0015\u0000mp\u0003,\u0016\u0000np\u0003."+
		"\u0017\u0000oc\u0001\u0000\u0000\u0000od\u0001\u0000\u0000\u0000oe\u0001"+
		"\u0000\u0000\u0000of\u0001\u0000\u0000\u0000og\u0001\u0000\u0000\u0000"+
		"oh\u0001\u0000\u0000\u0000oi\u0001\u0000\u0000\u0000oj\u0001\u0000\u0000"+
		"\u0000ok\u0001\u0000\u0000\u0000ol\u0001\u0000\u0000\u0000om\u0001\u0000"+
		"\u0000\u0000on\u0001\u0000\u0000\u0000p\u000b\u0001\u0000\u0000\u0000"+
		"qr\u0003\u0014\n\u0000ru\u0005-\u0000\u0000st\u0005\u001c\u0000\u0000"+
		"tv\u00030\u0018\u0000us\u0001\u0000\u0000\u0000uv\u0001\u0000\u0000\u0000"+
		"vw\u0001\u0000\u0000\u0000wx\u0005(\u0000\u0000x\u0084\u0001\u0000\u0000"+
		"\u0000yz\u0003\u0014\n\u0000z{\u0005&\u0000\u0000{|\u0005\'\u0000\u0000"+
		"|\u007f\u0005-\u0000\u0000}~\u0005\u001c\u0000\u0000~\u0080\u0003\u000e"+
		"\u0007\u0000\u007f}\u0001\u0000\u0000\u0000\u007f\u0080\u0001\u0000\u0000"+
		"\u0000\u0080\u0081\u0001\u0000\u0000\u0000\u0081\u0082\u0005(\u0000\u0000"+
		"\u0082\u0084\u0001\u0000\u0000\u0000\u0083q\u0001\u0000\u0000\u0000\u0083"+
		"y\u0001\u0000\u0000\u0000\u0084\r\u0001\u0000\u0000\u0000\u0085\u008e"+
		"\u0005&\u0000\u0000\u0086\u008b\u00030\u0018\u0000\u0087\u0088\u0005)"+
		"\u0000\u0000\u0088\u008a\u00030\u0018\u0000\u0089\u0087\u0001\u0000\u0000"+
		"\u0000\u008a\u008d\u0001\u0000\u0000\u0000\u008b\u0089\u0001\u0000\u0000"+
		"\u0000\u008b\u008c\u0001\u0000\u0000\u0000\u008c\u008f\u0001\u0000\u0000"+
		"\u0000\u008d\u008b\u0001\u0000\u0000\u0000\u008e\u0086\u0001\u0000\u0000"+
		"\u0000\u008e\u008f\u0001\u0000\u0000\u0000\u008f\u0090\u0001\u0000\u0000"+
		"\u0000\u0090\u0091\u0005\'\u0000\u0000\u0091\u000f\u0001\u0000\u0000\u0000"+
		"\u0092\u0093\u0005-\u0000\u0000\u0093\u0094\u0005&\u0000\u0000\u0094\u0095"+
		"\u00030\u0018\u0000\u0095\u0096\u0005\'\u0000\u0000\u0096\u0011\u0001"+
		"\u0000\u0000\u0000\u0097\u0098\u0003\u0010\b\u0000\u0098\u0099\u0005\u001c"+
		"\u0000\u0000\u0099\u009a\u00030\u0018\u0000\u009a\u009b\u0005(\u0000\u0000"+
		"\u009b\u0013\u0001\u0000\u0000\u0000\u009c\u009d\u0007\u0000\u0000\u0000"+
		"\u009d\u0015\u0001\u0000\u0000\u0000\u009e\u009f\u0005-\u0000\u0000\u009f"+
		"\u00a0\u0005\u001c\u0000\u0000\u00a0\u00a1\u00030\u0018\u0000\u00a1\u00a2"+
		"\u0005(\u0000\u0000\u00a2\u0017\u0001\u0000\u0000\u0000\u00a3\u00a4\u0005"+
		"\u0002\u0000\u0000\u00a4\u00a5\u0005\"\u0000\u0000\u00a5\u00a6\u00030"+
		"\u0018\u0000\u00a6\u00a7\u0005#\u0000\u0000\u00a7\u00aa\u0003\b\u0004"+
		"\u0000\u00a8\u00a9\u0005\u0003\u0000\u0000\u00a9\u00ab\u0003\b\u0004\u0000"+
		"\u00aa\u00a8\u0001\u0000\u0000\u0000\u00aa\u00ab\u0001\u0000\u0000\u0000"+
		"\u00ab\u0019\u0001\u0000\u0000\u0000\u00ac\u00ad\u0005\u0004\u0000\u0000"+
		"\u00ad\u00ae\u0005\"\u0000\u0000\u00ae\u00af\u00030\u0018\u0000\u00af"+
		"\u00b0\u0005#\u0000\u0000\u00b0\u00b1\u0005(\u0000\u0000\u00b1\u001b\u0001"+
		"\u0000\u0000\u0000\u00b2\u00b3\u0005-\u0000\u0000\u00b3\u00bc\u0005\""+
		"\u0000\u0000\u00b4\u00b9\u00030\u0018\u0000\u00b5\u00b6\u0005)\u0000\u0000"+
		"\u00b6\u00b8\u00030\u0018\u0000\u00b7\u00b5\u0001\u0000\u0000\u0000\u00b8"+
		"\u00bb\u0001\u0000\u0000\u0000\u00b9\u00b7\u0001\u0000\u0000\u0000\u00b9"+
		"\u00ba\u0001\u0000\u0000\u0000\u00ba\u00bd\u0001\u0000\u0000\u0000\u00bb"+
		"\u00b9\u0001\u0000\u0000\u0000\u00bc\u00b4\u0001\u0000\u0000\u0000\u00bc"+
		"\u00bd\u0001\u0000\u0000\u0000\u00bd\u00be\u0001\u0000\u0000\u0000\u00be"+
		"\u00bf\u0005#\u0000\u0000\u00bf\u00c0\u0005(\u0000\u0000\u00c0\u001d\u0001"+
		"\u0000\u0000\u0000\u00c1\u00c2\u0003\u0014\n\u0000\u00c2\u00c3\u0005-"+
		"\u0000\u0000\u00c3\u00c4\u0005\u001c\u0000\u0000\u00c4\u00c5\u00030\u0018"+
		"\u0000\u00c5\u001f\u0001\u0000\u0000\u0000\u00c6\u00c7\u0005-\u0000\u0000"+
		"\u00c7\u00c8\u0005\u001c\u0000\u0000\u00c8\u00c9\u00030\u0018\u0000\u00c9"+
		"!\u0001\u0000\u0000\u0000\u00ca\u00cb\u0005-\u0000\u0000\u00cb\u00cc\u0005"+
		"\u001c\u0000\u0000\u00cc\u00cd\u00030\u0018\u0000\u00cd#\u0001\u0000\u0000"+
		"\u0000\u00ce\u00cf\u0005\u0005\u0000\u0000\u00cf\u00d0\u0005\"\u0000\u0000"+
		"\u00d0\u00d1\u00030\u0018\u0000\u00d1\u00d2\u0005#\u0000\u0000\u00d2\u00d3"+
		"\u0003\b\u0004\u0000\u00d3%\u0001\u0000\u0000\u0000\u00d4\u00d5\u0005"+
		"\u0006\u0000\u0000\u00d5\u00d8\u0005\"\u0000\u0000\u00d6\u00d9\u0003\u001e"+
		"\u000f\u0000\u00d7\u00d9\u0003 \u0010\u0000\u00d8\u00d6\u0001\u0000\u0000"+
		"\u0000\u00d8\u00d7\u0001\u0000\u0000\u0000\u00d8\u00d9\u0001\u0000\u0000"+
		"\u0000\u00d9\u00da\u0001\u0000\u0000\u0000\u00da\u00dc\u0005(\u0000\u0000"+
		"\u00db\u00dd\u00030\u0018\u0000\u00dc\u00db\u0001\u0000\u0000\u0000\u00dc"+
		"\u00dd\u0001\u0000\u0000\u0000\u00dd\u00de\u0001\u0000\u0000\u0000\u00de"+
		"\u00e0\u0005(\u0000\u0000\u00df\u00e1\u0003\"\u0011\u0000\u00e0\u00df"+
		"\u0001\u0000\u0000\u0000\u00e0\u00e1\u0001\u0000\u0000\u0000\u00e1\u00e2"+
		"\u0001\u0000\u0000\u0000\u00e2\u00e3\u0005#\u0000\u0000\u00e3\u00e4\u0003"+
		"\b\u0004\u0000\u00e4\'\u0001\u0000\u0000\u0000\u00e5\u00e7\u0005\b\u0000"+
		"\u0000\u00e6\u00e8\u00030\u0018\u0000\u00e7\u00e6\u0001\u0000\u0000\u0000"+
		"\u00e7\u00e8\u0001\u0000\u0000\u0000\u00e8\u00e9\u0001\u0000\u0000\u0000"+
		"\u00e9\u00ea\u0005(\u0000\u0000\u00ea)\u0001\u0000\u0000\u0000\u00eb\u00ec"+
		"\u0005\u0010\u0000\u0000\u00ec\u00ed\u0005(\u0000\u0000\u00ed+\u0001\u0000"+
		"\u0000\u0000\u00ee\u00ef\u0005\u0011\u0000\u0000\u00ef\u00f0\u0005(\u0000"+
		"\u0000\u00f0-\u0001\u0000\u0000\u0000\u00f1\u00f2\u0005\u0012\u0000\u0000"+
		"\u00f2\u00f3\u0005,\u0000\u0000\u00f3\u00f4\u0005(\u0000\u0000\u00f4/"+
		"\u0001\u0000\u0000\u0000\u00f5\u00f6\u0006\u0018\uffff\uffff\u0000\u00f6"+
		"\u00f7\u0005\u0015\u0000\u0000\u00f7\u0113\u00030\u0018\u000f\u00f8\u00f9"+
		"\u0005\u001e\u0000\u0000\u00f9\u0113\u00030\u0018\u000e\u00fa\u00fb\u0005"+
		"\"\u0000\u0000\u00fb\u00fc\u00030\u0018\u0000\u00fc\u00fd\u0005#\u0000"+
		"\u0000\u00fd\u0113\u0001\u0000\u0000\u0000\u00fe\u0113\u0005+\u0000\u0000"+
		"\u00ff\u0113\u0005*\u0000\u0000\u0100\u0113\u0005,\u0000\u0000\u0101\u0113"+
		"\u0005\u000e\u0000\u0000\u0102\u0113\u0005\u000f\u0000\u0000\u0103\u0113"+
		"\u0005-\u0000\u0000\u0104\u0113\u0003\u0010\b\u0000\u0105\u0106\u0005"+
		"-\u0000\u0000\u0106\u010f\u0005\"\u0000\u0000\u0107\u010c\u00030\u0018"+
		"\u0000\u0108\u0109\u0005)\u0000\u0000\u0109\u010b\u00030\u0018\u0000\u010a"+
		"\u0108\u0001\u0000\u0000\u0000\u010b\u010e\u0001\u0000\u0000\u0000\u010c"+
		"\u010a\u0001\u0000\u0000\u0000\u010c\u010d\u0001\u0000\u0000\u0000\u010d"+
		"\u0110\u0001\u0000\u0000\u0000\u010e\u010c\u0001\u0000\u0000\u0000\u010f"+
		"\u0107\u0001\u0000\u0000\u0000\u010f\u0110\u0001\u0000\u0000\u0000\u0110"+
		"\u0111\u0001\u0000\u0000\u0000\u0111\u0113\u0005#\u0000\u0000\u0112\u00f5"+
		"\u0001\u0000\u0000\u0000\u0112\u00f8\u0001\u0000\u0000\u0000\u0112\u00fa"+
		"\u0001\u0000\u0000\u0000\u0112\u00fe\u0001\u0000\u0000\u0000\u0112\u00ff"+
		"\u0001\u0000\u0000\u0000\u0112\u0100\u0001\u0000\u0000\u0000\u0112\u0101"+
		"\u0001\u0000\u0000\u0000\u0112\u0102\u0001\u0000\u0000\u0000\u0112\u0103"+
		"\u0001\u0000\u0000\u0000\u0112\u0104\u0001\u0000\u0000\u0000\u0112\u0105"+
		"\u0001\u0000\u0000\u0000\u0113\u0122\u0001\u0000\u0000\u0000\u0114\u0115"+
		"\n\f\u0000\u0000\u0115\u0116\u0007\u0001\u0000\u0000\u0116\u0121\u0003"+
		"0\u0018\r\u0117\u0118\n\u000b\u0000\u0000\u0118\u0119\u0007\u0002\u0000"+
		"\u0000\u0119\u0121\u00030\u0018\f\u011a\u011b\n\n\u0000\u0000\u011b\u011c"+
		"\u0007\u0003\u0000\u0000\u011c\u0121\u00030\u0018\u000b\u011d\u011e\n"+
		"\t\u0000\u0000\u011e\u011f\u0007\u0004\u0000\u0000\u011f\u0121\u00030"+
		"\u0018\n\u0120\u0114\u0001\u0000\u0000\u0000\u0120\u0117\u0001\u0000\u0000"+
		"\u0000\u0120\u011a\u0001\u0000\u0000\u0000\u0120\u011d\u0001\u0000\u0000"+
		"\u0000\u0121\u0124\u0001\u0000\u0000\u0000\u0122\u0120\u0001\u0000\u0000"+
		"\u0000\u0122\u0123\u0001\u0000\u0000\u0000\u01231\u0001\u0000\u0000\u0000"+
		"\u0124\u0122\u0001\u0000\u0000\u0000\u00185=EJT^ou\u007f\u0083\u008b\u008e"+
		"\u00aa\u00b9\u00bc\u00d8\u00dc\u00e0\u00e7\u010c\u010f\u0112\u0120\u0122";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}