# web/app.py
import sys
import os
import time
import subprocess
import tempfile
from flask import Flask, render_template, request, jsonify

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from antlr4 import *
from gen.grammar.gramatica_v4Lexer import gramatica_v4Lexer
from gen.grammar.gramatica_v4Parser import gramatica_v4Parser
from src.custom_errors import ColectorErrores
from src.semantic_visitor import SemanticVisitor
from src.EvalVisitorImpl import EvalVisitor
from src.tac_generator import TACGenerator
from src.ir_generator import IRGenerator

app = Flask(__name__)


def ejecutar_fases(codigo):
    """Ejecuta todas las 6 fases del compilador y retorna resultados"""
    resultados = {
        "exito": False,
        "fases": [],
        "errores": [],
        "tac": "",
        "ir": "",
        "salida": []
    }

    with tempfile.NamedTemporaryFile(mode='w', suffix='.ml', delete=False, encoding='utf-8') as f:
        f.write(codigo)
        archivo_temp = f.name

    try:
        # Fase 1: Léxico
        t0 = time.perf_counter()
        input_stream = FileStream(archivo_temp, encoding='utf-8')
        colector = ColectorErrores()
        lexer = gramatica_v4Lexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(colector)
        token_stream = CommonTokenStream(lexer)
        token_stream.fill()
        t_lexico = (time.perf_counter() - t0) * 1000

        if colector.tiene_errores_lexicos():
            resultados["fases"].append({
                "nombre": "Análisis Léxico",
                "estado": "error",
                "tiempo": f"{t_lexico:.2f} ms",
                "detalle": colector.reporte()
            })
            resultados["errores"] = [colector.reporte()]
            return resultados
        resultados["fases"].append({
            "nombre": "Análisis Léxico",
            "estado": "ok",
            "tiempo": f"{t_lexico:.2f} ms"
        })

        # Fase 2: Sintáctico
        t0 = time.perf_counter()
        parser = gramatica_v4Parser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(colector)
        tree = parser.programa()
        t_sintactico = (time.perf_counter() - t0) * 1000

        if colector.tiene_errores_sintacticos():
            resultados["fases"].append({
                "nombre": "Análisis Sintáctico",
                "estado": "error",
                "tiempo": f"{t_sintactico:.2f} ms",
                "detalle": colector.reporte()
            })
            resultados["errores"] = [colector.reporte()]
            return resultados
        resultados["fases"].append({
            "nombre": "Análisis Sintáctico",
            "estado": "ok",
            "tiempo": f"{t_sintactico:.2f} ms"
        })

        # Fase 3: Semántico
        t0 = time.perf_counter()
        semantico = SemanticVisitor()
        semantico.visit(tree)
        t_semantico = (time.perf_counter() - t0) * 1000

        if semantico.tiene_errores():
            resultados["fases"].append({
                "nombre": "Análisis Semántico",
                "estado": "error",
                "tiempo": f"{t_semantico:.2f} ms",
                "detalle": semantico.reporte()
            })
            resultados["errores"] = [semantico.reporte()]
            return resultados
        resultados["fases"].append({
            "nombre": "Análisis Semántico",
            "estado": "ok",
            "tiempo": f"{t_semantico:.2f} ms"
        })

        # Fase 4: Generación TAC
        t0 = time.perf_counter()
        tac_gen = TACGenerator()
        tac_resultado = tac_gen.visit(tree)
        t_tac = (time.perf_counter() - t0) * 1000
        resultados["tac"] = tac_resultado or ""
        resultados["fases"].append({
            "nombre": "Generación TAC",
            "estado": "ok",
            "tiempo": f"{t_tac:.2f} ms"
        })

        # Fase 5: Generación LLVM IR
        t0 = time.perf_counter()
        ir_gen = IRGenerator()
        ir_resultado = ir_gen.visit(tree)
        t_ir = (time.perf_counter() - t0) * 1000
        resultados["ir"] = ir_resultado or ""
        resultados["fases"].append({
            "nombre": "Generación LLVM IR",
            "estado": "ok",
            "tiempo": f"{t_ir:.2f} ms"
        })

        # Fase 6: Ejecución (Interpretación)
        t0 = time.perf_counter()
        interprete = EvalVisitor(stdout_print=False)
        interprete.visit(tree)
        t_ejecucion = (time.perf_counter() - t0) * 1000
        resultados["salida"] = interprete.salida
        resultados["fases"].append({
            "nombre": "Ejecución (Intérprete)",
            "estado": "ok",
            "tiempo": f"{t_ejecucion:.2f} ms"
        })

        resultados["exito"] = True

        # Intentar ejecutar el IR con lli
        resultados["ir_output"] = _ejecutar_ll(resultados["ir"])

    except Exception as e:
        import traceback
        error_detallado = traceback.format_exc()
        resultados["fases"].append({
            "nombre": "Error de Ejecución",
            "estado": "error",
            "tiempo": "0 ms",
            "detalle": str(e)
        })
        resultados["errores"] = [str(e), error_detallado]

    finally:
        try:
            os.unlink(archivo_temp)
        except OSError:
            pass

    return resultados


def _ejecutar_ll(ir_code: str) -> dict:
    """Escribe el IR a un archivo temporal y ejecuta con lli."""
    resultado = {"salida": "", "error": "", "disponible": False}
    if not ir_code:
        return resultado
    try:
        with tempfile.NamedTemporaryFile(mode="w", suffix=".ll", delete=False, encoding='utf-8') as f:
            f.write(ir_code)
            ll_path = f.name
        proc = subprocess.run(
            ["lli", ll_path],
            capture_output=True, text=True, timeout=5,
        )
        resultado["disponible"] = True
        resultado["salida"] = proc.stdout
        resultado["error"] = proc.stderr
    except FileNotFoundError:
        resultado["error"] = "lli no encontrado. Instala LLVM para ejecutar el IR."
    except subprocess.TimeoutExpired:
        resultado["error"] = "Tiempo de ejecución agotado (5s)."
    except Exception as ex:
        resultado["error"] = str(ex)
    finally:
        try:
            os.unlink(ll_path)
        except (OSError, NameError):
            pass
    return resultado


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/compilar', methods=['POST'])
def compilar():
    data = request.get_json()
    codigo = data.get('codigo', '')
    
    if not codigo.strip():
        return jsonify({"error": "El código está vacío"}), 400
    
    resultados = ejecutar_fases(codigo)
    return jsonify(resultados)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)