# src/generate_ir.py
#!/usr/bin/env python
import sys
import os

# Agregar el directorio raíz al path (dos niveles arriba de src)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from antlr4 import *
from gen.grammar.MiniLangLexer import MiniLangLexer
from gen.grammar.MiniLangParser import MiniLangParser
from src.ir_generator import IRGenerator


def main():
    if len(sys.argv) < 2:
        print("Uso: python -m src.generate_ir <archivo.ml>")
        print("Ejemplo: python -m src.generate_ir tests/test_tac.ml")
        sys.exit(1)
    
    archivo = sys.argv[1]
    input_stream = FileStream(archivo, encoding='utf-8')
    lexer = MiniLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MiniLangParser(token_stream)
    tree = parser.programa()
    
    ir = IRGenerator()
    resultado = ir.visit(tree)
    
    # Guardar en archivo .ll
    archivo_salida = archivo.replace('.ml', '.ll')
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write(resultado)
    
    print(f"✅ LLVM IR generado en: {archivo_salida}")
    print(f"\n📝 Para ejecutar: lli {archivo_salida}")
    print(f"🔧 Para compilar a objeto: llc {archivo_salida} -o output.o")


if __name__ == "__main__":
    main()