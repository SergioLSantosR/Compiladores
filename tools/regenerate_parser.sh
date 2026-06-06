#!/usr/bin/env bash
#
# regenerate_parser.sh — Regenera el lexer/parser/visitor de ANTLR para la
# gramática MiniLang v4 dentro de gen/grammar/.
#
# El directorio gen/ está en .gitignore (los archivos generados por ANTLR no
# se versionan), por lo que cada integrante debe ejecutar este script tras
# clonar el repo o cambiar la gramática.
#
# Uso:
#   ./tools/regenerate_parser.sh
#
# Variables de entorno opcionales:
#   ANTLR_JAR  Ruta al jar de ANTLR (por defecto se autodetecta).
#
# Requisitos: java (JRE 11+) y el jar antlr-4.13.x-complete.jar.
set -euo pipefail

# Ubicarse en la raíz del proyecto (un nivel arriba de tools/).
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT_DIR"

GRAMMAR="grammar/gramatica_v4.g4"
OUT_DIR="gen/grammar"

# 1) Localizar el jar de ANTLR.
if [[ -z "${ANTLR_JAR:-}" ]]; then
  for cand in \
    /usr/local/lib/antlr/antlr-4.13.1-complete.jar \
    /usr/local/lib/antlr-4.13.1-complete.jar \
    /usr/share/java/antlr-4.13.1-complete.jar \
    "$ROOT_DIR/tools/antlr-4.13.1-complete.jar" \
    /usr/local/lib/antlr/antlr-*-complete.jar; do
    if [[ -f "$cand" ]]; then
      ANTLR_JAR="$cand"
      break
    fi
  done
fi

if [[ -z "${ANTLR_JAR:-}" || ! -f "$ANTLR_JAR" ]]; then
  echo "ERROR: no se encontró el jar de ANTLR." >&2
  echo "Descárgalo (https://www.antlr.org/download/antlr-4.13.1-complete.jar)" >&2
  echo "y exporta su ruta:  export ANTLR_JAR=/ruta/antlr-4.13.1-complete.jar" >&2
  exit 1
fi

echo "Usando ANTLR: $ANTLR_JAR"
echo "Generando parser para $GRAMMAR ..."

# 2) Generar. ANTLR replica la ruta de la gramática bajo -o, por lo que los
#    archivos quedan en gen/grammar/grammar/; luego los movemos un nivel arriba.
java -jar "$ANTLR_JAR" -Dlanguage=Python3 -visitor -no-listener -o "$OUT_DIR" "$GRAMMAR"

if [[ -d "$OUT_DIR/grammar" ]]; then
  mv -f "$OUT_DIR"/grammar/gramatica_v4* "$OUT_DIR"/
  rmdir "$OUT_DIR/grammar" 2>/dev/null || true
fi

echo "Listo. Archivos generados en $OUT_DIR/:"
ls -1 "$OUT_DIR"/gramatica_v4* 2>/dev/null || true
