# src/ir_generator.py — Generador de LLVM IR usando llvmlite
from __future__ import annotations

from llvmlite import ir

from gen.grammar.gramatica_v4Parser import gramatica_v4Parser
from gen.grammar.gramatica_v4Visitor import gramatica_v4Visitor

# Tipos LLVM reutilizables
INT32 = ir.IntType(32)
INT8 = ir.IntType(8)
INT1 = ir.IntType(1)
DOUBLE = ir.DoubleType()
VOID = ir.VoidType()
INT8_PTR = ir.PointerType(INT8)


class IRGenerator(gramatica_v4Visitor):
    """Genera LLVM IR ejecutable a partir del AST de MiniLang usando llvmlite."""

    def __init__(self):
        super().__init__()
        self.module = ir.Module(name="MiniLang")
        self.module.triple = "x86_64-unknown-linux-gnu"

        self.builder: ir.IRBuilder | None = None
        self.variables: dict[str, ir.AllocaInstr] = {}
        self.var_types: dict[str, ir.Type] = {}
        self.funciones: dict[str, ir.Function] = {}
        self.funciones_info: dict[str, dict] = {}
        self.pila_ciclos: list[tuple[ir.Block, ir.Block]] = []
        self.func_actual: ir.Function | None = None

        self._printf: ir.Function | None = None
        self._fmt_int: ir.GlobalVariable | None = None
        self._fmt_float: ir.GlobalVariable | None = None
        self._fmt_str: ir.GlobalVariable | None = None

    # ── Helpers ───────────────────────────────────────────────

    def _setup_printf(self):
        printf_ty = ir.FunctionType(INT32, [INT8_PTR], var_arg=True)
        self._printf = ir.Function(self.module, printf_ty, name="printf")

        self._fmt_int = self._global_string("%d\n", ".fmt.int")
        self._fmt_float = self._global_string("%f\n", ".fmt.float")
        self._fmt_str = self._global_string("%s\n", ".fmt.str")

    def _global_string(self, text: str, name: str) -> ir.GlobalVariable:
        encoded = bytearray((text + "\0").encode("utf8"))
        arr_ty = ir.ArrayType(INT8, len(encoded))
        gvar = ir.GlobalVariable(self.module, arr_ty, name=name)
        gvar.initializer = ir.Constant(arr_ty, encoded)
        gvar.global_constant = True
        gvar.linkage = "private"
        gvar.unnamed_addr = True
        return gvar

    def _gep_to_ptr(self, gvar: ir.GlobalVariable) -> ir.Value:
        zero = ir.Constant(INT32, 0)
        return self.builder.gep(gvar, [zero, zero], inbounds=True)

    def _tipo_llvm(self, tipo_str: str) -> ir.Type:
        if tipo_str in ("entero", "booleano"):
            return INT32
        if tipo_str == "flotante":
            return DOUBLE
        if tipo_str == "cadena":
            return INT8_PTR
        return INT32

    def _tipo_ret_llvm(self, tipo_str: str) -> ir.Type:
        if tipo_str == "vacio":
            return VOID
        return self._tipo_llvm(tipo_str)

    def _is_terminated(self) -> bool:
        return self.builder.block.is_terminated

    def _alloca_entry(self, func: ir.Function, typ: ir.Type, name: str) -> ir.AllocaInstr:
        """Alloca en el bloque entry de la función para estabilidad de mem2reg."""
        saved = self.builder.block
        self.builder.position_at_start(func.entry_basic_block)
        alloca = self.builder.alloca(typ, name=name)
        self.builder.position_at_end(saved)
        return alloca

    def _cast_to_i32(self, val: ir.Value) -> ir.Value:
        if val.type == INT1:
            return self.builder.zext(val, INT32)
        if val.type == DOUBLE:
            return self.builder.fptosi(val, INT32)
        return val

    def _cast_to_double(self, val: ir.Value) -> ir.Value:
        if val.type == INT32:
            return self.builder.sitofp(val, DOUBLE)
        if val.type == INT1:
            val32 = self.builder.zext(val, INT32)
            return self.builder.sitofp(val32, DOUBLE)
        return val

    def _to_bool_i32(self, val: ir.Value) -> ir.Value:
        if val.type == INT1:
            return self.builder.zext(val, INT32)
        return val

    def _to_i1(self, val: ir.Value) -> ir.Value:
        if val.type == INT1:
            return val
        if val.type == INT32:
            return self.builder.icmp_signed("!=", val, ir.Constant(INT32, 0))
        if val.type == DOUBLE:
            return self.builder.fcmp_ordered("!=", val, ir.Constant(DOUBLE, 0.0))
        return val

    # ── Programa ──────────────────────────────────────────────

    def visitPrograma(self, ctx: gramatica_v4Parser.ProgramaContext):
        self._setup_printf()

        for func_ctx in ctx.funcionDeclaracion():
            self._registrar_funcion(func_ctx)

        for func_ctx in ctx.funcionDeclaracion():
            self._generar_funcion(func_ctx)

        main_ty = ir.FunctionType(INT32, [])
        main_func = ir.Function(self.module, main_ty, name="main")
        entry = main_func.append_basic_block("entry")
        self.builder = ir.IRBuilder(entry)
        self.func_actual = main_func
        self.variables = {}
        self.var_types = {}

        for s in ctx.bloque().sentencia():
            if self._is_terminated():
                break
            self.visit(s)

        if not self._is_terminated():
            self.builder.ret(ir.Constant(INT32, 0))

        return str(self.module)

    def _registrar_funcion(self, ctx: gramatica_v4Parser.FuncionDeclaracionContext):
        nombre = ctx.IDENTIFICADOR().getText()
        params = []
        if ctx.parametros():
            for p in ctx.parametros().parametro():
                params.append((p.IDENTIFICADOR().getText(), p.tipo().getText()))

        tipo_ret_str = "vacio"
        if ctx.tipo():
            tipo_ret_str = ctx.tipo().getText()

        param_types = [self._tipo_llvm(t) for _, t in params]
        ret_type = self._tipo_ret_llvm(tipo_ret_str)
        func_ty = ir.FunctionType(ret_type, param_types)
        func = ir.Function(self.module, func_ty, name=nombre)

        for i, (pname, _) in enumerate(params):
            func.args[i].name = pname

        self.funciones[nombre] = func
        self.funciones_info[nombre] = {"params": params, "return": tipo_ret_str}

    def _generar_funcion(self, ctx: gramatica_v4Parser.FuncionDeclaracionContext):
        nombre = ctx.IDENTIFICADOR().getText()
        func = self.funciones[nombre]
        info = self.funciones_info[nombre]

        saved_builder = self.builder
        saved_vars = self.variables
        saved_types = self.var_types
        saved_func = self.func_actual

        entry = func.append_basic_block("entry")
        self.builder = ir.IRBuilder(entry)
        self.func_actual = func
        self.variables = {}
        self.var_types = {}

        for i, (pname, ptype) in enumerate(info["params"]):
            llvm_ty = self._tipo_llvm(ptype)
            ptr = self._alloca_entry(func, llvm_ty, pname)
            self.builder.store(func.args[i], ptr)
            self.variables[pname] = ptr
            self.var_types[pname] = llvm_ty

        for s in ctx.bloque().sentencia():
            if self._is_terminated():
                break
            self.visit(s)

        if not self._is_terminated():
            if func.return_value.type == VOID:
                self.builder.ret_void()
            else:
                self.builder.ret(ir.Constant(func.return_value.type, 0))

        self.builder = saved_builder
        self.variables = saved_vars
        self.var_types = saved_types
        self.func_actual = saved_func

    def visitFuncionDeclaracion(self, ctx):
        return None

    # ── Bloque ────────────────────────────────────────────────

    def visitBloque(self, ctx: gramatica_v4Parser.BloqueContext):
        for s in ctx.sentencia():
            if self._is_terminated():
                break
            self.visit(s)
        return None

    # ── Declaración y asignación ──────────────────────────────

    def visitDeclaracionVariable(self, ctx: gramatica_v4Parser.DeclaracionVariableContext):
        if self._is_terminated():
            return None
        tipo_str = ctx.tipo().getText()
        nombre = ctx.IDENTIFICADOR().getText()

        es_arreglo = ctx.CORCHETE_IZQ() is not None and ctx.CORCHETE_DER() is not None

        if es_arreglo:
            base_ty = self._tipo_llvm(tipo_str)
            arr_size = 64
            arr_ty = ir.ArrayType(base_ty, arr_size)
            ptr = self._alloca_entry(self.func_actual, arr_ty, nombre)
            self.variables[nombre] = ptr
            self.var_types[nombre] = arr_ty
            return None

        llvm_ty = self._tipo_llvm(tipo_str)
        ptr = self._alloca_entry(self.func_actual, llvm_ty, nombre)
        self.variables[nombre] = ptr
        self.var_types[nombre] = llvm_ty

        if ctx.expresion():
            val = self.visit(ctx.expresion())
            if val is not None:
                val = self._coerce(val, llvm_ty)
                self.builder.store(val, ptr)
        else:
            self.builder.store(ir.Constant(llvm_ty, 0), ptr)
        return None

    def _coerce(self, val: ir.Value, target: ir.Type) -> ir.Value:
        if val.type == target:
            return val
        if target == DOUBLE and val.type == INT32:
            return self.builder.sitofp(val, DOUBLE)
        if target == INT32 and val.type == INT1:
            return self.builder.zext(val, INT32)
        if target == INT32 and val.type == DOUBLE:
            return self.builder.fptosi(val, INT32)
        return val

    def visitAsignacion(self, ctx: gramatica_v4Parser.AsignacionContext):
        if self._is_terminated():
            return None
        nombre = ctx.IDENTIFICADOR().getText()
        val = self.visit(ctx.expresion())
        if nombre in self.variables and val is not None:
            target_ty = self.var_types.get(nombre, INT32)
            val = self._coerce(val, target_ty)
            self.builder.store(val, self.variables[nombre])
        return None

    def visitAsignacionArreglo(self, ctx: gramatica_v4Parser.AsignacionArregloContext):
        if self._is_terminated():
            return None
        acceso = ctx.accesoArreglo()
        nombre = acceso.IDENTIFICADOR().getText()
        indice = self.visit(acceso.expresion())
        valor = self.visit(ctx.expresion())
        if nombre in self.variables and indice is not None and valor is not None:
            zero = ir.Constant(INT32, 0)
            idx = self._cast_to_i32(indice)
            ptr = self.builder.gep(self.variables[nombre], [zero, idx], inbounds=True)
            self.builder.store(valor, ptr)
        return None

    # ── Impresión ─────────────────────────────────────────────

    def visitImpresion(self, ctx: gramatica_v4Parser.ImpresionContext):
        if self._is_terminated():
            return None
        val = self.visit(ctx.expresion())
        if val is None:
            return None

        if val.type == DOUBLE:
            fmt = self._gep_to_ptr(self._fmt_float)
            self.builder.call(self._printf, [fmt, val])
        elif val.type == INT8_PTR or (hasattr(val.type, 'pointee') and val.type.pointee == INT8):
            fmt = self._gep_to_ptr(self._fmt_str)
            self.builder.call(self._printf, [fmt, val])
        else:
            val32 = self._cast_to_i32(val)
            fmt = self._gep_to_ptr(self._fmt_int)
            self.builder.call(self._printf, [fmt, val32])
        return None

    # ── Condicional ───────────────────────────────────────────

    def visitCondicionalSi(self, ctx: gramatica_v4Parser.CondicionalSiContext):
        if self._is_terminated():
            return None
        cond = self._to_i1(self.visit(ctx.expresion()))
        then_bb = self.func_actual.append_basic_block("si.then")
        else_bb = self.func_actual.append_basic_block("si.else")
        merge_bb = self.func_actual.append_basic_block("si.merge")

        self.builder.cbranch(cond, then_bb, else_bb)

        self.builder.position_at_start(then_bb)
        self.visit(ctx.bloque(0))
        if not self._is_terminated():
            self.builder.branch(merge_bb)

        self.builder.position_at_start(else_bb)
        if ctx.SINO():
            self.visit(ctx.bloque(1))
        if not self._is_terminated():
            self.builder.branch(merge_bb)

        self.builder.position_at_start(merge_bb)
        return None

    # ── Ciclo mientras ────────────────────────────────────────

    def visitCicloMientras(self, ctx: gramatica_v4Parser.CicloMientrasContext):
        if self._is_terminated():
            return None
        cond_bb = self.func_actual.append_basic_block("mientras.cond")
        body_bb = self.func_actual.append_basic_block("mientras.body")
        end_bb = self.func_actual.append_basic_block("mientras.end")

        self.builder.branch(cond_bb)

        self.builder.position_at_start(cond_bb)
        cond = self._to_i1(self.visit(ctx.expresion()))
        self.builder.cbranch(cond, body_bb, end_bb)

        self.builder.position_at_start(body_bb)
        self.pila_ciclos.append((cond_bb, end_bb))
        self.visit(ctx.bloque())
        self.pila_ciclos.pop()
        if not self._is_terminated():
            self.builder.branch(cond_bb)

        self.builder.position_at_start(end_bb)
        return None

    # ── Ciclo para ────────────────────────────────────────────

    def visitCicloPara(self, ctx: gramatica_v4Parser.CicloParaContext):
        if self._is_terminated():
            return None

        if ctx.inicializacionPara():
            self.visit(ctx.inicializacionPara())
        elif ctx.asignacionPara():
            self.visit(ctx.asignacionPara())

        cond_bb = self.func_actual.append_basic_block("para.cond")
        body_bb = self.func_actual.append_basic_block("para.body")
        step_bb = self.func_actual.append_basic_block("para.step")
        end_bb = self.func_actual.append_basic_block("para.end")

        self.builder.branch(cond_bb)

        self.builder.position_at_start(cond_bb)
        if ctx.cond:
            cond = self._to_i1(self.visit(ctx.cond))
            self.builder.cbranch(cond, body_bb, end_bb)
        else:
            self.builder.branch(body_bb)

        self.builder.position_at_start(body_bb)
        self.pila_ciclos.append((step_bb, end_bb))
        self.visit(ctx.bloque())
        self.pila_ciclos.pop()
        if not self._is_terminated():
            self.builder.branch(step_bb)

        self.builder.position_at_start(step_bb)
        if ctx.actualizacionPara():
            self.visit(ctx.actualizacionPara())
        self.builder.branch(cond_bb)

        self.builder.position_at_start(end_bb)
        return None

    def visitInicializacionPara(self, ctx: gramatica_v4Parser.InicializacionParaContext):
        tipo_str = ctx.tipo().getText()
        nombre = ctx.IDENTIFICADOR().getText()
        llvm_ty = self._tipo_llvm(tipo_str)
        ptr = self._alloca_entry(self.func_actual, llvm_ty, nombre)
        val = self.visit(ctx.expresion())
        if val is not None:
            val = self._coerce(val, llvm_ty)
            self.builder.store(val, ptr)
        self.variables[nombre] = ptr
        self.var_types[nombre] = llvm_ty
        return None

    def visitAsignacionPara(self, ctx: gramatica_v4Parser.AsignacionParaContext):
        nombre = ctx.IDENTIFICADOR().getText()
        val = self.visit(ctx.expresion())
        if nombre in self.variables and val is not None:
            target_ty = self.var_types.get(nombre, INT32)
            val = self._coerce(val, target_ty)
            self.builder.store(val, self.variables[nombre])
        return None

    def visitActualizacionPara(self, ctx: gramatica_v4Parser.ActualizacionParaContext):
        nombre = ctx.IDENTIFICADOR().getText()
        val = self.visit(ctx.expresion())
        if nombre in self.variables and val is not None:
            target_ty = self.var_types.get(nombre, INT32)
            val = self._coerce(val, target_ty)
            self.builder.store(val, self.variables[nombre])
        return None

    # ── Break / Continue ──────────────────────────────────────

    def visitSentenciaBreak(self, ctx):
        if self._is_terminated():
            return None
        if self.pila_ciclos:
            _, end_bb = self.pila_ciclos[-1]
            self.builder.branch(end_bb)
        return None

    def visitSentenciaContinue(self, ctx):
        if self._is_terminated():
            return None
        if self.pila_ciclos:
            cont_bb, _ = self.pila_ciclos[-1]
            self.builder.branch(cont_bb)
        return None

    # ── Return ────────────────────────────────────────────────

    def visitSentenciaRetorna(self, ctx: gramatica_v4Parser.SentenciaRetornaContext):
        if self._is_terminated():
            return None
        if ctx.expresion():
            val = self.visit(ctx.expresion())
            if val is not None:
                ret_ty = self.func_actual.return_value.type
                val = self._coerce(val, ret_ty)
                self.builder.ret(val)
            else:
                self.builder.ret_void()
        else:
            self.builder.ret_void()
        return None

    # ── Llamadas a funciones ──────────────────────────────────

    def visitLlamadaFuncion(self, ctx: gramatica_v4Parser.LlamadaFuncionContext):
        if self._is_terminated():
            return None
        self._gen_call(ctx.IDENTIFICADOR().getText(), ctx.expresion())
        return None

    def visitLlamadaFuncionExpr(self, ctx: gramatica_v4Parser.LlamadaFuncionExprContext):
        if self._is_terminated():
            return None
        return self._gen_call(ctx.IDENTIFICADOR().getText(), ctx.expresion())

    def _gen_call(self, nombre: str, expr_list) -> ir.Value | None:
        if nombre not in self.funciones:
            return None
        func = self.funciones[nombre]
        info = self.funciones_info[nombre]
        args_ctx = list(expr_list) if expr_list else []
        args = []
        for i, arg_ctx in enumerate(args_ctx):
            val = self.visit(arg_ctx)
            if val is not None and i < len(info["params"]):
                _, ptype = info["params"][i]
                val = self._coerce(val, self._tipo_llvm(ptype))
                args.append(val)
            elif val is not None:
                args.append(val)
        result = self.builder.call(func, args)
        if func.return_value.type == VOID:
            return None
        return result

    # ── Import (no-op en IR) ──────────────────────────────────

    def visitSentenciaImportar(self, ctx):
        return None

    # ── Expresiones aritméticas ───────────────────────────────

    def visitMultiplicacionDivisionModulo(self, ctx):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        if izq is None or der is None:
            return ir.Constant(INT32, 0)

        op = ctx.op.type
        if op == gramatica_v4Parser.MODULO:
            a = self._cast_to_i32(izq)
            b = self._cast_to_i32(der)
            return self.builder.srem(a, b)

        if izq.type == DOUBLE or der.type == DOUBLE:
            a = self._cast_to_double(izq)
            b = self._cast_to_double(der)
            if op == gramatica_v4Parser.MULTIPLICACION:
                return self.builder.fmul(a, b)
            return self.builder.fdiv(a, b)

        a = self._cast_to_i32(izq)
        b = self._cast_to_i32(der)
        if op == gramatica_v4Parser.MULTIPLICACION:
            return self.builder.mul(a, b)
        return self.builder.sdiv(a, b)

    def visitMultiplicacionDivision(self, ctx):
        return self.visitMultiplicacionDivisionModulo(ctx)

    def visitSumaResta(self, ctx):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        if izq is None or der is None:
            return ir.Constant(INT32, 0)

        op = ctx.op.type
        if izq.type == DOUBLE or der.type == DOUBLE:
            a = self._cast_to_double(izq)
            b = self._cast_to_double(der)
            if op == gramatica_v4Parser.SUMA:
                return self.builder.fadd(a, b)
            return self.builder.fsub(a, b)

        a = self._cast_to_i32(izq)
        b = self._cast_to_i32(der)
        if op == gramatica_v4Parser.SUMA:
            return self.builder.add(a, b)
        return self.builder.sub(a, b)

    def visitNegacionLogica(self, ctx):
        val = self.visit(ctx.expresion())
        if val is None:
            return ir.Constant(INT32, 0)
        b = self._to_i1(val)
        neg = self.builder.not_(b)
        return self.builder.zext(neg, INT32)

    def visitMenosUnario(self, ctx):
        val = self.visit(ctx.expresion())
        if val is None:
            return ir.Constant(INT32, 0)
        if val.type == DOUBLE:
            return self.builder.fsub(ir.Constant(DOUBLE, 0.0), val)
        v32 = self._cast_to_i32(val)
        return self.builder.sub(ir.Constant(INT32, 0), v32)

    def visitParentesis(self, ctx):
        return self.visit(ctx.expresion())

    # ── Relacional ────────────────────────────────────────────

    def visitRelacional(self, ctx):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        if izq is None or der is None:
            return ir.Constant(INT32, 0)

        op = ctx.op.type
        op_map_int = {
            gramatica_v4Parser.MENOR_QUE: "<",
            gramatica_v4Parser.MENOR_IGUAL: "<=",
            gramatica_v4Parser.MAYOR_QUE: ">",
            gramatica_v4Parser.MAYOR_IGUAL: ">=",
            gramatica_v4Parser.IGUAL: "==",
            gramatica_v4Parser.DIFERENTE: "!=",
        }
        op_map_float = {
            gramatica_v4Parser.MENOR_QUE: "<",
            gramatica_v4Parser.MENOR_IGUAL: "<=",
            gramatica_v4Parser.MAYOR_QUE: ">",
            gramatica_v4Parser.MAYOR_IGUAL: ">=",
            gramatica_v4Parser.IGUAL: "==",
            gramatica_v4Parser.DIFERENTE: "!=",
        }

        if izq.type == DOUBLE or der.type == DOUBLE:
            a = self._cast_to_double(izq)
            b = self._cast_to_double(der)
            cmp = self.builder.fcmp_ordered(op_map_float[op], a, b)
        else:
            a = self._cast_to_i32(izq)
            b = self._cast_to_i32(der)
            cmp = self.builder.icmp_signed(op_map_int[op], a, b)

        return self.builder.zext(cmp, INT32)

    def visitLogica(self, ctx):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        if izq is None or der is None:
            return ir.Constant(INT32, 0)

        a = self._to_i1(izq)
        b = self._to_i1(der)

        if ctx.op.type == gramatica_v4Parser.Y_LOGICO:
            res = self.builder.and_(a, b)
        else:
            res = self.builder.or_(a, b)
        return self.builder.zext(res, INT32)

    # ── Literales ─────────────────────────────────────────────

    def visitLiteralEntero(self, ctx):
        return ir.Constant(INT32, int(ctx.ENTERO().getText()))

    def visitLiteralFlotante(self, ctx):
        return ir.Constant(DOUBLE, float(ctx.FLOTANTE().getText()))

    def visitLiteralCadena(self, ctx):
        s = ctx.CADENA().getText()[1:-1]
        gvar = self._global_string(s, f".str.{id(ctx)}")
        return self._gep_to_ptr(gvar)

    def visitLiteralVerdadero(self, ctx):
        return ir.Constant(INT32, 1)

    def visitLiteralFalso(self, ctx):
        return ir.Constant(INT32, 0)

    # ── Referencias ───────────────────────────────────────────

    def visitReferenciaVariable(self, ctx):
        nombre = ctx.IDENTIFICADOR().getText()
        if nombre in self.variables:
            ty = self.var_types.get(nombre, INT32)
            return self.builder.load(self.variables[nombre], name=nombre)
        return ir.Constant(INT32, 0)

    def visitAccesoArreglo(self, ctx):
        nombre = ctx.IDENTIFICADOR().getText()
        indice = self.visit(ctx.expresion())
        if nombre in self.variables and indice is not None:
            zero = ir.Constant(INT32, 0)
            idx = self._cast_to_i32(indice)
            ptr = self.builder.gep(self.variables[nombre], [zero, idx], inbounds=True)
            return self.builder.load(ptr)
        return ir.Constant(INT32, 0)

    def visitAccesoArregloExpr(self, ctx):
        return self.visit(ctx.accesoArreglo())

    def visitLiteralArreglo(self, ctx):
        return None
