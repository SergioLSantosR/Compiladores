# MiniLang — Compilador con ANTLR y Python

Lenguaje imperativo mínimo con tipos `int` y `bool`, operaciones aritméticas, lógicas y condicionales. Implementado con **ANTLR4** (gramática + generación de analizador) y **Python** (visitor de evaluación y validación).

---

## 1. Diseño del lenguaje

### Características soportadas

| Aspecto | Detalle |
|--------|---------|
| **Tipos** | `int`, `bool` |
| **Estructura** | `program { ... }` con bloque de sentencias |
| **Declaraciones** | `int x;`, `bool b;` (variables deben declararse antes de usarse) |
| **Asignaciones** | `x = expr;` con comprobación de tipos |
| **Aritmética** | `+`, `-`, `*`, `/` (división entera); solo sobre `int` |
| **Relacionales** | `==`, `!=`, `<>`, `<`, `<=`, `>`, `>=`; resultado `bool` |
| **Lógicos** | `&&`, `||`, `!`; solo sobre `bool` |
| **Condicional** | `if (expr) { ... } else { ... }`; condición debe ser `bool` |
| **Salida** | `print(expr);` |

### Ejemplo de programa válido

```text
program {
  int x;
  int y;
  int z;
  x = 10;
  y = 20;
  z = x + y * 2;
  if (z > 30) {
    z = z / 2;
  } else {
    z = z - 5;
  }
  print(z);
}
```

---

```
c
program {
  int n;
  int factorial;
  int i;
  n = 5;
  factorial = 1;
  i = 1;
  
  while (i <= n) {
    factorial = factorial * i;
    i = i + 1;
  }
  
  print(factorial); 
}

```

---

```
program {
  int num;
  int i;
  bool esPrimo;
  
  num = 17;
  esPrimo = true;
  i = 2;
  
  if (num <= 1) {
    esPrimo = false;
  } else {
    while (i < num && esPrimo) {
      if (num % i == 0) {
        esPrimo = false;
      }
      i = i + 1;
    }
  }
  
  if (esPrimo) {
    print(num);
    print("es primo");
  } else {
    print(num);
    print("no es primo");
  }
}

```

---

## 2. Gramática (ANTLR)

La gramática está en **`grammar/MiniLang.g4`**. Todos los nombres de reglas y tokens están en **español** para facilitar el aprendizaje.

- **Reglas léxicas**: palabras clave (`program`, `if`, `else`, `print`, `int`, `bool`, `true`, `false`), operadores, identificadores, literales enteros, espacios y comentarios (`//`, `/* */`).
- **Reglas sintácticas**: `programa` → `bloque`; `bloque` → secuencia de `sentencia`s; sentencias: `declaracionVariable`, `asignacion`, `condicionalSi`, `imprimir`; expresiones (`expresion`) con precedencia completa y asociatividad.

### Niveles de precedencia de expresiones (de mayor a menor)

| Prioridad | Regla | Operadores |
|-----------|-------|------------|
| 1 | `NegacionLogica` | `!` |
| 2 | `MenosUnario` | `-` (unario) |
| 3 | `Parentesis` | `( )` |
| 4 | `MultiplicacionDivision` | `*`, `/` |
| 5 | `SumaResta` | `+`, `-` |
| 6 | `Comparacion` | `<`, `<=`, `>`, `>=` |
| 7 | `Igualdad` | `==`, `!=` / `<>` |
| 8 | `YLogico` | `&&` |
| 9 | `OLogico` | `||` |

Para regenerar el analizador (después de cambiar la gramática):

```bash
antlr4 -Dlanguage=Python3 -visitor -no-listener -o gen/grammar grammar/MiniLang.g4
```

El código generado se integra con Python en `gen/grammar/` (lexer, parser, visitor base).

---

## 3. Generación del analizador léxico y sintáctico

- Se usa **ANTLR4** para generar a partir de `MiniLang.g4` el lexer y el parser en Python.
- El código generado vive en **`gen/grammar/`** y se integra con el resto del proyecto importando `MiniLangLexer`, `MiniLangParser` y `MiniLangVisitor` desde ahí.
- El punto de entrada **`src/run.py`** construye el flujo: `FileStream` → `MiniLangLexer` → `CommonTokenStream` → `MiniLangParser` → árbol de parsing para la regla `programa`.

---

## 4. Implementación del visitor

El **visitor de evaluación** está en **`src/EvalVisitorImpl.py`** (hereda de `MiniLangVisitor` generado por ANTLR).

- **Tabla de símbolos**: `memoria` (nombre → valor) y `tipos` (nombre → `"int"` o `"bool"`).
- **Aritmética**: evaluación de `+`, `-`, `*`, `/` (división entera) con comprobación de tipos `int` y detección de división por cero.
- **Lógicos y relacionales**: evaluación de `==`, `!=`, `<`, `<=`, `>`, `>=`, `&&`, `||`, `!` con comprobación de tipos.
- **Condicionales**: en `visitCondicionalSi` se exige que la condición sea de tipo `bool` antes de elegir la rama then/else.
- **Declaraciones y asignaciones**: comprobación de no redeclaración, uso solo de variables declaradas y coincidencia de tipo en asignaciones.

---

## 5. Validación del programa

- **Entrada**: un archivo de texto (por ejemplo `*.ml`) con el código fuente.
- **Proceso**:
  1. Lectura del archivo y análisis léxico/sintáctico con el parser.
  2. Errores de sintaxis reportados por **`src/error_listener.py`** (listener personalizado); si hay errores, se muestra el reporte y se sale con código de error.
  3. Si la sintaxis es correcta, se recorre el árbol con `EvalVisitor`; se validan tipos y reglas semánticas durante la evaluación.
- **Salida**: se imprimen los resultados de las operaciones (por ejemplo, valores en asignaciones y en `print`). Al final puede mostrarse “Programa válido” y el estado final de variables.

Uso típico:

```bash
python -m src.run examples/programa1.ml
```

---

## 6. Documentación y presentación

- **Diseño del lenguaje**: descrito en la sección 1 y reflejado en la gramática.
- **Gramática**: `grammar/MiniLang.g4`; resumen en la sección 2.
- **Pasos realizados**: generación con ANTLR (sección 3), visitor (sección 4), validación (sección 5).

### Cómo ejecutar y probar

**Requisitos:** Python 3, `antlr4-python3-runtime` (ver `requirements.txt`). Opcional: ANTLR4 CLI para regenerar a partir de la gramática.

```bash
# Crear y activar entorno virtual (recomendado)
python3 -m venv .venv
source .venv/bin/activate   # En Windows: .venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar un programa de ejemplo
python -m src.run examples/programa1.ml

# Ejemplo que contiene errores (división por cero / tipos)
python -m src.run examples/errores.ml
```

El primer comando debe completar la evaluación e imprimir resultados; el segundo debe terminar con mensajes de error de evaluación. Con esto se demuestra el correcto funcionamiento del analizador, del visitor y de la validación semántica.

---

## Estructura del proyecto

Compiladores
├── README.md
├── examples
│   ├── programa1.ml
│   ├── programa2_logicos.ml
│   ├── programa3_relacionales.ml
│   └── programa4_minimo.ml
├── gen
│   ├── __init__.py
│   ├── __pycache__
│   │   └── __init__.cpython-312.pyc
│   └── grammar
│       ├── MiniLang.interp
│       ├── MiniLang.tokens
│       ├── MiniLangLexer.interp
│       ├── MiniLangLexer.py
│       ├── MiniLangLexer.tokens
│       ├── MiniLangListener.py
│       ├── MiniLangParser.py
│       ├── MiniLangVisitor.py
│       ├── __init__.py
│       └── __pycache__
│           ├── MiniLangLexer.cpython-312.pyc
│           ├── MiniLangParser.cpython-312.pyc
│           ├── MiniLangVisitor.cpython-312.pyc
│           └── __init__.cpython-312.pyc
├── grammar
│   └── MiniLang.g4
├── pipeline.py
├── requirements.txt
├── src
│   ├── EvalVisitorImpl.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── EvalVisitorImpl.cpython-312.pyc
│   │   ├── __init__.cpython-312.pyc
│   │   ├── custom_errors.cpython-312.pyc
│   │   ├── generate_ir.cpython-312.pyc
│   │   ├── interpreter_visitor.cpython-312.pyc
│   │   ├── ir_generator.cpython-312.pyc
│   │   ├── run.cpython-312.pyc
│   │   ├── semantic_visitor.cpython-312.pyc
│   │   ├── symbol_table.cpython-312.pyc
│   │   ├── tac_generator.cpython-312.pyc
│   │   └── test_tac.cpython-312.pyc
│   ├── custom_errors.py
│   ├── error_listener.py
│   ├── generate_ir.py
│   ├── interpreter_visitor.py
│   ├── ir_generator.py
│   ├── run.py
│   ├── semantic_visitor.py
│   ├── symbol_table.py
│   ├── tac_generator.py
│   └── test_tac.py
├── tests
│   ├── Ejemplo_break_continue.ml
│   ├── busqueda_arreglos.ml
│   ├── ejemplo_completo.ml
│   ├── error_semantico_1.ml
│   ├── errores.ml
│   ├── errores_sintaxis.ml
│   ├── fibonacci_mientras.ml
│   ├── test_arreglo.ml
│   ├── test_errores_lexicos.ml
│   ├── test_errores_semanticos.ml
│   ├── test_errores_semanticos_2.ml
│   ├── test_errores_sintacticos.ml
│   ├── test_fase2.ml
│   ├── test_fase3.ml
│   ├── test_modulo.ml
│   ├── test_tabla_simbolos.py
│   ├── test_tac.ll
│   ├── test_tac.ml
│   └── test_tac.tac
└── web
    ├── app.py
    ├── static
    │   ├── css
    │   │   └── style.css
    │   └── js
    │       └── app.js
    └── templates
        └── index.html
