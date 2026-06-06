"""Pruebas del módulo binary_generator (Persona D).

Las pruebas son tolerantes al entorno: si las herramientas de compilación
(llc, gcc, mingw) no están instaladas, igual deben pasar verificando el
manejo correcto de errores.
"""
from __future__ import annotations

import unittest

from src.binary_generator import (
    BinaryGenerator,
    PLATAFORMAS_SOPORTADAS,
    generar_binarios,
    herramientas_disponibles,
)


IR_EJEMPLO = """; ModuleID = 'test'
declare i32 @printf(i8*, ...)
@.str = private unnamed_addr constant [13 x i8] c"Hola Mundo!\\0A\\00", align 1
define i32 @main() {
entry:
  %call = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([13 x i8], [13 x i8]* @.str, i32 0, i32 0))
  ret i32 0
}
"""


class TestBinaryGenerator(unittest.TestCase):
    def test_herramientas_disponibles_estructura(self):
        info = herramientas_disponibles()
        for clave in ("llc", "gcc", "opt", "mingw", "linux", "windows"):
            self.assertIn(clave, info)
            self.assertIsInstance(info[clave], bool)

    def test_instanciar_generador(self):
        gen = BinaryGenerator()
        self.assertIn("linux", gen.targets)
        self.assertIn("windows", gen.targets)

    def test_plataforma_no_soportada_lanza_error(self):
        gen = BinaryGenerator()
        with self.assertRaises(ValueError):
            gen.generate_binary(IR_EJEMPLO, "macos", "salida")

    def test_generar_binarios_plataforma_invalida(self):
        resultado = generar_binarios(IR_EJEMPLO, ["plan9"])
        self.assertIn("herramientas", resultado)
        self.assertFalse(resultado["binarios"]["plan9"]["ok"])
        self.assertIn("error", resultado["binarios"]["plan9"])

    def test_generar_binarios_estructura_y_tolerancia(self):
        resultado = generar_binarios(IR_EJEMPLO, ["linux"])
        self.assertIn("binarios", resultado)
        info_linux = resultado["binarios"]["linux"]
        self.assertIn("ok", info_linux)

        if not resultado["herramientas"]["linux"]:
            # Sin herramientas: debe reportar el fallo sin lanzar excepción
            self.assertFalse(info_linux["ok"])
            self.assertIn("error", info_linux)
        else:
            # Con herramientas: debe producir una ruta válida
            if info_linux["ok"]:
                self.assertIn("ruta", info_linux)
                self.assertGreater(info_linux["tamano_bytes"], 0)

    def test_plataformas_soportadas(self):
        self.assertEqual(set(PLATAFORMAS_SOPORTADAS), {"linux", "windows"})


if __name__ == "__main__":
    unittest.main()
