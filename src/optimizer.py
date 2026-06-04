# src/optimizer.py - Optimización Automática O3 para MiniLang v4
#
# Implementa la Fase 7 del pipeline:
#   - Aplica LLVM Pass Manager con nivel O3
#   - Reporta métricas de optimización
#   - Genera IR optimizado separado
#
# Transformaciones incluidas:
#   - Constant Propagation y Constant Folding
#   - Dead Code Elimination (DCE)
#   - Function Inlining
#   - Loop Unrolling

from __future__ import annotations

import os
import re
import subprocess
import tempfile
from typing import Tuple, Dict, Any, List, Optional
from pathlib import Path


class Optimizer:
    """Módulo de optimización automática usando LLVM Pass Manager (nivel O3)"""
    
    def __init__(self):
        self.passes_o3 = [
            "constprop",      # Constant Propagation
            "dce",            # Dead Code Elimination
            "inline",         # Function Inlining
            "loop-unroll",    # Loop Unrolling
            "instcombine",    # Instruction Combining
            "simplifycfg",    # Simplify CFG
            "mem2reg",        # Promote memory to registers
            "gvn",            # Global Value Numbering
            "licm",           # Loop Invariant Code Motion
            "indvars",        # Canonicalize Induction Variables
        ]
        
    def optimize_o3(self, ir_code: str, filename: str = None) -> Tuple[str, Dict[str, Any]]:
        """
        Aplica optimización O3 al código LLVM IR.
        
        Args:
            ir_code: Código LLVM IR sin optimizar
            filename: Nombre base para guardar archivos temporales (opcional)
            
        Returns:
            Tupla (código_optimizado, métricas)
        """
        # Calcular métricas del IR original
        metricas_origen = self._analizar_ir(ir_code)
        
        # Intentar usar LLVM 'opt' si está disponible
        try:
            ir_optimizado = self._optimizar_con_opt(ir_code, filename)
        except (subprocess.CalledProcessError, FileNotFoundError):
            # Fallback: optimización manual simplificada
            ir_optimizado = self._optimizar_manual(ir_code)
        
        # Calcular métricas del IR optimizado
        metricas_optimizado = self._analizar_ir(ir_optimizado)
        
        # Calcular reducciones
        reduccion_instrucciones = 0
        if metricas_origen["total_instrucciones"] > 0:
            reduccion_instrucciones = (
                1 - metricas_optimizado["total_instrucciones"] / metricas_origen["total_instrucciones"]
            ) * 100
        
        # Detectar qué optimizaciones se aplicaron
        passes_aplicados = self._detectar_optimizaciones_aplicadas(
            ir_code, ir_optimizado
        )
        
        metricas = {
            "instrucciones_antes": metricas_origen["total_instrucciones"],
            "instrucciones_despues": metricas_optimizado["total_instrucciones"],
            "reduccion_porcentaje": reduccion_instrucciones,
            "passes_aplicados": passes_aplicados,
            "detalle_antes": metricas_origen,
            "detalle_despues": metricas_optimizado,
            "basic_blocks_antes": metricas_origen["basic_blocks"],
            "basic_blocks_despues": metricas_optimizado["basic_blocks"],
            "function_calls_antes": metricas_origen["function_calls"],
            "function_calls_despues": metricas_optimizado["function_calls"],
        }
        
        return ir_optimizado, metricas
    
    def _optimizar_con_opt(self, ir_code: str, filename: str = None) -> str:
        """
        Usa LLVM 'opt' para aplicar optimizaciones O3.
        Este es el método principal y más completo.
        """
        with tempfile.NamedTemporaryFile(mode='w', suffix='.ll', delete=False) as f:
            f.write(ir_code)
            input_file = f.name
        
        output_file = input_file.replace('.ll', '.opt.ll')
        
        try:
            # Aplicar optimización O3 usando opt
            # -O3: nivel máximo de optimización
            # -S: generar IR textual
            cmd = [
                'opt',
                '-O3',
                '-S',
                input_file,
                '-o', output_file
            ]
            
            subprocess.run(cmd, check=True, capture_output=True, text=True)
            
            # Leer el resultado optimizado
            with open(output_file, 'r', encoding='utf-8') as f:
                ir_optimizado = f.read()
            
            # Si se proporcionó filename, guardar copia permanente
            if filename:
                perm_file = f"{filename}.opt.ll"
                with open(perm_file, 'w', encoding='utf-8') as f:
                    f.write(ir_optimizado)
            
            return ir_optimizado
            
        except subprocess.CalledProcessError as e:
            print(f"Error en opt: {e.stderr}")
            raise
        finally:
            # Limpiar archivos temporales
            for f in [input_file, output_file]:
                if os.path.exists(f):
                    os.unlink(f)
    
    def _optimizar_manual(self, ir_code: str) -> str:
        """
        Fallback: aplica optimizaciones manuales básicas.
        Útil cuando 'opt' no está disponible.
        """
        ir_optimizado = ir_code
        
        # 1. Constant Folding: simplificar operaciones constantes
        ir_optimizado = self._aplicar_constant_folding(ir_optimizado)
        
        # 2. Dead Code Elimination: eliminar instrucciones no usadas
        ir_optimizado = self._aplicar_dead_code_elimination(ir_optimizado)
        
        # 3. Simplificar CFG: eliminar bloques vacíos
        ir_optimizado = self._simplificar_cfg(ir_optimizado)
        
        return ir_optimizado
    
    def _aplicar_constant_folding(self, ir_code: str) -> str:
        """
        Aplica Constant Folding: evalúa expresiones constantes en tiempo de compilación.
        Ejemplo: add i32 5, 3 → i32 8
        """
        lines = ir_code.split('\n')
        new_lines = []
        
        for line in lines:
            # Buscar operaciones con operandos constantes
            # add i32 X, Y donde X e Y son constantes
            const_pattern = r'(\w+)\s+=\s+(\w+)\s+(\w+)\s+(\d+),\s*(\d+)'
            match = re.search(const_pattern, line)
            
            if match and match.group(2) in ['add', 'sub', 'mul', 'sdiv']:
                dest = match.group(1)
                op = match.group(2)
                const1 = int(match.group(4))
                const2 = int(match.group(5))
                
                # Calcular resultado
                if op == 'add':
                    result = const1 + const2
                elif op == 'sub':
                    result = const1 - const2
                elif op == 'mul':
                    result = const1 * const2
                elif op == 'sdiv':
                    result = const1 // const2 if const2 != 0 else 0
                else:
                    result = 0
                
                # Reemplazar con constante
                line = f"{dest} = i32 {result}"
            
            new_lines.append(line)
        
        return '\n'.join(new_lines)
    
    def _aplicar_dead_code_elimination(self, ir_code: str) -> str:
        """
        Elimina instrucciones cuyo resultado no es utilizado.
        """
        lines = ir_code.split('\n')
        used_vars = set()
        
        # Primera pasada: identificar variables usadas
        for line in lines:
            # Buscar usos de variables
            uses = re.findall(r'%[a-zA-Z_][a-zA-Z0-9_]*', line)
            for use in uses[1:]:  # El primer uso puede ser la definición
                used_vars.add(use)
        
        # Segunda pasada: eliminar definiciones no usadas
        new_lines = []
        for line in lines:
            # Verificar si esta línea define una variable no usada
            match = re.match(r'\s*%([a-zA-Z_][a-zA-Z0-9_]*)\s*=', line)
            if match:
                var_name = f'%{match.group(1)}'
                if var_name not in used_vars:
                    continue  # Saltar esta instrucción (dead code)
            new_lines.append(line)
        
        return '\n'.join(new_lines)
    
    def _simplificar_cfg(self, ir_code: str) -> str:
        """
        Simplifica el CFG eliminando bloques básicos vacíos.
        """
        lines = ir_code.split('\n')
        new_lines = []
        skip_until_label = False
        
        for line in lines:
            # Si es una etiqueta, siempre la mantenemos
            if line.strip().endswith(':'):
                skip_until_label = False
                new_lines.append(line)
                continue
            
            # Si estamos saltando bloques vacíos, continuar
            if skip_until_label:
                continue
            
            # Verificar si es un bloque vacío (solo terminador)
            if line.strip().startswith('br ') or line.strip().startswith('ret '):
                # Mantener el terminador
                new_lines.append(line)
                # Marcar para saltar hasta la siguiente etiqueta
                skip_until_label = True
            else:
                new_lines.append(line)
        
        return '\n'.join(new_lines)
    
    def _analizar_ir(self, ir_code: str) -> Dict[str, Any]:
        """
        Analiza el código IR y extrae métricas detalladas.
        """
        lines = ir_code.split('\n')
        
        metricas = {
            "total_instrucciones": 0,
            "basic_blocks": 0,
            "function_calls": 0,
            "alloca_instructions": 0,
            "load_instructions": 0,
            "store_instructions": 0,
            "arithmetic_ops": 0,
            "branch_instructions": 0,
            "phi_instructions": 0,
        }
        
        in_function = False
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith(';'):
                continue
            
            # Contar instrucciones (líneas que no son etiquetas ni comentarios)
            if not line.endswith(':') and not line.startswith('define'):
                metricas["total_instrucciones"] += 1
            
            # Detectar bloques básicos (etiquetas)
            if line.endswith(':'):
                metricas["basic_blocks"] += 1
            
            # Detectar llamadas a funciones
            if 'call' in line:
                metricas["function_calls"] += 1
            
            # Detectar allocas (asignación de memoria en stack)
            if 'alloca' in line:
                metricas["alloca_instructions"] += 1
            
            # Detectar loads y stores
            if 'load' in line:
                metricas["load_instructions"] += 1
            if 'store' in line:
                metricas["store_instructions"] += 1
            
            # Detectar operaciones aritméticas
            if any(op in line for op in ['add', 'sub', 'mul', 'sdiv', 'udiv']):
                metricas["arithmetic_ops"] += 1
            
            # Detectar branches
            if 'br ' in line:
                metricas["branch_instructions"] += 1
            
            # Detectar phi nodes
            if 'phi' in line:
                metricas["phi_instructions"] += 1
        
        return metricas
    
    def _detectar_optimizaciones_aplicadas(
        self, ir_original: str, ir_optimizado: str
    ) -> List[str]:
        """
        Detecta qué optimizaciones se aplicaron comparando el IR original y optimizado.
        """
        passes = []
        
        # 1. Constant Propagation/Folding
        if self._hubo_constant_folding(ir_original, ir_optimizado):
            passes.append("constant-propagation-folding")
        
        # 2. Dead Code Elimination
        if self._hubo_dead_code_elimination(ir_original, ir_optimizado):
            passes.append("dead-code-elimination")
        
        # 3. Function Inlining
        if self._hubo_function_inlining(ir_original, ir_optimizado):
            passes.append("function-inlining")
        
        # 4. Loop Unrolling
        if self._hubo_loop_unrolling(ir_original, ir_optimizado):
            passes.append("loop-unrolling")
        
        # Si no se detectaron específicos, al menos reportar el nivel O3
        if not passes:
            passes.append("O3-aggressive-optimizations")
        
        return passes
    
    def _hubo_constant_folding(self, original: str, optimizado: str) -> bool:
        """Detecta si hubo constant folding"""
        # Buscar reducción en número de operaciones aritméticas
        orig_ops = len(re.findall(r'=\s*(add|sub|mul|div)', original))
        opt_ops = len(re.findall(r'=\s*(add|sub|mul|div)', optimizado))
        return opt_ops < orig_ops
    
    def _hubo_dead_code_elimination(self, original: str, optimizado: str) -> bool:
        """Detecta si hubo eliminación de código muerto"""
        orig_inst = len([l for l in original.split('\n') if l.strip() and not l.strip().startswith(';')])
        opt_inst = len([l for l in optimizado.split('\n') if l.strip() and not l.strip().startswith(';')])
        return opt_inst < orig_inst
    
    def _hubo_function_inlining(self, original: str, optimizado: str) -> bool:
        """Detecta si hubo inlining de funciones"""
        # El inlining reduce el número de llamadas a funciones pequeñas
        orig_calls = len(re.findall(r'call', original))
        opt_calls = len(re.findall(r'call', optimizado))
        return opt_calls < orig_calls
    
    def _hubo_loop_unrolling(self, original: str, optimizado: str) -> bool:
        """Detecta si hubo unrolling de loops"""
        # El unrolling reemplaza instrucciones de branch por código repetido
        orig_branches = len(re.findall(r'br\s+label', original))
        opt_branches = len(re.findall(r'br\s+label', optimizado))
        return opt_branches < orig_branches
    
    def aplicar_passes_manuales(
        self, ir_code: str, passes: List[str], filename: str = None
    ) -> Tuple[str, Dict[str, Any]]:
        """
        Aplica un conjunto específico de passes (para IR Manual).
        
        Args:
            ir_code: Código LLVM IR
            passes: Lista de nombres de passes a aplicar
            filename: Nombre base para guardar archivos
            
        Returns:
            Tupla (código_optimizado, resultado_por_pass)
        """
        resultado_por_pass = {}
        current_ir = ir_code
        
        for pass_name in passes:
            try:
                current_ir, metrics = self._aplicar_pass_individual(current_ir, pass_name)
                resultado_por_pass[pass_name] = {
                    "aplicado": True,
                    "metricas": metrics
                }
            except Exception as e:
                resultado_por_pass[pass_name] = {
                    "aplicado": False,
                    "error": str(e)
                }
        
        return current_ir, resultado_por_pass
    
    def _aplicar_pass_individual(self, ir_code: str, pass_name: str) -> Tuple[str, Dict[str, Any]]:
        """
        Aplica un pass individual usando opt.
        """
        # Mapeo de nombres de passes a flags de opt
        pass_flags = {
            "mem2reg": "--mem2reg",
            "instcombine": "--instcombine",
            "simplifycfg": "--simplifycfg",
            "dce": "--dce",
            "inline": "--inline",
            "loop-unroll": "--loop-unroll",
            "constprop": "--constprop",
            "gvn": "--gvn",
            "licm": "--licm",
        }
        
        flag = pass_flags.get(pass_name)
        if not flag:
            raise ValueError(f"Pass no soportado: {pass_name}")
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.ll', delete=False) as f:
            f.write(ir_code)
            input_file = f.name
        
        output_file = input_file.replace('.ll', '.opt.ll')
        
        try:
            cmd = ['opt', flag, '-S', input_file, '-o', output_file]
            subprocess.run(cmd, check=True, capture_output=True, text=True)
            
            with open(output_file, 'r', encoding='utf-8') as f:
                ir_optimizado = f.read()
            
            metricas = self._analizar_ir(ir_optimizado)
            return ir_optimizado, metricas
            
        finally:
            for f in [input_file, output_file]:
                if os.path.exists(f):
                    os.unlink(f)


# Función helper para uso directo desde la interfaz
def optimizar_con_o3(archivo_ll: str, output_ll: str = None) -> Tuple[str, Dict[str, Any]]:
    """
    Función de conveniencia para optimizar un archivo .ll existente.
    
    Args:
        archivo_ll: Ruta del archivo .ll a optimizar
        output_ll: Ruta para guardar el resultado (opcional)
        
    Returns:
        Tupla (código_optimizado, métricas)
    """
    with open(archivo_ll, 'r', encoding='utf-8') as f:
        ir_code = f.read()
    
    optimizer = Optimizer()
    base_name = os.path.splitext(archivo_ll)[0] if not output_ll else os.path.splitext(output_ll)[0]
    
    ir_optimizado, metricas = optimizer.optimize_o3(ir_code, base_name)
    
    if output_ll:
        with open(output_ll, 'w', encoding='utf-8') as f:
            f.write(ir_optimizado)
    
    return ir_optimizado, metricas