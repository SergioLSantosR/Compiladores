"""Pruebas del módulo ir_manual (Persona C)."""
from __future__ import annotations

import os
import tempfile
import unittest

from src.ir_manual import (
    aplicar_optimizacion_manual,
    comparar_ir,
    exportar_ll,
    listar_passes,
    validar_passes,
)


IR_EJEMPLO = """; Ejemplo mínimo
define i32 @main() {
entry:
  %x = alloca i32
  store i32 10, i32* %x
  %y = add i32 5, 3
  %z = add i32 0, 0
  %a = load i32, i32* %x
  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.fmt.int, i32 0, i32 0), i32 %a)
  ret i32 0
}

declare i32 @printf(i8*, ...)
@.fmt.int = private unnamed_addr constant [4 x i8] c"%d\\0A\\00"
"""


class TestIRManual(unittest.TestCase):
    def test_listar_passes(self):
        passes = listar_passes()
        self.assertGreaterEqual(len(passes), 5)
        ids = {p["id"] for p in passes}
        self.assertIn("dce", ids)
        self.assertIn("constprop", ids)

    def test_validar_passes_filtra_desconocidos(self):
        resultado = validar_passes(["dce", "invalido", "constprop"])
        self.assertEqual(resultado, ["dce", "constprop"])

    def test_comparar_ir_detecta_cambios(self):
        original = "linea1\nlinea2\nlinea3\n"
        optimizado = "linea1\nlinea2_mod\nlinea4\n"
        diff = comparar_ir(original, optimizado)
        resumen = diff.resumen()
        self.assertGreater(resumen["modificadas"] + resumen["agregadas"] + resumen["eliminadas"], 0)
        self.assertTrue(diff.diff_unificado)

    def test_aplicar_optimizacion_manual(self):
        resultado = aplicar_optimizacion_manual(
            IR_EJEMPLO,
            ["constprop", "dce"],
            ejecutar=False,
        )
        self.assertTrue(resultado.ir_optimizado)
        self.assertEqual(resultado.passes_solicitados, ["constprop", "dce"])
        self.assertIn("instrucciones_antes", resultado.metricas)

    def test_exportar_ll(self):
        with tempfile.TemporaryDirectory() as tmp:
            ruta = os.path.join(tmp, "salida.ll")
            ruta_abs = exportar_ll(IR_EJEMPLO, ruta)
            self.assertTrue(os.path.isfile(ruta_abs))
            with open(ruta_abs, encoding="utf-8") as f:
                contenido = f.read()
            self.assertIn("define i32 @main", contenido)


if __name__ == "__main__":
    unittest.main()
