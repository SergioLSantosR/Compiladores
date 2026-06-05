import sys
import os
import tempfile
from flask import Flask, render_template, request, jsonify

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipeline import ejecutar_pipeline
from src.ir_manual import (
    aplicar_optimizacion_manual,
    listar_passes,
    reejecutar_ir,
)

app = Flask(__name__)


def ejecutar_fases(codigo: str) -> dict:
    """
    Ejecuta el pipeline completo y devuelve la información que usará la interfaz.
    """
    with tempfile.NamedTemporaryFile(mode="w", suffix=".ml", delete=False) as archivo_temp:
        archivo_temp.write(codigo)
        ruta_temp = archivo_temp.name

    try:
        resultado = ejecutar_pipeline(
            ruta_temp,
            stdout_print=False,
            generar_archivos=False,
        )

        errores = []
        for fase in resultado.fases:
            if fase.estado == "error" and fase.detalle:
                errores.append(fase.detalle)

        return {
            "exito": resultado.exito,
            "fases": [
                {
                    "nombre": fase.nombre,
                    "estado": fase.estado,
                    "tiempo": f"{fase.tiempo_ms:.2f} ms",
                    "detalle": fase.detalle,
                }
                for fase in resultado.fases
            ],
            "errores": errores,
            "tac": resultado.tac,
            "ir": resultado.ir,
            "ir_optimizado": resultado.ir_optimizado,
            "metricas_optimizacion": resultado.metricas_optimizacion,
            "salida": resultado.salida,
            "ir_output": resultado.salida_ir,
            "ir_output_optimizado": resultado.salida_ir_optimizado,
        }

    finally:
        try:
            os.unlink(ruta_temp)
        except OSError:
            pass


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/compilar", methods=["POST"])
def compilar():
    datos = request.get_json()
    codigo = datos.get("codigo", "")

    if not codigo.strip():
        return jsonify({"error": "El código está vacío"}), 400

    resultados = ejecutar_fases(codigo)
    resultados["passes_disponibles"] = listar_passes()
    return jsonify(resultados)


@app.route("/ir_manual", methods=["POST"])
def ir_manual():
    datos = request.get_json() or {}
    codigo_ir = datos.get("ir", "")
    passes = datos.get("passes", [])
    ejecutar = bool(datos.get("ejecutar", True))
    exportar = bool(datos.get("exportar", False))
    nombre_base = datos.get("nombre_base")

    if not codigo_ir.strip():
        return jsonify({"error": "No hay IR para optimizar. Compila primero."}), 400

    if not passes:
        return jsonify({"error": "Selecciona al menos un pass."}), 400

    ruta_exportacion = None
    if exportar:
        with tempfile.NamedTemporaryFile(suffix=".manual.ll", delete=False) as tmp:
            ruta_exportacion = tmp.name

    try:
        resultado = aplicar_optimizacion_manual(
            codigo_ir,
            passes,
            nombre_base=nombre_base,
            ejecutar=ejecutar,
            exportar=exportar,
            ruta_exportacion=ruta_exportacion,
        )
        respuesta = resultado.a_dict()
        if exportar and respuesta.get("archivo_exportado"):
            with open(respuesta["archivo_exportado"], "r", encoding="utf-8") as f:
                respuesta["ir_exportado_contenido"] = f.read()
        return jsonify(respuesta)
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@app.route("/ir_manual/ejecutar", methods=["POST"])
def ir_manual_ejecutar():
    datos = request.get_json() or {}
    codigo_ir = datos.get("ir", "")

    if not codigo_ir.strip():
        return jsonify({"error": "No hay IR para ejecutar."}), 400

    return jsonify(reejecutar_ir(codigo_ir))


@app.route("/passes", methods=["GET"])
def obtener_passes():
    return jsonify({"passes": listar_passes()})


if __name__ == "__main__":
    app.run(debug=True, port=5000)