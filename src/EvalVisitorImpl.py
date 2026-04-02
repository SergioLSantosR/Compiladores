# src/EvalVisitorImpl.py
from antlr4 import *
from gen.grammar.MiniLangParser import MiniLangParser
from gen.grammar.MiniLangVisitor import MiniLangVisitor

class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

class EvalVisitor(MiniLangVisitor):
    def __init__(self, stdout_print=True):
        super().__init__()
        self.global_memory = {}
        self.global_types = {}
        self.scope_stack = []
        self.functions = {}
        self.current_function = None
        self.return_value = None
        self.stdout_print = stdout_print
        self.output = []

    # ---- Manejo de ámbitos ----
    def push_scope(self):
        self.scope_stack.append(({}, {}))

    def pop_scope(self):
        self.scope_stack.pop()

    def current_memory(self):
        if self.scope_stack:
            return self.scope_stack[-1][0]
        return self.global_memory

    def current_types(self):
        if self.scope_stack:
            return self.scope_stack[-1][1]
        return self.global_types

    def declare_variable(self, name, typ, ctx):
        types = self.current_types()
        if name in types:
            raise RuntimeError(f"Variable '{name}' ya declarada en este ámbito (línea {ctx.start.line})")
        types[name] = typ
        if typ == 'int':
            self.current_memory()[name] = 0
        elif typ == 'float':
            self.current_memory()[name] = 0.0
        elif typ == 'bool':
            self.current_memory()[name] = False
        elif typ == 'string':
            self.current_memory()[name] = ""

    def get_variable(self, name, ctx):
        for memory, _ in reversed(self.scope_stack):
            if name in memory:
                return memory[name]
        if name in self.global_memory:
            return self.global_memory[name]
        raise RuntimeError(f"Variable '{name}' no definida (línea {ctx.start.line})")

    def set_variable(self, name, value, ctx):
        for i in range(len(self.scope_stack)-1, -1, -1):
            if name in self.scope_stack[i][0]:
                self.scope_stack[i][0][name] = value
                return
        if name in self.global_memory:
            self.global_memory[name] = value
            return
        raise RuntimeError(f"Variable '{name}' no definida (línea {ctx.start.line})")

    def get_type(self, name):
        for _, types in reversed(self.scope_stack):
            if name in types:
                return types[name]
        return self.global_types.get(name)

    # ---- Utilidades ----
    def _type_of(self, value):
        if isinstance(value, bool):
            return "bool"
        elif isinstance(value, int):
            return "int"
        elif isinstance(value, float):
            return "float"
        elif isinstance(value, str):
            return "string"
        return "desconocido"

    def _ensure_type(self, expected, value, ctx, op_desc=""):
        actual = self._type_of(value)
        if expected != actual:
            raise RuntimeError(f"Error de tipos en {op_desc} (línea {ctx.start.line}): se esperaba {expected}, obtuvo {actual}")

    def _println(self, text):
        if self.stdout_print:
            print(text)
        self.output.append(str(text))

    # ---- Program y funciones ----
    def visitProgram(self, ctx: MiniLangParser.ProgramContext):
        # Registrar funciones (todas, antes y después del grupo)
        for func_ctx in ctx.funcionDecl():
            self.visit(func_ctx)
        # Ejecutar bloque principal
        self.push_scope()
        self.visit(ctx.grupo())
        self.pop_scope()
        return None

    def visitFuncionDecl(self, ctx: MiniLangParser.FuncionDeclContext):
        name = ctx.ID().getText()
        # Determinar tipo de retorno (void si no hay tipo)
        tipo_retorno = "void"
        if ctx.tipo():
            tipo_retorno = ctx.tipo().getText()
        elif ctx.VOID():
            tipo_retorno = "void"
        params = []
        if ctx.parametros():
            for p in ctx.parametros().parametro():
                param_name = p.ID().getText()
                param_type = p.tipo().getText()
                params.append((param_name, param_type))
        self.functions[name] = (params, ctx.grupo(), tipo_retorno)
        return None

    def visitFuncCall(self, ctx: MiniLangParser.FuncCallContext):
        name = ctx.ID().getText()
        if name not in self.functions:
            raise RuntimeError(f"Función '{name}' no definida (línea {ctx.start.line})")
        params, body, ret_type = self.functions[name]
        # Evaluar argumentos
        args = []
        if ctx.expr():
            for arg_ctx in ctx.expr():
                args.append(self.visit(arg_ctx))
        if len(args) != len(params):
            raise RuntimeError(f"Número incorrecto de argumentos para función '{name}' (línea {ctx.start.line})")
        # Verificar tipos de argumentos
        for (pname, ptype), arg_val in zip(params, args):
            self._ensure_type(ptype, arg_val, ctx, f"parámetro '{pname}'")
        # Nuevo ámbito
        self.push_scope()
        for (pname, ptype), arg_val in zip(params, args):
            self.declare_variable(pname, ptype, ctx)
            self.set_variable(pname, arg_val, ctx)
        old_func = self.current_function
        self.current_function = name
        self.return_value = None
        try:
            self.visit(body)
        except ReturnException as e:
            self.return_value = e.value
        self.current_function = old_func
        self.pop_scope()
        if ret_type != "void":
            if self.return_value is None:
                raise RuntimeError(f"Función '{name}' debe retornar un valor")
            self._ensure_type(ret_type, self.return_value, ctx, f"retorno de '{name}'")
            return self.return_value
        return None

    def visitSentenciaRetorna(self, ctx: MiniLangParser.SentenciaRetornaContext):
        if self.current_function is None:
            raise RuntimeError(f"return fuera de función (línea {ctx.start.line})")
        value = None
        if ctx.expr():
            value = self.visit(ctx.expr())
        raise ReturnException(value)

    # ---- Grupo y sentencias ----
    def visitGrupo(self, ctx: MiniLangParser.GrupoContext):
        self.push_scope()
        for s in ctx.sentencia():
            self.visit(s)
        self.pop_scope()
        return None

    def visitDeclaraVariable(self, ctx: MiniLangParser.DeclaraVariableContext):
        typ = ctx.tipo().getText()
        name = ctx.ID().getText()
        self.declare_variable(name, typ, ctx)
        return None

    def visitSentenciaAsigna(self, ctx: MiniLangParser.SentenciaAsignaContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        var_type = self.get_type(name)
        if var_type is None:
            raise RuntimeError(f"Variable '{name}' no declarada (línea {ctx.start.line})")
        self._ensure_type(var_type, value, ctx, "asignación")
        self.set_variable(name, value, ctx)
        self._println(f"{name} = {value}")
        return None

    def visitSentenciaSI(self, ctx: MiniLangParser.SentenciaSIContext):
        cond = self.visit(ctx.expr())
        self._ensure_type("bool", cond, ctx, "condición if")
        if cond:
            self.visit(ctx.grupo(0))
        elif ctx.SINO():
            self.visit(ctx.grupo(1))
        return None

    def visitSentenciaImprime(self, ctx: MiniLangParser.SentenciaImprimeContext):
        value = self.visit(ctx.expr())
        self._println(value)
        return None

    def visitSentenciaMientras(self, ctx: MiniLangParser.SentenciaMientrasContext):
        while True:
            cond = self.visit(ctx.expr())
            self._ensure_type("bool", cond, ctx, "condición while")
            if not cond:
                break
            self.visit(ctx.grupo())
        return None

    # ---- Nuevos métodos para el bucle for ----
    def visitInicializacionPara(self, ctx: MiniLangParser.InicializacionParaContext):
        typ = ctx.tipo().getText()
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.declare_variable(name, typ, ctx)
        self.set_variable(name, value, ctx)
        return None

    def visitAsignacionPara(self, ctx: MiniLangParser.AsignacionParaContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        var_type = self.get_type(name)
        if var_type is None:
            raise RuntimeError(f"Variable '{name}' no declarada (línea {ctx.start.line})")
        self._ensure_type(var_type, value, ctx, "asignación en for")
        self.set_variable(name, value, ctx)
        return None

    def visitActualizacionPara(self, ctx: MiniLangParser.ActualizacionParaContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        var_type = self.get_type(name)
        if var_type is None:
            raise RuntimeError(f"Variable '{name}' no declarada (línea {ctx.start.line})")
        self._ensure_type(var_type, value, ctx, "actualización en for")
        self.set_variable(name, value, ctx)
        return None

    def visitSentenciaPara(self, ctx: MiniLangParser.SentenciaParaContext):
        # Inicialización
        if ctx.inicializacionPara():
            self.visit(ctx.inicializacionPara())
        elif ctx.asignacionPara():
            self.visit(ctx.asignacionPara())
        # Bucle
        while True:
            if ctx.cond:
                cond = self.visit(ctx.cond)
                self._ensure_type("bool", cond, ctx, "condición for")
                if not cond:
                    break
            self.visit(ctx.grupo())
            if ctx.actualizacionPara():
                self.visit(ctx.actualizacionPara())
        return None

    # ---- Llamada a funciones void como sentencia ----
    def visitSentenciaLlamada(self, ctx: MiniLangParser.SentenciaLlamadaContext):
        name = ctx.ID().getText()
        if name not in self.functions:
            raise RuntimeError(f"Función '{name}' no definida (línea {ctx.start.line})")
        params, body, ret_type = self.functions[name]
        args = []
        if ctx.expr():
            for arg_ctx in ctx.expr():
                args.append(self.visit(arg_ctx))
        if len(args) != len(params):
            raise RuntimeError(f"Número incorrecto de argumentos para función '{name}' (línea {ctx.start.line})")
        for (pname, ptype), arg_val in zip(params, args):
            self._ensure_type(ptype, arg_val, ctx, f"parámetro '{pname}'")
        # Nuevo ámbito
        self.push_scope()
        for (pname, ptype), arg_val in zip(params, args):
            self.declare_variable(pname, ptype, ctx)
            self.set_variable(pname, arg_val, ctx)
        old_func = self.current_function
        self.current_function = name
        self.return_value = None
        try:
            self.visit(body)
        except ReturnException as e:
            self.return_value = e.value
        self.current_function = old_func
        self.pop_scope()
        # No se retorna nada (void)
        return None

    # ---- Expresiones ----
    def visitUnaryNot(self, ctx):
        v = self.visit(ctx.expr())
        self._ensure_type("bool", v, ctx, "not")
        return not v

    def visitUnaryMinus(self, ctx):
        v = self.visit(ctx.expr())
        t = self._type_of(v)
        if t == "int":
            return -v
        elif t == "float":
            return -v
        else:
            raise RuntimeError(f"No se puede negar tipo {t}")

    def visitParen(self, ctx):
        return self.visit(ctx.expr())

    def visitMulDiv(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)
        t1 = self._type_of(l)
        t2 = self._type_of(r)
        if t1 == "int" and t2 == "int":
            if ctx.op.type == MiniLangParser.MULTI:
                return l * r
            else:
                if r == 0:
                    raise RuntimeError("División por cero")
                return l // r
        elif (t1 == "int" and t2 == "float") or (t1 == "float" and t2 == "int") or (t1 == "float" and t2 == "float"):
            lf = float(l) if t1 == "int" else l
            rf = float(r) if t2 == "int" else r
            if ctx.op.type == MiniLangParser.MULTI:
                return lf * rf
            else:
                if rf == 0.0:
                    raise RuntimeError("División por cero")
                return lf / rf
        else:
            raise RuntimeError(f"Tipos incompatibles para * o /: {t1} y {t2}")

    def visitAddSub(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)
        t1 = self._type_of(l)
        t2 = self._type_of(r)
        if t1 == "int" and t2 == "int":
            if ctx.op.type == MiniLangParser.SUMA:
                return l + r
            else:
                return l - r
        elif (t1 == "int" and t2 == "float") or (t1 == "float" and t2 == "int") or (t1 == "float" and t2 == "float"):
            lf = float(l) if t1 == "int" else l
            rf = float(r) if t2 == "int" else r
            if ctx.op.type == MiniLangParser.SUMA:
                return lf + rf
            else:
                return lf - rf
        elif t1 == "string" and t2 == "string" and ctx.op.type == MiniLangParser.SUMA:
            return l + r
        else:
            raise RuntimeError(f"Tipos incompatibles para + o -: {t1} y {t2}")

    def visitRelational(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)
        t1 = self._type_of(l)
        t2 = self._type_of(r)
        op = ctx.op.type
        if op in (MiniLangParser.EQ, MiniLangParser.NEQ):
            return (l == r) if op == MiniLangParser.EQ else (l != r)
        # Relacionales (<, <=, >, >=) solo con números
        if (t1 in ("int","float")) and (t2 in ("int","float")):
            lf = float(l) if t1 == "int" else l
            rf = float(r) if t2 == "int" else r
            if op == MiniLangParser.LT: return lf < rf
            if op == MiniLangParser.LE: return lf <= rf
            if op == MiniLangParser.GT: return lf > rf
            if op == MiniLangParser.GE: return lf >= rf
        raise RuntimeError(f"Operadores relacionales solo para números: {t1} y {t2}")

    def visitLogical(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)
        self._ensure_type("bool", l, ctx, "operación lógica")
        self._ensure_type("bool", r, ctx, "operación lógica")
        if ctx.op.type == MiniLangParser.AND:
            return l and r
        else:
            return l or r

    def visitIntLit(self, ctx):
        return int(ctx.INT().getText())

    def visitFloatLit(self, ctx):
        return float(ctx.FLOAT().getText())

    def visitStringLit(self, ctx):
        s = ctx.STRING().getText()
        return s[1:-1]

    def visitTrueLit(self, ctx):
        return True

    def visitFalseLit(self, ctx):
        return False

    def visitIdRef(self, ctx):
        name = ctx.ID().getText()
        return self.get_variable(name, ctx)