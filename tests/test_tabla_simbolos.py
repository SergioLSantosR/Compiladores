# tests/test_tabla_simbolos.py
"""
Pruebas de la TablaSimbolos (Persona 2).
Ejecutar: PYTHONPATH=. .venv/bin/python3 tests/test_tabla_simbolos.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.symbol_table import TablaSimbolos

errores = 0
pruebas = 0

def verificar(condicion, descripcion):
    global errores, pruebas
    pruebas += 1
    if condicion:
        print(f"  [OK] {descripcion}")
    else:
        print(f"  [FALLO] {descripcion}")
        errores += 1


# ============================================================
print("=== 1. Declarar variables en ámbito global ===")
ts = TablaSimbolos()
verificar(ts.profundidad == 1, "Profundidad inicial es 1 (solo global)")

s1 = ts.declarar("x", "int", 1, 0)
verificar(s1 is not None, "Declarar 'x' como int -> éxito")
verificar(s1.nombre == "x" and s1.tipo == "int", "Simbolo tiene nombre='x', tipo='int'")

s2 = ts.declarar("x", "float", 2, 0)
verificar(s2 is None, "Redeclarar 'x' en mismo ámbito -> None (error)")

s3 = ts.declarar("y", "string", 3, 0)
verificar(s3 is not None, "Declarar 'y' como string -> éxito")


# ============================================================
print("\n=== 2. Buscar variables ===")
encontrado = ts.buscar("x")
verificar(encontrado is not None and encontrado.tipo == "int", "Buscar 'x' -> encontrado como int")

no_existe = ts.buscar("z")
verificar(no_existe is None, "Buscar 'z' (no declarada) -> None")


# ============================================================
print("\n=== 3. Scopes: entrar y salir de ámbitos ===")
ts.entrar_ambito()
verificar(ts.profundidad == 2, "Después de entrar_ambito(), profundidad = 2")

s4 = ts.declarar("x", "float", 10, 0)
verificar(s4 is not None, "Declarar 'x' como float en scope local -> éxito (shadowing)")

encontrado_local = ts.buscar("x")
verificar(encontrado_local.tipo == "float", "Buscar 'x' retorna el float del scope local (shadowing)")

encontrado_global_y = ts.buscar("y")
verificar(encontrado_global_y is not None and encontrado_global_y.tipo == "string",
          "Buscar 'y' (solo en global) -> encontrado desde scope local")

ts.salir_ambito()
verificar(ts.profundidad == 1, "Después de salir_ambito(), profundidad = 1")

encontrado_despues = ts.buscar("x")
verificar(encontrado_despues.tipo == "int", "Buscar 'x' después de pop -> vuelve al int global")


# ============================================================
print("\n=== 4. Protección del ámbito global ===")
ts.salir_ambito()
verificar(ts.profundidad == 1, "salir_ambito() extra no elimina el global (profundidad sigue 1)")


# ============================================================
print("\n=== 5. Scopes anidados (función dentro de while) ===")
ts.entrar_ambito()   # simula entrar a función
ts.declarar("a", "int", 20, 0)

ts.entrar_ambito()   # simula entrar a while dentro de la función
ts.declarar("b", "bool", 21, 0)
verificar(ts.profundidad == 3, "Dos entrar_ambito() -> profundidad = 3")

verificar(ts.buscar("a") is not None, "Buscar 'a' desde scope más interno -> encontrado")
verificar(ts.buscar("b") is not None, "Buscar 'b' en scope actual -> encontrado")
verificar(ts.buscar("x") is not None, "Buscar 'x' (global) desde scope anidado -> encontrado")

ts.salir_ambito()
verificar(ts.buscar("b") is None, "Después de salir del while, 'b' ya no existe")
verificar(ts.buscar("a") is not None, "'a' sigue existiendo en el scope de la función")

ts.salir_ambito()


# ============================================================
print("\n=== 6. Funciones ===")
f1 = ts.declarar_funcion("factorial", "int", [("n", "int")], 1, 0)
verificar(f1 is not None, "Declarar función 'factorial' -> éxito")
verificar(f1.tipo_retorno == "int", "Tipo retorno = 'int'")
verificar(f1.parametros == [("n", "int")], "Parámetros = [('n', 'int')]")

f2 = ts.declarar_funcion("factorial", "int", [("n", "int")], 5, 0)
verificar(f2 is None, "Redeclarar 'factorial' -> None (error)")

f3 = ts.declarar_funcion("saludo", "void", [("nombre", "string")], 10, 0)
verificar(f3 is not None, "Declarar función 'saludo' void -> éxito")

encontrada = ts.buscar_funcion("factorial")
verificar(encontrada is not None and encontrada.tipo_retorno == "int",
          "Buscar función 'factorial' -> encontrada")

no_existe_f = ts.buscar_funcion("no_existe")
verificar(no_existe_f is None, "Buscar función 'no_existe' -> None")


# ============================================================
print("\n=== 7. buscar_ambito_actual ===")
ts.entrar_ambito()
ts.declarar("local_var", "int", 30, 0)
verificar(ts.buscar_ambito_actual("local_var") is not None,
          "buscar_ambito_actual('local_var') -> encontrada en scope actual")
verificar(ts.buscar_ambito_actual("x") is None,
          "buscar_ambito_actual('x') -> None (está en global, no en actual)")
verificar(ts.buscar("x") is not None,
          "buscar('x') -> encontrada (busca en todos los ámbitos)")
ts.salir_ambito()


# ============================================================
print("\n=== 8. Representación (__repr__) ===")
print(ts)
verificar("TablaSimbolos" in repr(ts), "__repr__ contiene 'TablaSimbolos'")
verificar("GLOBAL" in repr(ts), "__repr__ contiene 'GLOBAL'")
verificar("FUNCIONES" in repr(ts), "__repr__ contiene 'FUNCIONES'")


# ============================================================
print(f"\n{'='*50}")
print(f"Resultado: {pruebas - errores}/{pruebas} pruebas pasaron")
if errores == 0:
    print("TODAS LAS PRUEBAS PASARON")
else:
    print(f"{errores} prueba(s) fallaron")
    sys.exit(1)
