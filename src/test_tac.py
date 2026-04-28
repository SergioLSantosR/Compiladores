# src/test_tac.py
import sys
import os

# Agregar el directorio raíz al path de Python
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from antlr4 import *
from gen.grammar.MiniLangLexer import MiniLangLexer
from gen.grammar.MiniLangParser import MiniLangParser
from src.tac_generator import TACGenerator


def main():
    if len(sys.argv) < 2:
        print("Uso: python -m src.test_tac <archivo.ml>")
        print("Ejemplo: python -m src.test_tac tests/test_tac.ml")
        sys.exit(1)
    
    archivo = sys.argv[1]
    input_stream = FileStream(archivo, encoding='utf-8')
    lexer = MiniLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MiniLangParser(token_stream)
    tree = parser.programa()
    
    tac = TACGenerator()
    resultado = tac.visit(tree)
    
    # Guardar en archivo .tac
    archivo_salida = archivo.replace('.ml', '.tac')
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write(resultado)
    
    print(f"✅ TAC generado en: {archivo_salida}")
    print("\n" + "="*50)
    print("CÓDIGO DE TRES DIRECCIONES (TAC)")
    print("="*50)
    print(resultado)
    print("="*50)


if __name__ == "__main__":
    main()