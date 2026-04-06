# src/pipeline.py
"""Pipeline: léxico → sintáctico → AST → semántica → intérprete (una lectura del disco)."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from antlr4 import CommonTokenStream, InputStream
from antlr4.Token import Token

from gen.grammar.MiniLangLexer import MiniLangLexer
from gen.grammar.MiniLangParser import MiniLangParser

from src.ast_builder import AstBuilder
from src.custom_errors import LexerErrorListener, ParserErrorListener
from src.interpreter_visitor import InterpreterVisitor
from src.semantic_visitor import SemanticVisitor


def _load_utf8(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def fase_lexer(text: str) -> LexerErrorListener:
    lexer = MiniLangLexer(InputStream(text))
    lexer.removeErrorListeners()
    listener = LexerErrorListener()
    lexer.addErrorListener(listener)
    t = lexer.nextToken()
    while t.type != Token.EOF:
        t = lexer.nextToken()
    return listener


def fase_parser(text: str):
    lexer = MiniLangLexer(InputStream(text))
    lexer.removeErrorListeners()
    parser = MiniLangParser(CommonTokenStream(lexer))
    parser.removeErrorListeners()
    pl = ParserErrorListener()
    parser.addErrorListener(pl)
    return parser.programa(), pl


def run_pipeline(path: str, stdout_print: bool = True) -> int:
    """
    Códigos: 0 ok | 1 léxico/sintáctico | 2 semántico | 3 ejecución.
    """
    text = _load_utf8(path)

    lex = fase_lexer(text)
    if lex.has_errors():
        print(lex.report(), file=sys.stderr)
        return 1

    tree, par = fase_parser(text)
    if par.has_errors():
        print(par.report(), file=sys.stderr)
        return 1

    ast_root = AstBuilder().visit(tree)

    sem = SemanticVisitor()
    sem.analyze(ast_root)
    if sem.has_errors():
        print(sem.report(), file=sys.stderr)
        return 2

    interp = InterpreterVisitor(stdout_print=stdout_print)
    try:
        interp.run(ast_root)
        print("\nPrograma válido ✔️")
        if interp.memoria:
            print("Estado final de variables:", interp.memoria)
    except RuntimeError as ex:
        print(f"[Error en ejecución] {ex}", file=sys.stderr)
        return 3
    return 0


def parse_args():
    ap = argparse.ArgumentParser(
        description="MiniLang — pipeline léxico → sintáctico → AST → semántica → intérprete"
    )
    ap.add_argument("file", help="Archivo fuente (*.ml)")
    ap.add_argument("--no-print", action="store_true", help="Silenciar salidas print del programa")
    return ap.parse_args()


def main() -> None:
    args = parse_args()
    raise SystemExit(run_pipeline(args.file, stdout_print=(not args.no_print)))


if __name__ == "__main__":
    main()
