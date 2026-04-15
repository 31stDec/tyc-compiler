"""
AST Generation module for TyC programming language.
This module contains the ASTGeneration class that converts parse trees
into Abstract Syntax Trees using the visitor pattern.
"""

from functools import reduce
from build.TyCVisitor import TyCVisitor
from build.TyCParser import TyCParser
from src.utils.nodes import *

class ASTGeneration(TyCVisitor):
    """AST Generation visitor for TyC language."""

    # ==========================================
    # 1. Program & Declarations
    # ==========================================
    def visitProgram(self, ctx: TyCParser.ProgramContext):
        decls = []
        for child in ctx.getChildren():
            if isinstance(child, TyCParser.StructDeclContext):
                decls.append(self.visit(child))
            elif isinstance(child, TyCParser.FuncDeclContext):
                decls.append(self.visit(child))
        return Program(decls)

    def visitStructDecl(self, ctx: TyCParser.StructDeclContext):
        name = ctx.ID().getText()
        members = [self.visit(m) for m in ctx.structMember()]
        return StructDecl(name, members)

    def visitStructMember(self, ctx: TyCParser.StructMemberContext):
        typ = self.visit(ctx.type_())
        name = ctx.ID().getText()
        return MemberDecl(typ, name)

    def visitExplicitFuncDecl(self, ctx: TyCParser.ExplicitFuncDeclContext):
        if ctx.type_():
            ret_type = self.visit(ctx.type_())
        else:
            ret_type = VoidType()
            
        name = ctx.ID().getText()
        params = self.visit(ctx.paramList()) if ctx.paramList() else []
        body = self.visit(ctx.blockStmt())
        return FuncDecl(ret_type, name, params, body)

    def visitInferredFuncDecl(self, ctx: TyCParser.InferredFuncDeclContext):
        name = ctx.ID().getText()
        params = self.visit(ctx.paramList()) if ctx.paramList() else []
        body = self.visit(ctx.blockStmt())
        return FuncDecl(None, name, params, body)

    def visitParamList(self, ctx: TyCParser.ParamListContext):
        return [self.visit(p) for p in ctx.param()]

    def visitParam(self, ctx: TyCParser.ParamContext):
        typ = self.visit(ctx.type_())
        name = ctx.ID().getText()
        return Param(typ, name)

    def visitType(self, ctx: TyCParser.TypeContext):
        if ctx.K_INT(): return IntType()
        if ctx.K_FLOAT(): return FloatType()
        if ctx.K_STRING(): return StringType()
        if ctx.ID(): return StructType(ctx.ID().getText())

    # ==========================================
    # 2. Statements
    # ==========================================
    def visitStmt(self, ctx: TyCParser.StmtContext):
        if ctx.SEMI():
            return None
        return self.visit(ctx.getChild(0))

    def visitBlockStmt(self, ctx: TyCParser.BlockStmtContext):
        stmts = []
        for s in ctx.stmt():
            stmt = self.visit(s)
            if stmt is not None:
                stmts.append(stmt)
        return BlockStmt(stmts)

    def visitAutoDecl(self, ctx: TyCParser.AutoDeclContext):
        name = ctx.ID().getText()
        init_expr = self.visit(ctx.expr()) if ctx.expr() else None
        return VarDecl(None, name, init_expr)

    def visitExplicitDecl(self, ctx: TyCParser.ExplicitDeclContext):
        typ = self.visit(ctx.type_())
        name = ctx.ID().getText()
        init_expr = self.visit(ctx.expr()) if ctx.expr() else None
        return VarDecl(typ, name, init_expr)

    def visitIfStmt(self, ctx: TyCParser.IfStmtContext):
        cond = self.visit(ctx.expr())
        then_stmt = self.visit(ctx.stmt(0))
        else_stmt = self.visit(ctx.stmt(1)) if ctx.stmt(1) else None
        return IfStmt(cond, then_stmt, else_stmt)

    def visitWhileStmt(self, ctx: TyCParser.WhileStmtContext):
        cond = self.visit(ctx.expr())
        body = self.visit(ctx.stmt())
        return WhileStmt(cond, body)

    def visitForStmt(self, ctx: TyCParser.ForStmtContext):
        init = self.visit(ctx.forInit())
        
        cond = None
        update = None
        seen_semi = False
        
        for child in ctx.getChildren():
            if child == ctx.SEMI():
                seen_semi = True
            elif isinstance(child, TyCParser.ExprContext):
                if not seen_semi:
                    cond = self.visit(child)
                else:
                    update = self.visit(child)
                    
        body = self.visit(ctx.stmt())
        return ForStmt(init, cond, update, body)

    def visitForInit(self, ctx: TyCParser.ForInitContext):
        if ctx.SEMI():
            return None
        if ctx.varDeclStmt():
            return self.visit(ctx.varDeclStmt())
        if ctx.exprStmt():
            expr = self.visit(ctx.exprStmt().expr())
            if isinstance(expr, AssignExpr):
                return AssignStmt(expr)
            return ExprStmt(expr)

    def visitSwitchStmt(self, ctx: TyCParser.SwitchStmtContext):
        expr = self.visit(ctx.expr())
        cases = []
        default_case = None
        
        if ctx.switchBody():
            body_ctx = ctx.switchBody()
            current_case_expr = None
            current_stmts = []
            is_default = False
            
            for child in body_ctx.getChildren():
                if isinstance(child, TyCParser.CaseLabelContext):
                    if current_case_expr is not None:
                        cases.append(CaseStmt(current_case_expr, current_stmts))
                    elif is_default:
                        default_case = DefaultStmt(current_stmts)
                        
                    current_stmts = []
                    if child.K_CASE():
                        current_case_expr = self.visit(child.expr())
                        is_default = False
                    else:
                        is_default = True
                        current_case_expr = None
                        
                elif isinstance(child, TyCParser.StmtContext):
                    stmt = self.visit(child)
                    if stmt is not None:
                        current_stmts.append(stmt)
                        
            if current_case_expr is not None:
                cases.append(CaseStmt(current_case_expr, current_stmts))
            elif is_default:
                default_case = DefaultStmt(current_stmts)

        return SwitchStmt(expr, cases, default_case)

    def visitBreakStmt(self, ctx: TyCParser.BreakStmtContext):
        return BreakStmt()

    def visitContinueStmt(self, ctx: TyCParser.ContinueStmtContext):
        return ContinueStmt()

    def visitReturnStmt(self, ctx: TyCParser.ReturnStmtContext):
        expr = self.visit(ctx.expr()) if ctx.expr() else None
        return ReturnStmt(expr)

    def visitExprStmt(self, ctx: TyCParser.ExprStmtContext):
        expr = self.visit(ctx.expr())
        if isinstance(expr, AssignExpr):
            return AssignStmt(expr)
        return ExprStmt(expr)

    # ==========================================
    # 3. Expressions
    # ==========================================
    def visitMemberAccessExpr(self, ctx: TyCParser.MemberAccessExprContext):
        obj = self.visit(ctx.expr())
        member = ctx.ID().getText()
        return MemberAccess(obj, member)

    def visitFuncCallExpr(self, ctx: TyCParser.FuncCallExprContext):
        expr_node = self.visit(ctx.expr())
        name = expr_node.name if isinstance(expr_node, Identifier) else "unknown"
        args = self.visit(ctx.argList()) if ctx.argList() else []
        return FuncCall(name, args)

    def visitPostfixExpr(self, ctx: TyCParser.PostfixExprContext):
        operand = self.visit(ctx.expr())
        op = ctx.INC().getText() if ctx.INC() else ctx.DEC().getText()
        return PostfixOp(op, operand)

    def visitUnaryExpr(self, ctx: TyCParser.UnaryExprContext):
        operand = self.visit(ctx.expr())
        op = ctx.getChild(0).getText()
        return PrefixOp(op, operand)

    def visitMultiplicativeExpr(self, ctx: TyCParser.MultiplicativeExprContext):
        return BinaryOp(self.visit(ctx.expr(0)), ctx.getChild(1).getText(), self.visit(ctx.expr(1)))

    def visitAdditiveExpr(self, ctx: TyCParser.AdditiveExprContext):
        return BinaryOp(self.visit(ctx.expr(0)), ctx.getChild(1).getText(), self.visit(ctx.expr(1)))

    def visitRelationalExpr(self, ctx: TyCParser.RelationalExprContext):
        return BinaryOp(self.visit(ctx.expr(0)), ctx.getChild(1).getText(), self.visit(ctx.expr(1)))

    def visitEqualityExpr(self, ctx: TyCParser.EqualityExprContext):
        return BinaryOp(self.visit(ctx.expr(0)), ctx.getChild(1).getText(), self.visit(ctx.expr(1)))

    def visitLogicalAndExpr(self, ctx: TyCParser.LogicalAndExprContext):
        return BinaryOp(self.visit(ctx.expr(0)), ctx.AND().getText(), self.visit(ctx.expr(1)))

    def visitLogicalOrExpr(self, ctx: TyCParser.LogicalOrExprContext):
        return BinaryOp(self.visit(ctx.expr(0)), ctx.OR().getText(), self.visit(ctx.expr(1)))

    def visitAssignExpr(self, ctx: TyCParser.AssignExprContext):
        lhs = self.visit(ctx.expr(0))
        
        if not isinstance(lhs, (Identifier, MemberAccess)):
            raise Exception("Error: Left-hand side of assignment must be an identifier or member access")
        
        rhs = self.visit(ctx.expr(1))
        return AssignExpr(lhs, rhs)

    def visitPrimaryExpr(self, ctx: TyCParser.PrimaryExprContext):
        return self.visit(ctx.primary())

    def visitPrimary(self, ctx: TyCParser.PrimaryContext):
        if ctx.LPAR():
            return self.visit(ctx.expr())
        if ctx.ID():
            return Identifier(ctx.ID().getText())
        if ctx.INT_LIT():
            return IntLiteral(int(ctx.INT_LIT().getText()))
        if ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        if ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        if ctx.structLiteral():
            return self.visit(ctx.structLiteral())

    def visitStructLiteral(self, ctx: TyCParser.StructLiteralContext):
        values = self.visit(ctx.argList()) if ctx.argList() else []
        return StructLiteral(values)

    def visitArgList(self, ctx: TyCParser.ArgListContext):
        return [self.visit(expr) for expr in ctx.expr()]