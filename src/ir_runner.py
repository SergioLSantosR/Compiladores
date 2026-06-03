# src/ir_runner.py — Ejecuta LLVM IR y captura la salida de los print()
#
# Estrategia de ejecución del .ll (Fase 6 del enunciado):
#   1. Si el comando `lli` está disponible en el sistema, se usa directamente
#      (es lo que pide el enunciado: "ejecutable con lli archivo.ll").
#   2. Si `lli` no está instalado, se ejecuta el IR en proceso con el motor
#      JIT (MCJIT) de llvmlite. Esto hace que el panel de ejecución del IR
#      funcione siempre, sin depender de herramientas externas de LLVM.
from __future__ import annotations

import ctypes
import os
import shutil
import subprocess
import tempfile

from llvmlite import binding as llvm

_INICIALIZADO = False


def _cargar_libc():
    """Devuelve un handle a libc para poder hacer fflush() del stdio de C."""
    import ctypes.util

    for nombre in (None, "c", "System"):
        try:
            ruta = ctypes.util.find_library(nombre) if nombre else None
            return ctypes.CDLL(ruta)
        except OSError:
            continue
    return None


def _inicializar_llvm() -> None:
    # En llvmlite >= 0.44 la inicialización de LLVM es automática y estas
    # llamadas fueron deprecadas/eliminadas; las invocamos de forma defensiva
    # para mantener compatibilidad con versiones anteriores.
    global _INICIALIZADO
    if _INICIALIZADO:
        return
    for fn in ("initialize", "initialize_native_target", "initialize_native_asmprinter"):
        metodo = getattr(llvm, fn, None)
        if metodo is None:
            continue
        try:
            metodo()
        except Exception:  # noqa: BLE001
            pass
    _INICIALIZADO = True


def ejecutar_ir(ir_code: str, *, timeout: float = 5.0) -> dict:
    """Ejecuta el IR y retorna {'salida', 'error', 'motor', 'disponible'}."""
    resultado = {"salida": "", "error": "", "motor": "", "disponible": False}
    if not ir_code or not ir_code.strip():
        return resultado

    # 1) Intentar con lli (lo que pide el enunciado)
    if shutil.which("lli"):
        return _ejecutar_con_lli(ir_code, timeout=timeout)

    # 2) Fallback: motor JIT de llvmlite
    return _ejecutar_con_jit(ir_code)


def _ejecutar_con_lli(ir_code: str, *, timeout: float) -> dict:
    resultado = {"salida": "", "error": "", "motor": "lli", "disponible": True}
    ll_path = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", suffix=".ll", delete=False) as f:
            f.write(ir_code)
            ll_path = f.name
        proc = subprocess.run(
            ["lli", ll_path], capture_output=True, text=True, timeout=timeout
        )
        resultado["salida"] = proc.stdout
        resultado["error"] = proc.stderr
    except subprocess.TimeoutExpired:
        resultado["error"] = f"Tiempo de ejecución agotado ({timeout}s)."
    except Exception as ex:  # noqa: BLE001
        resultado["error"] = str(ex)
    finally:
        if ll_path:
            try:
                os.unlink(ll_path)
            except OSError:
                pass
    return resultado


def _ejecutar_con_jit(ir_code: str) -> dict:
    resultado = {"salida": "", "error": "", "motor": "llvmlite-jit", "disponible": True}
    _inicializar_llvm()

    # llvmlite asume el triple nativo; quitamos el triple/datalayout del módulo
    # para evitar conflictos con la máquina destino al hacer JIT.
    ir_saneado = _quitar_triple(ir_code)

    engine = None
    fd_guardado = None
    tmp_out = None
    try:
        mod = llvm.parse_assembly(ir_saneado)
        mod.verify()

        target = llvm.Target.from_default_triple()
        target_machine = target.create_target_machine()
        engine = llvm.create_mcjit_compiler(mod, target_machine)
        engine.finalize_object()
        engine.run_static_constructors()

        func_ptr = engine.get_function_address("main")
        cfunc = ctypes.CFUNCTYPE(ctypes.c_int32)(func_ptr)

        # Capturar lo que main imprime por stdout (fd 1) a nivel de C.
        # Importante: printf usa el buffer de stdio de libc, así que hay que
        # hacer fflush(NULL) antes de restaurar el descriptor, o la salida se
        # vaciaría al terminal real en lugar de quedar capturada.
        import sys

        libc = _cargar_libc()
        sys.stdout.flush()
        if libc is not None:
            libc.fflush(None)
        fd_guardado = os.dup(1)
        tmp_out = tempfile.TemporaryFile(mode="w+b")
        os.dup2(tmp_out.fileno(), 1)
        try:
            cfunc()
        finally:
            if libc is not None:
                libc.fflush(None)
            sys.stdout.flush()
            os.dup2(fd_guardado, 1)

        tmp_out.seek(0)
        resultado["salida"] = tmp_out.read().decode("utf-8", errors="replace")
    except Exception as ex:  # noqa: BLE001
        resultado["error"] = str(ex)
    finally:
        if fd_guardado is not None:
            try:
                os.dup2(fd_guardado, 1)
                os.close(fd_guardado)
            except OSError:
                pass
        if tmp_out is not None:
            tmp_out.close()
    return resultado


def _quitar_triple(ir_code: str) -> str:
    lineas = []
    for linea in ir_code.splitlines():
        despojada = linea.strip()
        if despojada.startswith("target triple") or despojada.startswith("target datalayout"):
            continue
        lineas.append(linea)
    return "\n".join(lineas)
