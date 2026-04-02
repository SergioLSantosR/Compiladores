// Generated from /home/sergio/Compiladores/grammar/MiniLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MiniLangParser}.
 */
public interface MiniLangListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MiniLangParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(MiniLangParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiniLangParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(MiniLangParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiniLangParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(MiniLangParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiniLangParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(MiniLangParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiniLangParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterStmt(MiniLangParser.StmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiniLangParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitStmt(MiniLangParser.StmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiniLangParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void enterVarDecl(MiniLangParser.VarDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiniLangParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void exitVarDecl(MiniLangParser.VarDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiniLangParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(MiniLangParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiniLangParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(MiniLangParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiniLangParser#assignStmt}.
	 * @param ctx the parse tree
	 */
	void enterAssignStmt(MiniLangParser.AssignStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiniLangParser#assignStmt}.
	 * @param ctx the parse tree
	 */
	void exitAssignStmt(MiniLangParser.AssignStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiniLangParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void enterIfStmt(MiniLangParser.IfStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiniLangParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void exitIfStmt(MiniLangParser.IfStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiniLangParser#printStmt}.
	 * @param ctx the parse tree
	 */
	void enterPrintStmt(MiniLangParser.PrintStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiniLangParser#printStmt}.
	 * @param ctx the parse tree
	 */
	void exitPrintStmt(MiniLangParser.PrintStmtContext ctx);
	/**
	 * Enter a parse tree produced by the {@code UnaryNot}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterUnaryNot(MiniLangParser.UnaryNotContext ctx);
	/**
	 * Exit a parse tree produced by the {@code UnaryNot}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitUnaryNot(MiniLangParser.UnaryNotContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MulDiv}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterMulDiv(MiniLangParser.MulDivContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MulDiv}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitMulDiv(MiniLangParser.MulDivContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AddSub}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAddSub(MiniLangParser.AddSubContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AddSub}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAddSub(MiniLangParser.AddSubContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Relational}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterRelational(MiniLangParser.RelationalContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Relational}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitRelational(MiniLangParser.RelationalContext ctx);
	/**
	 * Enter a parse tree produced by the {@code FalseLit}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterFalseLit(MiniLangParser.FalseLitContext ctx);
	/**
	 * Exit a parse tree produced by the {@code FalseLit}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitFalseLit(MiniLangParser.FalseLitContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Logical}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterLogical(MiniLangParser.LogicalContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Logical}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitLogical(MiniLangParser.LogicalContext ctx);
	/**
	 * Enter a parse tree produced by the {@code UnaryMinus}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterUnaryMinus(MiniLangParser.UnaryMinusContext ctx);
	/**
	 * Exit a parse tree produced by the {@code UnaryMinus}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitUnaryMinus(MiniLangParser.UnaryMinusContext ctx);
	/**
	 * Enter a parse tree produced by the {@code TrueLit}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterTrueLit(MiniLangParser.TrueLitContext ctx);
	/**
	 * Exit a parse tree produced by the {@code TrueLit}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitTrueLit(MiniLangParser.TrueLitContext ctx);
	/**
	 * Enter a parse tree produced by the {@code IdRef}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterIdRef(MiniLangParser.IdRefContext ctx);
	/**
	 * Exit a parse tree produced by the {@code IdRef}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitIdRef(MiniLangParser.IdRefContext ctx);
	/**
	 * Enter a parse tree produced by the {@code IntLit}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterIntLit(MiniLangParser.IntLitContext ctx);
	/**
	 * Exit a parse tree produced by the {@code IntLit}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitIntLit(MiniLangParser.IntLitContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Paren}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterParen(MiniLangParser.ParenContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Paren}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitParen(MiniLangParser.ParenContext ctx);
}