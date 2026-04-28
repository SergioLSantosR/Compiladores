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
from gen.grammar.MiniLangLexer import MiniLangLexer
from gen.grammar.MiniLangParser import MiniLangParser
from src.custom_errors import ColectorErrores
from src.semantic_visitor import SemanticVisitor
from src.EvalVisitorImpl import EvalVisitor
from src.tac_generator import TACGenerator
from src.ir_generator import IRGenerator

app = Flask(__name__)


def ejecutar_fases(codigo):
    """Ejecuta todas las fases del compilador y retorna resultados"""
    resultados = {
        "exito": False,
        "fases": [],
        "errores": [],
        "tac": "",
        "ir": "",
        "salida": []
    }
    
    # Crear un archivo temporal con el código
    with tempfile.NamedTemporaryFile(mode='w', suffix='.ml', delete=False) as f:
        f.write(codigo)
        archivo_temp = f.name
    
    try:
        # Fase 1 y 2: Léxico y Sintáctico
        tiempo_inicio = time.time()
        input_stream = FileStream(archivo_temp, encoding='utf-8')
        colector = ColectorErrores()
        lexer = MiniLangLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(colector)
        token_stream = CommonTokenStream(lexer)
        parser = MiniLangParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(colector)
        tree = parser.programa()
        tiempo_lexico_sintactico = (time.time() - tiempo_inicio) * 1000
        
        if colector.tiene_errores():
            resultados["fases"].append({
                "nombre": "Análisis Léxico/Sintáctico",
                "estado": "error",
                "tiempo": f"{tiempo_lexico_sintactico:.2f} ms",
                "detalle": colector.reporte()
            })
            resultados["errores"] = [colector.reporte()]
            return resultados
        else:
            resultados["fases"].append({
                "nombre": "Análisis Léxico/Sintáctico",
                "estado": "ok",
                "tiempo": f"{tiempo_lexico_sintactico:.2f} ms"
            })
        
        # Fase 3: Semántico
        tiempo_inicio = time.time()
        semantico = SemanticVisitor()
        semantico.visit(tree)
        tiempo_semantico = (time.time() - tiempo_inicio) * 1000
        
        if semantico.tiene_errores():
            resultados["fases"].append({
                "nombre": "Análisis Semántico",
                "estado": "error",
                "tiempo": f"{tiempo_semantico:.2f} ms",
                "detalle": semantico.reporte()
            })
            resultados["errores"] = [semantico.reporte()]
            return resultados
        else:
            resultados["fases"].append({
                "nombre": "Análisis Semántico",
                "estado": "ok",
                "tiempo": f"{tiempo_semantico:.2f} ms"
            })
        
        # Fase 4: Generación TAC
        tiempo_inicio = time.time()
        tac_gen = TACGenerator()
        tac_resultado = tac_gen.visit(tree)
        tiempo_tac = (time.time() - tiempo_inicio) * 1000
        resultados["tac"] = tac_resultado
        resultados["fases"].append({
            "nombre": "Generación TAC",
            "estado": "ok",
            "tiempo": f"{tiempo_tac:.2f} ms"
        })
        
        # Fase 5: Generación LLVM IR
        tiempo_inicio = time.time()
        ir_gen = IRGenerator()
        ir_resultado = ir_gen.visit(tree)
        tiempo_ir = (time.time() - tiempo_inicio) * 1000
        resultados["ir"] = ir_resultado
        resultados["fases"].append({
            "nombre": "Generación LLVM IR",
            "estado": "ok",
            "tiempo": f"{tiempo_ir:.2f} ms"
        })
        
        # Fase 6: Ejecución (Interpretación)
        tiempo_inicio = time.time()
        interprete = EvalVisitor(stdout_print=False)
        interprete.visit(tree)
        tiempo_ejecucion = (time.time() - tiempo_inicio) * 1000
        resultados["salida"] = interprete.salida
        resultados["fases"].append({
            "nombre": "Ejecución",
            "estado": "ok",
            "tiempo": f"{tiempo_ejecucion:.2f} ms"
        })
        
        resultados["exito"] = True
        
    except Exception as e:
        resultados["fases"].append({
            "nombre": "Error",
            "estado": "error",
            "tiempo": "0 ms",
            "detalle": str(e)
        })
        resultados["errores"] = [str(e)]
    
    finally:
        # Limpiar archivo temporal
        try:
            os.unlink(archivo_temp)
        except:
            pass
    
    return resultados


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
    app.run(debug=True, port=5000)
    