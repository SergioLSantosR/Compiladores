# src/custom_errors.py — Manejo de errores léxicos y sintácticos
from antlr4.error.ErrorListener import ErrorListener


class ErrorLexico:
    """Representa un error léxico (token no reconocido)."""
    __slots__ = ("linea", "columna", "caracter", "mensaje")

    def __init__(self, linea: int, columna: int, caracter: str, mensaje: str):
        self.linea = linea
        self.columna = columna
        self.caracter = caracter
        self.mensaje = mensaje

    def __str__(self):
        return f"[Error Léxico] Línea {self.linea}, Col {self.columna}: {self.mensaje}"


class ErrorSintactico:
    """Representa un error sintáctico (regla gramatical violada)."""
    __slots__ = ("linea", "columna", "token", "mensaje")

    def __init__(self, linea: int, columna: int, token: str, mensaje: str):
        self.linea = linea
        self.columna = columna
        self.token = token
        self.mensaje = mensaje

    def __str__(self):
        return f"[Error Sintáctico] Línea {self.linea}, Col {self.columna}: {self.mensaje}"


class ColectorErrores(ErrorListener):
    """
    ErrorListener personalizado que separa errores léxicos de sintácticos.

    - Errores léxicos: provienen del Lexer (recognizer sin parser),
      típicamente "token recognition error at: ..."
    - Errores sintácticos: provienen del Parser,
      típicamente "mismatched input ...", "missing ...", "extraneous input ..."
    """

    def __init__(self):
        super().__init__()
        self.errores_lexicos: list[ErrorLexico] = []
        self.errores_sintacticos: list[ErrorSintactico] = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        from antlr4 import Lexer
        if isinstance(recognizer, Lexer):
            caracter = ""
            if "token recognition error at: " in msg:
                caracter = msg.split("token recognition error at: ")[-1].strip("'")
            error = ErrorLexico(
                linea=line,
                columna=column,
                caracter=caracter,
                mensaje=f"Carácter no reconocido: {caracter!r}" if caracter else msg,
            )
            self.errores_lexicos.append(error)
        else:
            token_text = ""
            if offendingSymbol is not None:
                token_text = offendingSymbol.text
            error = ErrorSintactico(
                linea=line,
                columna=column,
                token=token_text,
                mensaje=self._traducir_mensaje(msg),
            )
            self.errores_sintacticos.append(error)

    @staticmethod
    def _traducir_mensaje(msg: str) -> str:
        traducciones = {
            "mismatched input": "entrada inesperada",
            "missing": "falta",
            "extraneous input": "entrada adicional no esperada",
            "no viable alternative at input": "no hay alternativa válida en",
            "expecting": "se esperaba",
        }
        resultado = msg
        for en, es in traducciones.items():
            resultado = resultado.replace(en, es)
        return resultado

    def tiene_errores(self) -> bool:
        return len(self.errores_lexicos) > 0 or len(self.errores_sintacticos) > 0

    def tiene_errores_lexicos(self) -> bool:
        return len(self.errores_lexicos) > 0

    def tiene_errores_sintacticos(self) -> bool:
        return len(self.errores_sintacticos) > 0

    def total_errores(self) -> int:
        return len(self.errores_lexicos) + len(self.errores_sintacticos)

    def reporte(self) -> str:
        lineas = []
        if self.errores_lexicos:
            lineas.append(f"=== Errores Léxicos ({len(self.errores_lexicos)}) ===")
            for err in self.errores_lexicos:
                lineas.append(f"  {err}")
        if self.errores_sintacticos:
            lineas.append(f"=== Errores Sintácticos ({len(self.errores_sintacticos)}) ===")
            for err in self.errores_sintacticos:
                lineas.append(f"  {err}")
        lineas.append(f"\nTotal: {self.total_errores()} error(es) encontrado(s).")
        return "\n".join(lineas)
