# pipeline.py — Orquestador del compilador MiniLang
#
# Fases:
#   1. Análisis Léxico   (ANTLR Lexer)
#   2. Análisis Sintáctico (ANTLR Parser)
#   3. Análisis Semántico  (SemanticVisitor + TablaSimbolos)
#   4. Interpretación      (InterpreterVisitor)
#
# Si alguna fase detecta errores se detiene y reporta sin continuar.

from __future__ import annotations

import sys

from antlr4 import CommonTokenStream, FileStream

from gen.grammar.MiniLangLexer import MiniLangLexer
from gen.grammar.MiniLangParser import MiniLangParser
from src.custom_errors import ColectorErrores
from src.semantic_visitor import SemanticVisitor
from src.interpreter_visitor import InterpreterVisitor


class ResultadoPipeline:
    """Encapsula el resultado de ejecutar el pipeline completo."""

    def __init__(self):
        self.exito: bool = False
        self.fase_error: str | None = None
        self.errores_lexicos: list = []
        self.errores_sintacticos: list = []
        self.errores_semanticos: list[str] = []
        self.error_ejecucion: str | None = None
        self.salida: list[str] = []
        self.memoria: dict | None = None

    @property
    def tiene_errores(self) -> bool:
        return not self.exito


def ejecutar_pipeline(
    ruta_archivo: str,
    *,
    stdout_print: bool = True,
    trace_assignments: bool = False,
) -> ResultadoPipeline:
    """
    Ejecuta las 4 fases del compilador sobre el archivo dado.

    Retorna un ResultadoPipeline con toda la información del proceso.
    """
    resultado = ResultadoPipeline()

    # ── Fase 1 y 2: Léxico + Sintáctico ────────────────────────
    input_stream = FileStream(ruta_archivo, encoding="utf-8")
    colector = ColectorErrores()

    lexer = MiniLangLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(colector)

    token_stream = CommonTokenStream(lexer)

    parser = MiniLangParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(colector)

    tree = parser.programa()

    if colector.tiene_errores_lexicos():
        resultado.fase_error = "léxico"
        resultado.errores_lexicos = colector.errores_lexicos
        resultado.errores_sintacticos = colector.errores_sintacticos
        _reportar_errores(colector, file=sys.stderr)
        return resultado

    if colector.tiene_errores_sintacticos():
        resultado.fase_error = "sintáctico"
        resultado.errores_sintacticos = colector.errores_sintacticos
        _reportar_errores(colector, file=sys.stderr)
        return resultado

    # ── Fase 3: Semántico ──────────────────────────────────────
    semantico = SemanticVisitor()
    semantico.visit(tree)

    if semantico.tiene_errores():
        resultado.fase_error = "semántico"
        resultado.errores_semanticos = semantico.errores
        print(semantico.reporte(), file=sys.stderr)
        return resultado

    # ── Fase 4: Interpretación ─────────────────────────────────
    interprete = InterpreterVisitor(
        stdout_print=stdout_print,
        trace_assignments=trace_assignments,
    )
    try:
        interprete.visit(tree)
    except RuntimeError as ex:
        resultado.fase_error = "ejecución"
        resultado.error_ejecucion = str(ex)
        resultado.salida = interprete.salida
        print(f"[Error de Ejecución] {ex}", file=sys.stderr)
        return resultado

    resultado.exito = True
    resultado.salida = interprete.salida
    resultado.memoria = interprete.memoria
    return resultado


def _reportar_errores(colector: ColectorErrores, *, file=sys.stderr) -> None:
    print(colector.reporte(), file=file)


# ── CLI ────────────────────────────────────────────────────────
def main():
    import argparse

    ap = argparse.ArgumentParser(
        description="MiniLang — Pipeline completo (léxico → sintáctico → semántico → intérprete)"
    )
    ap.add_argument("archivo", help="Ruta del archivo fuente (.ml)")
    ap.add_argument(
        "--silencioso",
        action="store_true",
        help="No imprimir salida del programa (solo reportar errores)",
    )
    ap.add_argument(
        "--traza",
        action="store_true",
        help="Mostrar asignaciones durante la ejecución",
    )
    args = ap.parse_args()

    resultado = ejecutar_pipeline(
        args.archivo,
        stdout_print=(not args.silencioso),
        trace_assignments=args.traza,
    )

    if resultado.exito:
        print("\nPrograma ejecutado correctamente ✔️")
        sys.exit(0)
    else:
        sys.exit(1 if resultado.fase_error in ("léxico", "sintáctico") else 2)


if __name__ == "__main__":
    main()
