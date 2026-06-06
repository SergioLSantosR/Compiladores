# src/binary_generator.py - Generación de Binarios Nativos para MiniLang v4
#
# Implementa la Fase 8 del pipeline:
#   - Compilación para Linux (nativo WSL2)
#   - Compilación cruzada para Windows (.exe desde WSL2)
#
# Requisitos del sistema para Windows:
#   sudo apt-get install gcc-mingw-w64-x86-64
#   sudo apt-get install llvm lld

from __future__ import annotations

import os
import sys
import time
import shutil
import subprocess
import tempfile
import platform
from typing import Any, Optional, Dict, List, Tuple
from pathlib import Path


class BinaryGenerator:
    """Generador de binarios nativos para Linux y Windows desde LLVM IR"""
    
    def __init__(self, verbose: bool = False):
        """
        Inicializa el generador de binarios.
        
        Args:
            verbose: Si es True, muestra la salida de los comandos
        """
        self.verbose = verbose
        self._verificar_herramientas()
        
        # Configuración de targets
        self.targets = {
            "linux": {
                "triple": "x86_64-pc-linux-gnu",
                "linker": "gcc",
                "extension": "",
                "linker_flags": ["-no-pie"],
                "description": "Linux x86_64 (WSL2/Ubuntu)"
            },
            "windows": {
                "triple": "x86_64-pc-windows-gnu",
                "linker": "x86_64-w64-mingw32-gcc",
                "extension": ".exe",
                "linker_flags": [],
                "description": "Windows 64-bit (PE32+)"
            }
        }
    
    def _verificar_herramientas(self) -> None:
        """Verifica que las herramientas necesarias estén instaladas (solo avisa en modo verbose)."""
        if not self.verbose:
            return

        herramientas = {
            "llc": "llc (LLVM compiler)",
            "gcc": "gcc (GNU C compiler)",
            "opt": "opt (LLVM optimizer)"
        }

        for cmd, desc in herramientas.items():
            if shutil.which(cmd) is None:
                print(f"⚠️  Advertencia: {desc} no encontrado", file=sys.stderr)

        if shutil.which('x86_64-w64-mingw32-gcc') is None:
            print("⚠️  Advertencia: MinGW-w64 no encontrado. Para compilar a Windows, instale:", file=sys.stderr)
            print("   sudo apt-get install gcc-mingw-w64-x86-64", file=sys.stderr)
    
    def generate_binary(
        self, 
        ir_code: str, 
        platform: str, 
        output_name: str = "output",
        save_files: bool = False,
        optimization_level: int = 2
    ) -> Optional[str]:
        """
        Genera un binario ejecutable desde código LLVM IR.
        
        Args:
            ir_code: Código LLVM IR (optimizado o no)
            platform: 'linux' o 'windows'
            output_name: Nombre base del archivo de salida
            save_files: Si es True, conserva archivos intermedios (.o, .ll)
            optimization_level: Nivel de optimización para llc (0-3)
            
        Returns:
            Ruta del binario generado o None si falló
        """
        if platform not in self.targets:
            raise ValueError(f"Plataforma no soportada: {platform}. Use 'linux' o 'windows'")
        
        target_config = self.targets[platform]
        output_ext = target_config["extension"]
        output_path = f"{output_name}_{platform}{output_ext}"
        
        # Archivos temporales
        temp_dir = tempfile.mkdtemp(prefix="minilang_")
        ir_file = os.path.join(temp_dir, "input.ll")
        obj_file = os.path.join(temp_dir, "output.o")
        
        try:
            # Guardar IR en archivo temporal
            with open(ir_file, 'w', encoding='utf-8') as f:
                f.write(ir_code)
            
            if self.verbose:
                print(f"  📝 IR guardado en: {ir_file}")
            
            # Paso 1: Compilar IR a objeto
            if not self._compile_to_object(ir_file, obj_file, target_config["triple"], optimization_level):
                return None
            
            if self.verbose:
                print(f"  🔧 Objeto generado: {obj_file}")
            
            # Paso 2: Linkear a ejecutable
            if not self._link_executable(obj_file, output_path, target_config):
                return None
            
            # Paso 3: Hacer ejecutable en Linux
            if platform == "linux":
                os.chmod(output_path, 0o755)
            
            if self.verbose:
                print(f"  ✅ Binario generado: {output_path}")
                if platform == "windows":
                    file_size = os.path.getsize(output_path) / 1024
                    print(f"  📦 Tamaño: {file_size:.1f} KB")
            
            return output_path
            
        except Exception as e:
            print(f"❌ Error generando binario: {e}", file=sys.stderr)
            if self.verbose:
                import traceback
                traceback.print_exc()
            return None
            
        finally:
            # Limpiar archivos temporales (a menos que se pida guardarlos)
            if not save_files and os.path.exists(temp_dir):
                for f in os.listdir(temp_dir):
                    os.unlink(os.path.join(temp_dir, f))
                os.rmdir(temp_dir)
    
    def _compile_to_object(
        self, 
        ir_file: str, 
        obj_file: str, 
        target_triple: str,
        optimization_level: int = 2
    ) -> bool:
        """
        Compila LLVM IR a archivo objeto usando llc.
        """
        # Construir comando llc
        cmd = [
            'llc',
            f'-mtriple={target_triple}',
            f'-O{optimization_level}',
            '-filetype=obj',
            ir_file,
            '-o', obj_file
        ]
        
        if self.verbose:
            print(f"  🔨 Ejecutando: {' '.join(cmd)}")
        
        try:
            result = subprocess.run(
                cmd, 
                capture_output=True, 
                text=True,
                check=True
            )
            if self.verbose and result.stderr:
                print(f"  ℹ️  llc: {result.stderr}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Error en llc: {e.stderr}", file=sys.stderr)
            return False
    
    def _link_executable(
        self, 
        obj_file: str, 
        output_path: str, 
        target_config: Dict
    ) -> bool:
        """
        Linkea el archivo objeto a un ejecutable.
        """
        linker = target_config["linker"]
        linker_flags = target_config.get("linker_flags", [])
        
        cmd = [linker, obj_file, '-o', output_path] + linker_flags
        
        if self.verbose:
            print(f"  🔗 Ejecutando: {' '.join(cmd)}")
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            if self.verbose and result.stderr:
                print(f"  ℹ️  {linker}: {result.stderr}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Error en linker {linker}: {e.stderr}", file=sys.stderr)
            return False
    
    def generate_for_platforms(
        self,
        ir_code: str,
        platforms: List[str],
        output_name: str = "output",
        save_files: bool = False
    ) -> Dict[str, Optional[str]]:
        """
        Genera binarios para múltiples plataformas.
        
        Args:
            ir_code: Código LLVM IR
            platforms: Lista de plataformas ['linux', 'windows']
            output_name: Nombre base de los archivos
            save_files: Conservar archivos intermedios
            
        Returns:
            Diccionario con rutas de binarios generados
        """
        results = {}
        
        for platform_name in platforms:
            if platform_name not in self.targets:
                print(f"⚠️  Plataforma ignorada: {platform_name}", file=sys.stderr)
                continue
            
            print(f"\n📦 Generando binario para {self.targets[platform_name]['description']}...")
            
            binary_path = self.generate_binary(
                ir_code=ir_code,
                platform=platform_name,
                output_name=output_name,
                save_files=save_files
            )
            
            results[platform_name] = binary_path
            if binary_path:
                print(f"  ✅ {platform_name.upper()}: {binary_path}")
            else:
                print(f"  ❌ Falló la generación para {platform_name}")
        
        return results
    
    def ejecutar_binary_linux(self, binary_path: str) -> Tuple[int, str, str]:
        """
        Ejecuta un binario de Linux y captura su salida.
        
        Args:
            binary_path: Ruta del binario Linux
            
        Returns:
            Tupla (código_retorno, stdout, stderr)
        """
        try:
            result = subprocess.run(
                [binary_path],
                capture_output=True,
                text=True,
                check=False
            )
            return result.returncode, result.stdout, result.stderr
        except Exception as e:
            return -1, "", str(e)
    
    def ejecutar_binary_windows(self, binary_path: str, wine_prefix: str = "") -> Tuple[int, str, str]:
        """
        Ejecuta un binario de Windows (puede requerir Wine en WSL2).
        
        Args:
            binary_path: Ruta del binario Windows (.exe)
            wine_prefix: Prefijo de Wine para ejecutar (opcional)
            
        Returns:
            Tupla (código_retorno, stdout, stderr)
        """
        try:
            # En WSL2, podemos usar wine para ejecutar .exe
            if platform.system() == "Linux" and shutil.which("wine"):
                cmd = ["wine", binary_path]
                if wine_prefix:
                    cmd = [f"WINEPREFIX={wine_prefix}"] + cmd
            else:
                # En Windows nativo o si no hay wine
                cmd = [binary_path]
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=False,
                shell=(platform.system() == "Windows")
            )
            return result.returncode, result.stdout, result.stderr
        except Exception as e:
            return -1, "", str(e)
    
    def verificar_binario(self, binary_path: str, platform_name: str) -> bool:
        """
        Verifica que un binario sea válido.
        
        Args:
            binary_path: Ruta del binario
            platform_name: 'linux' o 'windows'
            
        Returns:
            True si el binario parece válido
        """
        if not os.path.exists(binary_path):
            print(f"❌ El archivo no existe: {binary_path}", file=sys.stderr)
            return False
        
        if os.path.getsize(binary_path) == 0:
            print(f"❌ El archivo está vacío: {binary_path}", file=sys.stderr)
            return False
        
        # Verificaciones específicas por plataforma
        if platform_name == "linux":
            # Verificar que sea ejecutable
            if not os.access(binary_path, os.X_OK):
                print(f"⚠️  El archivo no es ejecutable: {binary_path}", file=sys.stderr)
                # Intentar hacerlo ejecutable
                os.chmod(binary_path, 0o755)
        
        elif platform_name == "windows":
            # Verificar extensión .exe
            if not binary_path.endswith('.exe'):
                print(f"⚠️  El archivo no tiene extensión .exe: {binary_path}", file=sys.stderr)
        
        return True


PLATAFORMAS_SOPORTADAS: List[str] = ["linux", "windows"]


def herramientas_disponibles() -> Dict[str, bool]:
    """
    Reporta qué herramientas de compilación están instaladas y qué plataformas
    se pueden generar en la máquina actual.
    """
    def existe(cmd: str) -> bool:
        return shutil.which(cmd) is not None

    tiene_llc = existe("llc")
    return {
        "llc": tiene_llc,
        "gcc": existe("gcc"),
        "opt": existe("opt"),
        "mingw": existe("x86_64-w64-mingw32-gcc"),
        "linux": tiene_llc and existe("gcc"),
        "windows": tiene_llc and existe("x86_64-w64-mingw32-gcc"),
    }


def generar_binarios(
    ir_code: str,
    plataformas: List[str],
    *,
    nombre_base: str = "programa",
    ejecutar: bool = False,
    verbose: bool = False,
) -> Dict[str, Any]:
    """
    Genera binarios nativos para las plataformas pedidas y devuelve información
    estructurada. Es tolerante: si faltan herramientas no lanza excepción, sino
    que reporta el motivo por plataforma.

    Returns:
        dict con:
          - "herramientas": estado de las herramientas del sistema
          - "binarios": {plataforma: {"ok": bool, "ruta"/"error", ...}}
    """
    disponibles = herramientas_disponibles()
    salida: Dict[str, Any] = {"herramientas": disponibles, "binarios": {}}

    generador = BinaryGenerator(verbose=verbose)

    for plataforma in plataformas:
        if plataforma not in PLATAFORMAS_SOPORTADAS:
            salida["binarios"][plataforma] = {
                "ok": False,
                "error": f"Plataforma no soportada: {plataforma}",
                "tiempo_ms": 0.0,
            }
            continue

        if not disponibles.get(plataforma):
            salida["binarios"][plataforma] = {
                "ok": False,
                "error": (
                    f"Faltan herramientas para '{plataforma}' "
                    f"(se requiere llc y el linker correspondiente)."
                ),
                "tiempo_ms": 0.0,
            }
            continue

        t0 = time.perf_counter()
        try:
            ruta = generador.generate_binary(ir_code, plataforma, output_name=nombre_base)
        except Exception as ex:  # pragma: no cover - defensivo
            salida["binarios"][plataforma] = {
                "ok": False,
                "error": str(ex),
                "tiempo_ms": (time.perf_counter() - t0) * 1000,
            }
            continue

        tiempo_ms = (time.perf_counter() - t0) * 1000

        if not ruta or not os.path.exists(ruta):
            salida["binarios"][plataforma] = {
                "ok": False,
                "error": "La generación del binario falló (revise los logs).",
                "tiempo_ms": tiempo_ms,
            }
            continue

        info: Dict[str, Any] = {
            "ok": True,
            "ruta": os.path.abspath(ruta),
            "tamano_bytes": os.path.getsize(ruta),
            "tiempo_ms": tiempo_ms,
        }

        if ejecutar and plataforma == "linux":
            codigo, stdout, stderr = generador.ejecutar_binary_linux(ruta)
            info["ejecucion"] = {"codigo": codigo, "stdout": stdout, "stderr": stderr}

        salida["binarios"][plataforma] = info

    return salida


# Función helper para uso directo
def generar_binario_desde_archivo(
    archivo_ll: str,
    plataforma: str,
    output_name: str = None,
    verbose: bool = True
) -> Optional[str]:
    """
    Función de conveniencia para generar un binario desde un archivo .ll existente.
    
    Args:
        archivo_ll: Ruta del archivo .ll
        plataforma: 'linux' o 'windows'
        output_name: Nombre del binario de salida (opcional)
        verbose: Mostrar información detallada
        
    Returns:
        Ruta del binario generado
    """
    with open(archivo_ll, 'r', encoding='utf-8') as f:
        ir_code = f.read()
    
    if output_name is None:
        output_name = os.path.splitext(archivo_ll)[0]
    
    generator = BinaryGenerator(verbose=verbose)
    return generator.generate_binary(ir_code, plataforma, output_name)


# Ejemplo de uso
if __name__ == "__main__":
    # Este código se ejecuta solo si se llama directamente al archivo
    import sys
    
    print("🔧 BinaryGenerator - Prueba de funcionalidad")
    print("=" * 50)
    
    generator = BinaryGenerator(verbose=True)
    
    # Código IR de ejemplo (programa Hola Mundo)
    ejemplo_ir = '''
; ModuleID = 'test'
source_filename = "test"

declare i32 @printf(i8*, ...)

@.str = private unnamed_addr constant [14 x i8] c"Hola Mundo!\\0A\\00", align 1

define i32 @main() {
entry:
  %call = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([14 x i8], [14 x i8]* @.str, i32 0, i32 0))
  ret i32 0
}
'''
    
    print("\n📝 Generando binario de prueba para Linux...")
    bin_linux = generator.generate_binary(ejemplo_ir, "linux", "test_output")
    
    if bin_linux:
        print(f"\n✅ Binario Linux generado: {bin_linux}")
        print("\nEjecutando el binario:")
        ret, out, err = generator.ejecutar_binary_linux(bin_linux)
        if out:
            print(f"Salida: {out}")
    
    print("\n📝 Generando binario de prueba para Windows...")
    bin_windows = generator.generate_binary(ejemplo_ir, "windows", "test_output")
    
    if bin_windows:
        print(f"\n✅ Binario Windows generado: {bin_windows}")