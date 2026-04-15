# src/run.py
import sys
import argparse
from antlr4 import *
from gen.grammar.MiniLangLexer import MiniLangLexer
from gen.grammar.MiniLangParser import MiniLangParser
from src.error_listener import VerboseErrorListener
from src.semantic_visitor import SemanticVisitor
from src.EvalVisitorImpl import EvalVisitor


def parse_args():
    ap = argparse.ArgumentParser(description="MiniLang - Parser + Semántica + Evaluador (ANTLR4 + Python)")
    ap.add_argument("file", help="Ruta del archivo de entrada (*.ml)")
    ap.add_argument("--no-print", action="store_true", help="No imprimir durante ejecución (solo guardar resultados)")
    return ap.parse_args()


def main():
    args = parse_args()
    input_stream = FileStream(args.file, encoding="utf-8")

    # Lexer
    lexer = MiniLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Parser
    parser = MiniLangParser(token_stream)
    err_listener = VerboseErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(err_listener)

    tree = parser.programa()

    # Errores sintácticos
    if err_listener.has_errors():
        print(err_listener.report(), file=sys.stderr)
        sys.exit(1)

    # Análisis semántico
    semantic_visitor = SemanticVisitor()
    semantic_visitor.visit(tree)

    if semantic_visitor.tiene_errores():
        print(semantic_visitor.reporte(), file=sys.stderr)
        sys.exit(2)

    # Evaluación
    visitor = EvalVisitor(stdout_print=(not args.no_print))
    try:
        visitor.visit(tree)
        print("\nPrograma válido ✔️")
    except RuntimeError as ex:
        print(f"[Error en evaluación] {ex}", file=sys.stderr)
        sys.exit(3)


if __name__ == "__main__":
    main()