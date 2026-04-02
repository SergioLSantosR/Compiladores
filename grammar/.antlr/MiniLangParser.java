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
		VOID=9, INT_T=10, BOOL_T=11, FLOAT_T=12, STRING_T=13, TRUE=14, FALSE=15, 
		AND=16, OR=17, NOT=18, EQ=19, NEQ=20, LE=21, GE=22, LT=23, GT=24, ASIGNA=25, 
		SUMA=26, RESTA=27, MULTI=28, DIVIDE=29, PARENTESIS_IZQ=30, PARENTESIS_DER=31, 
		LLAVE_IZQ=32, LLAVE_DER=33, CORCHETE_IZQ=34, CORCHETE_DER=35, PUNTO_COMA=36, 
		COMA=37, INT=38, FLOAT=39, STRING=40, ID=41, WS=42, LINEA_COMENTARIO=43, 
		GRUPO_COMENTARIO=44;
	public static final int
		RULE_program = 0, RULE_funcionDecl = 1, RULE_parametros = 2, RULE_parametro = 3, 
		RULE_grupo = 4, RULE_sentencia = 5, RULE_declaraVariable = 6, RULE_tipo = 7, 
		RULE_sentenciaAsigna = 8, RULE_sentenciaSI = 9, RULE_sentenciaImprime = 10, 
		RULE_sentenciaLlamada = 11, RULE_inicializacionPara = 12, RULE_asignacionPara = 13, 
		RULE_actualizacionPara = 14, RULE_sentenciaMientras = 15, RULE_sentenciaPara = 16, 
		RULE_sentenciaRetorna = 17, RULE_expr = 18;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "funcionDecl", "parametros", "parametro", "grupo", "sentencia", 
			"declaraVariable", "tipo", "sentenciaAsigna", "sentenciaSI", "sentenciaImprime", 
			"sentenciaLlamada", "inicializacionPara", "asignacionPara", "actualizacionPara", 
			"sentenciaMientras", "sentenciaPara", "sentenciaRetorna", "expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'program'", "'si'", "'sino'", "'imprime'", "'mientras'", "'para'", 
			"'funcion'", "'retorna'", "'void'", "'int'", "'bool'", "'float'", "'string'", 
			"'true'", "'false'", "'&&'", "'||'", "'!'", "'=='", null, "'<='", "'>='", 
			"'<'", "'>'", "'='", "'+'", "'-'", "'*'", "'/'", "'('", "')'", "'{'", 
			"'}'", "'['", "']'", "';'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PROGRAM", "SI", "SINO", "IMPRIME", "MIENTRAS", "PARA", "FUNCION", 
			"RETORNA", "VOID", "INT_T", "BOOL_T", "FLOAT_T", "STRING_T", "TRUE", 
			"FALSE", "AND", "OR", "NOT", "EQ", "NEQ", "LE", "GE", "LT", "GT", "ASIGNA", 
			"SUMA", "RESTA", "MULTI", "DIVIDE", "PARENTESIS_IZQ", "PARENTESIS_DER", 
			"LLAVE_IZQ", "LLAVE_DER", "CORCHETE_IZQ", "CORCHETE_DER", "PUNTO_COMA", 
			"COMA", "INT", "FLOAT", "STRING", "ID", "WS", "LINEA_COMENTARIO", "GRUPO_COMENTARIO"
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
			setState(41);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNCION) {
				{
				{
				setState(38);
				funcionDecl();
				}
				}
				setState(43);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(44);
			match(PROGRAM);
			setState(45);
			grupo();
			setState(49);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNCION) {
				{
				{
				setState(46);
				funcionDecl();
				}
				}
				setState(51);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(52);
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
		public TerminalNode VOID() { return getToken(MiniLangParser.VOID, 0); }
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
			setState(54);
			match(FUNCION);
			setState(57);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT_T:
			case BOOL_T:
			case FLOAT_T:
			case STRING_T:
				{
				setState(55);
				tipo();
				}
				break;
			case VOID:
				{
				setState(56);
				match(VOID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(59);
			match(ID);
			setState(60);
			match(PARENTESIS_IZQ);
			setState(62);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 15360L) != 0)) {
				{
				setState(61);
				parametros();
				}
			}

			setState(64);
			match(PARENTESIS_DER);
			setState(65);
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
			setState(67);
			parametro();
			setState(72);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMA) {
				{
				{
				setState(68);
				match(COMA);
				setState(69);
				parametro();
				}
				}
				setState(74);
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
			setState(75);
			tipo();
			setState(76);
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
			setState(78);
			match(LLAVE_IZQ);
			setState(82);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2199023271284L) != 0)) {
				{
				{
				setState(79);
				sentencia();
				}
				}
				setState(84);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(85);
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
		public SentenciaLlamadaContext sentenciaLlamada() {
			return getRuleContext(SentenciaLlamadaContext.class,0);
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
			setState(95);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(87);
				declaraVariable();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(88);
				sentenciaAsigna();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(89);
				sentenciaSI();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(90);
				sentenciaImprime();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(91);
				sentenciaMientras();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(92);
				sentenciaPara();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(93);
				sentenciaRetorna();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(94);
				sentenciaLlamada();
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
			setState(97);
			tipo();
			setState(98);
			match(ID);
			setState(99);
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
			setState(101);
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
			setState(103);
			match(ID);
			setState(104);
			match(ASIGNA);
			setState(105);
			expr(0);
			setState(106);
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
			setState(108);
			match(SI);
			setState(109);
			match(PARENTESIS_IZQ);
			setState(110);
			expr(0);
			setState(111);
			match(PARENTESIS_DER);
			setState(112);
			grupo();
			setState(115);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SINO) {
				{
				setState(113);
				match(SINO);
				setState(114);
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
			setState(117);
			match(IMPRIME);
			setState(118);
			match(PARENTESIS_IZQ);
			setState(119);
			expr(0);
			setState(120);
			match(PARENTESIS_DER);
			setState(121);
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
	public static class SentenciaLlamadaContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MiniLangParser.ID, 0); }
		public TerminalNode PARENTESIS_IZQ() { return getToken(MiniLangParser.PARENTESIS_IZQ, 0); }
		public TerminalNode PARENTESIS_DER() { return getToken(MiniLangParser.PARENTESIS_DER, 0); }
		public TerminalNode PUNTO_COMA() { return getToken(MiniLangParser.PUNTO_COMA, 0); }
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
		public SentenciaLlamadaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentenciaLlamada; }
	}

	public final SentenciaLlamadaContext sentenciaLlamada() throws RecognitionException {
		SentenciaLlamadaContext _localctx = new SentenciaLlamadaContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_sentenciaLlamada);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(123);
			match(ID);
			setState(124);
			match(PARENTESIS_IZQ);
			setState(133);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4124376875008L) != 0)) {
				{
				setState(125);
				expr(0);
				setState(130);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMA) {
					{
					{
					setState(126);
					match(COMA);
					setState(127);
					expr(0);
					}
					}
					setState(132);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(135);
			match(PARENTESIS_DER);
			setState(136);
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
		public TerminalNode ID() { return getToken(MiniLangParser.ID, 0); }
		public TerminalNode ASIGNA() { return getToken(MiniLangParser.ASIGNA, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public InicializacionParaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inicializacionPara; }
	}

	public final InicializacionParaContext inicializacionPara() throws RecognitionException {
		InicializacionParaContext _localctx = new InicializacionParaContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_inicializacionPara);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(138);
			tipo();
			setState(139);
			match(ID);
			setState(140);
			match(ASIGNA);
			setState(141);
			expr(0);
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
		public TerminalNode ID() { return getToken(MiniLangParser.ID, 0); }
		public TerminalNode ASIGNA() { return getToken(MiniLangParser.ASIGNA, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AsignacionParaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacionPara; }
	}

	public final AsignacionParaContext asignacionPara() throws RecognitionException {
		AsignacionParaContext _localctx = new AsignacionParaContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_asignacionPara);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			match(ID);
			setState(144);
			match(ASIGNA);
			setState(145);
			expr(0);
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
		public TerminalNode ID() { return getToken(MiniLangParser.ID, 0); }
		public TerminalNode ASIGNA() { return getToken(MiniLangParser.ASIGNA, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ActualizacionParaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_actualizacionPara; }
	}

	public final ActualizacionParaContext actualizacionPara() throws RecognitionException {
		ActualizacionParaContext _localctx = new ActualizacionParaContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_actualizacionPara);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(147);
			match(ID);
			setState(148);
			match(ASIGNA);
			setState(149);
			expr(0);
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
		enterRule(_localctx, 30, RULE_sentenciaMientras);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(151);
			match(MIENTRAS);
			setState(152);
			match(PARENTESIS_IZQ);
			setState(153);
			expr(0);
			setState(154);
			match(PARENTESIS_DER);
			setState(155);
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
		public InicializacionParaContext inicializacionPara() {
			return getRuleContext(InicializacionParaContext.class,0);
		}
		public AsignacionParaContext asignacionPara() {
			return getRuleContext(AsignacionParaContext.class,0);
		}
		public ActualizacionParaContext actualizacionPara() {
			return getRuleContext(ActualizacionParaContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public SentenciaParaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentenciaPara; }
	}

	public final SentenciaParaContext sentenciaPara() throws RecognitionException {
		SentenciaParaContext _localctx = new SentenciaParaContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_sentenciaPara);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(157);
			match(PARA);
			setState(158);
			match(PARENTESIS_IZQ);
			setState(161);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT_T:
			case BOOL_T:
			case FLOAT_T:
			case STRING_T:
				{
				setState(159);
				inicializacionPara();
				}
				break;
			case ID:
				{
				setState(160);
				asignacionPara();
				}
				break;
			case PUNTO_COMA:
				break;
			default:
				break;
			}
			setState(163);
			match(PUNTO_COMA);
			setState(165);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4124376875008L) != 0)) {
				{
				setState(164);
				((SentenciaParaContext)_localctx).cond = expr(0);
				}
			}

			setState(167);
			match(PUNTO_COMA);
			setState(169);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(168);
				actualizacionPara();
				}
			}

			setState(171);
			match(PARENTESIS_DER);
			setState(172);
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
		enterRule(_localctx, 34, RULE_sentenciaRetorna);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(174);
			match(RETORNA);
			setState(176);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4124376875008L) != 0)) {
				{
				setState(175);
				expr(0);
				}
			}

			setState(178);
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
		int _startState = 36;
		enterRecursionRule(_localctx, 36, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(208);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				{
				_localctx = new UnaryNotContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(181);
				match(NOT);
				setState(182);
				expr(14);
				}
				break;
			case 2:
				{
				_localctx = new UnaryMinusContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(183);
				match(RESTA);
				setState(184);
				expr(13);
				}
				break;
			case 3:
				{
				_localctx = new ParenContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(185);
				match(PARENTESIS_IZQ);
				setState(186);
				expr(0);
				setState(187);
				match(PARENTESIS_DER);
				}
				break;
			case 4:
				{
				_localctx = new IntLitContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(189);
				match(INT);
				}
				break;
			case 5:
				{
				_localctx = new FloatLitContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(190);
				match(FLOAT);
				}
				break;
			case 6:
				{
				_localctx = new StringLitContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(191);
				match(STRING);
				}
				break;
			case 7:
				{
				_localctx = new TrueLitContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(192);
				match(TRUE);
				}
				break;
			case 8:
				{
				_localctx = new FalseLitContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(193);
				match(FALSE);
				}
				break;
			case 9:
				{
				_localctx = new IdRefContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(194);
				match(ID);
				}
				break;
			case 10:
				{
				_localctx = new FuncCallContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(195);
				match(ID);
				setState(196);
				match(PARENTESIS_IZQ);
				setState(205);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4124376875008L) != 0)) {
					{
					setState(197);
					expr(0);
					setState(202);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMA) {
						{
						{
						setState(198);
						match(COMA);
						setState(199);
						expr(0);
						}
						}
						setState(204);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(207);
				match(PARENTESIS_DER);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(224);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(222);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
					case 1:
						{
						_localctx = new MulDivContext(new ExprContext(_parentctx, _parentState));
						((MulDivContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(210);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(211);
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
						setState(212);
						((MulDivContext)_localctx).right = expr(12);
						}
						break;
					case 2:
						{
						_localctx = new AddSubContext(new ExprContext(_parentctx, _parentState));
						((AddSubContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(213);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(214);
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
						setState(215);
						((AddSubContext)_localctx).right = expr(11);
						}
						break;
					case 3:
						{
						_localctx = new RelationalContext(new ExprContext(_parentctx, _parentState));
						((RelationalContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(216);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(217);
						((RelationalContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 33030144L) != 0)) ) {
							((RelationalContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(218);
						((RelationalContext)_localctx).right = expr(10);
						}
						break;
					case 4:
						{
						_localctx = new LogicalContext(new ExprContext(_parentctx, _parentState));
						((LogicalContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(219);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(220);
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
						setState(221);
						((LogicalContext)_localctx).right = expr(9);
						}
						break;
					}
					} 
				}
				setState(226);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
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
		case 18:
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
		"\u0004\u0001,\u00e4\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0001\u0000\u0005\u0000(\b\u0000\n\u0000\f\u0000+\t\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0005\u00000\b\u0000\n\u0000\f\u00003\t\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001"+
		":\b\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001?\b\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0005"+
		"\u0002G\b\u0002\n\u0002\f\u0002J\t\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0005\u0004Q\b\u0004\n\u0004\f\u0004T\t"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005`\b"+
		"\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001"+
		"\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t"+
		"\u0001\t\u0001\t\u0001\t\u0001\t\u0003\tt\b\t\u0001\n\u0001\n\u0001\n"+
		"\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0005\u000b\u0081\b\u000b\n\u000b\f\u000b\u0084\t\u000b\u0003"+
		"\u000b\u0086\b\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0003\u0010\u00a2\b\u0010\u0001\u0010\u0001\u0010\u0003\u0010"+
		"\u00a6\b\u0010\u0001\u0010\u0001\u0010\u0003\u0010\u00aa\b\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0003\u0011\u00b1"+
		"\b\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0005\u0012\u00c9"+
		"\b\u0012\n\u0012\f\u0012\u00cc\t\u0012\u0003\u0012\u00ce\b\u0012\u0001"+
		"\u0012\u0003\u0012\u00d1\b\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0005\u0012\u00df\b\u0012\n\u0012\f\u0012"+
		"\u00e2\t\u0012\u0001\u0012\u0000\u0001$\u0013\u0000\u0002\u0004\u0006"+
		"\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$\u0000"+
		"\u0005\u0001\u0000\n\r\u0001\u0000\u001c\u001d\u0001\u0000\u001a\u001b"+
		"\u0001\u0000\u0013\u0018\u0001\u0000\u0010\u0011\u00f4\u0000)\u0001\u0000"+
		"\u0000\u0000\u00026\u0001\u0000\u0000\u0000\u0004C\u0001\u0000\u0000\u0000"+
		"\u0006K\u0001\u0000\u0000\u0000\bN\u0001\u0000\u0000\u0000\n_\u0001\u0000"+
		"\u0000\u0000\fa\u0001\u0000\u0000\u0000\u000ee\u0001\u0000\u0000\u0000"+
		"\u0010g\u0001\u0000\u0000\u0000\u0012l\u0001\u0000\u0000\u0000\u0014u"+
		"\u0001\u0000\u0000\u0000\u0016{\u0001\u0000\u0000\u0000\u0018\u008a\u0001"+
		"\u0000\u0000\u0000\u001a\u008f\u0001\u0000\u0000\u0000\u001c\u0093\u0001"+
		"\u0000\u0000\u0000\u001e\u0097\u0001\u0000\u0000\u0000 \u009d\u0001\u0000"+
		"\u0000\u0000\"\u00ae\u0001\u0000\u0000\u0000$\u00d0\u0001\u0000\u0000"+
		"\u0000&(\u0003\u0002\u0001\u0000\'&\u0001\u0000\u0000\u0000(+\u0001\u0000"+
		"\u0000\u0000)\'\u0001\u0000\u0000\u0000)*\u0001\u0000\u0000\u0000*,\u0001"+
		"\u0000\u0000\u0000+)\u0001\u0000\u0000\u0000,-\u0005\u0001\u0000\u0000"+
		"-1\u0003\b\u0004\u0000.0\u0003\u0002\u0001\u0000/.\u0001\u0000\u0000\u0000"+
		"03\u0001\u0000\u0000\u00001/\u0001\u0000\u0000\u000012\u0001\u0000\u0000"+
		"\u000024\u0001\u0000\u0000\u000031\u0001\u0000\u0000\u000045\u0005\u0000"+
		"\u0000\u00015\u0001\u0001\u0000\u0000\u000069\u0005\u0007\u0000\u0000"+
		"7:\u0003\u000e\u0007\u00008:\u0005\t\u0000\u000097\u0001\u0000\u0000\u0000"+
		"98\u0001\u0000\u0000\u0000:;\u0001\u0000\u0000\u0000;<\u0005)\u0000\u0000"+
		"<>\u0005\u001e\u0000\u0000=?\u0003\u0004\u0002\u0000>=\u0001\u0000\u0000"+
		"\u0000>?\u0001\u0000\u0000\u0000?@\u0001\u0000\u0000\u0000@A\u0005\u001f"+
		"\u0000\u0000AB\u0003\b\u0004\u0000B\u0003\u0001\u0000\u0000\u0000CH\u0003"+
		"\u0006\u0003\u0000DE\u0005%\u0000\u0000EG\u0003\u0006\u0003\u0000FD\u0001"+
		"\u0000\u0000\u0000GJ\u0001\u0000\u0000\u0000HF\u0001\u0000\u0000\u0000"+
		"HI\u0001\u0000\u0000\u0000I\u0005\u0001\u0000\u0000\u0000JH\u0001\u0000"+
		"\u0000\u0000KL\u0003\u000e\u0007\u0000LM\u0005)\u0000\u0000M\u0007\u0001"+
		"\u0000\u0000\u0000NR\u0005 \u0000\u0000OQ\u0003\n\u0005\u0000PO\u0001"+
		"\u0000\u0000\u0000QT\u0001\u0000\u0000\u0000RP\u0001\u0000\u0000\u0000"+
		"RS\u0001\u0000\u0000\u0000SU\u0001\u0000\u0000\u0000TR\u0001\u0000\u0000"+
		"\u0000UV\u0005!\u0000\u0000V\t\u0001\u0000\u0000\u0000W`\u0003\f\u0006"+
		"\u0000X`\u0003\u0010\b\u0000Y`\u0003\u0012\t\u0000Z`\u0003\u0014\n\u0000"+
		"[`\u0003\u001e\u000f\u0000\\`\u0003 \u0010\u0000]`\u0003\"\u0011\u0000"+
		"^`\u0003\u0016\u000b\u0000_W\u0001\u0000\u0000\u0000_X\u0001\u0000\u0000"+
		"\u0000_Y\u0001\u0000\u0000\u0000_Z\u0001\u0000\u0000\u0000_[\u0001\u0000"+
		"\u0000\u0000_\\\u0001\u0000\u0000\u0000_]\u0001\u0000\u0000\u0000_^\u0001"+
		"\u0000\u0000\u0000`\u000b\u0001\u0000\u0000\u0000ab\u0003\u000e\u0007"+
		"\u0000bc\u0005)\u0000\u0000cd\u0005$\u0000\u0000d\r\u0001\u0000\u0000"+
		"\u0000ef\u0007\u0000\u0000\u0000f\u000f\u0001\u0000\u0000\u0000gh\u0005"+
		")\u0000\u0000hi\u0005\u0019\u0000\u0000ij\u0003$\u0012\u0000jk\u0005$"+
		"\u0000\u0000k\u0011\u0001\u0000\u0000\u0000lm\u0005\u0002\u0000\u0000"+
		"mn\u0005\u001e\u0000\u0000no\u0003$\u0012\u0000op\u0005\u001f\u0000\u0000"+
		"ps\u0003\b\u0004\u0000qr\u0005\u0003\u0000\u0000rt\u0003\b\u0004\u0000"+
		"sq\u0001\u0000\u0000\u0000st\u0001\u0000\u0000\u0000t\u0013\u0001\u0000"+
		"\u0000\u0000uv\u0005\u0004\u0000\u0000vw\u0005\u001e\u0000\u0000wx\u0003"+
		"$\u0012\u0000xy\u0005\u001f\u0000\u0000yz\u0005$\u0000\u0000z\u0015\u0001"+
		"\u0000\u0000\u0000{|\u0005)\u0000\u0000|\u0085\u0005\u001e\u0000\u0000"+
		"}\u0082\u0003$\u0012\u0000~\u007f\u0005%\u0000\u0000\u007f\u0081\u0003"+
		"$\u0012\u0000\u0080~\u0001\u0000\u0000\u0000\u0081\u0084\u0001\u0000\u0000"+
		"\u0000\u0082\u0080\u0001\u0000\u0000\u0000\u0082\u0083\u0001\u0000\u0000"+
		"\u0000\u0083\u0086\u0001\u0000\u0000\u0000\u0084\u0082\u0001\u0000\u0000"+
		"\u0000\u0085}\u0001\u0000\u0000\u0000\u0085\u0086\u0001\u0000\u0000\u0000"+
		"\u0086\u0087\u0001\u0000\u0000\u0000\u0087\u0088\u0005\u001f\u0000\u0000"+
		"\u0088\u0089\u0005$\u0000\u0000\u0089\u0017\u0001\u0000\u0000\u0000\u008a"+
		"\u008b\u0003\u000e\u0007\u0000\u008b\u008c\u0005)\u0000\u0000\u008c\u008d"+
		"\u0005\u0019\u0000\u0000\u008d\u008e\u0003$\u0012\u0000\u008e\u0019\u0001"+
		"\u0000\u0000\u0000\u008f\u0090\u0005)\u0000\u0000\u0090\u0091\u0005\u0019"+
		"\u0000\u0000\u0091\u0092\u0003$\u0012\u0000\u0092\u001b\u0001\u0000\u0000"+
		"\u0000\u0093\u0094\u0005)\u0000\u0000\u0094\u0095\u0005\u0019\u0000\u0000"+
		"\u0095\u0096\u0003$\u0012\u0000\u0096\u001d\u0001\u0000\u0000\u0000\u0097"+
		"\u0098\u0005\u0005\u0000\u0000\u0098\u0099\u0005\u001e\u0000\u0000\u0099"+
		"\u009a\u0003$\u0012\u0000\u009a\u009b\u0005\u001f\u0000\u0000\u009b\u009c"+
		"\u0003\b\u0004\u0000\u009c\u001f\u0001\u0000\u0000\u0000\u009d\u009e\u0005"+
		"\u0006\u0000\u0000\u009e\u00a1\u0005\u001e\u0000\u0000\u009f\u00a2\u0003"+
		"\u0018\f\u0000\u00a0\u00a2\u0003\u001a\r\u0000\u00a1\u009f\u0001\u0000"+
		"\u0000\u0000\u00a1\u00a0\u0001\u0000\u0000\u0000\u00a1\u00a2\u0001\u0000"+
		"\u0000\u0000\u00a2\u00a3\u0001\u0000\u0000\u0000\u00a3\u00a5\u0005$\u0000"+
		"\u0000\u00a4\u00a6\u0003$\u0012\u0000\u00a5\u00a4\u0001\u0000\u0000\u0000"+
		"\u00a5\u00a6\u0001\u0000\u0000\u0000\u00a6\u00a7\u0001\u0000\u0000\u0000"+
		"\u00a7\u00a9\u0005$\u0000\u0000\u00a8\u00aa\u0003\u001c\u000e\u0000\u00a9"+
		"\u00a8\u0001\u0000\u0000\u0000\u00a9\u00aa\u0001\u0000\u0000\u0000\u00aa"+
		"\u00ab\u0001\u0000\u0000\u0000\u00ab\u00ac\u0005\u001f\u0000\u0000\u00ac"+
		"\u00ad\u0003\b\u0004\u0000\u00ad!\u0001\u0000\u0000\u0000\u00ae\u00b0"+
		"\u0005\b\u0000\u0000\u00af\u00b1\u0003$\u0012\u0000\u00b0\u00af\u0001"+
		"\u0000\u0000\u0000\u00b0\u00b1\u0001\u0000\u0000\u0000\u00b1\u00b2\u0001"+
		"\u0000\u0000\u0000\u00b2\u00b3\u0005$\u0000\u0000\u00b3#\u0001\u0000\u0000"+
		"\u0000\u00b4\u00b5\u0006\u0012\uffff\uffff\u0000\u00b5\u00b6\u0005\u0012"+
		"\u0000\u0000\u00b6\u00d1\u0003$\u0012\u000e\u00b7\u00b8\u0005\u001b\u0000"+
		"\u0000\u00b8\u00d1\u0003$\u0012\r\u00b9\u00ba\u0005\u001e\u0000\u0000"+
		"\u00ba\u00bb\u0003$\u0012\u0000\u00bb\u00bc\u0005\u001f\u0000\u0000\u00bc"+
		"\u00d1\u0001\u0000\u0000\u0000\u00bd\u00d1\u0005&\u0000\u0000\u00be\u00d1"+
		"\u0005\'\u0000\u0000\u00bf\u00d1\u0005(\u0000\u0000\u00c0\u00d1\u0005"+
		"\u000e\u0000\u0000\u00c1\u00d1\u0005\u000f\u0000\u0000\u00c2\u00d1\u0005"+
		")\u0000\u0000\u00c3\u00c4\u0005)\u0000\u0000\u00c4\u00cd\u0005\u001e\u0000"+
		"\u0000\u00c5\u00ca\u0003$\u0012\u0000\u00c6\u00c7\u0005%\u0000\u0000\u00c7"+
		"\u00c9\u0003$\u0012\u0000\u00c8\u00c6\u0001\u0000\u0000\u0000\u00c9\u00cc"+
		"\u0001\u0000\u0000\u0000\u00ca\u00c8\u0001\u0000\u0000\u0000\u00ca\u00cb"+
		"\u0001\u0000\u0000\u0000\u00cb\u00ce\u0001\u0000\u0000\u0000\u00cc\u00ca"+
		"\u0001\u0000\u0000\u0000\u00cd\u00c5\u0001\u0000\u0000\u0000\u00cd\u00ce"+
		"\u0001\u0000\u0000\u0000\u00ce\u00cf\u0001\u0000\u0000\u0000\u00cf\u00d1"+
		"\u0005\u001f\u0000\u0000\u00d0\u00b4\u0001\u0000\u0000\u0000\u00d0\u00b7"+
		"\u0001\u0000\u0000\u0000\u00d0\u00b9\u0001\u0000\u0000\u0000\u00d0\u00bd"+
		"\u0001\u0000\u0000\u0000\u00d0\u00be\u0001\u0000\u0000\u0000\u00d0\u00bf"+
		"\u0001\u0000\u0000\u0000\u00d0\u00c0\u0001\u0000\u0000\u0000\u00d0\u00c1"+
		"\u0001\u0000\u0000\u0000\u00d0\u00c2\u0001\u0000\u0000\u0000\u00d0\u00c3"+
		"\u0001\u0000\u0000\u0000\u00d1\u00e0\u0001\u0000\u0000\u0000\u00d2\u00d3"+
		"\n\u000b\u0000\u0000\u00d3\u00d4\u0007\u0001\u0000\u0000\u00d4\u00df\u0003"+
		"$\u0012\f\u00d5\u00d6\n\n\u0000\u0000\u00d6\u00d7\u0007\u0002\u0000\u0000"+
		"\u00d7\u00df\u0003$\u0012\u000b\u00d8\u00d9\n\t\u0000\u0000\u00d9\u00da"+
		"\u0007\u0003\u0000\u0000\u00da\u00df\u0003$\u0012\n\u00db\u00dc\n\b\u0000"+
		"\u0000\u00dc\u00dd\u0007\u0004\u0000\u0000\u00dd\u00df\u0003$\u0012\t"+
		"\u00de\u00d2\u0001\u0000\u0000\u0000\u00de\u00d5\u0001\u0000\u0000\u0000"+
		"\u00de\u00d8\u0001\u0000\u0000\u0000\u00de\u00db\u0001\u0000\u0000\u0000"+
		"\u00df\u00e2\u0001\u0000\u0000\u0000\u00e0\u00de\u0001\u0000\u0000\u0000"+
		"\u00e0\u00e1\u0001\u0000\u0000\u0000\u00e1%\u0001\u0000\u0000\u0000\u00e2"+
		"\u00e0\u0001\u0000\u0000\u0000\u0013)19>HR_s\u0082\u0085\u00a1\u00a5\u00a9"+
		"\u00b0\u00ca\u00cd\u00d0\u00de\u00e0";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}