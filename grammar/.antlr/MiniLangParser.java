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
		PROGRAM=1, SI=2, SINO=3, IMPRIME=4, MIENTRAS=5, PARA=6, FUNCION=7, RETORNA=8, 
		INT_T=9, BOOL_T=10, FLOAT_T=11, STRING_T=12, TRUE=13, FALSE=14, AND=15, 
		OR=16, NOT=17, EQ=18, NEQ=19, LE=20, GE=21, LT=22, GT=23, ASIGNA=24, SUMA=25, 
		RESTA=26, MULTI=27, DIVIDE=28, PARENTESIS_IZQ=29, PARENTESIS_DER=30, LLAVE_IZQ=31, 
		LLAVE_DER=32, CORCHETE_IZQ=33, CORCHETE_DER=34, PUNTO_COMA=35, COMA=36, 
		INT=37, FLOAT=38, STRING=39, ID=40, WS=41, LINEA_COMENTARIO=42, GRUPO_COMENTARIO=43;
	public static final int
		RULE_program = 0, RULE_funcionDecl = 1, RULE_parametros = 2, RULE_parametro = 3, 
		RULE_grupo = 4, RULE_sentencia = 5, RULE_declaraVariable = 6, RULE_tipo = 7, 
		RULE_sentenciaAsigna = 8, RULE_sentenciaSI = 9, RULE_sentenciaImprime = 10, 
		RULE_inicializacion = 11, RULE_sentenciaMientras = 12, RULE_sentenciaPara = 13, 
		RULE_sentenciaRetorna = 14, RULE_expr = 15;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "funcionDecl", "parametros", "parametro", "grupo", "sentencia", 
			"declaraVariable", "tipo", "sentenciaAsigna", "sentenciaSI", "sentenciaImprime", 
			"inicializacion", "sentenciaMientras", "sentenciaPara", "sentenciaRetorna", 
			"expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'program'", "'si'", "'sino'", "'imprime'", "'mientras'", "'para'", 
			"'funcion'", "'retorna'", "'int'", "'bool'", "'float'", "'string'", "'true'", 
			"'false'", "'&&'", "'||'", "'!'", "'=='", null, "'<='", "'>='", "'<'", 
			"'>'", "'='", "'+'", "'-'", "'*'", "'/'", "'('", "')'", "'{'", "'}'", 
			"'['", "']'", "';'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PROGRAM", "SI", "SINO", "IMPRIME", "MIENTRAS", "PARA", "FUNCION", 
			"RETORNA", "INT_T", "BOOL_T", "FLOAT_T", "STRING_T", "TRUE", "FALSE", 
			"AND", "OR", "NOT", "EQ", "NEQ", "LE", "GE", "LT", "GT", "ASIGNA", "SUMA", 
			"RESTA", "MULTI", "DIVIDE", "PARENTESIS_IZQ", "PARENTESIS_DER", "LLAVE_IZQ", 
			"LLAVE_DER", "CORCHETE_IZQ", "CORCHETE_DER", "PUNTO_COMA", "COMA", "INT", 
			"FLOAT", "STRING", "ID", "WS", "LINEA_COMENTARIO", "GRUPO_COMENTARIO"
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
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode PROGRAM() { return getToken(MiniLangParser.PROGRAM, 0); }
		public GrupoContext grupo() {
			return getRuleContext(GrupoContext.class,0);
		}
		public TerminalNode EOF() { return getToken(MiniLangParser.EOF, 0); }
		public List<FuncionDeclContext> funcionDecl() {
			return getRuleContexts(FuncionDeclContext.class);
		}
		public FuncionDeclContext funcionDecl(int i) {
			return getRuleContext(FuncionDeclContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(32);
			match(PROGRAM);
			setState(36);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNCION) {
				{
				{
				setState(33);
				funcionDecl();
				}
				}
				setState(38);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(39);
			grupo();
			setState(40);
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
	public static class FuncionDeclContext extends ParserRuleContext {
		public TerminalNode FUNCION() { return getToken(MiniLangParser.FUNCION, 0); }
		public TerminalNode ID() { return getToken(MiniLangParser.ID, 0); }
		public TerminalNode PARENTESIS_IZQ() { return getToken(MiniLangParser.PARENTESIS_IZQ, 0); }
		public TerminalNode PARENTESIS_DER() { return getToken(MiniLangParser.PARENTESIS_DER, 0); }
		public GrupoContext grupo() {
			return getRuleContext(GrupoContext.class,0);
		}
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public ParametrosContext parametros() {
			return getRuleContext(ParametrosContext.class,0);
		}
		public FuncionDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcionDecl; }
	}

	public final FuncionDeclContext funcionDecl() throws RecognitionException {
		FuncionDeclContext _localctx = new FuncionDeclContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_funcionDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(42);
			match(FUNCION);
			setState(44);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 7680L) != 0)) {
				{
				setState(43);
				tipo();
				}
			}

			setState(46);
			match(ID);
			setState(47);
			match(PARENTESIS_IZQ);
			setState(49);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 7680L) != 0)) {
				{
				setState(48);
				parametros();
				}
			}

			setState(51);
			match(PARENTESIS_DER);
			setState(52);
			grupo();
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
			setState(54);
			parametro();
			setState(59);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMA) {
				{
				{
				setState(55);
				match(COMA);
				setState(56);
				parametro();
				}
				}
				setState(61);
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
		public TerminalNode ID() { return getToken(MiniLangParser.ID, 0); }
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
			setState(62);
			tipo();
			setState(63);
			match(ID);
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
	public static class GrupoContext extends ParserRuleContext {
		public TerminalNode LLAVE_IZQ() { return getToken(MiniLangParser.LLAVE_IZQ, 0); }
		public TerminalNode LLAVE_DER() { return getToken(MiniLangParser.LLAVE_DER, 0); }
		public List<SentenciaContext> sentencia() {
			return getRuleContexts(SentenciaContext.class);
		}
		public SentenciaContext sentencia(int i) {
			return getRuleContext(SentenciaContext.class,i);
		}
		public GrupoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_grupo; }
	}

	public final GrupoContext grupo() throws RecognitionException {
		GrupoContext _localctx = new GrupoContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_grupo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(65);
			match(LLAVE_IZQ);
			setState(69);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1099511635828L) != 0)) {
				{
				{
				setState(66);
				sentencia();
				}
				}
				setState(71);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(72);
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
		public DeclaraVariableContext declaraVariable() {
			return getRuleContext(DeclaraVariableContext.class,0);
		}
		public SentenciaAsignaContext sentenciaAsigna() {
			return getRuleContext(SentenciaAsignaContext.class,0);
		}
		public SentenciaSIContext sentenciaSI() {
			return getRuleContext(SentenciaSIContext.class,0);
		}
		public SentenciaImprimeContext sentenciaImprime() {
			return getRuleContext(SentenciaImprimeContext.class,0);
		}
		public SentenciaMientrasContext sentenciaMientras() {
			return getRuleContext(SentenciaMientrasContext.class,0);
		}
		public SentenciaParaContext sentenciaPara() {
			return getRuleContext(SentenciaParaContext.class,0);
		}
		public SentenciaRetornaContext sentenciaRetorna() {
			return getRuleContext(SentenciaRetornaContext.class,0);
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
			setState(81);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT_T:
			case BOOL_T:
			case FLOAT_T:
			case STRING_T:
				enterOuterAlt(_localctx, 1);
				{
				setState(74);
				declaraVariable();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(75);
				sentenciaAsigna();
				}
				break;
			case SI:
				enterOuterAlt(_localctx, 3);
				{
				setState(76);
				sentenciaSI();
				}
				break;
			case IMPRIME:
				enterOuterAlt(_localctx, 4);
				{
				setState(77);
				sentenciaImprime();
				}
				break;
			case MIENTRAS:
				enterOuterAlt(_localctx, 5);
				{
				setState(78);
				sentenciaMientras();
				}
				break;
			case PARA:
				enterOuterAlt(_localctx, 6);
				{
				setState(79);
				sentenciaPara();
				}
				break;
			case RETORNA:
				enterOuterAlt(_localctx, 7);
				{
				setState(80);
				sentenciaRetorna();
				}
				break;
			default:
				throw new NoViableAltException(this);
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
	public static class DeclaraVariableContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode ID() { return getToken(MiniLangParser.ID, 0); }
		public TerminalNode PUNTO_COMA() { return getToken(MiniLangParser.PUNTO_COMA, 0); }
		public DeclaraVariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaraVariable; }
	}

	public final DeclaraVariableContext declaraVariable() throws RecognitionException {
		DeclaraVariableContext _localctx = new DeclaraVariableContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_declaraVariable);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			tipo();
			setState(84);
			match(ID);
			setState(85);
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
		public TerminalNode INT_T() { return getToken(MiniLangParser.INT_T, 0); }
		public TerminalNode BOOL_T() { return getToken(MiniLangParser.BOOL_T, 0); }
		public TerminalNode FLOAT_T() { return getToken(MiniLangParser.FLOAT_T, 0); }
		public TerminalNode STRING_T() { return getToken(MiniLangParser.STRING_T, 0); }
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 7680L) != 0)) ) {
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
	public static class SentenciaAsignaContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MiniLangParser.ID, 0); }
		public TerminalNode ASIGNA() { return getToken(MiniLangParser.ASIGNA, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode PUNTO_COMA() { return getToken(MiniLangParser.PUNTO_COMA, 0); }
		public SentenciaAsignaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentenciaAsigna; }
	}

	public final SentenciaAsignaContext sentenciaAsigna() throws RecognitionException {
		SentenciaAsignaContext _localctx = new SentenciaAsignaContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_sentenciaAsigna);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			match(ID);
			setState(90);
			match(ASIGNA);
			setState(91);
			expr(0);
			setState(92);
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
	public static class SentenciaSIContext extends ParserRuleContext {
		public TerminalNode SI() { return getToken(MiniLangParser.SI, 0); }
		public TerminalNode PARENTESIS_IZQ() { return getToken(MiniLangParser.PARENTESIS_IZQ, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode PARENTESIS_DER() { return getToken(MiniLangParser.PARENTESIS_DER, 0); }
		public List<GrupoContext> grupo() {
			return getRuleContexts(GrupoContext.class);
		}
		public GrupoContext grupo(int i) {
			return getRuleContext(GrupoContext.class,i);
		}
		public TerminalNode SINO() { return getToken(MiniLangParser.SINO, 0); }
		public SentenciaSIContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentenciaSI; }
	}

	public final SentenciaSIContext sentenciaSI() throws RecognitionException {
		SentenciaSIContext _localctx = new SentenciaSIContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_sentenciaSI);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			match(SI);
			setState(95);
			match(PARENTESIS_IZQ);
			setState(96);
			expr(0);
			setState(97);
			match(PARENTESIS_DER);
			setState(98);
			grupo();
			setState(101);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SINO) {
				{
				setState(99);
				match(SINO);
				setState(100);
				grupo();
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
	public static class SentenciaImprimeContext extends ParserRuleContext {
		public TerminalNode IMPRIME() { return getToken(MiniLangParser.IMPRIME, 0); }
		public TerminalNode PARENTESIS_IZQ() { return getToken(MiniLangParser.PARENTESIS_IZQ, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode PARENTESIS_DER() { return getToken(MiniLangParser.PARENTESIS_DER, 0); }
		public TerminalNode PUNTO_COMA() { return getToken(MiniLangParser.PUNTO_COMA, 0); }
		public SentenciaImprimeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentenciaImprime; }
	}

	public final SentenciaImprimeContext sentenciaImprime() throws RecognitionException {
		SentenciaImprimeContext _localctx = new SentenciaImprimeContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_sentenciaImprime);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(103);
			match(IMPRIME);
			setState(104);
			match(PARENTESIS_IZQ);
			setState(105);
			expr(0);
			setState(106);
			match(PARENTESIS_DER);
			setState(107);
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
	public static class InicializacionContext extends ParserRuleContext {
		public DeclaraVariableContext declaraVariable() {
			return getRuleContext(DeclaraVariableContext.class,0);
		}
		public SentenciaAsignaContext sentenciaAsigna() {
			return getRuleContext(SentenciaAsignaContext.class,0);
		}
		public InicializacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inicializacion; }
	}

	public final InicializacionContext inicializacion() throws RecognitionException {
		InicializacionContext _localctx = new InicializacionContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_inicializacion);
		try {
			setState(111);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT_T:
			case BOOL_T:
			case FLOAT_T:
			case STRING_T:
				enterOuterAlt(_localctx, 1);
				{
				setState(109);
				declaraVariable();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(110);
				sentenciaAsigna();
				}
				break;
			default:
				throw new NoViableAltException(this);
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
	public static class SentenciaMientrasContext extends ParserRuleContext {
		public TerminalNode MIENTRAS() { return getToken(MiniLangParser.MIENTRAS, 0); }
		public TerminalNode PARENTESIS_IZQ() { return getToken(MiniLangParser.PARENTESIS_IZQ, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode PARENTESIS_DER() { return getToken(MiniLangParser.PARENTESIS_DER, 0); }
		public GrupoContext grupo() {
			return getRuleContext(GrupoContext.class,0);
		}
		public SentenciaMientrasContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentenciaMientras; }
	}

	public final SentenciaMientrasContext sentenciaMientras() throws RecognitionException {
		SentenciaMientrasContext _localctx = new SentenciaMientrasContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_sentenciaMientras);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(113);
			match(MIENTRAS);
			setState(114);
			match(PARENTESIS_IZQ);
			setState(115);
			expr(0);
			setState(116);
			match(PARENTESIS_DER);
			setState(117);
			grupo();
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
	public static class SentenciaParaContext extends ParserRuleContext {
		public ExprContext cond;
		public SentenciaAsignaContext update;
		public TerminalNode PARA() { return getToken(MiniLangParser.PARA, 0); }
		public TerminalNode PARENTESIS_IZQ() { return getToken(MiniLangParser.PARENTESIS_IZQ, 0); }
		public List<TerminalNode> PUNTO_COMA() { return getTokens(MiniLangParser.PUNTO_COMA); }
		public TerminalNode PUNTO_COMA(int i) {
			return getToken(MiniLangParser.PUNTO_COMA, i);
		}
		public TerminalNode PARENTESIS_DER() { return getToken(MiniLangParser.PARENTESIS_DER, 0); }
		public GrupoContext grupo() {
			return getRuleContext(GrupoContext.class,0);
		}
		public InicializacionContext inicializacion() {
			return getRuleContext(InicializacionContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public SentenciaAsignaContext sentenciaAsigna() {
			return getRuleContext(SentenciaAsignaContext.class,0);
		}
		public SentenciaParaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentenciaPara; }
	}

	public final SentenciaParaContext sentenciaPara() throws RecognitionException {
		SentenciaParaContext _localctx = new SentenciaParaContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_sentenciaPara);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(119);
			match(PARA);
			setState(120);
			match(PARENTESIS_IZQ);
			setState(122);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1099511635456L) != 0)) {
				{
				setState(121);
				inicializacion();
				}
			}

			setState(124);
			match(PUNTO_COMA);
			setState(126);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2062188437504L) != 0)) {
				{
				setState(125);
				((SentenciaParaContext)_localctx).cond = expr(0);
				}
			}

			setState(128);
			match(PUNTO_COMA);
			setState(130);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(129);
				((SentenciaParaContext)_localctx).update = sentenciaAsigna();
				}
			}

			setState(132);
			match(PARENTESIS_DER);
			setState(133);
			grupo();
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
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public SentenciaRetornaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentenciaRetorna; }
	}

	public final SentenciaRetornaContext sentenciaRetorna() throws RecognitionException {
		SentenciaRetornaContext _localctx = new SentenciaRetornaContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_sentenciaRetorna);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(135);
			match(RETORNA);
			setState(137);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2062188437504L) != 0)) {
				{
				setState(136);
				expr(0);
				}
			}

			setState(139);
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
	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MulDivContext extends ExprContext {
		public ExprContext left;
		public Token op;
		public ExprContext right;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode MULTI() { return getToken(MiniLangParser.MULTI, 0); }
		public TerminalNode DIVIDE() { return getToken(MiniLangParser.DIVIDE, 0); }
		public MulDivContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AddSubContext extends ExprContext {
		public ExprContext left;
		public Token op;
		public ExprContext right;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode SUMA() { return getToken(MiniLangParser.SUMA, 0); }
		public TerminalNode RESTA() { return getToken(MiniLangParser.RESTA, 0); }
		public AddSubContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class RelationalContext extends ExprContext {
		public ExprContext left;
		public Token op;
		public ExprContext right;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode EQ() { return getToken(MiniLangParser.EQ, 0); }
		public TerminalNode NEQ() { return getToken(MiniLangParser.NEQ, 0); }
		public TerminalNode LT() { return getToken(MiniLangParser.LT, 0); }
		public TerminalNode LE() { return getToken(MiniLangParser.LE, 0); }
		public TerminalNode GT() { return getToken(MiniLangParser.GT, 0); }
		public TerminalNode GE() { return getToken(MiniLangParser.GE, 0); }
		public RelationalContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FalseLitContext extends ExprContext {
		public TerminalNode FALSE() { return getToken(MiniLangParser.FALSE, 0); }
		public FalseLitContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LogicalContext extends ExprContext {
		public ExprContext left;
		public Token op;
		public ExprContext right;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode AND() { return getToken(MiniLangParser.AND, 0); }
		public TerminalNode OR() { return getToken(MiniLangParser.OR, 0); }
		public LogicalContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class UnaryMinusContext extends ExprContext {
		public TerminalNode RESTA() { return getToken(MiniLangParser.RESTA, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public UnaryMinusContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IdRefContext extends ExprContext {
		public TerminalNode ID() { return getToken(MiniLangParser.ID, 0); }
		public IdRefContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StringLitContext extends ExprContext {
		public TerminalNode STRING() { return getToken(MiniLangParser.STRING, 0); }
		public StringLitContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FuncCallContext extends ExprContext {
		public TerminalNode ID() { return getToken(MiniLangParser.ID, 0); }
		public TerminalNode PARENTESIS_IZQ() { return getToken(MiniLangParser.PARENTESIS_IZQ, 0); }
		public TerminalNode PARENTESIS_DER() { return getToken(MiniLangParser.PARENTESIS_DER, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMA() { return getTokens(MiniLangParser.COMA); }
		public TerminalNode COMA(int i) {
			return getToken(MiniLangParser.COMA, i);
		}
		public FuncCallContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class UnaryNotContext extends ExprContext {
		public TerminalNode NOT() { return getToken(MiniLangParser.NOT, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public UnaryNotContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FloatLitContext extends ExprContext {
		public TerminalNode FLOAT() { return getToken(MiniLangParser.FLOAT, 0); }
		public FloatLitContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class TrueLitContext extends ExprContext {
		public TerminalNode TRUE() { return getToken(MiniLangParser.TRUE, 0); }
		public TrueLitContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IntLitContext extends ExprContext {
		public TerminalNode INT() { return getToken(MiniLangParser.INT, 0); }
		public IntLitContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParenContext extends ExprContext {
		public TerminalNode PARENTESIS_IZQ() { return getToken(MiniLangParser.PARENTESIS_IZQ, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode PARENTESIS_DER() { return getToken(MiniLangParser.PARENTESIS_DER, 0); }
		public ParenContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 30;
		enterRecursionRule(_localctx, 30, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(169);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				{
				_localctx = new UnaryNotContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(142);
				match(NOT);
				setState(143);
				expr(14);
				}
				break;
			case 2:
				{
				_localctx = new UnaryMinusContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(144);
				match(RESTA);
				setState(145);
				expr(13);
				}
				break;
			case 3:
				{
				_localctx = new ParenContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(146);
				match(PARENTESIS_IZQ);
				setState(147);
				expr(0);
				setState(148);
				match(PARENTESIS_DER);
				}
				break;
			case 4:
				{
				_localctx = new IntLitContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(150);
				match(INT);
				}
				break;
			case 5:
				{
				_localctx = new FloatLitContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(151);
				match(FLOAT);
				}
				break;
			case 6:
				{
				_localctx = new StringLitContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(152);
				match(STRING);
				}
				break;
			case 7:
				{
				_localctx = new TrueLitContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(153);
				match(TRUE);
				}
				break;
			case 8:
				{
				_localctx = new FalseLitContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(154);
				match(FALSE);
				}
				break;
			case 9:
				{
				_localctx = new IdRefContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(155);
				match(ID);
				}
				break;
			case 10:
				{
				_localctx = new FuncCallContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(156);
				match(ID);
				setState(157);
				match(PARENTESIS_IZQ);
				setState(166);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2062188437504L) != 0)) {
					{
					setState(158);
					expr(0);
					setState(163);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMA) {
						{
						{
						setState(159);
						match(COMA);
						setState(160);
						expr(0);
						}
						}
						setState(165);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(168);
				match(PARENTESIS_DER);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(185);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(183);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
					case 1:
						{
						_localctx = new MulDivContext(new ExprContext(_parentctx, _parentState));
						((MulDivContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(171);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(172);
						((MulDivContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==MULTI || _la==DIVIDE) ) {
							((MulDivContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(173);
						((MulDivContext)_localctx).right = expr(12);
						}
						break;
					case 2:
						{
						_localctx = new AddSubContext(new ExprContext(_parentctx, _parentState));
						((AddSubContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(174);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(175);
						((AddSubContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==SUMA || _la==RESTA) ) {
							((AddSubContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(176);
						((AddSubContext)_localctx).right = expr(11);
						}
						break;
					case 3:
						{
						_localctx = new RelationalContext(new ExprContext(_parentctx, _parentState));
						((RelationalContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(177);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(178);
						((RelationalContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 16515072L) != 0)) ) {
							((RelationalContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(179);
						((RelationalContext)_localctx).right = expr(10);
						}
						break;
					case 4:
						{
						_localctx = new LogicalContext(new ExprContext(_parentctx, _parentState));
						((LogicalContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(180);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(181);
						((LogicalContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==AND || _la==OR) ) {
							((LogicalContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(182);
						((LogicalContext)_localctx).right = expr(9);
						}
						break;
					}
					} 
				}
				setState(187);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
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
		case 15:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 11);
		case 1:
			return precpred(_ctx, 10);
		case 2:
			return precpred(_ctx, 9);
		case 3:
			return precpred(_ctx, 8);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001+\u00bd\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0001\u0000\u0001\u0000\u0005\u0000#\b\u0000\n\u0000\f\u0000&\t\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0003\u0001"+
		"-\b\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u00012\b\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0005"+
		"\u0002:\b\u0002\n\u0002\f\u0002=\t\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0005\u0004D\b\u0004\n\u0004\f\u0004G\t"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005R\b\u0005\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0003\tf\b\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\u000b\u0001\u000b\u0003\u000bp\b\u000b\u0001\f\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0003\r{\b"+
		"\r\u0001\r\u0001\r\u0003\r\u007f\b\r\u0001\r\u0001\r\u0003\r\u0083\b\r"+
		"\u0001\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0003\u000e\u008a\b\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0005\u000f\u00a2\b\u000f"+
		"\n\u000f\f\u000f\u00a5\t\u000f\u0003\u000f\u00a7\b\u000f\u0001\u000f\u0003"+
		"\u000f\u00aa\b\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0005\u000f\u00b8\b\u000f\n\u000f\f\u000f\u00bb\t\u000f"+
		"\u0001\u000f\u0000\u0001\u001e\u0010\u0000\u0002\u0004\u0006\b\n\f\u000e"+
		"\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e\u0000\u0005\u0001\u0000"+
		"\t\f\u0001\u0000\u001b\u001c\u0001\u0000\u0019\u001a\u0001\u0000\u0012"+
		"\u0017\u0001\u0000\u000f\u0010\u00cc\u0000 \u0001\u0000\u0000\u0000\u0002"+
		"*\u0001\u0000\u0000\u0000\u00046\u0001\u0000\u0000\u0000\u0006>\u0001"+
		"\u0000\u0000\u0000\bA\u0001\u0000\u0000\u0000\nQ\u0001\u0000\u0000\u0000"+
		"\fS\u0001\u0000\u0000\u0000\u000eW\u0001\u0000\u0000\u0000\u0010Y\u0001"+
		"\u0000\u0000\u0000\u0012^\u0001\u0000\u0000\u0000\u0014g\u0001\u0000\u0000"+
		"\u0000\u0016o\u0001\u0000\u0000\u0000\u0018q\u0001\u0000\u0000\u0000\u001a"+
		"w\u0001\u0000\u0000\u0000\u001c\u0087\u0001\u0000\u0000\u0000\u001e\u00a9"+
		"\u0001\u0000\u0000\u0000 $\u0005\u0001\u0000\u0000!#\u0003\u0002\u0001"+
		"\u0000\"!\u0001\u0000\u0000\u0000#&\u0001\u0000\u0000\u0000$\"\u0001\u0000"+
		"\u0000\u0000$%\u0001\u0000\u0000\u0000%\'\u0001\u0000\u0000\u0000&$\u0001"+
		"\u0000\u0000\u0000\'(\u0003\b\u0004\u0000()\u0005\u0000\u0000\u0001)\u0001"+
		"\u0001\u0000\u0000\u0000*,\u0005\u0007\u0000\u0000+-\u0003\u000e\u0007"+
		"\u0000,+\u0001\u0000\u0000\u0000,-\u0001\u0000\u0000\u0000-.\u0001\u0000"+
		"\u0000\u0000./\u0005(\u0000\u0000/1\u0005\u001d\u0000\u000002\u0003\u0004"+
		"\u0002\u000010\u0001\u0000\u0000\u000012\u0001\u0000\u0000\u000023\u0001"+
		"\u0000\u0000\u000034\u0005\u001e\u0000\u000045\u0003\b\u0004\u00005\u0003"+
		"\u0001\u0000\u0000\u00006;\u0003\u0006\u0003\u000078\u0005$\u0000\u0000"+
		"8:\u0003\u0006\u0003\u000097\u0001\u0000\u0000\u0000:=\u0001\u0000\u0000"+
		"\u0000;9\u0001\u0000\u0000\u0000;<\u0001\u0000\u0000\u0000<\u0005\u0001"+
		"\u0000\u0000\u0000=;\u0001\u0000\u0000\u0000>?\u0003\u000e\u0007\u0000"+
		"?@\u0005(\u0000\u0000@\u0007\u0001\u0000\u0000\u0000AE\u0005\u001f\u0000"+
		"\u0000BD\u0003\n\u0005\u0000CB\u0001\u0000\u0000\u0000DG\u0001\u0000\u0000"+
		"\u0000EC\u0001\u0000\u0000\u0000EF\u0001\u0000\u0000\u0000FH\u0001\u0000"+
		"\u0000\u0000GE\u0001\u0000\u0000\u0000HI\u0005 \u0000\u0000I\t\u0001\u0000"+
		"\u0000\u0000JR\u0003\f\u0006\u0000KR\u0003\u0010\b\u0000LR\u0003\u0012"+
		"\t\u0000MR\u0003\u0014\n\u0000NR\u0003\u0018\f\u0000OR\u0003\u001a\r\u0000"+
		"PR\u0003\u001c\u000e\u0000QJ\u0001\u0000\u0000\u0000QK\u0001\u0000\u0000"+
		"\u0000QL\u0001\u0000\u0000\u0000QM\u0001\u0000\u0000\u0000QN\u0001\u0000"+
		"\u0000\u0000QO\u0001\u0000\u0000\u0000QP\u0001\u0000\u0000\u0000R\u000b"+
		"\u0001\u0000\u0000\u0000ST\u0003\u000e\u0007\u0000TU\u0005(\u0000\u0000"+
		"UV\u0005#\u0000\u0000V\r\u0001\u0000\u0000\u0000WX\u0007\u0000\u0000\u0000"+
		"X\u000f\u0001\u0000\u0000\u0000YZ\u0005(\u0000\u0000Z[\u0005\u0018\u0000"+
		"\u0000[\\\u0003\u001e\u000f\u0000\\]\u0005#\u0000\u0000]\u0011\u0001\u0000"+
		"\u0000\u0000^_\u0005\u0002\u0000\u0000_`\u0005\u001d\u0000\u0000`a\u0003"+
		"\u001e\u000f\u0000ab\u0005\u001e\u0000\u0000be\u0003\b\u0004\u0000cd\u0005"+
		"\u0003\u0000\u0000df\u0003\b\u0004\u0000ec\u0001\u0000\u0000\u0000ef\u0001"+
		"\u0000\u0000\u0000f\u0013\u0001\u0000\u0000\u0000gh\u0005\u0004\u0000"+
		"\u0000hi\u0005\u001d\u0000\u0000ij\u0003\u001e\u000f\u0000jk\u0005\u001e"+
		"\u0000\u0000kl\u0005#\u0000\u0000l\u0015\u0001\u0000\u0000\u0000mp\u0003"+
		"\f\u0006\u0000np\u0003\u0010\b\u0000om\u0001\u0000\u0000\u0000on\u0001"+
		"\u0000\u0000\u0000p\u0017\u0001\u0000\u0000\u0000qr\u0005\u0005\u0000"+
		"\u0000rs\u0005\u001d\u0000\u0000st\u0003\u001e\u000f\u0000tu\u0005\u001e"+
		"\u0000\u0000uv\u0003\b\u0004\u0000v\u0019\u0001\u0000\u0000\u0000wx\u0005"+
		"\u0006\u0000\u0000xz\u0005\u001d\u0000\u0000y{\u0003\u0016\u000b\u0000"+
		"zy\u0001\u0000\u0000\u0000z{\u0001\u0000\u0000\u0000{|\u0001\u0000\u0000"+
		"\u0000|~\u0005#\u0000\u0000}\u007f\u0003\u001e\u000f\u0000~}\u0001\u0000"+
		"\u0000\u0000~\u007f\u0001\u0000\u0000\u0000\u007f\u0080\u0001\u0000\u0000"+
		"\u0000\u0080\u0082\u0005#\u0000\u0000\u0081\u0083\u0003\u0010\b\u0000"+
		"\u0082\u0081\u0001\u0000\u0000\u0000\u0082\u0083\u0001\u0000\u0000\u0000"+
		"\u0083\u0084\u0001\u0000\u0000\u0000\u0084\u0085\u0005\u001e\u0000\u0000"+
		"\u0085\u0086\u0003\b\u0004\u0000\u0086\u001b\u0001\u0000\u0000\u0000\u0087"+
		"\u0089\u0005\b\u0000\u0000\u0088\u008a\u0003\u001e\u000f\u0000\u0089\u0088"+
		"\u0001\u0000\u0000\u0000\u0089\u008a\u0001\u0000\u0000\u0000\u008a\u008b"+
		"\u0001\u0000\u0000\u0000\u008b\u008c\u0005#\u0000\u0000\u008c\u001d\u0001"+
		"\u0000\u0000\u0000\u008d\u008e\u0006\u000f\uffff\uffff\u0000\u008e\u008f"+
		"\u0005\u0011\u0000\u0000\u008f\u00aa\u0003\u001e\u000f\u000e\u0090\u0091"+
		"\u0005\u001a\u0000\u0000\u0091\u00aa\u0003\u001e\u000f\r\u0092\u0093\u0005"+
		"\u001d\u0000\u0000\u0093\u0094\u0003\u001e\u000f\u0000\u0094\u0095\u0005"+
		"\u001e\u0000\u0000\u0095\u00aa\u0001\u0000\u0000\u0000\u0096\u00aa\u0005"+
		"%\u0000\u0000\u0097\u00aa\u0005&\u0000\u0000\u0098\u00aa\u0005\'\u0000"+
		"\u0000\u0099\u00aa\u0005\r\u0000\u0000\u009a\u00aa\u0005\u000e\u0000\u0000"+
		"\u009b\u00aa\u0005(\u0000\u0000\u009c\u009d\u0005(\u0000\u0000\u009d\u00a6"+
		"\u0005\u001d\u0000\u0000\u009e\u00a3\u0003\u001e\u000f\u0000\u009f\u00a0"+
		"\u0005$\u0000\u0000\u00a0\u00a2\u0003\u001e\u000f\u0000\u00a1\u009f\u0001"+
		"\u0000\u0000\u0000\u00a2\u00a5\u0001\u0000\u0000\u0000\u00a3\u00a1\u0001"+
		"\u0000\u0000\u0000\u00a3\u00a4\u0001\u0000\u0000\u0000\u00a4\u00a7\u0001"+
		"\u0000\u0000\u0000\u00a5\u00a3\u0001\u0000\u0000\u0000\u00a6\u009e\u0001"+
		"\u0000\u0000\u0000\u00a6\u00a7\u0001\u0000\u0000\u0000\u00a7\u00a8\u0001"+
		"\u0000\u0000\u0000\u00a8\u00aa\u0005\u001e\u0000\u0000\u00a9\u008d\u0001"+
		"\u0000\u0000\u0000\u00a9\u0090\u0001\u0000\u0000\u0000\u00a9\u0092\u0001"+
		"\u0000\u0000\u0000\u00a9\u0096\u0001\u0000\u0000\u0000\u00a9\u0097\u0001"+
		"\u0000\u0000\u0000\u00a9\u0098\u0001\u0000\u0000\u0000\u00a9\u0099\u0001"+
		"\u0000\u0000\u0000\u00a9\u009a\u0001\u0000\u0000\u0000\u00a9\u009b\u0001"+
		"\u0000\u0000\u0000\u00a9\u009c\u0001\u0000\u0000\u0000\u00aa\u00b9\u0001"+
		"\u0000\u0000\u0000\u00ab\u00ac\n\u000b\u0000\u0000\u00ac\u00ad\u0007\u0001"+
		"\u0000\u0000\u00ad\u00b8\u0003\u001e\u000f\f\u00ae\u00af\n\n\u0000\u0000"+
		"\u00af\u00b0\u0007\u0002\u0000\u0000\u00b0\u00b8\u0003\u001e\u000f\u000b"+
		"\u00b1\u00b2\n\t\u0000\u0000\u00b2\u00b3\u0007\u0003\u0000\u0000\u00b3"+
		"\u00b8\u0003\u001e\u000f\n\u00b4\u00b5\n\b\u0000\u0000\u00b5\u00b6\u0007"+
		"\u0004\u0000\u0000\u00b6\u00b8\u0003\u001e\u000f\t\u00b7\u00ab\u0001\u0000"+
		"\u0000\u0000\u00b7\u00ae\u0001\u0000\u0000\u0000\u00b7\u00b1\u0001\u0000"+
		"\u0000\u0000\u00b7\u00b4\u0001\u0000\u0000\u0000\u00b8\u00bb\u0001\u0000"+
		"\u0000\u0000\u00b9\u00b7\u0001\u0000\u0000\u0000\u00b9\u00ba\u0001\u0000"+
		"\u0000\u0000\u00ba\u001f\u0001\u0000\u0000\u0000\u00bb\u00b9\u0001\u0000"+
		"\u0000\u0000\u0011$,1;EQeoz~\u0082\u0089\u00a3\u00a6\u00a9\u00b7\u00b9";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}