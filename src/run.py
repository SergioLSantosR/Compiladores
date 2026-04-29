# src/run.py — Punto de entrada alternativo (ejecuta pipeline.py)
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipeline import ejecutar_pipeline, _imprimir_fases


def main():
    import argparse

    ap = argparse.ArgumentParser(description="MiniLang v3 — Compilador e Intérprete")
    ap.add_argument("file", help="Ruta del archivo de entrada (*.ml)")
    ap.add_argument("--no-print", action="store_true", help="No imprimir durante ejecución")
    args = ap.parse_args()

    resultado = ejecutar_pipeline(
        args.file,
        stdout_print=(not args.no_print),
    )

    _imprimir_fases(resultado)

    if resultado.exito:
        print("\nPrograma válido ✔️")
    sys.exit(0 if resultado.exito else 1)


if __name__ == "__main__":
    main()
