# src/ir_generator.py
from gen.grammar.MiniLangParser import MiniLangParser
from gen.grammar.MiniLangVisitor import MiniLangVisitor


class IRGenerator(MiniLangVisitor):
    """
    Generador de LLVM IR simplificado
    Produce código .ll demostrativo
    """
    
    def __init__(self):
        super().__init__()
        self.codigo = []
        self.temp_counter = 0
        self.label_counter = 0
        self.funcion_actual = None
        self.variables = {}
        self.call_counter = 0
        self.funciones_info = {}
        self.pila_ciclos = []
        self.string_constants = []
        self.string_counter = 0
        
    def nuevo_temporal(self):
        self.temp_counter += 1
        return f"%t{self.temp_counter}"
    
    def nueva_etiqueta(self):
        self.label_counter += 1
        return f"L{self.label_counter}"
    
    def nueva_llamada(self):
        self.call_counter += 1
        return f"%call{self.call_counter}"
    
    def emitir(self, linea):
        self.codigo.append(linea)
    
    def get_ir(self):
        return "\n".join(self.codigo)
    
    def _nueva_cadena(self, texto):
        self.string_counter += 1
        name = f"@.str.{self.string_counter}"
        escaped = texto.replace('\\', '\\5C').replace('"', '\\22')
        length = len(texto) + 1
        self.string_constants.append(
            f'{name} = private unnamed_addr constant [{length} x i8] c"{escaped}\\00", align 1'
        )
        return name, length
    
    def visitPrograma(self, ctx: MiniLangParser.ProgramaContext):
        self.codigo = []
        self.string_constants = []
        
        # Collect function info
        for func_ctx in ctx.funcionDeclaracion():
            nombre = func_ctx.IDENTIFICADOR().getText()
            params = []
            if func_ctx.parametros():
                for p in func_ctx.parametros().parametro():
                    params.append((p.IDENTIFICADOR().getText(), p.tipo().getText()))
            tipo_ret = "vacio"
            if func_ctx.tipo():
                tipo_ret = func_ctx.tipo().getText()
            self.funciones_info[nombre] = {"params": params, "return": tipo_ret}
        
        header = []
        header.append("; ModuleID = 'MiniLang'")
        header.append("")
        header.append("declare i32 @printf(i8*, ...)")
        header.append("declare i32 @puts(i8*)")
        header.append("")
        
        func_code = []
        
        # Generate user functions
        for func_ctx in ctx.funcionDeclaracion():
            self.codigo = []
            self.variables = {}
            self.temp_counter = 0
            self.label_counter = 0
            self.call_counter = 0
            self._gen_funcion(func_ctx)
            func_code.extend(self.codigo)
            func_code.append("")
        
        # Generate main
        self.codigo = []
        self.variables = {}
        self.temp_counter = 0
        self.label_counter = 0
        self.call_counter = 0
        
        self.emitir("define i32 @main() {")
        self.emitir("entry:")
        self.visit(ctx.bloque())
        self.emitir("  ret i32 0")
        self.emitir("}")
        
        main_code = self.codigo
        
        # Assemble final output
        final = header
        # Format strings
        final.append('@.str.int = private unnamed_addr constant [4 x i8] c"%d\\0A\\00", align 1')
        final.append('@.str.float = private unnamed_addr constant [4 x i8] c"%f\\0A\\00", align 1')
        for sc in self.string_constants:
            final.append(sc)
        final.append("")
        final.extend(func_code)
        final.extend(main_code)
        
        self.codigo = final
        return self.get_ir()
    
    def _gen_funcion(self, ctx):
        nombre = ctx.IDENTIFICADOR().getText()
        info = self.funciones_info[nombre]
        ret_type = "i32" if info["return"] != "vacio" else "void"
        
        params_ir = ", ".join(f"i32 %{p[0]}.arg" for p in info["params"])
        self.emitir(f"define {ret_type} @{nombre}({params_ir}) {{")
        self.emitir("entry:")
        
        # Alloca for params
        for pname, ptype in info["params"]:
            self.variables[pname] = f"%{pname}"
            self.emitir(f"  %{pname} = alloca i32")
            self.emitir(f"  store i32 %{pname}.arg, i32* %{pname}")
        
        # Body
        self.visit(ctx.bloque())
        
        # Default return if not already returned
        if ret_type == "void":
            self.emitir("  ret void")
        else:
            self.emitir("  ret i32 0")
        
        self.emitir("}")
    
    def visitBloque(self, ctx: MiniLangParser.BloqueContext):
        for sentencia in ctx.sentencia():
            self.visit(sentencia)
        return None
    
    def visitDeclaracionVariable(self, ctx: MiniLangParser.DeclaracionVariableContext):
        tipo = ctx.tipo().getText()
        nombre = ctx.IDENTIFICADOR().getText()
        
        self.variables[nombre] = f"%{nombre}"
        self.emitir(f"  %{nombre} = alloca i32")
        
        if ctx.expresion():
            valor = self.visit(ctx.expresion())
            self.emitir(f"  store i32 {valor}, i32* %{nombre}")
        else:
            self.emitir(f"  store i32 0, i32* %{nombre}")
        
        return None
    
    def visitAsignacion(self, ctx: MiniLangParser.AsignacionContext):
        nombre = ctx.IDENTIFICADOR().getText()
        valor = self.visit(ctx.expresion())
        
        if nombre in self.variables:
            self.emitir(f"  store i32 {valor}, i32* %{nombre}")
        return None
    
    def visitImpresion(self, ctx: MiniLangParser.ImpresionContext):
        valor = self.visit(ctx.expresion())
        call_temp = self.nueva_llamada()
        self.emitir(f"  {call_temp} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.int, i32 0, i32 0), i32 {valor})")
        return None
    
    def visitLiteralEntero(self, ctx):
        return ctx.ENTERO().getText()
    
    def visitLiteralFlotante(self, ctx):
        return ctx.FLOTANTE().getText()
    
    def visitLiteralCadena(self, ctx):
        s = ctx.CADENA().getText()[1:-1]
        name, length = self._nueva_cadena(s)
        temp = self.nuevo_temporal()
        self.emitir(f"  {temp} = getelementptr [{length} x i8], [{length} x i8]* {name}, i32 0, i32 0")
        return temp
    
    def visitLiteralVerdadero(self, ctx):
        return "1"
    
    def visitLiteralFalso(self, ctx):
        return "0"
    
    def visitReferenciaVariable(self, ctx):
        nombre = ctx.IDENTIFICADOR().getText()
        if nombre in self.variables:
            temp = self.nuevo_temporal()
            self.emitir(f"  {temp} = load i32, i32* %{nombre}")
            return temp
        return "0"
    
    def visitMultiplicacionDivisionModulo(self, ctx):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        op = ctx.op.text
        temp = self.nuevo_temporal()
        
        if op == '*':
            self.emitir(f"  {temp} = mul i32 {izq}, {der}")
        elif op == '/':
            self.emitir(f"  {temp} = sdiv i32 {izq}, {der}")
        elif op == '%':
            self.emitir(f"  {temp} = srem i32 {izq}, {der}")
        
        return temp
    
    def visitSumaResta(self, ctx):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        op = ctx.op.text
        temp = self.nuevo_temporal()
        
        if op == '+':
            self.emitir(f"  {temp} = add i32 {izq}, {der}")
        else:
            self.emitir(f"  {temp} = sub i32 {izq}, {der}")
        
        return temp
    
    def visitNegacionLogica(self, ctx):
        expr = self.visit(ctx.expresion())
        temp_bool = self.nuevo_temporal()
        temp_not = self.nuevo_temporal()
        temp = self.nuevo_temporal()
        self.emitir(f"  {temp_bool} = icmp ne i32 {expr}, 0")
        self.emitir(f"  {temp_not} = xor i1 {temp_bool}, true")
        self.emitir(f"  {temp} = zext i1 {temp_not} to i32")
        return temp
    
    def visitMenosUnario(self, ctx):
        expr = self.visit(ctx.expresion())
        temp = self.nuevo_temporal()
        self.emitir(f"  {temp} = sub i32 0, {expr}")
        return temp
    
    def visitParentesis(self, ctx):
        return self.visit(ctx.expresion())
    
    def visitRelacional(self, ctx):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        op = ctx.op.text
        temp = self.nuevo_temporal()
        temp_int = self.nuevo_temporal()
        
        if op == '<':
            self.emitir(f"  {temp} = icmp slt i32 {izq}, {der}")
        elif op == '<=':
            self.emitir(f"  {temp} = icmp sle i32 {izq}, {der}")
        elif op == '>':
            self.emitir(f"  {temp} = icmp sgt i32 {izq}, {der}")
        elif op == '>=':
            self.emitir(f"  {temp} = icmp sge i32 {izq}, {der}")
        elif op == '==':
            self.emitir(f"  {temp} = icmp eq i32 {izq}, {der}")
        elif op == '!=':
            self.emitir(f"  {temp} = icmp ne i32 {izq}, {der}")
        
        self.emitir(f"  {temp_int} = zext i1 {temp} to i32")
        return temp_int
    
    def visitLogica(self, ctx):
        izq = self.visit(ctx.izq)
        der = self.visit(ctx.der)
        op = ctx.op.text
        temp_bool_izq = self.nuevo_temporal()
        temp_bool_der = self.nuevo_temporal()
        temp_result = self.nuevo_temporal()
        temp = self.nuevo_temporal()
        
        self.emitir(f"  {temp_bool_izq} = icmp ne i32 {izq}, 0")
        self.emitir(f"  {temp_bool_der} = icmp ne i32 {der}, 0")
        
        if op == '&&':
            self.emitir(f"  {temp_result} = and i1 {temp_bool_izq}, {temp_bool_der}")
        else:
            self.emitir(f"  {temp_result} = or i1 {temp_bool_izq}, {temp_bool_der}")
        
        self.emitir(f"  {temp} = zext i1 {temp_result} to i32")
        return temp
    
    def visitCondicionalSi(self, ctx: MiniLangParser.CondicionalSiContext):
        cond = self.visit(ctx.expresion())
        etiqueta_then = self.nueva_etiqueta()
        etiqueta_else = self.nueva_etiqueta()
        etiqueta_end = self.nueva_etiqueta()
        
        cond_temp = self.nuevo_temporal()
        self.emitir(f"  {cond_temp} = icmp ne i32 {cond}, 0")
        self.emitir(f"  br i1 {cond_temp}, label %{etiqueta_then}, label %{etiqueta_else}")
        
        self.emitir(f"\n{etiqueta_then}:")
        self.visit(ctx.bloque(0))
        self.emitir(f"  br label %{etiqueta_end}")
        
        self.emitir(f"\n{etiqueta_else}:")
        if ctx.SINO():
            self.visit(ctx.bloque(1))
        self.emitir(f"  br label %{etiqueta_end}")
        
        self.emitir(f"\n{etiqueta_end}:")
        return None
    
    def visitCicloMientras(self, ctx: MiniLangParser.CicloMientrasContext):
        etiqueta_cond = self.nueva_etiqueta()
        etiqueta_body = self.nueva_etiqueta()
        etiqueta_end = self.nueva_etiqueta()
        
        self.emitir(f"  br label %{etiqueta_cond}")
        
        self.emitir(f"\n{etiqueta_cond}:")
        cond = self.visit(ctx.expresion())
        cond_temp = self.nuevo_temporal()
        self.emitir(f"  {cond_temp} = icmp ne i32 {cond}, 0")
        self.emitir(f"  br i1 {cond_temp}, label %{etiqueta_body}, label %{etiqueta_end}")
        
        self.emitir(f"\n{etiqueta_body}:")
        self.pila_ciclos.append((etiqueta_cond, etiqueta_end))
        self.visit(ctx.bloque())
        self.pila_ciclos.pop()
        self.emitir(f"  br label %{etiqueta_cond}")
        
        self.emitir(f"\n{etiqueta_end}:")
        return None
    
    def visitCicloPara(self, ctx: MiniLangParser.CicloParaContext):
        etiqueta_cond = self.nueva_etiqueta()
        etiqueta_body = self.nueva_etiqueta()
        etiqueta_step = self.nueva_etiqueta()
        etiqueta_end = self.nueva_etiqueta()
        
        if ctx.inicializacionPara():
            self.visit(ctx.inicializacionPara())
        elif ctx.asignacionPara():
            self.visit(ctx.asignacionPara())
        
        self.emitir(f"  br label %{etiqueta_cond}")
        
        self.emitir(f"\n{etiqueta_cond}:")
        if ctx.cond:
            cond = self.visit(ctx.cond)
            cond_temp = self.nuevo_temporal()
            self.emitir(f"  {cond_temp} = icmp ne i32 {cond}, 0")
            self.emitir(f"  br i1 {cond_temp}, label %{etiqueta_body}, label %{etiqueta_end}")
        else:
            self.emitir(f"  br label %{etiqueta_body}")
        
        self.emitir(f"\n{etiqueta_body}:")
        self.pila_ciclos.append((etiqueta_step, etiqueta_end))
        self.visit(ctx.bloque())
        self.pila_ciclos.pop()
        self.emitir(f"  br label %{etiqueta_step}")
        
        self.emitir(f"\n{etiqueta_step}:")
        if ctx.actualizacionPara():
            self.visit(ctx.actualizacionPara())
        self.emitir(f"  br label %{etiqueta_cond}")
        
        self.emitir(f"\n{etiqueta_end}:")
        return None
    
    def visitInicializacionPara(self, ctx: MiniLangParser.InicializacionParaContext):
        nombre = ctx.IDENTIFICADOR().getText()
        valor = self.visit(ctx.expresion())
        self.variables[nombre] = f"%{nombre}"
        self.emitir(f"  %{nombre} = alloca i32")
        self.emitir(f"  store i32 {valor}, i32* %{nombre}")
        return None
    
    def visitAsignacionPara(self, ctx: MiniLangParser.AsignacionParaContext):
        nombre = ctx.IDENTIFICADOR().getText()
        valor = self.visit(ctx.expresion())
        self.emitir(f"  store i32 {valor}, i32* %{nombre}")
        return None
    
    def visitActualizacionPara(self, ctx: MiniLangParser.ActualizacionParaContext):
        nombre = ctx.IDENTIFICADOR().getText()
        valor = self.visit(ctx.expresion())
        self.emitir(f"  store i32 {valor}, i32* %{nombre}")
        return None
    
    def visitSentenciaRetorna(self, ctx):
        if ctx.expresion():
            valor = self.visit(ctx.expresion())
            self.emitir(f"  ret i32 {valor}")
        else:
            self.emitir(f"  ret void")
        return None
    
    def visitLlamadaFuncion(self, ctx):
        nombre = ctx.IDENTIFICADOR().getText()
        args = []
        if ctx.expresion():
            for arg in ctx.expresion():
                args.append(self.visit(arg))
        
        info = self.funciones_info.get(nombre)
        if info and info["return"] == "vacio":
            args_str = ", ".join(f"i32 {a}" for a in args)
            self.emitir(f"  call void @{nombre}({args_str})")
        else:
            args_str = ", ".join(f"i32 {a}" for a in args)
            temp = self.nueva_llamada()
            self.emitir(f"  {temp} = call i32 @{nombre}({args_str})")
        return None
    
    def visitLlamadaFuncionExpr(self, ctx):
        nombre = ctx.IDENTIFICADOR().getText()
        args = []
        if ctx.expresion():
            for arg in ctx.expresion():
                args.append(self.visit(arg))
        
        args_str = ", ".join(f"i32 {a}" for a in args)
        temp = self.nueva_llamada()
        self.emitir(f"  {temp} = call i32 @{nombre}({args_str})")
        return temp
    
    def visitSentenciaBreak(self, ctx):
        if self.pila_ciclos:
            _, etiqueta_end = self.pila_ciclos[-1]
            self.emitir(f"  br label %{etiqueta_end}")
        return None
    
    def visitSentenciaContinue(self, ctx):
        if self.pila_ciclos:
            etiqueta_cond, _ = self.pila_ciclos[-1]
            self.emitir(f"  br label %{etiqueta_cond}")
        return None
    
    def visitSentenciaImportar(self, ctx):
        return None
    
    def visitAccesoArreglo(self, ctx):
        nombre = ctx.IDENTIFICADOR().getText()
        indice = self.visit(ctx.expresion())
        temp_ptr = self.nuevo_temporal()
        temp = self.nuevo_temporal()
        
        if nombre in self.variables:
            self.emitir(f"  {temp_ptr} = getelementptr i32, i32* %{nombre}, i32 {indice}")
            self.emitir(f"  {temp} = load i32, i32* {temp_ptr}")
            return temp
        return "0"
    
    def visitAccesoArregloExpr(self, ctx):
        return self.visit(ctx.accesoArreglo())
    
    def visitAsignacionArreglo(self, ctx: MiniLangParser.AsignacionArregloContext):
        acceso = ctx.accesoArreglo()
        nombre = acceso.IDENTIFICADOR().getText()
        indice = self.visit(acceso.expresion())
        valor = self.visit(ctx.expresion())
        temp_ptr = self.nuevo_temporal()
        
        if nombre in self.variables:
            self.emitir(f"  {temp_ptr} = getelementptr i32, i32* %{nombre}, i32 {indice}")
            self.emitir(f"  store i32 {valor}, i32* {temp_ptr}")
        return None
    
    def visitLiteralArreglo(self, ctx):
        valores = []
        if ctx.expresion():
            for expr in ctx.expresion():
                valores.append(self.visit(expr))
        return valores
    
    def visitMultiplicacionDivision(self, ctx):
        return self.visitMultiplicacionDivisionModulo(ctx)
