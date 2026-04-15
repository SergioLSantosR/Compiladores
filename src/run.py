# src/run.py — Punto de entrada alternativo (usa pipeline.py internamente)
import sys
import argparse
from antlr4 import CommonTokenStream, FileStream
from gen.grammar.MiniLangLexer import MiniLangLexer
from gen.grammar.MiniLangParser import MiniLangParser
from src.custom_errors import ColectorErrores
from src.semantic_visitor import SemanticVisitor
from src.interpreter_visitor import InterpreterVisitor


def parse_args():
    ap = argparse.ArgumentParser(description="MiniLang — Compilador e Intérprete")
    ap.add_argument("file", help="Ruta del archivo de entrada (*.ml)")
    ap.add_argument("--no-print", action="store_true", help="No imprimir durante ejecución")
    return ap.parse_args()


def main():
    args = parse_args()
    input_stream = FileStream(args.file, encoding="utf-8")

    colector = ColectorErrores()

    # Lexer
    lexer = MiniLangLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(colector)

    token_stream = CommonTokenStream(lexer)

    # Parser
    parser = MiniLangParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(colector)

    tree = parser.programa()

    if colector.tiene_errores():
        print(colector.reporte(), file=sys.stderr)
        sys.exit(1)

    # Análisis semántico
    semantico = SemanticVisitor()
    semantico.visit(tree)

    if semantico.tiene_errores():
        print(semantico.reporte(), file=sys.stderr)
        sys.exit(2)

    # Interpretación
    interprete = InterpreterVisitor(stdout_print=(not args.no_print))
    try:
        interprete.visit(tree)
        print("\nPrograma válido ✔️")
    except RuntimeError as ex:
        print(f"[Error de Ejecución] {ex}", file=sys.stderr)
        sys.exit(3)


if __name__ == "__main__":
    main()
