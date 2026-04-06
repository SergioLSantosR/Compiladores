# src/custom_errors.py
import re
from antlr4.error.ErrorListener import ErrorListener


def _columna_usuario(columna_antlr: int) -> int:
    return columna_antlr + 1


def _extraer_simbolo_lexico(msg: str, offending_symbol) -> str:
    m = re.search(r"token recognition error at:\s*(.+)$", msg)
    if m:
        s = m.group(1).strip()
        if (s.startswith("'") and s.endswith("'")) or (s.startswith('"') and s.endswith('"')):
            return s[1:-1]
        return s
    if offending_symbol is not None and getattr(offending_symbol, "text", None):
        return offending_symbol.text
    return msg


def _simplificar_esperado(esperado_raw: str) -> str:
    m = re.search(r"'([^']*)'", esperado_raw)
    if m:
        return f"'{m.group(1)}'"
    m2 = re.match(r"(\S+)", esperado_raw)
    if m2:
        return f"'{m2.group(1)}'"
    return esperado_raw


def _formatear_mensaje_parser(msg: str, offending_symbol) -> str:
    patrones = [
        (r"mismatched input '([^']*)' expecting (.+)$", "std"),
        (r"extraneous input '([^']*)' expecting (.+)$", "std"),
        (r"missing '([^']*)' at '([^']*)'$", "missing"),
    ]
    for pat, kind in patrones:
        m = re.search(pat, msg)
        if not m:
            continue
        if kind == "missing":
            return f"Se esperaba '{m.group(1)}' pero se encontró '{m.group(2)}'"
        encontrado, esperado_raw = m.group(1), m.group(2).strip()
        return f"Se esperaba {_simplificar_esperado(esperado_raw)} pero se encontró '{encontrado}'"

    if offending_symbol is not None and getattr(offending_symbol, "text", None):
        t = offending_symbol.text
        return f"Se esperaba (revisar gramática) pero se encontró '{t}'"
    return msg


class _ErrorCollector(ErrorListener):
    """Base: acumula mensajes y permite has_errors / report."""

    __slots__ = ("errors",)

    def __init__(self):
        super().__init__()
        self.errors: list[str] = []

    def has_errors(self) -> bool:
        return bool(self.errors)

    def report(self) -> str:
        return "\n".join(self.errors)


class LexerErrorListener(_ErrorCollector):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        sim = _extraer_simbolo_lexico(msg, offendingSymbol)
        c = _columna_usuario(column)
        self.errors.append(
            f"[Error Léxico] Línea {line}, Columna {c}: Símbolo no reconocido '{sim}'"
        )


class ParserErrorListener(_ErrorCollector):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        c = _columna_usuario(column)
        det = _formatear_mensaje_parser(msg, offendingSymbol)
        self.errors.append(f"[Error Sintáctico] Línea {line}, Columna {c}: {det}")
