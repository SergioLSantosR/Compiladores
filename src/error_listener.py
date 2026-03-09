# src/error_listener.py
from antlr4.error.ErrorListener import ErrorListener

class VerboseErrorListener(ErrorListener):
    def __init__(self):
        super(VerboseErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        text = f"[Error de sintaxis] Línea {line}, Col {column}: {msg}"
        self.errors.append(text)

    def has_errors(self):
        return len(self.errors) > 0

    def report(self):
        return "\n".join(self.errors)
