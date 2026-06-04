import sys
import os
import tempfile
from flask import Flask, render_template, request, jsonify

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipeline import ejecutar_pipeline

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
    return jsonify(resultados)


if __name__ == "__main__":
    app.run(debug=True, port=5000)