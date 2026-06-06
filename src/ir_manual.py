# src/ir_manual.py — Optimización manual de LLVM IR (Persona C)
#
# Selector de passes individuales, aplicación programática en orden,
# comparador diff (líneas +/−/modificadas), re-ejecución del IR
# (reutiliza ir_runner.py) y exportación a .ll.
from __future__ import annotations

import os
from dataclasses import dataclass, field
from difflib import SequenceMatcher, unified_diff
from typing import Any, Dict, List, Optional

from src.ir_runner import ejecutar_ir
from src.optimizer import Optimizer
from src.passes import aplicar_passes_en_orden


PASSES_DISPONIBLES: List[Dict[str, str]] = [
    {"id": "mem2reg", "nombre": "mem2reg", "descripcion": "Promueve allocas a registros SSA"},
    {"id": "instcombine", "nombre": "instcombine", "descripcion": "Combina instrucciones redundantes"},
    {"id": "simplifycfg", "nombre": "simplifycfg", "descripcion": "Simplifica el grafo de flujo de control"},
    {"id": "dce", "nombre": "dce", "descripcion": "Elimina código muerto (Dead Code Elimination)"},
    {"id": "inline", "nombre": "inline", "descripcion": "Inline de funciones pequeñas"},
    {"id": "loop-unroll", "nombre": "loop-unroll", "descripcion": "Desenrollado de bucles"},
    {"id": "constprop", "nombre": "constprop", "descripcion": "Propagación y plegado de constantes"},
    {"id": "gvn", "nombre": "gvn", "descripcion": "Global Value Numbering"},
    {"id": "licm", "nombre": "licm", "descripcion": "Loop Invariant Code Motion"},
]


@dataclass
class ResultadoDiff:
    agregadas: List[Dict[str, Any]] = field(default_factory=list)
    eliminadas: List[Dict[str, Any]] = field(default_factory=list)
    modificadas: List[Dict[str, Any]] = field(default_factory=list)
    sin_cambios: int = 0
    diff_unificado: str = ""

    def resumen(self) -> Dict[str, int]:
        return {
            "agregadas": len(self.agregadas),
            "eliminadas": len(self.eliminadas),
            "modificadas": len(self.modificadas),
            "sin_cambios": self.sin_cambios,
        }

    def a_dict(self) -> Dict[str, Any]:
        return {
            "agregadas": self.agregadas,
            "eliminadas": self.eliminadas,
            "modificadas": self.modificadas,
            "sin_cambios": self.sin_cambios,
            "resumen": self.resumen(),
            "diff_unificado": self.diff_unificado,
        }


@dataclass
class ResultadoOptimizacionManual:
    ir_original: str
    ir_optimizado: str
    passes_solicitados: List[str]
    resultado_por_pass: Dict[str, Any]
    diff: ResultadoDiff
    metricas: Dict[str, Any]
    salida_ejecucion: Optional[Dict[str, Any]] = None
    archivo_exportado: Optional[str] = None

    def a_dict(self) -> Dict[str, Any]:
        return {
            "ir_original": self.ir_original,
            "ir_optimizado": self.ir_optimizado,
            "passes_solicitados": self.passes_solicitados,
            "resultado_por_pass": self.resultado_por_pass,
            "diff": self.diff.a_dict(),
            "metricas": self.metricas,
            "salida_ejecucion": self.salida_ejecucion,
            "archivo_exportado": self.archivo_exportado,
        }


def listar_passes() -> List[Dict[str, str]]:
    """Devuelve la lista de passes LLVM disponibles para selección manual."""
    return list(PASSES_DISPONIBLES)


def validar_passes(passes: List[str]) -> List[str]:
    """Filtra passes desconocidos y conserva el orden de aparición."""
    ids_validos = {p["id"] for p in PASSES_DISPONIBLES}
    return [p for p in passes if p in ids_validos]


def comparar_ir(original: str, optimizado: str) -> ResultadoDiff:
    """
    Compara dos versiones de IR línea a línea.

    Clasifica cada línea como agregada (+), eliminada (−) o modificada (~).
    """
    lineas_orig = original.splitlines()
    lineas_opt = optimizado.splitlines()

    matcher = SequenceMatcher(None, lineas_orig, lineas_opt, autojunk=False)
    diff = ResultadoDiff()

    diff.diff_unificado = "\n".join(
        unified_diff(
            lineas_orig,
            lineas_opt,
            fromfile="original.ll",
            tofile="optimizado.ll",
            lineterm="",
        )
    )

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            diff.sin_cambios += i2 - i1
            continue

        if tag in ("replace", "delete"):
            for idx in range(i1, i2):
                diff.eliminadas.append({"linea": idx + 1, "texto": lineas_orig[idx]})

        if tag in ("replace", "insert"):
            for idx in range(j1, j2):
                diff.agregadas.append({"linea": idx + 1, "texto": lineas_opt[idx]})

        if tag == "replace":
            pares = min(i2 - i1, j2 - j1)
            for k in range(pares):
                texto_antes = lineas_orig[i1 + k]
                texto_despues = lineas_opt[j1 + k]
                if texto_antes != texto_despues:
                    diff.modificadas.append(
                        {
                            "linea_antes": i1 + k + 1,
                            "linea_despues": j1 + k + 1,
                            "antes": texto_antes,
                            "despues": texto_despues,
                        }
                    )

    return diff


def _calcular_metricas(ir_original: str, ir_optimizado: str) -> Dict[str, Any]:
    optimizador = Optimizer()
    antes = optimizador._analizar_ir(ir_original)
    despues = optimizador._analizar_ir(ir_optimizado)

    reduccion = 0.0
    if antes["total_instrucciones"] > 0:
        reduccion = (
            1 - despues["total_instrucciones"] / antes["total_instrucciones"]
        ) * 100

    return {
        "instrucciones_antes": antes["total_instrucciones"],
        "instrucciones_despues": despues["total_instrucciones"],
        "reduccion_porcentaje": reduccion,
        "basic_blocks_antes": antes["basic_blocks"],
        "basic_blocks_despues": despues["basic_blocks"],
        "function_calls_antes": antes["function_calls"],
        "function_calls_despues": despues["function_calls"],
    }


def aplicar_optimizacion_manual(
    codigo_ir: str,
    passes: List[str],
    *,
    nombre_base: str | None = None,
    ejecutar: bool = False,
    exportar: bool = False,
    ruta_exportacion: str | None = None,
) -> ResultadoOptimizacionManual:
    """
    Aplica los passes seleccionados en orden sobre el IR dado.

    Args:
        codigo_ir: LLVM IR sin optimizar.
        passes: Lista ordenada de nombres de passes.
        nombre_base: Prefijo opcional para archivos generados.
        ejecutar: Si True, re-ejecuta el IR optimizado con ir_runner.
        exportar: Si True, escribe el IR optimizado a disco.
        ruta_exportacion: Ruta del .ll de salida (requerida si exportar=True).
    """
    passes_validos = validar_passes(passes)
    ir_optimizado, resultado_por_pass = aplicar_passes_en_orden(
        codigo_ir, passes_validos, nombre_base
    )

    diff = comparar_ir(codigo_ir, ir_optimizado)
    metricas = _calcular_metricas(codigo_ir, ir_optimizado)

    salida_ejecucion = None
    if ejecutar and ir_optimizado.strip():
        salida_ejecucion = ejecutar_ir(ir_optimizado)

    archivo_exportado = None
    if exportar:
        destino = ruta_exportacion or (
            f"{nombre_base}.manual.ll" if nombre_base else None
        )
        if destino:
            archivo_exportado = exportar_ll(ir_optimizado, destino)

    return ResultadoOptimizacionManual(
        ir_original=codigo_ir,
        ir_optimizado=ir_optimizado,
        passes_solicitados=passes_validos,
        resultado_por_pass=resultado_por_pass,
        diff=diff,
        metricas=metricas,
        salida_ejecucion=salida_ejecucion,
        archivo_exportado=archivo_exportado,
    )


def exportar_ll(codigo_ir: str, ruta_salida: str) -> str:
    """Escribe el IR a un archivo .ll y devuelve la ruta absoluta."""
    ruta_abs = os.path.abspath(ruta_salida)
    os.makedirs(os.path.dirname(ruta_abs) or ".", exist_ok=True)
    with open(ruta_abs, "w", encoding="utf-8") as archivo:
        archivo.write(codigo_ir)
    return ruta_abs


def reejecutar_ir(codigo_ir: str) -> Dict[str, Any]:
    """Re-ejecuta el IR optimizado (wrapper sobre ir_runner.ejecutar_ir)."""
    return ejecutar_ir(codigo_ir)
