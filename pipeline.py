# pipeline.py — Orquestador del compilador MiniLang v4
#
# Fases:
#   1. Análisis Léxico   (ANTLR Lexer)
#   2. Análisis Sintáctico (ANTLR Parser)
#   3. Análisis Semántico  (SemanticVisitor + TablaSimbolos)
#   4. Generación TAC      (TACGenerator → archivo .tac)
#   5. Generación LLVM IR  (IRGenerator → archivo .ll)
#   6. Interpretación      (EvalVisitor)
#
# Si alguna fase detecta errores se detiene y reporta sin continuar.

from __future__ import annotations

import os
import sys
import time

from antlr4 import CommonTokenStream, FileStream

from gen.grammar.gramatica_v4Lexer import gramatica_v4Lexer
from gen.grammar.gramatica_v4Parser import gramatica_v4Parser
from src.custom_errors import ColectorErrores
from src.semantic_visitor import SemanticVisitor
from src.tac_generator import TACGenerator
from src.ir_generator import IRGenerator
from src.EvalVisitorImpl import EvalVisitor


class FaseResultado:
    __slots__ = ("nombre", "estado", "tiempo_ms", "detalle")

    def __init__(self, nombre: str, estado: str, tiempo_ms: float, detalle: str = ""):
        self.nombre = nombre
        self.estado = estado
        self.tiempo_ms = tiempo_ms
        self.detalle = detalle

    def __str__(self):
        marca = "OK" if self.estado == "ok" else "ERROR"
        linea = f"  [{marca}] {self.nombre} ({self.tiempo_ms:.2f} ms)"
        if self.detalle:
            linea += f"\n       {self.detalle}"
        return linea


class ResultadoPipeline:
    def __init__(self):
        self.exito: bool = False
        self.fases: list[FaseResultado] = []
        self.tac: str = ""
        self.ir: str = ""
        self.salida: list[str] = []
        self.archivo_tac: str | None = None
        self.archivo_ll: str | None = None


def ejecutar_pipeline(
    ruta_archivo: str,
    *,
    stdout_print: bool = True,
    generar_archivos: bool = True,
) -> ResultadoPipeline:
    resultado = ResultadoPipeline()
    base = os.path.splitext(ruta_archivo)[0]

    # ── Fase 1: Léxico ─────────────────────────────────────────
    t0 = time.perf_counter()
    input_stream = FileStream(ruta_archivo, encoding="utf-8")
    colector = ColectorErrores()

    lexer = gramatica_v4Lexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(colector)

    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    t_lexico = (time.perf_counter() - t0) * 1000

    if colector.tiene_errores_lexicos():
        resultado.fases.append(FaseResultado("Análisis Léxico", "error", t_lexico, colector.reporte()))
        return resultado
    resultado.fases.append(FaseResultado("Análisis Léxico", "ok", t_lexico))

    # ── Fase 2: Sintáctico ─────────────────────────────────────
    t0 = time.perf_counter()
    parser = gramatica_v4Parser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(colector)
    tree = parser.programa()
    t_sintactico = (time.perf_counter() - t0) * 1000

    if colector.tiene_errores_sintacticos():
        resultado.fases.append(FaseResultado("Análisis Sintáctico", "error", t_sintactico, colector.reporte()))
        return resultado
    resultado.fases.append(FaseResultado("Análisis Sintáctico", "ok", t_sintactico))

    # ── Fase 3: Semántico ──────────────────────────────────────
    t0 = time.perf_counter()
    semantico = SemanticVisitor()
    semantico.visit(tree)
    t_semantico = (time.perf_counter() - t0) * 1000

    if semantico.tiene_errores():
        resultado.fases.append(FaseResultado("Análisis Semántico", "error", t_semantico, semantico.reporte()))
        return resultado
    resultado.fases.append(FaseResultado("Análisis Semántico", "ok", t_semantico))

    # ── Fase 4: Generación TAC ─────────────────────────────────
    t0 = time.perf_counter()
    try:
        tac_gen = TACGenerator()
        resultado.tac = tac_gen.visit(tree) or ""
        t_tac = (time.perf_counter() - t0) * 1000
        resultado.fases.append(FaseResultado("Generación TAC", "ok", t_tac))
        if generar_archivos:
            resultado.archivo_tac = base + ".tac"
            with open(resultado.archivo_tac, "w", encoding="utf-8") as f:
                f.write(resultado.tac)
    except Exception as ex:
        t_tac = (time.perf_counter() - t0) * 1000
        resultado.fases.append(FaseResultado("Generación TAC", "error", t_tac, str(ex)))
        return resultado

    # ── Fase 5: Generación LLVM IR ─────────────────────────────
    t0 = time.perf_counter()
    try:
        ir_gen = IRGenerator()
        resultado.ir = ir_gen.visit(tree) or ""
        t_ir = (time.perf_counter() - t0) * 1000
        resultado.fases.append(FaseResultado("Generación LLVM IR", "ok", t_ir))
        if generar_archivos:
            resultado.archivo_ll = base + ".ll"
            with open(resultado.archivo_ll, "w", encoding="utf-8") as f:
                f.write(resultado.ir)
    except Exception as ex:
        t_ir = (time.perf_counter() - t0) * 1000
        resultado.fases.append(FaseResultado("Generación LLVM IR", "error", t_ir, str(ex)))
        return resultado

    # ── Fase 6: Interpretación ─────────────────────────────────
    t0 = time.perf_counter()
    interprete = EvalVisitor(stdout_print=stdout_print)
    try:
        interprete.visit(tree)
        t_ejecucion = (time.perf_counter() - t0) * 1000
        resultado.fases.append(FaseResultado("Ejecución (Intérprete)", "ok", t_ejecucion))
    except Exception as ex:
        t_ejecucion = (time.perf_counter() - t0) * 1000
        resultado.fases.append(FaseResultado("Ejecución (Intérprete)", "error", t_ejecucion, str(ex)))
        resultado.salida = interprete.salida
        return resultado

    resultado.exito = True
    resultado.salida = interprete.salida
    return resultado


def _imprimir_fases(resultado: ResultadoPipeline) -> None:
    print("\n╔══════════════════════════════════════════╗", file=sys.stderr)
    print("║       Pipeline MiniLang v4 — Fases       ║", file=sys.stderr)
    print("╠══════════════════════════════════════════╣", file=sys.stderr)
    for fase in resultado.fases:
        print(f"║ {fase}", file=sys.stderr)
    print("╚══════════════════════════════════════════╝", file=sys.stderr)


# ── CLI ────────────────────────────────────────────────────────
def main():
    import argparse

    ap = argparse.ArgumentParser(
        description="MiniLang v4 — Pipeline completo (léxico → sintáctico → semántico → TAC → IR → intérprete)"
    )
    ap.add_argument("archivo", help="Ruta del archivo fuente (.ml)")
    ap.add_argument("--silencioso", action="store_true", help="No imprimir salida del programa")
    ap.add_argument("--sin-archivos", action="store_true", help="No generar archivos .tac y .ll")
    args = ap.parse_args()

    resultado = ejecutar_pipeline(
        args.archivo,
        stdout_print=(not args.silencioso),
        generar_archivos=(not args.sin_archivos),
    )

    _imprimir_fases(resultado)

    if resultado.exito:
        print(f"\nPrograma ejecutado correctamente ✔️")
        if resultado.archivo_tac:
            print(f"  TAC generado: {resultado.archivo_tac}")
        if resultado.archivo_ll:
            print(f"  LLVM IR generado: {resultado.archivo_ll}")
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
