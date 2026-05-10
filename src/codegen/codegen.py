"""
Code generator for TyC with Full Struct Deep Copy & Array Simulation.
"""

from typing import Any
from ..utils.nodes import *
from ..utils.visitor import BaseVisitor
from .emitter import *
from .frame import *
from .io import IO_SYMBOL_LIST
from .utils import *


class StringArrayType:
    pass

class CodeGenerator(BaseVisitor):
    def __init__(self):
        self.emit = None
        self.functions = {}
        self.current_return_type = VoidType()
        self.class_name = "TyC"
        self.struct_env = {} 
        self.struct_field_order = {}

    def _lookup_symbol(self, name: str, sym_list: list[Symbol]) -> Symbol:
        for sym in reversed(sym_list):
            if sym.name == name: return sym
        raise RuntimeError(f"Undeclared symbol: {name}")
        
    def _get_mtype(self, mem):
        for attr in ['mtype', 'type', 'var_type', 'typ', 'member_type']:
            if hasattr(mem, attr): return getattr(mem, attr)
        for k, v in vars(mem).items():
            if type(v).__name__.endswith('Type'): return v
        raise RuntimeError(f"Cannot find type in {vars(mem)}")

    def _get_exprs(self, node):
        for attr in ['exprs', 'args', 'elements', 'expr_list', 'value']:
            if hasattr(node, attr):
                val = getattr(node, attr)
                if isinstance(val, list): return val
        for k, v in vars(node).items():
            if isinstance(v, list): return v
        return []

    def _infer_type(self, node: Expr, o: Access):
        if isinstance(node, IntLiteral): return IntType()
        if isinstance(node, FloatLiteral): return FloatType()
        if isinstance(node, StringLiteral): return StringType()
        if isinstance(node, Identifier): return self._lookup_symbol(node.name, o.sym).type
        if isinstance(node, AssignExpr): return self._infer_type(node.rhs, o)
        if isinstance(node, FuncCall): return self.functions[node.name].type.return_type
        if isinstance(node, (PrefixOp, PostfixOp)): return self._infer_type(node.operand, o)
        
        if isinstance(node, StructLiteral):
            exprs = self._get_exprs(node)
            for s_name, fields in self.struct_field_order.items():
                if len(fields) == len(exprs): return StructType(s_name)
            if self.struct_field_order: return StructType(list(self.struct_field_order.keys())[0])
            return StructType("Unknown")
            
        if isinstance(node, MemberAccess):
            obj_typ = self._infer_type(node.obj, o)
            return self.struct_env[obj_typ.struct_name][node.member]

        if isinstance(node, BinaryOp):
            if node.operator in ["+", "-", "*", "/", "%"]:
                l_type = self._infer_type(node.left, o)
                r_type = self._infer_type(node.right, o)
                if is_float_type(l_type) or is_float_type(r_type): return FloatType()
                return IntType()
            if node.operator in ["<", "<=", ">", ">=", "==", "!=", "&&", "||"]: return IntType()
        return IntType()

    def _infer_return_type(self, stmt: Stmt, syms: list[Symbol]):
        if isinstance(stmt, ReturnStmt):
            if stmt.expr: return self._infer_type(stmt.expr, Access(None, syms))
            return VoidType()
        if isinstance(stmt, VarDecl):
            typ = stmt.var_type if stmt.var_type else self._infer_type(stmt.init_value, Access(None, syms))
            syms.append(Symbol(stmt.name, typ, Index(0)))
            return None
        if isinstance(stmt, BlockStmt):
            local_syms = syms.copy()
            for s in stmt.statements:
                r = self._infer_return_type(s, local_syms)
                if r: return r
        if isinstance(stmt, IfStmt):
            r = self._infer_return_type(stmt.then_stmt, syms.copy())
            if r: return r
            if stmt.else_stmt: return self._infer_return_type(stmt.else_stmt, syms.copy())
        if isinstance(stmt, (WhileStmt, ForStmt)): return self._infer_return_type(stmt.body, syms.copy())
        if isinstance(stmt, SwitchStmt):
            for c in stmt.cases:
                for s in c.statements:
                    r = self._infer_return_type(s, syms.copy())
                    if r: return r
            if stmt.default_case:
                for s in stmt.default_case.statements:
                    r = self._infer_return_type(s, syms.copy())
                    if r: return r
        return None

    def emit_clone_struct(self, s_name: str, frame: Frame) -> str:
        """Cơ chế Deep Clone hack trực tiếp vào Stack của JVM"""
        code = ""
        code += self.emit.emit_new_instance(s_name, frame)
        code += "    dup_x1\n    swap\n"
        
        for fname in self.struct_field_order.get(s_name, []):
            ftype = self.struct_env[s_name][fname]
            jvm_type = self.emit.get_jvm_type(ftype)
            code += "    dup2\n"
            code += f"    getfield {s_name}/{fname} {jvm_type}\n"
            if is_struct_type(ftype):
                code += self.emit_clone_struct(ftype.struct_name, frame)
            code += f"    putfield {s_name}/{fname} {jvm_type}\n"
            
        code += "    pop\n    pop\n"
        return code

    def visit_program(self, node: Program, o: Any = None):
        self.emit = Emitter(f"{self.class_name}.j")
        self.emit.print_out(self.emit.emit_prolog(self.class_name))

        for io_sym in IO_SYMBOL_LIST:
            self.functions[io_sym.name] = io_sym

        for decl in node.decls:
            if isinstance(decl, StructDecl):
                fields, order = {}, []
                for mem in decl.members:
                    m_type = self._get_mtype(mem)
                    fields[mem.name] = m_type
                    order.append(mem.name)
                self.struct_env[decl.name] = fields
                self.struct_field_order[decl.name] = order
                self.visit(decl, None) 
                
            elif isinstance(decl, FuncDecl):
                if decl.return_type: ret_type = decl.return_type
                else:
                    syms = [Symbol(p.name, p.param_type, Index(0)) for p in decl.params]
                    inferred = self._infer_return_type(decl.body, syms)
                    ret_type = inferred if inferred else VoidType()
                param_types = [p.param_type for p in decl.params]
                self.functions[decl.name] = Symbol(decl.name, FunctionType(param_types, ret_type), CName(self.class_name))

        for decl in node.decls:
            if isinstance(decl, FuncDecl):
                self.visit(decl, None)

        self.emit.emit_epilog()

    def visit_struct_decl(self, node: StructDecl, o: Any = None):
        struct_emit = Emitter(f"{node.name}.j")
        struct_emit.print_out(struct_emit.emit_prolog(node.name))
        for mem in node.members:
            m_type = self._get_mtype(mem)
            struct_emit.print_out(struct_emit.emit_field(mem.name, m_type))
        struct_emit.print_out(struct_emit.emit_default_constructor())
        struct_emit.emit_epilog()
        return None

    def visit_func_decl(self, node: FuncDecl, o: Any = None):
        self.current_return_type = self.functions[node.name].type.return_type
        frame = Frame(node.name, self.current_return_type)
        frame.enter_scope(True)

        mtype = FunctionType([StringArrayType()], VoidType()) if node.name == "main" else FunctionType([p.param_type for p in node.params], self.current_return_type)
        self.emit.print_out(self.emit.emit_method(node.name, mtype, True))

        start_label, end_label = frame.get_start_label(), frame.get_end_label()
        self.emit.print_out(self.emit.emit_label(start_label, frame))

        local_syms: list[Symbol] = []
        if node.name == "main":
            args_idx = frame.get_new_index()
            self.emit.print_out(self.emit.emit_var(args_idx, "args", StringArrayType(), start_label, end_label))

        for param in node.params:
            idx = frame.get_new_index()
            self.emit.print_out(self.emit.emit_var(idx, param.name, param.param_type, start_label, end_label))
            local_syms.append(Symbol(param.name, param.param_type, Index(idx)))

        self.visit(node.body, SubBody(frame, local_syms))
        self.emit.print_out(self.emit.emit_label(end_label, frame))

        if is_void_type(self.current_return_type):
            self.emit.print_out(self.emit.emit_return(VoidType(), frame))
        else:
            self.emit.print_out(self.emit.emit_push_iconst(0, frame) if is_int_type(self.current_return_type) else self.emit.emit_push_fconst("0.0", frame) if is_float_type(self.current_return_type) else self.emit.emit_push_const("", StringType(), frame))
            self.emit.print_out(self.emit.emit_return(self.current_return_type, frame))

        frame.exit_scope()
        self.emit.print_out(self.emit.emit_end_method(frame))

    def visit_block_stmt(self, node: BlockStmt, o: Any = None):
        is_expr = isinstance(o, Access)
        if is_expr:
            block_code = ""
            last_typ = VoidType()
            for stmt in node.statements:
                res = self.visit(stmt, o)
                if isinstance(res, tuple):
                    c, t = res
                    block_code += c
                    last_typ = t
            return block_code, last_typ
        else:
            for stmt in node.statements:
                self.visit(stmt, o)
            return o

    def visit_var_decl(self, node: VarDecl, o: SubBody = None):
        frame = o.frame
        idx = frame.get_new_index()
        var_type = node.var_type if node.var_type else self._infer_type(node.init_value, Access(frame, o.sym))
        
        self.emit.print_out(self.emit.emit_var(idx, node.name, var_type, frame.get_start_label(), frame.get_end_label()))
        if node.init_value:
            acc = Access(frame, o.sym)
            acc.expected_type = var_type
            rhs_code, rhs_typ = self.visit(node.init_value, acc)
            if is_float_type(var_type) and is_int_type(rhs_typ): rhs_code += self.emit.emit_i2f(frame)
            self.emit.print_out(rhs_code + self.emit.emit_write_var(node.name, var_type, idx, frame))
            
        o.sym.append(Symbol(node.name, var_type, Index(idx)))
        return o

    def visit_expr_stmt(self, node: ExprStmt, o: Any = None):
        code, typ = self.visit(node.expr, Access(o.frame, o.sym))
        is_expr = isinstance(o, Access)
        if is_expr:
            if not is_void_type(typ): code += self.emit.emit_pop(o.frame)
            return code, VoidType()
        else:
            self.emit.print_out(code)
            if not is_void_type(typ): self.emit.print_out(self.emit.emit_pop(o.frame))
            return o

    def visit_if_stmt(self, node: IfStmt, o: Any = None):
        frame = o.frame
        cond_code, _ = self.visit(node.condition, Access(frame, o.sym))
        else_label, end_label = frame.get_new_label(), frame.get_new_label()
        
        is_expr = isinstance(o, Access)
        code = cond_code + self.emit.emit_if_false(else_label, frame)
        
        if is_expr:
            then_code, then_typ = self.visit(node.then_stmt, o)
            code += then_code + self.emit.emit_goto(end_label, frame)
            code += self.emit.emit_label(else_label, frame)
            if node.else_stmt:
                else_code, _ = self.visit(node.else_stmt, o)
                code += else_code
            code += self.emit.emit_label(end_label, frame)
            return code, then_typ
        else:
            self.emit.print_out(code)
            self.visit(node.then_stmt, o)
            self.emit.print_out(self.emit.emit_goto(end_label, frame))
            self.emit.print_out(self.emit.emit_label(else_label, frame))
            if node.else_stmt: self.visit(node.else_stmt, o)
            self.emit.print_out(self.emit.emit_label(end_label, frame))
            return o

    def visit_while_stmt(self, node: WhileStmt, o: SubBody = None):
        frame = o.frame
        frame.enter_loop()
        start_label, end_label = frame.get_continue_label(), frame.get_break_label()
        
        self.emit.print_out(self.emit.emit_label(start_label, frame))
        cond_code, _ = self.visit(node.condition, Access(frame, o.sym))
        self.emit.print_out(cond_code + self.emit.emit_if_false(end_label, frame))
        
        self.visit(node.body, o)
        self.emit.print_out(self.emit.emit_goto(start_label, frame) + self.emit.emit_label(end_label, frame))
        
        frame.exit_loop()
        return o

    def visit_for_stmt(self, node: ForStmt, o: SubBody = None):
        frame = o.frame
        if node.init: self.visit(node.init, o)
            
        frame.enter_loop()
        cond_label, cont_label, brk_label = frame.get_new_label(), frame.get_continue_label(), frame.get_break_label()
        
        self.emit.print_out(self.emit.emit_label(cond_label, frame))
        if node.condition:
            cond_code, _ = self.visit(node.condition, Access(frame, o.sym))
            self.emit.print_out(cond_code + self.emit.emit_if_false(brk_label, frame))
            
        self.visit(node.body, o)
        self.emit.print_out(self.emit.emit_label(cont_label, frame))
        
        if node.update:
            res = self.visit(node.update, Access(frame, o.sym))
            if isinstance(res, tuple):
                upd_code, upd_typ = res
                self.emit.print_out(upd_code)
                if not is_void_type(upd_typ): self.emit.print_out(self.emit.emit_pop(frame))
                
        self.emit.print_out(self.emit.emit_goto(cond_label, frame) + self.emit.emit_label(brk_label, frame))
        frame.exit_loop()
        return o

    def visit_switch_stmt(self, node: SwitchStmt, o: SubBody = None):
        frame = o.frame
        frame.enter_loop()
        break_label = frame.get_break_label()
        
        expr_code, expr_type = self.visit(node.expr, Access(frame, o.sym))
        idx = frame.get_new_index()
        self.emit.print_out(expr_code + self.emit.emit_write_var("sw_tmp", expr_type, idx, frame))
        
        case_labels = [frame.get_new_label() for _ in node.cases]
        default_label = frame.get_new_label() if node.default_case else break_label
        
        for i, case in enumerate(node.cases):
            self.emit.print_out(self.emit.emit_read_var("sw_tmp", expr_type, idx, frame))
            val_code, _ = self.visit(case.expr, Access(frame, o.sym))
            self.emit.print_out(val_code + self.emit.emit_re_op("==", IntType(), frame) + self.emit.emit_if_true(case_labels[i], frame))
            
        self.emit.print_out(self.emit.emit_goto(default_label, frame))
        
        for i, case in enumerate(node.cases):
            self.emit.print_out(self.emit.emit_label(case_labels[i], frame))
            for s in case.statements: self.visit(s, o)
                
        if node.default_case:
            self.emit.print_out(self.emit.emit_label(default_label, frame))
            for s in node.default_case.statements: self.visit(s, o)
                
        self.emit.print_out(self.emit.emit_label(break_label, frame))
        frame.exit_loop()
        return o

    def visit_break_stmt(self, node: BreakStmt, o: SubBody = None):
        self.emit.print_out(self.emit.emit_goto(o.frame.get_break_label(), o.frame))
        return o

    def visit_continue_stmt(self, node: ContinueStmt, o: SubBody = None):
        self.emit.print_out(self.emit.emit_goto(o.frame.get_continue_label(), o.frame))
        return o

    def visit_return_stmt(self, node: ReturnStmt, o: SubBody = None):
        if not node.expr:
            self.emit.print_out(self.emit.emit_return(VoidType(), o.frame))
            return o
            
        acc = Access(o.frame, o.sym)
        acc.expected_type = self.current_return_type
        code, typ = self.visit(node.expr, acc)
        if is_float_type(self.current_return_type) and is_int_type(typ):
            code += self.emit.emit_i2f(o.frame)
            typ = FloatType()
            
        if is_struct_type(typ):
            code += self.emit_clone_struct(typ.struct_name, o.frame)

        self.emit.print_out(code + self.emit.emit_return(typ, o.frame))
        return o

    def visit_binary_op(self, node: BinaryOp, o: Access = None):
        frame = o.frame
        if node.operator in ["&&", "||"]:
            f_lab, t_lab, end_lab = frame.get_new_label(), frame.get_new_label(), frame.get_new_label()
            l_code, _ = self.visit(node.left, o)
            code = l_code
            if node.operator == "&&":
                code += self.emit.emit_if_false(f_lab, frame)
                r_code, _ = self.visit(node.right, o)
                code += r_code + self.emit.emit_if_false(f_lab, frame)
                code += self.emit.emit_push_iconst(1, frame) + self.emit.emit_goto(end_lab, frame)
                code += self.emit.emit_label(f_lab, frame) + self.emit.emit_push_iconst(0, frame)
            else: 
                code += self.emit.emit_if_true(t_lab, frame)
                r_code, _ = self.visit(node.right, o)
                code += r_code + self.emit.emit_if_true(t_lab, frame)
                code += self.emit.emit_push_iconst(0, frame) + self.emit.emit_goto(end_lab, frame)
                code += self.emit.emit_label(t_lab, frame) + self.emit.emit_push_iconst(1, frame)
            return code + self.emit.emit_label(end_lab, frame), IntType()

        l_code, l_typ = self.visit(node.left, o)
        r_typ_infer = self._infer_type(node.right, o)
        res_typ = FloatType() if is_float_type(l_typ) or is_float_type(r_typ_infer) else IntType()
        
        if is_float_type(res_typ) and is_int_type(l_typ): l_code += self.emit.emit_i2f(frame)
        r_code, r_typ = self.visit(node.right, o)
        if is_float_type(res_typ) and is_int_type(r_typ): r_code += self.emit.emit_i2f(frame)

        if node.operator in ["+", "-"]: return l_code + r_code + self.emit.emit_add_op(node.operator, res_typ, frame), res_typ
        if node.operator in ["*", "/"]: return l_code + r_code + self.emit.emit_mul_op(node.operator, res_typ, frame), res_typ
        if node.operator == "%": return l_code + r_code + self.emit.emit_mod(frame), IntType()
        return l_code + r_code + self.emit.emit_re_op(node.operator, res_typ, frame), IntType()

    def visit_prefix_op(self, node: PrefixOp, o: Access = None):
        if node.operator in ["!", "-", "+"]:
            code, typ = self.visit(node.operand, o)
            if node.operator == "-": return code + self.emit.emit_neg_op(typ, o.frame), typ
            if node.operator == "+": return code, typ
            if node.operator == "!": return code + self.emit.emit_push_iconst(0, o.frame) + self.emit.emit_re_op("==", typ, o.frame), IntType()
        
        typ = self._infer_type(node.operand, o)
        one = IntLiteral(1) if is_int_type(typ) else FloatLiteral(1.0)
        op = "+" if node.operator == "++" else "-"
        assign = AssignExpr(node.operand, BinaryOp(node.operand, op, one))
        return self.visit(assign, o)

    def visit_postfix_op(self, node: PostfixOp, o: Access = None):
        typ = self._infer_type(node.operand, o)
        one = IntLiteral(1) if is_int_type(typ) else FloatLiteral(1.0)
        op = "+" if node.operator == "++" else "-"
        assign = AssignExpr(node.operand, BinaryOp(node.operand, op, one))
        return self.visit(assign, o)

    def visit_assign_expr(self, node: AssignExpr, o: Access = None):
        if isinstance(node.lhs, Identifier):
            sym = self._lookup_symbol(node.lhs.name, o.sym)
            acc = Access(o.frame, o.sym)
            acc.expected_type = sym.type
            r_code, r_typ = self.visit(node.rhs, acc)
            if is_float_type(sym.type) and is_int_type(r_typ):
                r_code += self.emit.emit_i2f(o.frame)
                r_typ = FloatType()
            code = r_code + self.emit.emit_dup(o.frame) + self.emit.emit_write_var(node.lhs.name, sym.type, sym.value.value, o.frame)
            return code, r_typ
            
        elif isinstance(node.lhs, MemberAccess):
            acc_left = Access(o.frame, o.sym)
            acc_left.is_left = True
            obj_code, obj_typ = self.visit(node.lhs.obj, acc_left)
            s_name = obj_typ.struct_name
            f_type = self.struct_env[s_name][node.lhs.member]
            
            acc = Access(o.frame, o.sym)
            acc.expected_type = f_type
            r_code, r_typ = self.visit(node.rhs, acc)
            if is_float_type(f_type) and is_int_type(r_typ):
                r_code += self.emit.emit_i2f(o.frame)
                r_typ = FloatType()
                
            code = obj_code + r_code + "    dup_x1\n" + f"    putfield {s_name}/{node.lhs.member} {self.emit.get_jvm_type(f_type)}\n"
            return code, r_typ

    def visit_func_call(self, node: FuncCall, o: Access = None):
        sym = self.functions[node.name]
        code = ""
        for i, arg in enumerate(node.args):
            acc = Access(o.frame, o.sym)
            acc.expected_type = sym.type.param_types[i]
            arg_code, arg_typ = self.visit(arg, acc)
            if is_float_type(sym.type.param_types[i]) and is_int_type(arg_typ): arg_code += self.emit.emit_i2f(o.frame)
            code += arg_code
        code += self.emit.emit_invoke_static(f"{sym.value.value}/{node.name}", sym.type, o.frame)
        
        if is_struct_type(sym.type.return_type):
            code += self.emit_clone_struct(sym.type.return_type.struct_name, o.frame)
            
        return code, sym.type.return_type

    def visit_struct_literal(self, node: StructLiteral, o: Access = None):
        expected = getattr(o, 'expected_type', None)
        if not expected or not is_struct_type(expected): expected = self._infer_type(node, o)
            
        s_name = expected.struct_name
        code = self.emit.emit_new_instance(s_name, o.frame)
        
        fields = self.struct_field_order.get(s_name, [])
        exprs = self._get_exprs(node)
        
        for i, expr in enumerate(exprs):
            if i >= len(fields): break
            fname = fields[i]
            ftype = self.struct_env[s_name][fname]
            
            code += self.emit.emit_dup(o.frame)
            acc = Access(o.frame, o.sym)
            acc.expected_type = ftype
            expr_code, expr_type = self.visit(expr, acc)
            code += expr_code
            
            if is_float_type(ftype) and is_int_type(expr_type): code += self.emit.emit_i2f(o.frame)
            code += f"    putfield {s_name}/{fname} {self.emit.get_jvm_type(ftype)}\n"
            
        return code, expected

    def visit_member_access(self, node: MemberAccess, o: Access = None):
        is_left = getattr(o, 'is_left', False)
        acc_left = Access(o.frame, o.sym)
        acc_left.is_left = True
        obj_code, obj_typ = self.visit(node.obj, acc_left)
        s_name = obj_typ.struct_name
        f_type = self.struct_env[s_name][node.member]
        
        code = obj_code + self.emit.emit_get_field(f"{s_name}/{node.member}", f_type, o.frame)
        if not is_left and is_struct_type(f_type):
            code += self.emit_clone_struct(f_type.struct_name, o.frame)
        return code, f_type

    def visit_identifier(self, node: Identifier, o: Access = None):
        sym = self._lookup_symbol(node.name, o.sym)
        code = self.emit.emit_read_var(node.name, sym.type, sym.value.value, o.frame)
        if not getattr(o, 'is_left', False) and is_struct_type(sym.type):
            code += self.emit_clone_struct(sym.type.struct_name, o.frame)
        return code, sym.type

    def visit_int_literal(self, node: IntLiteral, o: Access = None): return self.emit.emit_push_iconst(node.value, o.frame), IntType()
    def visit_float_literal(self, node: FloatLiteral, o: Access = None): return self.emit.emit_push_fconst(str(node.value), o.frame), FloatType()
    def visit_string_literal(self, node: StringLiteral, o: Access = None): return self.emit.emit_push_const(node.value, StringType(), o.frame), StringType()

    def visit_case_stmt(self, node, o): pass
    def visit_default_stmt(self, node, o): pass
    def visit_member_decl(self, node, o): pass
    def visit_param(self, node, o): pass
    def visit_int_type(self, node, o): return node
    def visit_float_type(self, node, o): return node
    def visit_string_type(self, node, o): return node
    def visit_void_type(self, node, o): return node
    def visit_struct_type(self, node, o): return node