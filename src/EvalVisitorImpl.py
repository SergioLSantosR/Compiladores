# src/EvalVisitorImpl.py
from antlr4 import *
from gen.grammar.MiniLangParser import MiniLangParser
from gen.grammar.MiniLangVisitor import MiniLangVisitor


class ExcepcionRetorno(Exception):
    def __init__(self, valor):
        self.valor = valor


class EvalVisitor(MiniLangVisitor):
    def __init__(self, stdout_print=True):
        super().__init__()
        self.memoria_global = {}
        self.tipos_global = {}
        self.pila_ambitos = []
        self.funciones = {}
        self.funcion_actual = None
        self.valor_retorno = None
        self.stdout_print = stdout_print
        self.salida = []

    # ---- Manejo de ámbitos ----
    def entrar_ambito(self):
        self.pila_ambitos.append(({}, {}))

    def salir_ambito(self):
        self.pila_ambitos.pop()

    def memoria_actual(self):
        if self.pila_ambitos:
            return self.pila_ambitos[-1][0]
        return self.memoria_global

    def tipos_actual(self):
        if self.pila_ambitos:
            return self.pila_ambitos[-1][1]
        return self.tipos_global

    def declarar_variable(self, nombre, tipo, ctx):
        tipos = self.tipos_actual()
        if nombre in tipos:
            raise RuntimeError(f"Variable '{nombre}' ya declarada en este ámbito (línea {ctx.start.line})")
        tipos[nombre] = tipo
        if tipo == 'entero':
            self.memoria_actual()[nombre] = 0
        elif tipo == 'flotante':
            self.memoria_actual()[nombre] = 0.0
        elif tipo == 'booleano':
            self.memoria_actual()[nombre] = False
        elif tipo == 'cadena':
            self.memoria_actual()[nombre] = ""

    def obtener_variable(self, nombre, ctx):
        for memoria, _ in reversed(self.pila_ambitos):
            if nombre in memoria:
                return memoria[nombre]
        if nombre in self.memoria_global:
            return self.memoria_global[nombre]
        raise RuntimeError(f"Variable '{nombre}' no definida (línea {ctx.start.line})")

    def asignar_variable(self, nombre, valor, ctx):
        for i in range(len(self.pila_ambitos) - 1, -1, -1):
            if nombre in self.pila_ambitos[i][0]:
                self.pila_ambitos[i][0][nombre] = valor
                return
        if nombre in self.memoria_global:
            self.memoria_global[nombre] = valor
            return
        raise RuntimeError(f"Variable '{nombre}' no definida (línea {ctx.start.line})")

    def obtener_tipo(self, nombre):
        for _, tipos in reversed(self.pila_ambitos):
            if nombre in tipos:
                return tipos[nombre]
        return self.tipos_global.get(nombre)

    # ---- Utilidades ----
    def _tipo_de(self, valor):
        if isinstance(valor, bool):
            return "booleano"
        elif isinstance(valor, int):
            return "entero"
        elif isinstance(valor, float):
            return "flotante"
        elif isinstance(valor, str):
            return "cadena"
        return "desconocido"

    def _verificar_tipo(self, esperado, valor, ctx, descripcion=""):
        actual = self._tipo_de(valor)
        if esperado != actual:
            raise RuntimeError(
                f"Error de tipos en {descripcion} (línea {ctx.start.line}): "
                f"se esperaba {esperado}, obtuvo {actual}"
            )

    def _imprimir(self, texto):
        if self.stdout_print:
            print(texto)
        self.salida.append(str(texto))

    # ---- Programa y funciones ----
    def visitPrograma(self, ctx: MiniLangParser.ProgramaContext):
        for func_ctx in ctx.funcionDeclaracion():
            self.visit(func_ctx)
        self.entrar_ambito()
        self.visit(ctx.bloque())
        self.salir_ambito()
        return None

    def visitFuncionDeclaracion(self, ctx: MiniLangParser.FuncionDeclaracionContext):
        nombre = ctx.IDENTIFICADOR().getText()
        tipo_retorno = "vacio"
        if ctx.tipo():
            tipo_retorno = ctx.tipo().getText()
        elif ctx.VOID():
            tipo_retorno = "vacio"
        params = []
        if ctx.parametros():
            for p in ctx.parametros().parametro():
                nombre_param = p.IDENTIFICADOR().getText()
                tipo_param = p.tipo().getText()
                params.append((nombre_param, tipo_param))
        self.funciones[nombre] = (params, ctx.bloque(), tipo_retorno)
        return None

    def visitLlamadaFuncionExpr(self, ctx: MiniLangParser.LlamadaFuncionExprContext):
        nombre = ctx.IDENTIFICADOR().getText()
        if nombre not in self.funciones:
            raise RuntimeError(f"Función '{nombre}' no definida (línea {ctx.start.line})")
        params, cuerpo, tipo_ret = self.funciones[nombre]
        args = [self.visit(arg) for arg in ctx.expresion()] if ctx.expresion() else []
        if len(args) != len(params):
            raise RuntimeError(f"Número incorrecto de argumentos para función '{nombre}' (línea {ctx.start.line})")
        for (pnombre, ptipo), arg_val in zip(params, args):
            self._verificar_tipo(ptipo, arg_val, ctx, f"parámetro '{pnombre}'")
        self.entrar_ambito()
        for (pnombre, ptipo), arg_val in zip(params, args):
            self.declarar_variable(pnombre, ptipo, ctx)
            self.asignar_variable(pnombre, arg_val, ctx)
        func_anterior = self.funcion_actual
        self.funcion_actual = nombre
        self.valor_retorno = None
        try:
            self.visit(cuerpo)
        except ExcepcionRetorno as e:
            self.valor_retorno = e.valor
        self.funcion_actual = func_anterior
        self.salir_ambito()
        if tipo_ret != "vacio":
            if self.valor_retorno is None:
                raise RuntimeError(f"Función '{nombre}' debe retornar un valor")
            self._verificar_tipo(tipo_ret, self.valor_retorno, ctx, f"retorno de '{nombre}'")
            return self.valor_retorno
        return None

    def visitSentenciaRetorna(self, ctx: MiniLangParser.SentenciaRetornaContext):
        if self.funcion_actual is None:
            raise RuntimeError(f"retorna fuera de función (línea {ctx.start.line})")
        valor = None
        if ctx.expresion():
            valor = self.visit(ctx.expresion())
        raise ExcepcionRetorno(valor)

    # ---- Bloque y sentencias ----
    def visitBloque(self, ctx: MiniLangParser.BloqueContext):
        self.entrar_ambito()
        for s in ctx.sentencia():
            self.visit(s)
        self.salir_ambito()
        return None

    def visitDeclaracionVariable(self, ctx: MiniLangParser.DeclaracionVariableContext):
        tipo = ctx.tipo().getText()
        nombre = ctx.IDENTIFICADOR().getText()
        self.declarar_variable(nombre, tipo, ctx)
        if ctx.expresion():
            valor = self.visit(ctx.expresion())
            self._verificar_tipo(tipo, valor, ctx, "inicialización")
            self.asignar_variable(nombre, valor, ctx)
        return None

    def visitAsignacion(self, ctx: MiniLangParser.AsignacionContext):
        nombre = ctx.IDENTIFICADOR().getText()
        valor = self.visit(ctx.expresion())
        tipo_var = self.obtener_tipo(nombre)
        if tipo_var is None:
            raise RuntimeError(f"Variable '{nombre}' no declarada (línea {ctx.start.line})")
        self._verificar_tipo(tipo_var, valor, ctx, "asignación")
        self.asignar_variable(nombre, valor, ctx)
        self._imprimir(f"{nombre} = {valor}")
        return None

    def visitCondicionalSi(self, ctx: MiniLangParser.CondicionalSiContext):
        condicion = self.visit(ctx.expresion())
        self._verificar_tipo("booleano", condicion, ctx, "condición si")
        if condicion:
            self.visit(ctx.bloque(0))
        elif ctx.SINO():
            self.visit(ctx.bloque(1))
        return None

    def visitImpresion(self, ctx: MiniLangParser.ImpresionContext):
        valor = self.visit(ctx.expresion())
        self._imprimir(valor)
        return None

    def visitCicloMientras(self, ctx: MiniLangParser.CicloMientrasContext):
        while True:
            condicion = self.visit(ctx.expresion())
            self._verificar_tipo("booleano", condicion, ctx, "condición mientras")
            if not condicion:
                break
            self.visit(ctx.bloque())
        return None

    # ---- Bucle para ----
    def visitInicializacionPara(self, ctx: MiniLangParser.InicializacionParaContext):
        tipo = ctx.tipo().getText()
        nombre = ctx.IDENTIFICADOR().getText()
        valor = self.visit(ctx.expresion())
        self.declarar_variable(nombre, tipo, ctx)
        self.asignar_variable(nombre, valor, ctx)
        return None

    def visitAsignacionPara(self, ctx: MiniLangParser.AsignacionParaContext):
        nombre = ctx.IDENTIFICADOR().getText()
        valor = self.visit(ctx.expresion())
        tipo_var = self.obtener_tipo(nombre)
        if tipo_var is None:
            raise RuntimeError(f"Variable '{nombre}' no declarada (línea {ctx.start.line})")
        self._verificar_tipo(tipo_var, valor, ctx, "asignación en para")
        self.asignar_variable(nombre, valor, ctx)
        return None

    def visitActualizacionPara(self, ctx: MiniLangParser.ActualizacionParaContext):
        nombre = ctx.IDENTIFICADOR().getText()
        valor = self.visit(ctx.expresion())
        tipo_var = self.obtener_tipo(nombre)
        if tipo_var is None:
            raise RuntimeError(f"Variable '{nombre}' no declarada (línea {ctx.start.line})")
        self._verificar_tipo(tipo_var, valor, ctx, "actualización en para")
        self.asignar_variable(nombre, valor, ctx)
        return None

    def visitCicloPara(self, ctx: MiniLangParser.CicloParaContext):
        if ctx.inicializacionPara():
            self.visit(ctx.inicializacionPara())
        elif ctx.asignacionPara():
            self.visit(ctx.asignacionPara())
        while True:
            if ctx.cond:
                condicion = self.visit(ctx.cond)
                self._verificar_tipo("booleano", condicion, ctx, "condición para")
                if not condicion:
                    break
            self.visit(ctx.bloque())
            if ctx.actualizacionPara():
                self.visit(ctx.actualizacionPara())
        return None

    # ---- Llamada a funciones vacio como sentencia ----
    def visitLlamadaFuncion(self, ctx: MiniLangParser.LlamadaFuncionContext):
        nombre = ctx.IDENTIFICADOR().getText()
        if nombre not in self.funciones:
            raise RuntimeError(f"Función '{nombre}' no definida (línea {ctx.start.line})")
        params, cuerpo, tipo_ret = self.funciones[nombre]
        args = [self.visit(arg) for arg in ctx.expresion()] if ctx.expresion() else []
        if len(args) != len(params):
            raise RuntimeError(f"Número incorrecto de argumentos para función '{nombre}' (línea {ctx.start.line})")
        for (pnombre, ptipo), arg_val in zip(params, args):
            self._verificar_tipo(ptipo, arg_val, ctx, f"parámetro '{pnombre}'")
        self.entrar_ambito()
        for (pnombre, ptipo), arg_val in zip(params, args):
            self.declarar_variable(pnombre, ptipo, ctx)
            self.asignar_variable(pnombre, arg_val, ctx)
        func_anterior = self.funcion_actual
        self.funcion_actual = nombre
        self.valor_retorno = None
        try:
            self.visit(cuerpo)
        except ExcepcionRetorno as e:
            self.valor_retorno = e.valor
        self.funcion_actual = func_anterior
        self.salir_ambito()
        return None

    # ---- Expresiones ----
    def visitNegacionLogica(self, ctx):
        v = self.visit(ctx.expresion())
        self._verificar_tipo("booleano", v, ctx, "negación lógica")
        return not v

    def visitMenosUnario(self, ctx):
        v = self.visit(ctx.expresion())
        t = self._tipo_de(v)
        if t in ("entero", "flotante"):
            return -v
        raise RuntimeError(f"No se puede negar tipo {t}")

    def visitParentesis(self, ctx):
        return self.visit(ctx.expresion())

    def visitMultiplicacionDivision(self, ctx):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        t1 = self._tipo_de(izq)
        t2 = self._tipo_de(der)
        if t1 == "entero" and t2 == "entero":
            if ctx.op.type == MiniLangParser.MULTIPLICACION:
                return izq * der
            if der == 0:
                raise RuntimeError("División por cero")
            return izq // der
        if {t1, t2} <= {"entero", "flotante"}:
            lf = float(izq)
            rf = float(der)
            if ctx.op.type == MiniLangParser.MULTIPLICACION:
                return lf * rf
            if rf == 0.0:
                raise RuntimeError("División por cero")
            return lf / rf
        raise RuntimeError(f"Tipos incompatibles para * o /: {t1} y {t2}")

    def visitSumaResta(self, ctx):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        t1 = self._tipo_de(izq)
        t2 = self._tipo_de(der)
        if t1 == "entero" and t2 == "entero":
            return izq + der if ctx.op.type == MiniLangParser.SUMA else izq - der
        if {t1, t2} <= {"entero", "flotante"}:
            lf = float(izq)
            rf = float(der)
            return lf + rf if ctx.op.type == MiniLangParser.SUMA else lf - rf
        if t1 == "cadena" and t2 == "cadena" and ctx.op.type == MiniLangParser.SUMA:
            return izq + der
        raise RuntimeError(f"Tipos incompatibles para + o -: {t1} y {t2}")

    def visitRelacional(self, ctx):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        t1 = self._tipo_de(izq)
        t2 = self._tipo_de(der)
        op = ctx.op.type
        if op in (MiniLangParser.IGUAL, MiniLangParser.DIFERENTE):
            return (izq == der) if op == MiniLangParser.IGUAL else (izq != der)
        if {t1, t2} <= {"entero", "flotante"}:
            lf = float(izq)
            rf = float(der)
            if op == MiniLangParser.MENOR_QUE: return lf < rf
            if op == MiniLangParser.MENOR_IGUAL: return lf <= rf
            if op == MiniLangParser.MAYOR_QUE: return lf > rf
            if op == MiniLangParser.MAYOR_IGUAL: return lf >= rf
        raise RuntimeError(f"Operadores relacionales solo para números: {t1} y {t2}")

    def visitLogica(self, ctx):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        self._verificar_tipo("booleano", izq, ctx, "operación lógica")
        self._verificar_tipo("booleano", der, ctx, "operación lógica")
        if ctx.op.type == MiniLangParser.Y_LOGICO:
            return izq and der
        return izq or der

    def visitLiteralEntero(self, ctx):
        return int(ctx.ENTERO().getText())

    def visitLiteralFlotante(self, ctx):
        return float(ctx.FLOTANTE().getText())

    def visitLiteralCadena(self, ctx):
        s = ctx.CADENA().getText()
        return s[1:-1]

    def visitLiteralVerdadero(self, ctx):
        return True

    def visitLiteralFalso(self, ctx):
        return False

    def visitReferenciaVariable(self, ctx):
        nombre = ctx.IDENTIFICADOR().getText()
        return self.obtener_variable(nombre, ctx)
