"""
Code generator for TyC.
"""

from typing import Any
from ..utils.nodes import *
from ..utils.visitor import BaseVisitor
from .emitter import *
from .frame import *
from .io import IO_SYMBOL_LIST
from .utils import *

class StringArrayType:
    """Marker type for JVM main(String[] args)."""
    pass

class CodeGenerator(BaseVisitor):
    """Minimal AST -> Jasmin code generator."""

    def __init__(self):
        self.emit = None
        self.functions = {}
        self.current_return_type = VoidType()
        self.class_name = "TyC"

    def _lookup_symbol(self, name: str, sym_list: list[Symbol]) -> Symbol:
        for sym in reversed(sym_list):
            if sym.name == name:
                return sym
        raise RuntimeError(f"Undeclared symbol: {name}")

    def _infer_type(self, node: Expr, o: Access):
        if isinstance(node, IntLiteral): return IntType()
        if isinstance(node, FloatLiteral): return FloatType()
        if isinstance(node, StringLiteral): return StringType()
        if isinstance(node, Identifier):
            return self._lookup_symbol(node.name, o.sym).type
        if isinstance(node, AssignExpr):
            return self._infer_type(node.rhs, o)
        if isinstance(node, FuncCall):
            return self.functions[node.name].type.return_type
        if isinstance(node, (PrefixOp, PostfixOp)):
            return self._infer_type(node.operand, o)
        if isinstance(node, BinaryOp):
            if node.operator in ["+", "-", "*", "/", "%"]:
                left_type = self._infer_type(node.left, o)
                right_type = self._infer_type(node.right, o)
                if is_float_type(left_type) or is_float_type(right_type):
                    return FloatType()
                return IntType()
            if node.operator in ["<", "<=", ">", ">=", "==", "!=", "&&", "||"]:
                return IntType()
        return IntType()

    def visit_program(self, node: Program, o: Any = None):
        self.emit = Emitter(f"{self.class_name}.j")
        self.emit.print_out(self.emit.emit_prolog(self.class_name))

        for io_sym in IO_SYMBOL_LIST:
            self.functions[io_sym.name] = io_sym

        for decl in node.decls:
            if isinstance(decl, FuncDecl):
                return_type = decl.return_type if decl.return_type else VoidType()
                param_types = [p.param_type for p in decl.params]
                self.functions[decl.name] = Symbol(
                    decl.name, FunctionType(param_types, return_type), CName(self.class_name)
                )

        for decl in node.decls:
            if isinstance(decl, FuncDecl):
                self.visit(decl, None)

        self.emit.emit_epilog()

    def visit_func_decl(self, node: FuncDecl, o: Any = None):
        self.current_return_type = node.return_type if node.return_type else VoidType()
        frame = Frame(node.name, self.current_return_type)
        frame.enter_scope(True)

        if node.name == "main":
            mtype = FunctionType([StringArrayType()], VoidType())
        else:
            mtype = FunctionType([p.param_type for p in node.params], self.current_return_type)

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

        if is_void_type(self.current_return_type):
            self.emit.print_out(self.emit.emit_return(VoidType(), frame))

        self.emit.print_out(self.emit.emit_label(end_label, frame))
        frame.exit_scope()
        self.emit.print_out(self.emit.emit_end_method(frame))

    def visit_block_stmt(self, node: BlockStmt, o: SubBody = None):
        for stmt in node.statements:
            self.visit(stmt, o)
        return o

    def visit_var_decl(self, node: VarDecl, o: SubBody = None):
        frame = o.frame
        idx = frame.get_new_index()
        var_type = node.var_type if node.var_type else self._infer_type(node.init_value, Access(frame, o.sym))
        self.emit.print_out(self.emit.emit_var(idx, node.name, var_type, frame.get_start_label(), frame.get_end_label()))
        if node.init_value:
            rhs_code, _ = self.visit(node.init_value, Access(frame, o.sym))
            self.emit.print_out(rhs_code)
            self.emit.print_out(self.emit.emit_write_var(node.name, var_type, idx, frame))
        o.sym.append(Symbol(node.name, var_type, Index(idx)))
        return o

    def visit_if_stmt(self, node: IfStmt, o: SubBody = None):
        frame = o.frame
        cond_code, _ = self.visit(node.condition, Access(frame, o.sym))
        else_label, end_label = frame.get_new_label(), frame.get_new_label()
        self.emit.print_out(cond_code)
        self.emit.print_out(self.emit.emit_if_false(else_label, frame))
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
        self.emit.print_out(cond_code)
        self.emit.print_out(self.emit.emit_if_false(end_label, frame))
        self.visit(node.body, o)
        self.emit.print_out(self.emit.emit_goto(start_label, frame))
        self.emit.print_out(self.emit.emit_label(end_label, frame))
        frame.exit_loop()
        return o

    def visit_for_stmt(self, node: ForStmt, o: SubBody = None):
        frame = o.frame
        if node.init: 
            self.visit(node.init, o)
            
        frame.enter_loop()
        cond_label, cont_label, brk_label = frame.get_new_label(), frame.get_continue_label(), frame.get_break_label()
        
        self.emit.print_out(self.emit.emit_label(cond_label, frame))
        if node.condition:
            cond_code, _ = self.visit(node.condition, Access(frame, o.sym))
            self.emit.print_out(cond_code)
            self.emit.print_out(self.emit.emit_if_false(brk_label, frame))
            
        self.visit(node.body, o)
        
        self.emit.print_out(self.emit.emit_label(cont_label, frame))
        if node.update: 
            upd_code, upd_typ = self.visit(node.update, Access(frame, o.sym))
            self.emit.print_out(upd_code)
            # Vì update là một biểu thức, nó có thể để lại giá trị thừa trên Stack, cần dọn dẹp (pop)
            if not is_void_type(upd_typ):
                self.emit.print_out(self.emit.emit_pop(frame))
                
        self.emit.print_out(self.emit.emit_goto(cond_label, frame))
        self.emit.print_out(self.emit.emit_label(brk_label, frame))
        
        frame.exit_loop()
        return o

    def visit_switch_stmt(self, node: SwitchStmt, o: SubBody = None):
        frame = o.frame
        frame.enter_loop()
        break_label = frame.get_break_label()
        expr_code, expr_type = self.visit(node.expr, Access(frame, o.sym))
        self.emit.print_out(expr_code)
        idx = frame.get_new_index()
        self.emit.print_out(self.emit.emit_write_var("switch_tmp", expr_type, idx, frame))
        case_labels = [frame.get_new_label() for _ in node.cases]
        default_label = frame.get_new_label() if node.default_case else break_label
        for i, case in enumerate(node.cases):
            self.emit.print_out(self.emit.emit_read_var("switch_tmp", expr_type, idx, frame))
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
    
    def visit_continue_stmt(self, node: ContinueStmt, o: SubBody = None):
        self.emit.print_out(self.emit.emit_goto(o.frame.get_continue_label(), o.frame))
    
    def visit_return_stmt(self, node: ReturnStmt, o: SubBody = None):
        if not node.expr: self.emit.print_out(self.emit.emit_return(VoidType(), o.frame))
        else:
            code, typ = self.visit(node.expr, Access(o.frame, o.sym))
            self.emit.print_out(code + self.emit.emit_return(typ, o.frame))
            
    def visit_expr_stmt(self, node: ExprStmt, o: SubBody = None):
        code, typ = self.visit(node.expr, Access(o.frame, o.sym))
        self.emit.print_out(code)
        if not is_void_type(typ): self.emit.print_out(self.emit.emit_pop(o.frame))

    def visit_binary_op(self, node: BinaryOp, o: Access = None):
        l_code, l_typ = self.visit(node.left, o)
        frame = o.frame
        if node.operator in ["&&", "||"]:
            f_lab, t_lab, e_lab = frame.get_new_label(), frame.get_new_label(), frame.get_new_label()
            code = l_code
            if node.operator == "&&": code += self.emit.emit_if_false(f_lab, frame)
            else: code += self.emit.emit_if_true(t_lab, frame)
            r_code, _ = self.visit(node.right, o)
            code += r_code + self.emit.emit_if_false(f_lab, frame) + self.emit.emit_label(t_lab, frame) + self.emit.emit_push_iconst(1, frame)
            code += self.emit.emit_goto(e_lab, frame) + self.emit.emit_label(f_lab, frame) + self.emit.emit_push_iconst(0, frame) + self.emit.emit_label(e_lab, frame)
            return code, IntType()
        r_code, r_typ = self.visit(node.right, o)
        res_typ = FloatType() if is_float_type(l_typ) or is_float_type(r_typ) else IntType()
        if node.operator in ["+", "-"]: return l_code + r_code + self.emit.emit_add_op(node.operator, res_typ, frame), res_typ
        if node.operator in ["*", "/"]: return l_code + r_code + self.emit.emit_mul_op(node.operator, res_typ, frame), res_typ
        if node.operator == "%": return l_code + r_code + self.emit.emit_mod(frame), IntType()
        return l_code + r_code + self.emit.emit_re_op(node.operator, res_typ, frame), IntType()

    def visit_prefix_op(self, node: PrefixOp, o: Access = None):
        code, typ = self.visit(node.operand, o)
        if node.operator == "-": return code + self.emit.emit_neg_op(typ, o.frame), typ
        if node.operator == "+": return code, typ
        if node.operator == "!": return code + self.emit.emit_push_iconst(0, o.frame) + self.emit.emit_re_op("==", typ, o.frame), IntType()
        if node.operator in ["++", "--"]:
            sym = self._lookup_symbol(node.operand.name, o.sym)
            inc = self.emit.emit_push_iconst(1, o.frame) if is_int_type(typ) else self.emit.emit_push_fconst("1.0", o.frame)
            res = code + inc + self.emit.emit_add_op("+" if node.operator == "++" else "-", typ, o.frame) + self.emit.emit_dup(o.frame) + self.emit.emit_write_var(node.operand.name, typ, sym.value.value, o.frame)
            return res, typ
        return code, typ

    def visit_postfix_op(self, node: PostfixOp, o: Access = None):
        sym = self._lookup_symbol(node.operand.name, o.sym)
        code, typ = self.visit(node.operand, o)
        inc = self.emit.emit_push_iconst(1, o.frame) if is_int_type(typ) else self.emit.emit_push_fconst("1.0", o.frame)
        res = code + self.emit.emit_dup(o.frame) + inc + self.emit.emit_add_op("+" if node.operator == "++" else "-", typ, o.frame) + self.emit.emit_write_var(node.operand.name, typ, sym.value.value, o.frame)
        return res, typ

    def visit_assign_expr(self, node: AssignExpr, o: Access = None):
        r_code, r_typ = self.visit(node.rhs, o)
        sym = self._lookup_symbol(node.lhs.name, o.sym)
        return r_code + self.emit.emit_dup(o.frame) + self.emit.emit_write_var(node.lhs.name, sym.type, sym.value.value, o.frame), r_typ

    def visit_func_call(self, node: FuncCall, o: Access = None):
        sym = self.functions[node.name]
        code = "".join([self.visit(a, o)[0] for a in node.args])
        return code + self.emit.emit_invoke_static(f"{sym.value.value}/{node.name}", sym.type, o.frame), sym.type.return_type

    def visit_identifier(self, node: Identifier, o: Access = None):
        sym = self._lookup_symbol(node.name, o.sym)
        return self.emit.print_out("") or self.emit.emit_read_var(node.name, sym.type, sym.value.value, o.frame), sym.type
    def visit_int_literal(self, node: IntLiteral, o: Access = None): return self.emit.emit_push_iconst(node.value, o.frame), IntType()
    def visit_float_literal(self, node: FloatLiteral, o: Access = None): return self.emit.emit_push_fconst(str(node.value), o.frame), FloatType()
    def visit_string_literal(self, node: StringLiteral, o: Access = None): return self.emit.emit_push_const(node.value, StringType(), o.frame), StringType()
    def visit_case_stmt(self, node, o): pass
    def visit_default_stmt(self, node, o): pass
    def visit_struct_decl(self, node, o): pass
    def visit_member_decl(self, node, o): pass
    def visit_param(self, node, o): pass
    def visit_int_type(self, node, o): return node
    def visit_float_type(self, node, o): return node
    def visit_string_type(self, node, o): return node
    def visit_void_type(self, node, o): return node
    def visit_struct_type(self, node, o): return node
    def visit_member_access(self, node, o): raise RuntimeError("Not supported in minimal codegen")
    def visit_struct_literal(self, node, o): raise RuntimeError("Not supported in minimal codegen")
