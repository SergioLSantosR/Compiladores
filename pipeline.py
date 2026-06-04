from __future__ import annotations

import os
import sys
import time

from antlr4 import CommonTokenStream, FileStream

from gen.grammar.gramatica_v3Lexer import gramatica_v3Lexer
from gen.grammar.gramatica_v3Parser import gramatica_v3Parser
from src.custom_errors import ColectorErrores
from src.semantic_visitor import SemanticVisitor
from src.tac_generator import TACGenerator
from src.ir_generator import IRGenerator
from src.EvalVisitorImpl import EvalVisitor
from src.ir_runner import ejecutar_ir
from src.passes import aplicar_optimizacion_o3


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
        self.ir_optimizado: str = ""
        self.metricas_optimizacion: dict = {}
        self.salida: list[str] = []
        self.salida_ir: str = ""
        self.salida_ir_optimizado: str = ""
        self.archivo_tac: str | None = None
        self.archivo_ll: str | None = None
        self.archivo_ll_optimizado: str | None = None


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

    lexer = gramatica_v3Lexer(input_stream)
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
    parser = gramatica_v3Parser(token_stream)
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
            with open(resultado.archivo_tac, "w", encoding="utf-8") as archivo:
                archivo.write(resultado.tac)
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
            with open(resultado.archivo_ll, "w", encoding="utf-8") as archivo:
                archivo.write(resultado.ir)
    except Exception as ex:
        t_ir = (time.perf_counter() - t0) * 1000
        resultado.fases.append(FaseResultado("Generación LLVM IR", "error", t_ir, str(ex)))
        return resultado

    # ── Fase 6: Ejecución (Intérprete) ─────────────────────────
    t0 = time.perf_counter()
    interprete = EvalVisitor(stdout_print=stdout_print)
    try:
        interprete.visit(tree)
        t_ejecucion = (time.perf_counter() - t0) * 1000
        resultado.fases.append(FaseResultado("Ejecución (Intérprete)", "ok", t_ejecucion))
        resultado.salida = interprete.salida
    except Exception as ex:
        t_ejecucion = (time.perf_counter() - t0) * 1000
        resultado.fases.append(FaseResultado("Ejecución (Intérprete)", "error", t_ejecucion, str(ex)))
        resultado.salida = interprete.salida
        return resultado

    # ── Fase 7: Optimización O3 ────────────────────────────────
    t0 = time.perf_counter()
    try:
        nombre_base = base if generar_archivos else None
        resultado.ir_optimizado, resultado.metricas_optimizacion = aplicar_optimizacion_o3(
            resultado.ir,
            nombre_base,
        )
        t_opt = (time.perf_counter() - t0) * 1000

        antes = resultado.metricas_optimizacion.get("instrucciones_antes", 0)
        despues = resultado.metricas_optimizacion.get("instrucciones_despues", 0)
        reduccion = resultado.metricas_optimizacion.get("reduccion_porcentaje", 0.0)

        detalle = (
            f"Instrucciones: {antes} → {despues} | "
            f"Reducción: {reduccion:.2f}%"
        )

        resultado.fases.append(FaseResultado("Optimización O3", "ok", t_opt, detalle))

        if generar_archivos:
            resultado.archivo_ll_optimizado = base + ".opt.ll"
    except Exception as ex:
        t_opt = (time.perf_counter() - t0) * 1000
        resultado.fases.append(FaseResultado("Optimización O3", "error", t_opt, str(ex)))
        return resultado

    # Salida del IR original
    try:
        resultado.salida_ir = ejecutar_ir(resultado.ir)
    except Exception as ex:
        resultado.salida_ir = f"Error al ejecutar IR original: {ex}"

    # Salida del IR optimizado
    try:
        if resultado.ir_optimizado:
            resultado.salida_ir_optimizado = ejecutar_ir(resultado.ir_optimizado)
    except Exception as ex:
        resultado.salida_ir_optimizado = f"Error al ejecutar IR optimizado: {ex}"

    resultado.exito = True
    return resultado


def _imprimir_fases(resultado: ResultadoPipeline) -> None:
    print("\n╔══════════════════════════════════════════╗", file=sys.stderr)
    print("║       Pipeline MiniLang v4 — 7 fases     ║", file=sys.stderr)
    print("╠══════════════════════════════════════════╣", file=sys.stderr)
    for fase in resultado.fases:
        print(f"║ {fase}", file=sys.stderr)
    print("╚══════════════════════════════════════════╝", file=sys.stderr)


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="MiniLang v4 — Pipeline completo con optimización O3"
    )
    parser.add_argument("archivo", help="Ruta del archivo fuente (.ml)")
    parser.add_argument("--silencioso", action="store_true", help="No imprimir salida del programa")
    parser.add_argument("--sin-archivos", action="store_true", help="No generar archivos .tac, .ll y .opt.ll")
    args = parser.parse_args()

    resultado = ejecutar_pipeline(
        args.archivo,
        stdout_print=(not args.silencioso),
        generar_archivos=(not args.sin_archivos),
    )

    _imprimir_fases(resultado)

    if resultado.exito:
        print("\nPrograma ejecutado correctamente")
        if resultado.archivo_tac:
            print(f"  TAC generado: {resultado.archivo_tac}")
        if resultado.archivo_ll:
            print(f"  LLVM IR generado: {resultado.archivo_ll}")
        if resultado.archivo_ll_optimizado:
            print(f"  LLVM IR optimizado generado: {resultado.archivo_ll_optimizado}")
        sys.exit(0)

    sys.exit(1)


if __name__ == "__main__":
    main()