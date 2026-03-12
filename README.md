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
  
  print(factorial);  // Debería imprimir 120
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

La gramática está en **`grammar/MiniLang.g4`**.

- **Reglas léxicas**: palabras clave (`program`, `if`, `else`, `print`, `int`, `bool`, `true`, `false`), operadores, identificadores, literales enteros, espacios y comentarios (`//`, `/* */`).
- **Reglas sintácticas**: `program` → `block`; `block` → secuencia de sentencias; sentencias: declaraciones, asignaciones, `if`, `print`; expresiones con precedencia y asociatividad (unarios, `*`/`/`, `+`/`-`, relacionales, `&&`/`||`).

Para regenerar el analizador (después de cambiar la gramática):

```bash
antlr4 -Dlanguage=Python3 -visitor -no-listener -o gen/grammar grammar/MiniLang.g4
```

El código generado se integra con Python en `gen/grammar/` (lexer, parser, visitor base).

---

## 3. Generación del analizador léxico y sintáctico

- Se usa **ANTLR4** para generar a partir de `MiniLang.g4` el lexer y el parser en Python.
- El código generado vive en **`gen/grammar/`** y se integra con el resto del proyecto importando `MiniLangLexer`, `MiniLangParser` y `MiniLangVisitor` desde ahí.
- El punto de entrada **`src/run.py`** construye el flujo: `FileStream` → `MiniLangLexer` → `CommonTokenStream` → `MiniLangParser` → árbol de parsing para la regla `program`.

---

## 4. Implementación del visitor

El **visitor de evaluación** está en **`src/EvalVisitorImpl.py`** (hereda de `MiniLangVisitor` generado por ANTLR).

- **Tabla de símbolos**: `memory` (nombre → valor) y `types` (nombre → `"int"` o `"bool"`).
- **Aritmética**: evaluación de `+`, `-`, `*`, `/` (división entera) con comprobación de tipos `int` y detección de división por cero.
- **Lógicos y relacionales**: evaluación de `==`, `!=`, `<`, `<=`, `>`, `>=`, `&&`, `||`, `!` con comprobación de tipos.
- **Condicionales**: en `visitIfStmt` se exige que la condición sea de tipo `bool` antes de elegir la rama then/else.
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

```text
Compiladores/
├── grammar/
│   └── MiniLang.g4          # Gramática ANTLR (léxica y sintáctica)
├── gen/
│   └── grammar/             # Código generado por ANTLR (lexer, parser, visitor base)
├── src/
│   ├── run.py               # Entrada: lee archivo, parsea, evalúa
│   ├── EvalVisitorImpl.py   # Visitor de evaluación y validación
│   └── error_listener.py    # Listener de errores de sintaxis
├── examples/
│   ├── programa1.ml         # Programa de ejemplo válido
│   └── errores.ml           # Programa con errores (pruebas)
├── requirements.txt
```
