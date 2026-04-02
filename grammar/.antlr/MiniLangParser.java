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
		PROGRAM=1, SI=2, SINO=3, IMPRIME=4, INT_T=5, BOOL_T=6, TRUE=7, FALSE=8, 
		AND=9, OR=10, NOT=11, EQ=12, NEQ=13, LE=14, GE=15, LT=16, GT=17, ASIGNA=18, 
		SUMA=19, RESTA=20, MULTI=21, DIVIDE=22, PARENTESIS_IZQ=23, PARENTESIS_DER=24, 
		LLAVE_IZQ=25, LLAVE_DER=26, CORCHETE_IZQ=27, CORCHETE_DER=28, PUNTO_COMA=29, 
		COMA=30, ID=31, INT=32, WS=33, LINEA_COMENTARIO=34, GRUPO_COMENTARIO=35;
	public static final int
		RULE_program = 0, RULE_grupo = 1, RULE_sentencia = 2, RULE_declaraVariable = 3, 
		RULE_tipo = 4, RULE_sentenciaAsigna = 5, RULE_sentenciaSI = 6, RULE_sentenciaImprime = 7, 
		RULE_expr = 8;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "grupo", "sentencia", "declaraVariable", "tipo", "sentenciaAsigna", 
			"sentenciaSI", "sentenciaImprime", "expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'program'", "'si'", "'sino'", "'imprime'", "'int'", "'bool'", 
			"'true'", "'false'", "'&&'", "'||'", "'!'", "'=='", null, "'<='", "'>='", 
			"'<'", "'>'", "'='", "'+'", "'-'", "'*'", "'/'", "'('", "')'", "'{'", 
			"'}'", "'['", "']'", "';'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PROGRAM", "SI", "SINO", "IMPRIME", "INT_T", "BOOL_T", "TRUE", 
			"FALSE", "AND", "OR", "NOT", "EQ", "NEQ", "LE", "GE", "LT", "GT", "ASIGNA", 
			"SUMA", "RESTA", "MULTI", "DIVIDE", "PARENTESIS_IZQ", "PARENTESIS_DER", 
			"LLAVE_IZQ", "LLAVE_DER", "CORCHETE_IZQ", "CORCHETE_DER", "PUNTO_COMA", 
			"COMA", "ID", "INT", "WS", "LINEA_COMENTARIO", "GRUPO_COMENTARIO"
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
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(18);
			match(PROGRAM);
			setState(19);
			grupo();
			setState(20);
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
		enterRule(_localctx, 2, RULE_grupo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(22);
			match(LLAVE_IZQ);
			setState(26);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2147483764L) != 0)) {
				{
				{
				setState(23);
				sentencia();
				}
				}
				setState(28);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(29);
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
		public SentenciaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentencia; }
	}

	public final SentenciaContext sentencia() throws RecognitionException {
		SentenciaContext _localctx = new SentenciaContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_sentencia);
		try {
			setState(35);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT_T:
			case BOOL_T:
				enterOuterAlt(_localctx, 1);
				{
				setState(31);
				declaraVariable();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(32);
				sentenciaAsigna();
				}
				break;
			case SI:
				enterOuterAlt(_localctx, 3);
				{
				setState(33);
				sentenciaSI();
				}
				break;
			case IMPRIME:
				enterOuterAlt(_localctx, 4);
				{
				setState(34);
				sentenciaImprime();
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
		enterRule(_localctx, 6, RULE_declaraVariable);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(37);
			tipo();
			setState(38);
			match(ID);
			setState(39);
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
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(41);
			_la = _input.LA(1);
			if ( !(_la==INT_T || _la==BOOL_T) ) {
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
		enterRule(_localctx, 10, RULE_sentenciaAsigna);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(43);
			match(ID);
			setState(44);
			match(ASIGNA);
			setState(45);
			expr(0);
			setState(46);
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
		enterRule(_localctx, 12, RULE_sentenciaSI);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			match(SI);
			setState(49);
			match(PARENTESIS_IZQ);
			setState(50);
			expr(0);
			setState(51);
			match(PARENTESIS_DER);
			setState(52);
			grupo();
			setState(55);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SINO) {
				{
				setState(53);
				match(SINO);
				setState(54);
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
		enterRule(_localctx, 14, RULE_sentenciaImprime);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(57);
			match(IMPRIME);
			setState(58);
			match(PARENTESIS_IZQ);
			setState(59);
			expr(0);
			setState(60);
			match(PARENTESIS_DER);
			setState(61);
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
	public static class UnaryNotContext extends ExprContext {
		public TerminalNode NOT() { return getToken(MiniLangParser.NOT, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public UnaryNotContext(ExprContext ctx) { copyFrom(ctx); }
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
	public static class TrueLitContext extends ExprContext {
		public TerminalNode TRUE() { return getToken(MiniLangParser.TRUE, 0); }
		public TrueLitContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IdRefContext extends ExprContext {
		public TerminalNode ID() { return getToken(MiniLangParser.ID, 0); }
		public IdRefContext(ExprContext ctx) { copyFrom(ctx); }
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
		int _startState = 16;
		enterRecursionRule(_localctx, 16, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				{
				_localctx = new UnaryNotContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(64);
				match(NOT);
				setState(65);
				expr(11);
				}
				break;
			case RESTA:
				{
				_localctx = new UnaryMinusContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(66);
				match(RESTA);
				setState(67);
				expr(10);
				}
				break;
			case PARENTESIS_IZQ:
				{
				_localctx = new ParenContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(68);
				match(PARENTESIS_IZQ);
				setState(69);
				expr(0);
				setState(70);
				match(PARENTESIS_DER);
				}
				break;
			case INT:
				{
				_localctx = new IntLitContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(72);
				match(INT);
				}
				break;
			case TRUE:
				{
				_localctx = new TrueLitContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(73);
				match(TRUE);
				}
				break;
			case FALSE:
				{
				_localctx = new FalseLitContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(74);
				match(FALSE);
				}
				break;
			case ID:
				{
				_localctx = new IdRefContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(75);
				match(ID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(92);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(90);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
					case 1:
						{
						_localctx = new MulDivContext(new ExprContext(_parentctx, _parentState));
						((MulDivContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(78);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(79);
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
						setState(80);
						((MulDivContext)_localctx).right = expr(9);
						}
						break;
					case 2:
						{
						_localctx = new AddSubContext(new ExprContext(_parentctx, _parentState));
						((AddSubContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(81);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(82);
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
						setState(83);
						((AddSubContext)_localctx).right = expr(8);
						}
						break;
					case 3:
						{
						_localctx = new RelationalContext(new ExprContext(_parentctx, _parentState));
						((RelationalContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(84);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(85);
						((RelationalContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 258048L) != 0)) ) {
							((RelationalContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(86);
						((RelationalContext)_localctx).right = expr(7);
						}
						break;
					case 4:
						{
						_localctx = new LogicalContext(new ExprContext(_parentctx, _parentState));
						((LogicalContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(87);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(88);
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
						setState(89);
						((LogicalContext)_localctx).right = expr(6);
						}
						break;
					}
					} 
				}
				setState(94);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
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
		case 8:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 8);
		case 1:
			return precpred(_ctx, 7);
		case 2:
			return precpred(_ctx, 6);
		case 3:
			return precpred(_ctx, 5);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001#`\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002\u0002"+
		"\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002\u0005"+
		"\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002\b\u0007"+
		"\b\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0005\u0001\u0019\b\u0001\n\u0001\f\u0001\u001c\t\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002$\b"+
		"\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0003\u00068\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b"+
		"\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003"+
		"\bM\b\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0005\b[\b\b\n\b\f\b^\t\b\u0001\b\u0000"+
		"\u0001\u0010\t\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0000\u0005\u0001"+
		"\u0000\u0005\u0006\u0001\u0000\u0015\u0016\u0001\u0000\u0013\u0014\u0001"+
		"\u0000\f\u0011\u0001\u0000\t\ne\u0000\u0012\u0001\u0000\u0000\u0000\u0002"+
		"\u0016\u0001\u0000\u0000\u0000\u0004#\u0001\u0000\u0000\u0000\u0006%\u0001"+
		"\u0000\u0000\u0000\b)\u0001\u0000\u0000\u0000\n+\u0001\u0000\u0000\u0000"+
		"\f0\u0001\u0000\u0000\u0000\u000e9\u0001\u0000\u0000\u0000\u0010L\u0001"+
		"\u0000\u0000\u0000\u0012\u0013\u0005\u0001\u0000\u0000\u0013\u0014\u0003"+
		"\u0002\u0001\u0000\u0014\u0015\u0005\u0000\u0000\u0001\u0015\u0001\u0001"+
		"\u0000\u0000\u0000\u0016\u001a\u0005\u0019\u0000\u0000\u0017\u0019\u0003"+
		"\u0004\u0002\u0000\u0018\u0017\u0001\u0000\u0000\u0000\u0019\u001c\u0001"+
		"\u0000\u0000\u0000\u001a\u0018\u0001\u0000\u0000\u0000\u001a\u001b\u0001"+
		"\u0000\u0000\u0000\u001b\u001d\u0001\u0000\u0000\u0000\u001c\u001a\u0001"+
		"\u0000\u0000\u0000\u001d\u001e\u0005\u001a\u0000\u0000\u001e\u0003\u0001"+
		"\u0000\u0000\u0000\u001f$\u0003\u0006\u0003\u0000 $\u0003\n\u0005\u0000"+
		"!$\u0003\f\u0006\u0000\"$\u0003\u000e\u0007\u0000#\u001f\u0001\u0000\u0000"+
		"\u0000# \u0001\u0000\u0000\u0000#!\u0001\u0000\u0000\u0000#\"\u0001\u0000"+
		"\u0000\u0000$\u0005\u0001\u0000\u0000\u0000%&\u0003\b\u0004\u0000&\'\u0005"+
		"\u001f\u0000\u0000\'(\u0005\u001d\u0000\u0000(\u0007\u0001\u0000\u0000"+
		"\u0000)*\u0007\u0000\u0000\u0000*\t\u0001\u0000\u0000\u0000+,\u0005\u001f"+
		"\u0000\u0000,-\u0005\u0012\u0000\u0000-.\u0003\u0010\b\u0000./\u0005\u001d"+
		"\u0000\u0000/\u000b\u0001\u0000\u0000\u000001\u0005\u0002\u0000\u0000"+
		"12\u0005\u0017\u0000\u000023\u0003\u0010\b\u000034\u0005\u0018\u0000\u0000"+
		"47\u0003\u0002\u0001\u000056\u0005\u0003\u0000\u000068\u0003\u0002\u0001"+
		"\u000075\u0001\u0000\u0000\u000078\u0001\u0000\u0000\u00008\r\u0001\u0000"+
		"\u0000\u00009:\u0005\u0004\u0000\u0000:;\u0005\u0017\u0000\u0000;<\u0003"+
		"\u0010\b\u0000<=\u0005\u0018\u0000\u0000=>\u0005\u001d\u0000\u0000>\u000f"+
		"\u0001\u0000\u0000\u0000?@\u0006\b\uffff\uffff\u0000@A\u0005\u000b\u0000"+
		"\u0000AM\u0003\u0010\b\u000bBC\u0005\u0014\u0000\u0000CM\u0003\u0010\b"+
		"\nDE\u0005\u0017\u0000\u0000EF\u0003\u0010\b\u0000FG\u0005\u0018\u0000"+
		"\u0000GM\u0001\u0000\u0000\u0000HM\u0005 \u0000\u0000IM\u0005\u0007\u0000"+
		"\u0000JM\u0005\b\u0000\u0000KM\u0005\u001f\u0000\u0000L?\u0001\u0000\u0000"+
		"\u0000LB\u0001\u0000\u0000\u0000LD\u0001\u0000\u0000\u0000LH\u0001\u0000"+
		"\u0000\u0000LI\u0001\u0000\u0000\u0000LJ\u0001\u0000\u0000\u0000LK\u0001"+
		"\u0000\u0000\u0000M\\\u0001\u0000\u0000\u0000NO\n\b\u0000\u0000OP\u0007"+
		"\u0001\u0000\u0000P[\u0003\u0010\b\tQR\n\u0007\u0000\u0000RS\u0007\u0002"+
		"\u0000\u0000S[\u0003\u0010\b\bTU\n\u0006\u0000\u0000UV\u0007\u0003\u0000"+
		"\u0000V[\u0003\u0010\b\u0007WX\n\u0005\u0000\u0000XY\u0007\u0004\u0000"+
		"\u0000Y[\u0003\u0010\b\u0006ZN\u0001\u0000\u0000\u0000ZQ\u0001\u0000\u0000"+
		"\u0000ZT\u0001\u0000\u0000\u0000ZW\u0001\u0000\u0000\u0000[^\u0001\u0000"+
		"\u0000\u0000\\Z\u0001\u0000\u0000\u0000\\]\u0001\u0000\u0000\u0000]\u0011"+
		"\u0001\u0000\u0000\u0000^\\\u0001\u0000\u0000\u0000\u0006\u001a#7LZ\\";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}