# Persona 4 — ejecutar solo esta variante MiniLang (inglés) desde esta carpeta:
#   cd Compiladores && python -m src.run examples/interpreter_demo.ml
import sys
import argparse
from antlr4 import *
from gen.grammar.MiniLangLexer import MiniLangLexer
from gen.grammar.MiniLangParser import MiniLangParser
from src.error_listener import VerboseErrorListener
from src.interpreter_visitor import InterpreterVisitor


def parse_args():
    ap = argparse.ArgumentParser(description="MiniLang Persona 4 — intérprete (ANTLR4 + Python)")
    ap.add_argument("file", help="Archivo fuente (*.ml)")
    ap.add_argument("--no-print", action="store_true", help="No imprimir durante ejecución")
    return ap.parse_args()


def main():
    args = parse_args()
    input_stream = FileStream(args.file, encoding="utf-8")
    lexer = MiniLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MiniLangParser(token_stream)
    err_listener = VerboseErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(err_listener)

    tree = parser.programa()

    if err_listener.has_errors():
        print(err_listener.report(), file=sys.stderr)
        sys.exit(1)

    visitor = InterpreterVisitor(stdout_print=(not args.no_print))
    try:
        visitor.visit(tree)
        print("\nPrograma válido ✔️")
        if visitor.memoria:
            print("Estado final de variables:", visitor.memoria)
    except RuntimeError as ex:
        print(f"[Error en evaluación] {ex}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
