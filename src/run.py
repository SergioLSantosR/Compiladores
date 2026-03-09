# src/run.py
import sys
import argparse
from antlr4 import *
from gen.grammar.MiniLangLexer import MiniLangLexer
from gen.grammar.MiniLangParser import MiniLangParser
from src.error_listener import VerboseErrorListener
from src.EvalVisitorImpl import EvalVisitor

def parse_args():
    ap = argparse.ArgumentParser(description="MiniLang - Parser + Evaluador (ANTLR4 + Python)")
    ap.add_argument("file", help="Ruta del archivo de entrada (*.ml)")
    ap.add_argument("--no-print", action="store_true", help="No imprimir durante ejecución (solo guardar resultados)")
    return ap.parse_args()

def main():
    args = parse_args()
    input_stream = FileStream(args.file, encoding='utf-8')

    # Lexer
    lexer = MiniLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Parser
    parser = MiniLangParser(token_stream)
    # Quitar oyente por defecto y agregar el nuestro
    err_listener = VerboseErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(err_listener)

    tree = parser.program()

    # Si hubo errores de sintaxis, reportarlos
    if err_listener.has_errors():
        print(err_listener.report(), file=sys.stderr)
        sys.exit(1)

    # Evaluar
    visitor = EvalVisitor(stdout_print=(not args.no_print))
    try:
        visitor.visit(tree)
        print("\nPrograma válido ✔️")
        # Mostrar memoria final
        if visitor.memory:
            print("Estado final de variables:", visitor.memory)
    except RuntimeError as ex:
        print(f"[Error en evaluación] {ex}", file=sys.stderr)
        sys.exit(2)

if __name__ == "__main__":
    main()
