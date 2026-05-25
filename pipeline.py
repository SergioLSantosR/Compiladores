# pipeline.py — Orquestador del compilador MiniLang v4
#
# Fases:
#   1. Análisis Léxico     (ANTLR Lexer)
#   2. Análisis Sintáctico (ANTLR Parser)
#   3. Análisis Semántico  (SemanticVisitor + TablaSimbolos)
#   4. Generación TAC      (TACGenerator → archivo .tac)
#   5. Generación LLVM IR  (IRGenerator → archivo .ll)
#   6. Interpretación      (EvalVisitor)
#   7. Optimización O3     (PassManager → archivo .opt.ll)  // NUEVO v4
#   8. Generación Binario  (Target triple → Linux/Windows .exe) // NUEVO v4
#
# Si alguna fase detecta errores se detiene y reporta sin continuar.

from __future__ import annotations

import os
import sys
import time
import subprocess
from pathlib import Path
from typing import Dict, Any, Optional, Tuple

from antlr4 import CommonTokenStream, FileStream

# NUEVO v4: Importar gramática v4
from gen.grammar.gramatica_v4Lexer import gramatica_v4Lexer
from gen.grammar.gramatica_v4Parser import gramatica_v4Parser
from src.custom_errors import ColectorErrores
from src.semantic_visitor import SemanticVisitor
from src.tac_generator import TACGenerator
from src.ir_generator import IRGenerator
from src.EvalVisitorImpl import EvalVisitor
from src.optimizer import Optimizer  # NUEVO v4: Módulo de optimización
from src.binary_generator import BinaryGenerator  # NUEVO v4: Generador de binarios


class FaseResultado:
    __slots__ = ("nombre", "estado", "tiempo_ms", "detalle", "metadata")

    def __init__(self, nombre: str, estado: str, tiempo_ms: float, detalle: str = "", metadata: Dict[str, Any] = None):
        self.nombre = nombre
        self.estado = estado
        self.tiempo_ms = tiempo_ms
        self.detalle = detalle
        self.metadata = metadata or {}

    def __str__(self):
        marca = "✓" if self.estado == "ok" else "✗"
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
        self.ir_optimizado: str = ""  # NUEVO v4: IR optimizado
        self.salida: list[str] = []
        self.archivo_tac: str | None = None
        self.archivo_ll: str | None = None
        self.archivo_ll_opt: str | None = None  # NUEVO v4
        self.binarios_generados: Dict[str, str] = {}  # NUEVO v4: {'linux': 'ruta', 'windows': 'ruta'}
        self.metricas_optimizacion: Dict[str, Any] = {}  # NUEVO v4: Métricas de optimización


def ejecutar_pipeline(
    ruta_archivo: str,
    *,
    stdout_print: bool = True,
    generar_archivos: bool = True,
    optimizar: bool = False,  # NUEVO v4: Activar optimización O3
    plataformas: list[str] = None,  # NUEVO v4: ['linux', 'windows'] o ambas
) -> ResultadoPipeline:
    """
    Ejecuta el pipeline completo de 8 fases.
    
    Args:
        ruta_archivo: Ruta del archivo fuente
        stdout_print: Mostrar salida del programa
        generar_archivos: Generar archivos intermedios (.tac, .ll, etc.)
        optimizar: Aplicar optimización O3 (Fase 7)
        plataformas: Plataformas para generar binarios (Fase 8)
    """
    resultado = ResultadoPipeline()
    base = os.path.splitext(ruta_archivo)[0]
    
    if plataformas is None:
        plataformas = []

    # ── Fase 1: Léxico ─────────────────────────────────────────
    t0 = time.perf_counter()
    input_stream = FileStream(ruta_archivo, encoding="utf-8")
    colector = ColectorErrores()

    # NUEVO v4: Usar lexer de v4
    lexer = gramatica_v4Lexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(colector)

    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    t_lexico = (time.perf_counter() - t0) * 1000

    if colector.tiene_errores_lexicos():
        resultado.fases.append(FaseResultado("1. Análisis Léxico", "error", t_lexico, colector.reporte()))
        return resultado
    resultado.fases.append(FaseResultado("1. Análisis Léxico", "ok", t_lexico))

    # ── Fase 2: Sintáctico ─────────────────────────────────────
    t0 = time.perf_counter()
    # NUEVO v4: Usar parser de v4
    parser = gramatica_v4Parser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(colector)
    tree = parser.programa()
    t_sintactico = (time.perf_counter() - t0) * 1000

    if colector.tiene_errores_sintacticos():
        resultado.fases.append(FaseResultado("2. Análisis Sintáctico", "error", t_sintactico, colector.reporte()))
        return resultado
    resultado.fases.append(FaseResultado("2. Análisis Sintáctico", "ok", t_sintactico))

    # ── Fase 3: Semántico ──────────────────────────────────────
    t0 = time.perf_counter()
    semantico = SemanticVisitor()
    semantico.visit(tree)
    t_semantico = (time.perf_counter() - t0) * 1000

    if semantico.tiene_errores():
        resultado.fases.append(FaseResultado("3. Análisis Semántico", "error", t_semantico, semantico.reporte()))
        return resultado
    resultado.fases.append(FaseResultado("3. Análisis Semántico", "ok", t_semantico))

    # ── Fase 4: Generación TAC ─────────────────────────────────
    t0 = time.perf_counter()
    try:
        tac_gen = TACGenerator()
        resultado.tac = tac_gen.visit(tree) or ""
        t_tac = (time.perf_counter() - t0) * 1000
        resultado.fases.append(FaseResultado("4. Generación TAC", "ok", t_tac))
        if generar_archivos:
            resultado.archivo_tac = base + ".tac"
            with open(resultado.archivo_tac, "w", encoding="utf-8") as f:
                f.write(resultado.tac)
    except Exception as ex:
        t_tac = (time.perf_counter() - t0) * 1000
        resultado.fases.append(FaseResultado("4. Generación TAC", "error", t_tac, str(ex)))
        return resultado

    # ── Fase 5: Generación LLVM IR ─────────────────────────────
    t0 = time.perf_counter()
    try:
        ir_gen = IRGenerator()
        resultado.ir = ir_gen.visit(tree) or ""
        t_ir = (time.perf_counter() - t0) * 1000
        resultado.fases.append(FaseResultado("5. Generación LLVM IR", "ok", t_ir))
        if generar_archivos:
            resultado.archivo_ll = base + ".ll"
            with open(resultado.archivo_ll, "w", encoding="utf-8") as f:
                f.write(resultado.ir)
    except Exception as ex:
        t_ir = (time.perf_counter() - t0) * 1000
        resultado.fases.append(FaseResultado("5. Generación LLVM IR", "error", t_ir, str(ex)))
        return resultado

    # ── Fase 6: Interpretación ─────────────────────────────────
    t0 = time.perf_counter()
    interprete = EvalVisitor(stdout_print=stdout_print)
    try:
        interprete.visit(tree)
        t_ejecucion = (time.perf_counter() - t0) * 1000
        resultado.fases.append(FaseResultado("6. Ejecución (Intérprete)", "ok", t_ejecucion))
    except Exception as ex:
        t_ejecucion = (time.perf_counter() - t0) * 1000
        resultado.fases.append(FaseResultado("6. Ejecución (Intérprete)", "error", t_ejecucion, str(ex)))
        resultado.salida = interprete.salida
        return resultado

    resultado.salida = interprete.salida

    # ── Fase 7: Optimización Automática O3 (NUEVO v4) ──────────
    if optimizar and resultado.ir:
        t0 = time.perf_counter()
        try:
            from src.optimizer import Optimizer
            optimizer = Optimizer()
            
            # Aplicar optimización O3
            resultado.ir_optimizado, resultado.metricas_optimizacion = optimizer.optimize_o3(
                resultado.ir,
                filename=base if generar_archivos else None
            )
            
            if generar_archivos and resultado.ir_optimizado:
                resultado.archivo_ll_opt = base + ".opt.ll"
                with open(resultado.archivo_ll_opt, "w", encoding="utf-8") as f:
                    f.write(resultado.ir_optimizado)
            
            t_optimizacion = (time.perf_counter() - t0) * 1000
            
            # Crear metadata con métricas
            metadata = {
                "instrucciones_antes": resultado.metricas_optimizacion.get("instrucciones_antes", 0),
                "instrucciones_despues": resultado.metricas_optimizacion.get("instrucciones_despues", 0),
                "reduccion_porcentaje": resultado.metricas_optimizacion.get("reduccion_porcentaje", 0),
                "passes_aplicados": resultado.metricas_optimizacion.get("passes_aplicados", [])
            }
            
            detalle = f"Instrucciones: {metadata['instrucciones_antes']} → {metadata['instrucciones_despues']} "
            detalle += f"({metadata['reduccion_porcentaje']:.1f}% reducción)"
            
            resultado.fases.append(FaseResultado(
                "7. Optimización O3", 
                "ok", 
                t_optimizacion, 
                detalle,
                metadata
            ))
        except Exception as ex:
            t_optimizacion = (time.perf_counter() - t0) * 1000
            resultado.fases.append(FaseResultado(
                "7. Optimización O3", 
                "error", 
                t_optimizacion, 
                str(ex)
            ))
            # Nota: La optimización puede fallar pero continuamos (es opcional)
    else:
        resultado.fases.append(FaseResultado(
            "7. Optimización O3", 
            "ok", 
            0.0, 
            "No ejecutada (optimización desactivada)"
        ))

    # ── Fase 8: Generación de Binarios Nativos (NUEVO v4) ──────
    if plataformas and resultado.ir:
        # Usar IR optimizado si está disponible, sino el original
        ir_a_usar = resultado.ir_optimizado if resultado.ir_optimizado else resultado.ir
        
        t0 = time.perf_counter()
        try:
            from src.binary_generator import BinaryGenerator
            binary_gen = BinaryGenerator()
            
            for plataforma in plataformas:
                if plataforma.lower() not in ['linux', 'windows']:
                    continue
                    
                bin_path = binary_gen.generate_binary(
                    ir_code=ir_a_usar,
                    platform=plataforma.lower(),
                    output_name=base,
                    save_file=generar_archivos
                )
                
                if bin_path:
                    resultado.binarios_generados[plataforma.lower()] = bin_path
            
            t_binario = (time.perf_counter() - t0) * 1000
            
            if resultado.binarios_generados:
                detalle = f"Generados: {', '.join(resultado.binarios_generados.keys())}"
                resultado.fases.append(FaseResultado(
                    "8. Generación de Binarios", 
                    "ok", 
                    t_binario, 
                    detalle,
                    {"binarios": resultado.binarios_generados}
                ))
            else:
                resultado.fases.append(FaseResultado(
                    "8. Generación de Binarios", 
                    "error", 
                    t_binario, 
                    "No se generó ningún binario"
                ))
        except Exception as ex:
            t_binario = (time.perf_counter() - t0) * 1000
            resultado.fases.append(FaseResultado(
                "8. Generación de Binarios", 
                "error", 
                t_binario, 
                str(ex)
            ))
    else:
        resultado.fases.append(FaseResultado(
            "8. Generación de Binarios", 
            "ok", 
            0.0, 
            "No ejecutada (sin plataformas seleccionadas)"
        ))

    resultado.exito = True
    return resultado


def _imprimir_fases(resultado: ResultadoPipeline) -> None:
    """Imprime el resumen de fases con formato mejorado"""
    print("\n╔══════════════════════════════════════════════════════════════════╗", file=sys.stderr)
    print("║                    Pipeline MiniLang v4 — Fases                    ║", file=sys.stderr)
    print("╠══════════════════════════════════════════════════════════════════╣", file=sys.stderr)
    
    for fase in resultado.fases:
        print(f"║ {fase}", file=sys.stderr)
    
    # Mostrar métricas de optimización si existen
    fase7 = next((f for f in resultado.fases if "Optimización O3" in f.nombre), None)
    if fase7 and fase7.metadata and fase7.estado == "ok":
        print("╠══════════════════════════════════════════════════════════════════╣", file=sys.stderr)
        print(f"║  📊 Métricas: {fase7.metadata.get('instrucciones_antes', 0)} → {fase7.metadata.get('instrucciones_despues', 0)} instrucciones", file=sys.stderr)
        print(f"║     Reducción: {fase7.metadata.get('reduccion_porcentaje', 0):.1f}%", file=sys.stderr)
        if fase7.metadata.get('passes_aplicados'):
            passes = ', '.join(fase7.metadata['passes_aplicados'][:3])
            print(f"║     Passes: {passes}...", file=sys.stderr)
    
    # Mostrar binarios generados
    fase8 = next((f for f in resultado.fases if "Generación de Binarios" in f.nombre), None)
    if fase8 and fase8.metadata and fase8.estado == "ok":
        print("╠══════════════════════════════════════════════════════════════════╣", file=sys.stderr)
        for platform, path in fase8.metadata.get('binarios', {}).items():
            print(f"║  💾 {platform.upper()}: {path}", file=sys.stderr)
    
    print("╚══════════════════════════════════════════════════════════════════╝", file=sys.stderr)


# ── CLI Mejorada con nuevas opciones ────────────────────────────────────────
def main():
    import argparse

    ap = argparse.ArgumentParser(
        description="MiniLang v4 — Pipeline completo (8 fases: Léxico → Sintáctico → Semántico → TAC → IR → Intérprete → Optimización → Binarios)"
    )
    ap.add_argument("archivo", help="Ruta del archivo fuente (.ml)")
    ap.add_argument("--silencioso", action="store_true", help="No imprimir salida del programa")
    ap.add_argument("--sin-archivos", action="store_true", help="No generar archivos intermedios (.tac, .ll)")
    ap.add_argument("-O", "--optimizar", action="store_true", help="Activar optimización O3 (Fase 7)")
    ap.add_argument("--linux", action="store_true", help="Generar binario para Linux (Fase 8)")
    ap.add_argument("--windows", action="store_true", help="Generar binario para Windows .exe (Fase 8)")
    ap.add_argument("--todas-plataformas", action="store_true", help="Generar binarios para Linux y Windows")
    
    args = ap.parse_args()
    
    # Determinar plataformas
    plataformas = []
    if args.linux:
        plataformas.append("linux")
    if args.windows:
        plataformas.append("windows")
    if args.todas_plataformas:
        plataformas = ["linux", "windows"]
    
    resultado = ejecutar_pipeline(
        args.archivo,
        stdout_print=(not args.silencioso),
        generar_archivos=(not args.sin_archivos),
        optimizar=args.optimizar,
        plataformas=plataformas,
    )

    _imprimir_fases(resultado)

    if resultado.exito:
        print(f"\n✅ Programa compilado y ejecutado correctamente", file=sys.stderr)
        
        # Mostrar archivos generados
        if resultado.archivo_tac:
            print(f"  📄 TAC: {resultado.archivo_tac}", file=sys.stderr)
        if resultado.archivo_ll:
            print(f"  📄 LLVM IR: {resultado.archivo_ll}", file=sys.stderr)
        if resultado.archivo_ll_opt:
            print(f"  📄 LLVM IR Optimizado: {resultado.archivo_ll_opt}", file=sys.stderr)
        
        # Mostrar salida del programa si no es silencioso
        if not args.silencioso and resultado.salida:
            print("\n" + "="*50, file=sys.stderr)
            print("Salida del programa:", file=sys.stderr)
            print("="*50, file=sys.stderr)
            for linea in resultado.salida:
                print(linea, end="")
        
        sys.exit(0)
    else:
        print(f"\n❌ Pipeline fallido", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()