from __future__ import annotations

from typing import Any, Dict, List, Tuple

from src.optimizer import Optimizer


def aplicar_optimizacion_o3(
    codigo_ir: str, nombre_base: str | None = None
) -> Tuple[str, Dict[str, Any]]:
    """
    Helper compartido para aplicar optimización automática O3.
    Lo reutiliza la Persona B y también puede reutilizarlo la Persona C.
    """
    optimizador = Optimizer()
    return optimizador.optimize_o3(codigo_ir, nombre_base)


def aplicar_passes_en_orden(
    codigo_ir: str, passes: List[str], nombre_base: str | None = None
) -> Tuple[str, Dict[str, Any]]:
    """
    Helper compartido para aplicar passes manuales en el orden indicado.
    """
    optimizador = Optimizer()
    return optimizador.aplicar_passes_manuales(codigo_ir, passes, nombre_base)