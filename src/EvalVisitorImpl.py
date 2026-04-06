# src/EvalVisitorImpl.py
"""
Compatibilidad: la evaluación pasa por AST + InterpreterVisitor.
Para el flujo completo con fases léxicas/sintácticas use src.pipeline.
"""
from src.ast_builder import AstBuilder
from src.interpreter_visitor import InterpreterVisitor
from src.semantic_visitor import SemanticVisitor


class EvalVisitor:
    """Evalúa el árbol de parsing ANTLR construyendo primero el AST."""

    def __init__(self, stdout_print=True):
        self.stdout_print = stdout_print
        self.memoria = {}
        self.tipos = {}
        self.salida = []

    def visit(self, tree):
        ast = AstBuilder().visit(tree)
        sem = SemanticVisitor()
        sem.analyze(ast)
        if sem.has_errors():
            raise RuntimeError(sem.report())
        interp = InterpreterVisitor(stdout_print=self.stdout_print)
        interp.run(ast)
        self.memoria = dict(interp.memoria)
        self.salida = list(interp.salida)
        self.tipos = {k: interp._tipo_de(v) for k, v in self.memoria.items()}
