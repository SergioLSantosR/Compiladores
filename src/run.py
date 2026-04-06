# src/run.py
import argparse
import sys

from src.pipeline import run_pipeline


def parse_args():
    ap = argparse.ArgumentParser(description="MiniLang - Parser + Evaluador (ANTLR4 + Python)")
    ap.add_argument("file", help="Ruta del archivo de entrada (*.ml)")
    ap.add_argument(
        "--no-print",
        action="store_true",
        help="No imprimir durante ejecución (solo guardar resultados)",
    )
    return ap.parse_args()


def main():
    args = parse_args()
    code = run_pipeline(args.file, stdout_print=(not args.no_print))
    raise SystemExit(code)


if __name__ == "__main__":
    main()
