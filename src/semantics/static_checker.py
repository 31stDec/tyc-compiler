"""
Static Semantic Checker for TyC Programming Language

This module implements a comprehensive static semantic checker using visitor pattern
for the TyC procedural programming language. It performs type checking,
scope management, type inference, and detects all semantic errors as
specified in the TyC language specification.
"""

from functools import reduce
from typing import (
    Dict,
    List,
    Set,
    Optional,
    Any,
    Tuple,
    NamedTuple,
    Union,
    TYPE_CHECKING,
)
from ..utils.visitor import ASTVisitor
from ..utils.nodes import (
    ASTNode,
    Program,
    StructDecl,
    MemberDecl,
    FuncDecl,
    Param,
    VarDecl,
    IfStmt,
    WhileStmt,
    ForStmt,
    BreakStmt,
    ContinueStmt,
    ReturnStmt,
    BlockStmt,
    SwitchStmt,
    CaseStmt,
    DefaultStmt,
    Type,
    IntType,
    FloatType,
    StringType,
    VoidType,
    StructType,
    BinaryOp,
    PrefixOp,
    PostfixOp,
    AssignExpr,
    MemberAccess,
    FuncCall,
    Identifier,
    StructLiteral,
    IntLiteral,
    FloatLiteral,
    StringLiteral,
    ExprStmt,
    Expr,
    Stmt,
    Decl,
)

# Type aliases for better type hints
TyCType = Union[IntType, FloatType, StringType, VoidType, StructType]
from .static_error import (
    StaticError,
    Redeclared,
    UndeclaredIdentifier,
    UndeclaredFunction,
    UndeclaredStruct,
    TypeCannotBeInferred,
    TypeMismatchInStatement,
    TypeMismatchInExpression,
    MustInLoop,
)

class AutoType(Type):
    def __init__(self):
        self.inferred_type = None
    
    def accept(self, visitor, o=None):
        return self

    def __str__(self):
        return str(self.inferred_type) if self.inferred_type else "AutoType"

class Symbol:
    pass

class VarSymbol(Symbol):
    def __init__(self, typ: Type):
        self.typ = typ

class FuncSymbol(Symbol):
    def __init__(self, params: List[Type], return_type: Type):
        self.params = params
        self.return_type = return_type

class StructSymbol(Symbol):
    def __init__(self, members: Dict[str, Type]):
        self.members = members

class StaticChecker(ASTVisitor):
    def __init__(self):
        self.envs: List[Dict[str, VarSymbol]] = [{}]
        self.funcs: Dict[str, FuncSymbol] = {}
        self.structs: Dict[str, StructSymbol] = {}
        self.loop_depth = 0
        self.switch_depth = 0
        self.current_func_name = None

        self.funcs["readInt"] = FuncSymbol([], IntType())
        self.funcs["readFloat"] = FuncSymbol([], FloatType())
        self.funcs["readString"] = FuncSymbol([], StringType())
        self.funcs["printInt"] = FuncSymbol([IntType()], VoidType())
        self.funcs["printFloat"] = FuncSymbol([FloatType()], VoidType())
        self.funcs["printString"] = FuncSymbol([StringType()], VoidType())

    def check_program(self, ast):
        self.visit(ast, None)
        return []

    def enter_scope(self):
        self.envs.append({})

    def exit_scope(self):
        self.envs.pop()

    def lookup_var(self, name: str) -> Optional[VarSymbol]:
        for scope in reversed(self.envs):
            if name in scope:
                return scope[name]
        return None

    def are_types_equal(self, t1: Type, t2: Type) -> bool:
        if type(t1) is type(t2):
            if isinstance(t1, StructType) and isinstance(t2, StructType):
                return t1.struct_name == t2.struct_name
            return True
        return False

    def check_struct_literal(self, literal: StructLiteral, expected_type: Type):
        if not isinstance(expected_type, StructType):
            raise TypeMismatchInExpression(literal)
        struct_sym = self.structs.get(expected_type.struct_name)
        if not struct_sym:
            raise UndeclaredStruct(expected_type.struct_name)
        if len(literal.values) != len(struct_sym.members):
            raise TypeMismatchInExpression(literal)
        
        for val, expected_mtype in zip(literal.values, struct_sym.members.values()):
            val_type = self.visit(val, None)
            if isinstance(val_type, StructLiteral):
                val_type = self.check_struct_literal(val_type, expected_mtype)
            if isinstance(val_type, AutoType) and val_type.inferred_type is None:
                val_type.inferred_type = expected_mtype
                val_type = expected_mtype
            if not self.are_types_equal(expected_mtype, val_type):
                raise TypeMismatchInExpression(literal)
        return expected_type

    def visit_program(self, node: "Program", o: Any = None):
        for decl in node.decls:
            if isinstance(decl, StructDecl):
                if decl.name in self.structs:
                    raise Redeclared("Struct", decl.name)
                members = {}
                for m in decl.members:
                    if m.name in members:
                        raise Redeclared("Member", m.name)
                    if isinstance(m.member_type, StructType):
                        if m.member_type.struct_name not in self.structs:
                            raise UndeclaredStruct(m.member_type.struct_name)
                    members[m.name] = m.member_type
                self.structs[decl.name] = StructSymbol(members)
            elif isinstance(decl, FuncDecl):
                if decl.name in self.funcs:
                    raise Redeclared("Function", decl.name)
                param_types = []
                param_names = set()
                for p in decl.params:
                    if p.name in param_names:
                        raise Redeclared("Parameter", p.name)
                    param_names.add(p.name)
                    if isinstance(p.param_type, StructType):
                        if p.param_type.struct_name not in self.structs:
                            raise UndeclaredStruct(p.param_type.struct_name)
                    param_types.append(p.param_type)
                ret_type = decl.return_type if decl.return_type else AutoType()
                if isinstance(ret_type, StructType):
                    if ret_type.struct_name not in self.structs:
                        raise UndeclaredStruct(ret_type.struct_name)
                self.funcs[decl.name] = FuncSymbol(param_types, ret_type)

        for decl in node.decls:
            if isinstance(decl, FuncDecl):
                self.visit(decl, o)

    def visit_struct_decl(self, node: "StructDecl", o: Any = None):
        pass

    def visit_member_decl(self, node: "MemberDecl", o: Any = None):
        pass

    def visit_param(self, node: "Param", o: Any = None):
        pass

    def visit_func_decl(self, node: "FuncDecl", o: Any = None):
        self.current_func_name = node.name
        self.enter_scope()
        for param in node.params:
            self.envs[-1][param.name] = VarSymbol(param.param_type)

        if isinstance(node.body, BlockStmt):
            for stmt in node.body.statements:
                self.visit(stmt, o)
        elif isinstance(node.body, list):
            for stmt in node.body:
                self.visit(stmt, o)

        for var_name, var_sym in self.envs[-1].items():
            if isinstance(var_sym.typ, AutoType) and var_sym.typ.inferred_type is None:
                raise TypeCannotBeInferred(node.body)

        self.exit_scope()
        self.current_func_name = None

    # Type system
    def visit_int_type(self, node: "IntType", o: Any = None):
        return IntType()

    def visit_float_type(self, node: "FloatType", o: Any = None):
        return FloatType()

    def visit_string_type(self, node: "StringType", o: Any = None):
        return StringType()

    def visit_void_type(self, node: "VoidType", o: Any = None):
        return VoidType()

    def visit_struct_type(self, node: "StructType", o: Any = None):
        if node.struct_name not in self.structs:
            raise UndeclaredStruct(node.struct_name)
        return node

    # Statements
    def visit_block_stmt(self, node: "BlockStmt", o: Any = None):
        self.enter_scope()
        for stmt in node.statements:
            self.visit(stmt, o)
        for var_name, var_sym in self.envs[-1].items():
            if isinstance(var_sym.typ, AutoType) and var_sym.typ.inferred_type is None:
                raise TypeCannotBeInferred(node)
        self.exit_scope()

    def visit_var_decl(self, node: "VarDecl", o: Any = None):
        if node.name in self.envs[-1]:
            raise Redeclared("Variable", node.name)
        init_type = self.visit(node.init_value, o) if node.init_value else None
        
        if node.var_type:
            decl_type = self.visit(node.var_type, o)
            if node.init_value:
                if isinstance(init_type, StructLiteral):
                    init_type = self.check_struct_literal(init_type, decl_type)
                if isinstance(init_type, AutoType) and init_type.inferred_type is None:
                    init_type.inferred_type = decl_type
                    init_type = decl_type
                if not self.are_types_equal(decl_type, init_type):
                    raise TypeMismatchInStatement(node)
            self.envs[-1][node.name] = VarSymbol(decl_type)
        else:
            var_type = AutoType()
            if node.init_value:
                if isinstance(init_type, StructLiteral):
                    raise TypeCannotBeInferred(node.init_value)
                if isinstance(init_type, AutoType) and init_type.inferred_type is None:
                    raise TypeCannotBeInferred(node.init_value)
                var_type.inferred_type = init_type
            self.envs[-1][node.name] = VarSymbol(var_type)

    def visit_if_stmt(self, node: "IfStmt", o: Any = None):
        cond_type = self.visit(node.condition, o)
        if isinstance(cond_type, AutoType) and cond_type.inferred_type is None:
            raise TypeCannotBeInferred(node.condition)
        if not isinstance(cond_type, IntType):
            raise TypeMismatchInStatement(node)
        self.visit(node.then_stmt, o)
        if node.else_stmt:
            self.visit(node.else_stmt, o)

    def visit_while_stmt(self, node: "WhileStmt", o: Any = None):
        cond_type = self.visit(node.condition, o)
        if isinstance(cond_type, AutoType) and cond_type.inferred_type is None:
            raise TypeCannotBeInferred(node.condition)
        if not isinstance(cond_type, IntType):
            raise TypeMismatchInStatement(node)
        self.loop_depth += 1
        self.visit(node.body, o)
        self.loop_depth -= 1

    def visit_for_stmt(self, node: "ForStmt", o: Any = None):
        self.enter_scope()
        if node.init:
            self.visit(node.init, o)
        if node.condition:
            cond_type = self.visit(node.condition, o)
            if isinstance(cond_type, AutoType) and cond_type.inferred_type is None:
                raise TypeCannotBeInferred(node.condition)
            if not isinstance(cond_type, IntType):
                raise TypeMismatchInStatement(node)
        if node.update:
            self.visit(node.update, o)
        self.loop_depth += 1
        self.visit(node.body, o)
        self.loop_depth -= 1
        
        for var_name, var_sym in self.envs[-1].items():
            if isinstance(var_sym.typ, AutoType) and var_sym.typ.inferred_type is None:
                raise TypeCannotBeInferred(node)
        self.exit_scope()

    def visit_switch_stmt(self, node: "SwitchStmt", o: Any = None):
        expr_type = self.visit(node.expr, o)
        if isinstance(expr_type, AutoType) and expr_type.inferred_type is None:
            raise TypeCannotBeInferred(node.expr)
        if not isinstance(expr_type, IntType):
            raise TypeMismatchInStatement(node)
        self.switch_depth += 1
        for case_stmt in node.cases:
            self.visit(case_stmt, o)
        if node.default_case:
            self.visit(node.default_case, o)
        self.switch_depth -= 1

    def visit_case_stmt(self, node: "CaseStmt", o: Any = None):
        case_type = self.visit(node.expr, o)
        if isinstance(case_type, AutoType) and case_type.inferred_type is None:
            raise TypeCannotBeInferred(node.expr)
        if not isinstance(case_type, IntType):
            raise TypeMismatchInStatement(node)
        for stmt in node.statements:
            self.visit(stmt, o)

    def visit_default_stmt(self, node: "DefaultStmt", o: Any = None):
        for stmt in node.statements:
            self.visit(stmt, o)

    def visit_break_stmt(self, node: "BreakStmt", o: Any = None):
        if self.loop_depth == 0 and self.switch_depth == 0:
            raise MustInLoop(node)

    def visit_continue_stmt(self, node: "ContinueStmt", o: Any = None):
        if self.loop_depth == 0:
            raise MustInLoop(node)

    def visit_return_stmt(self, node: "ReturnStmt", o: Any = None):
        ret_type = self.visit(node.expr, o) if node.expr else VoidType()
        func_sym = self.funcs[self.current_func_name]
        
        expected_type = func_sym.return_type
        if isinstance(expected_type, AutoType) and expected_type.inferred_type is not None:
            expected_type = expected_type.inferred_type
            
        if isinstance(ret_type, StructLiteral):
            if isinstance(expected_type, AutoType) and expected_type.inferred_type is None:
                raise TypeCannotBeInferred(node.expr)
            ret_type = self.check_struct_literal(ret_type, expected_type)
            
        if isinstance(func_sym.return_type, AutoType):
            if func_sym.return_type.inferred_type is None:
                if isinstance(ret_type, AutoType) and ret_type.inferred_type is None:
                    raise TypeCannotBeInferred(node.expr)
                func_sym.return_type.inferred_type = ret_type
            else:
                if isinstance(ret_type, AutoType) and ret_type.inferred_type is None:
                    ret_type.inferred_type = func_sym.return_type.inferred_type
                    ret_type = func_sym.return_type.inferred_type
                if not self.are_types_equal(func_sym.return_type.inferred_type, ret_type):
                    raise TypeMismatchInStatement(node)
        else:
            if isinstance(ret_type, AutoType) and ret_type.inferred_type is None:
                ret_type.inferred_type = func_sym.return_type
                ret_type = func_sym.return_type
            if not self.are_types_equal(func_sym.return_type, ret_type):
                raise TypeMismatchInStatement(node)

    def visit_expr_stmt(self, node: "ExprStmt", o: Any = None):
        self.visit(node.expr, node)

    # Expressions
    def visit_binary_op(self, node: "BinaryOp", o: Any = None):
        l_type = self.visit(node.left, o)
        r_type = self.visit(node.right, o)
        
        if node.operator in ['+', '-', '*', '/']:
            if isinstance(l_type, AutoType) and l_type.inferred_type is None:
                if isinstance(r_type, IntType): 
                    l_type.inferred_type = IntType()
                    l_type = IntType()
                elif isinstance(r_type, FloatType): 
                    l_type.inferred_type = FloatType()
                    l_type = FloatType()
            if isinstance(r_type, AutoType) and r_type.inferred_type is None:
                if isinstance(l_type, IntType): 
                    r_type.inferred_type = IntType()
                    r_type = IntType()
                elif isinstance(l_type, FloatType): 
                    r_type.inferred_type = FloatType()
                    r_type = FloatType()
                
            if isinstance(l_type, AutoType) or isinstance(r_type, AutoType):
                raise TypeCannotBeInferred(node)
                
            if not (isinstance(l_type, (IntType, FloatType)) and isinstance(r_type, (IntType, FloatType))):
                raise TypeMismatchInExpression(node)
                
            if isinstance(l_type, FloatType) or isinstance(r_type, FloatType):
                return FloatType()
            return IntType()
            
        elif node.operator == '%':
            if isinstance(l_type, AutoType) and l_type.inferred_type is None:
                l_type.inferred_type = IntType()
                l_type = IntType()
            if isinstance(r_type, AutoType) and r_type.inferred_type is None:
                r_type.inferred_type = IntType()
                r_type = IntType()
            if not (isinstance(l_type, IntType) and isinstance(r_type, IntType)):
                raise TypeMismatchInExpression(node)
            return IntType()
            
        elif node.operator in ['&&', '||']:
            if isinstance(l_type, AutoType) and l_type.inferred_type is None:
                l_type.inferred_type = IntType()
                l_type = IntType()
            if isinstance(r_type, AutoType) and r_type.inferred_type is None:
                r_type.inferred_type = IntType()
                r_type = IntType()
            if not (isinstance(l_type, IntType) and isinstance(r_type, IntType)):
                raise TypeMismatchInExpression(node)
            return IntType()
            
        elif node.operator in ['==', '!=', '<', '<=', '>', '>=']:
            if isinstance(l_type, AutoType) and l_type.inferred_type is None:
                if isinstance(r_type, IntType): 
                    l_type.inferred_type = IntType()
                    l_type = IntType()
                elif isinstance(r_type, FloatType): 
                    l_type.inferred_type = FloatType()
                    l_type = FloatType()
            if isinstance(r_type, AutoType) and r_type.inferred_type is None:
                if isinstance(l_type, IntType): 
                    r_type.inferred_type = IntType()
                    r_type = IntType()
                elif isinstance(l_type, FloatType): 
                    r_type.inferred_type = FloatType()
                    r_type = FloatType()
                
            if isinstance(l_type, AutoType) or isinstance(r_type, AutoType):
                raise TypeCannotBeInferred(node)
                
            if not (isinstance(l_type, (IntType, FloatType)) and isinstance(r_type, (IntType, FloatType))):
                raise TypeMismatchInExpression(node)
            return IntType()

    def visit_prefix_op(self, node: "PrefixOp", o: Any = None):
        op_type = self.visit(node.operand, o)
        if node.operator in ['+', '-']:
            if isinstance(op_type, AutoType) and op_type.inferred_type is None:
                raise TypeCannotBeInferred(node)
            if not isinstance(op_type, (IntType, FloatType)):
                raise TypeMismatchInExpression(node)
            return op_type
        elif node.operator in ['!', '++', '--']:
            if node.operator in ['++', '--']:
                if not isinstance(node.operand, (Identifier, MemberAccess)):
                    raise TypeMismatchInExpression(node)
            if isinstance(op_type, AutoType) and op_type.inferred_type is None:
                op_type.inferred_type = IntType()
                op_type = IntType()
            if not isinstance(op_type, IntType):
                raise TypeMismatchInExpression(node)
            return IntType()

    def visit_postfix_op(self, node: "PostfixOp", o: Any = None):
        if not isinstance(node.operand, (Identifier, MemberAccess)):
            raise TypeMismatchInExpression(node)
        op_type = self.visit(node.operand, o)
        if isinstance(op_type, AutoType) and op_type.inferred_type is None:
            op_type.inferred_type = IntType()
            op_type = IntType()
        if not isinstance(op_type, IntType):
            raise TypeMismatchInExpression(node)
        return IntType()

    def visit_assign_expr(self, node: "AssignExpr", o: Any = None):
        lhs_type = self.visit(node.lhs, None)
        rhs_type = self.visit(node.rhs, None)
        
        if isinstance(rhs_type, StructLiteral):
            if isinstance(lhs_type, AutoType) and lhs_type.inferred_type is None:
                raise TypeCannotBeInferred(node.rhs)
            rhs_type = self.check_struct_literal(rhs_type, lhs_type)
            
        if isinstance(lhs_type, AutoType) and lhs_type.inferred_type is None:
            if isinstance(rhs_type, AutoType) and rhs_type.inferred_type is None:
                raise TypeCannotBeInferred(node)
            lhs_type.inferred_type = rhs_type
            lhs_type = rhs_type
            
        if isinstance(rhs_type, AutoType) and rhs_type.inferred_type is None:
            rhs_type.inferred_type = lhs_type
            rhs_type = lhs_type
            
        if not self.are_types_equal(lhs_type, rhs_type):
            if isinstance(o, ExprStmt):
                raise TypeMismatchInStatement(o)
            raise TypeMismatchInExpression(node)
            
        return lhs_type

    def visit_member_access(self, node: "MemberAccess", o: Any = None):
        obj_type = self.visit(node.obj, o)
        if isinstance(obj_type, AutoType) and obj_type.inferred_type is None:
            raise TypeCannotBeInferred(node)
        if not isinstance(obj_type, StructType):
            raise TypeMismatchInExpression(node)
            
        struct_sym = self.structs.get(obj_type.struct_name)
        if node.member not in struct_sym.members:
            raise TypeMismatchInExpression(node)
            
        return struct_sym.members[node.member]

    def visit_func_call(self, node: "FuncCall", o: Any = None):
        if node.name not in self.funcs:
            raise UndeclaredFunction(node.name)
        func_sym = self.funcs[node.name]
        
        if len(node.args) != len(func_sym.params):
            raise TypeMismatchInExpression(node)
            
        for i in range(len(node.args)):
            arg_type = self.visit(node.args[i], o)
            param_type = func_sym.params[i]
            
            if isinstance(arg_type, StructLiteral):
                arg_type = self.check_struct_literal(arg_type, param_type)
                
            if isinstance(arg_type, AutoType) and arg_type.inferred_type is None:
                arg_type.inferred_type = param_type
                arg_type = param_type
                
            if not self.are_types_equal(param_type, arg_type):
                raise TypeMismatchInExpression(node)
                
        ret_type = func_sym.return_type
        if isinstance(ret_type, AutoType):
            if ret_type.inferred_type is not None:
                return ret_type.inferred_type
            return ret_type
        return ret_type

    def visit_identifier(self, node: "Identifier", o: Any = None):
        var_sym = self.lookup_var(node.name)
        if not var_sym:
            raise UndeclaredIdentifier(node.name)
        if isinstance(var_sym.typ, AutoType):
            if var_sym.typ.inferred_type is not None:
                return var_sym.typ.inferred_type
            return var_sym.typ
        return var_sym.typ

    def visit_struct_literal(self, node: "StructLiteral", o: Any = None):
        return node

    # Literals
    def visit_int_literal(self, node: "IntLiteral", o: Any = None):
        return IntType()

    def visit_float_literal(self, node: "FloatLiteral", o: Any = None):
        return FloatType()

    def visit_string_literal(self, node: "StringLiteral", o: Any = None):
        return StringType()