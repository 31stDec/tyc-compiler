"""
AST Generation test cases for TyC compiler.
Implemented 100 test cases to cover all AST nodes and structures.
"""

import unittest
from tests.utils import ASTGenerator

class ASTGenSuite(unittest.TestCase):
    
    def check(self, code, expected, test_num):
        """Evaluate the full program AST (Program, Struct, Func)."""
        ast_generator = ASTGenerator(code)
        actual = str(ast_generator.generate())
        self.assertEqual(actual, expected, f"Test {test_num} Failed.\nExpect: {expected}\nGot   : {actual}")

    def check_stmt(self, stmt_code, expected_stmt, test_num):
        """Helper to wrap a statement inside void main() { ... } for concise testing."""
        code = f"void main() {{ {stmt_code} }}"
        if expected_stmt == "":
            expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([]))])"
        else:
            expected = f"Program([FuncDecl(VoidType(), main, [], BlockStmt([{expected_stmt}]))])"
        self.check(code, expected, test_num)

    def check_expr(self, expr_code, expected_expr, test_num):
        """Helper to wrap an expression as an ExprStmt inside void main() { ... }."""
        self.check_stmt(f"{expr_code};", f"ExprStmt({expected_expr})", test_num)

    # ==========================================================================
    # GROUP 1: PROGRAM & FUNCTION DECLARATIONS (15 Tests)
    # ==========================================================================
    def test_301(self): self.check("void main() {}", "Program([FuncDecl(VoidType(), main, [], BlockStmt([]))])", 301)
    def test_302(self): self.check("int main() {}", "Program([FuncDecl(IntType(), main, [], BlockStmt([]))])", 302)
    def test_303(self): self.check("main() {}", "Program([FuncDecl(auto, main, [], BlockStmt([]))])", 303)
    def test_304(self): self.check("void f(int a) {}", "Program([FuncDecl(VoidType(), f, [Param(IntType(), a)], BlockStmt([]))])", 304)
    def test_305(self): self.check("void f(int a, float b) {}", "Program([FuncDecl(VoidType(), f, [Param(IntType(), a), Param(FloatType(), b)], BlockStmt([]))])", 305)
    def test_306(self): self.check("void f(string s, Point p) {}", "Program([FuncDecl(VoidType(), f, [Param(StringType(), s), Param(StructType(Point), p)], BlockStmt([]))])", 306)
    def test_307(self): self.check("void f() {} void g() {}", "Program([FuncDecl(VoidType(), f, [], BlockStmt([])), FuncDecl(VoidType(), g, [], BlockStmt([]))])", 307)
    def test_308(self): self.check("f() {}", "Program([FuncDecl(auto, f, [], BlockStmt([]))])", 308)
    def test_309(self): self.check("string f() {}", "Program([FuncDecl(StringType(), f, [], BlockStmt([]))])", 309)
    def test_310(self): self.check("Point f() {}", "Program([FuncDecl(StructType(Point), f, [], BlockStmt([]))])", 310)
    def test_311(self): self.check("int add(int x, int y) { return x + y; }", "Program([FuncDecl(IntType(), add, [Param(IntType(), x), Param(IntType(), y)], BlockStmt([ReturnStmt(return BinaryOp(Identifier(x), +, Identifier(y)))]))])", 311)
    def test_312(self): self.check("void main(int argc) {}", "Program([FuncDecl(VoidType(), main, [Param(IntType(), argc)], BlockStmt([]))])", 312)
    def test_313(self): self.check("void f(int a, int b, int c, int d) {}", "Program([FuncDecl(VoidType(), f, [Param(IntType(), a), Param(IntType(), b), Param(IntType(), c), Param(IntType(), d)], BlockStmt([]))])", 313)
    def test_314(self): self.check("void f() { return; }", "Program([FuncDecl(VoidType(), f, [], BlockStmt([ReturnStmt(return)]))])", 314)
    def test_315(self): self.check("void f() { return 1; }", "Program([FuncDecl(VoidType(), f, [], BlockStmt([ReturnStmt(return IntLiteral(1))]))])", 315)

    # ==========================================================================
    # GROUP 2: STRUCT DECLARATIONS (10 Tests)
    # ==========================================================================
    def test_316(self): self.check("struct A {};", "Program([StructDecl(A, [])])", 316)
    def test_317(self): self.check("struct A { int x; };", "Program([StructDecl(A, [MemberDecl(IntType(), x)])])", 317)
    def test_318(self): self.check("struct A { int x; float y; };", "Program([StructDecl(A, [MemberDecl(IntType(), x), MemberDecl(FloatType(), y)])])", 318)
    def test_319(self): self.check("struct A { string s; };", "Program([StructDecl(A, [MemberDecl(StringType(), s)])])", 319)
    def test_320(self): self.check("struct A { B b; };", "Program([StructDecl(A, [MemberDecl(StructType(B), b)])])", 320)
    def test_321(self): self.check("struct A { int x; }; void main() {}", "Program([StructDecl(A, [MemberDecl(IntType(), x)]), FuncDecl(VoidType(), main, [], BlockStmt([]))])", 321)
    def test_322(self): self.check("struct A { int x; }; struct B { int y; };", "Program([StructDecl(A, [MemberDecl(IntType(), x)]), StructDecl(B, [MemberDecl(IntType(), y)])])", 322)
    def test_323(self): self.check("struct Point { float x; float y; };", "Program([StructDecl(Point, [MemberDecl(FloatType(), x), MemberDecl(FloatType(), y)])])", 323)
    def test_324(self): self.check("struct Empty {};", "Program([StructDecl(Empty, [])])", 324)
    def test_325(self): self.check("struct Node { int val; Node next; };", "Program([StructDecl(Node, [MemberDecl(IntType(), val), MemberDecl(StructType(Node), next)])])", 325)

    # ==========================================================================
    # GROUP 3: VARIABLE DECLARATIONS (15 Tests)
    # ==========================================================================
    def test_326(self): self.check_stmt("int x;", "VarDecl(IntType(), x)", 326)
    def test_327(self): self.check_stmt("float y;", "VarDecl(FloatType(), y)", 327)
    def test_328(self): self.check_stmt("string s;", "VarDecl(StringType(), s)", 328)
    def test_329(self): self.check_stmt("Point p;", "VarDecl(StructType(Point), p)", 329)
    def test_330(self): self.check_stmt("auto x;", "VarDecl(auto, x)", 330)
    def test_331(self): self.check_stmt("int x = 1;", "VarDecl(IntType(), x = IntLiteral(1))", 331)
    def test_332(self): self.check_stmt("float x = 1.5;", "VarDecl(FloatType(), x = FloatLiteral(1.5))", 332)
    def test_333(self): self.check_stmt('string x = "abc";', "VarDecl(StringType(), x = StringLiteral('abc'))", 333)
    def test_334(self): self.check_stmt("auto x = 1;", "VarDecl(auto, x = IntLiteral(1))", 334)
    def test_335(self): self.check_stmt("Point p = {1, 2};", "VarDecl(StructType(Point), p = StructLiteral({IntLiteral(1), IntLiteral(2)}))", 335)
    def test_336(self): self.check_stmt("auto p = {1, 2};", "VarDecl(auto, p = StructLiteral({IntLiteral(1), IntLiteral(2)}))", 336)
    def test_337(self): self.check_stmt("int x; int y;", "VarDecl(IntType(), x), VarDecl(IntType(), y)", 337)
    def test_338(self): self.check_stmt("auto x = y;", "VarDecl(auto, x = Identifier(y))", 338)
    def test_339(self): self.check_stmt("int x = a + b;", "VarDecl(IntType(), x = BinaryOp(Identifier(a), +, Identifier(b)))", 339)
    def test_340(self): self.check_stmt("auto x = f();", "VarDecl(auto, x = FuncCall(f, []))", 340)

    # ==========================================================================
    # GROUP 4: ASSIGNMENTS & EXPRESSION STATEMENTS (15 Tests)
    # ==========================================================================
    def test_341(self): self.check_stmt("x = 1;", "AssignStmt(AssignExpr(Identifier(x) = IntLiteral(1)))", 341)
    def test_342(self): self.check_stmt("x = y = 1;", "AssignStmt(AssignExpr(Identifier(x) = AssignExpr(Identifier(y) = IntLiteral(1))))", 342)
    def test_343(self): self.check_stmt("p.x = 1;", "AssignStmt(AssignExpr(MemberAccess(Identifier(p).x) = IntLiteral(1)))", 343)
    def test_344(self): self.check_stmt("p.x.y = 1;", "AssignStmt(AssignExpr(MemberAccess(MemberAccess(Identifier(p).x).y) = IntLiteral(1)))", 344)
    def test_345(self): self.check_stmt("f();", "ExprStmt(FuncCall(f, []))", 345)
    def test_346(self): self.check_stmt("f(1);", "ExprStmt(FuncCall(f, [IntLiteral(1)]))", 346)
    def test_347(self): self.check_stmt("f(1, 2);", "ExprStmt(FuncCall(f, [IntLiteral(1), IntLiteral(2)]))", 347)
    def test_348(self): self.check_stmt("x + 1;", "ExprStmt(BinaryOp(Identifier(x), +, IntLiteral(1)))", 348)
    def test_349(self): self.check_stmt("x++;", "ExprStmt(PostfixOp(Identifier(x)++))", 349)
    def test_350(self): self.check_stmt("++x;", "ExprStmt(PrefixOp(++Identifier(x)))", 350)
    def test_351(self): self.check_stmt("--x;", "ExprStmt(PrefixOp(--Identifier(x)))", 351)
    def test_352(self): self.check_stmt("x--;", "ExprStmt(PostfixOp(Identifier(x)--))", 352)
    def test_353(self): self.check_stmt("!x;", "ExprStmt(PrefixOp(!Identifier(x)))", 353)
    def test_354(self): self.check_stmt("-x;", "ExprStmt(PrefixOp(-Identifier(x)))", 354)
    def test_355(self): self.check_stmt("+x;", "ExprStmt(PrefixOp(+Identifier(x)))", 355)

    # ==========================================================================
    # GROUP 5: BINARY OPERATIONS (15 Tests)
    # ==========================================================================
    def test_356(self): self.check_expr("a + b", "BinaryOp(Identifier(a), +, Identifier(b))", 356)
    def test_357(self): self.check_expr("a - b", "BinaryOp(Identifier(a), -, Identifier(b))", 357)
    def test_358(self): self.check_expr("a * b", "BinaryOp(Identifier(a), *, Identifier(b))", 358)
    def test_359(self): self.check_expr("a / b", "BinaryOp(Identifier(a), /, Identifier(b))", 359)
    def test_360(self): self.check_expr("a % b", "BinaryOp(Identifier(a), %, Identifier(b))", 360)
    def test_361(self): self.check_expr("a == b", "BinaryOp(Identifier(a), ==, Identifier(b))", 361)
    def test_362(self): self.check_expr("a != b", "BinaryOp(Identifier(a), !=, Identifier(b))", 362)
    def test_363(self): self.check_expr("a < b", "BinaryOp(Identifier(a), <, Identifier(b))", 363)
    def test_364(self): self.check_expr("a > b", "BinaryOp(Identifier(a), >, Identifier(b))", 364)
    def test_365(self): self.check_expr("a <= b", "BinaryOp(Identifier(a), <=, Identifier(b))", 365)
    def test_366(self): self.check_expr("a >= b", "BinaryOp(Identifier(a), >=, Identifier(b))", 366)
    def test_367(self): self.check_expr("a && b", "BinaryOp(Identifier(a), &&, Identifier(b))", 367)
    def test_368(self): self.check_expr("a || b", "BinaryOp(Identifier(a), ||, Identifier(b))", 368)
    def test_369(self): self.check_expr("a + b * c", "BinaryOp(Identifier(a), +, BinaryOp(Identifier(b), *, Identifier(c)))", 369)
    def test_370(self): self.check_expr("(a + b) * c", "BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), *, Identifier(c))", 370)

    # ==========================================================================
    # GROUP 6: CONTROL FLOW - IF & WHILE (15 Tests)
    # ==========================================================================
    def test_371(self): self.check_stmt("if (x) y;", "IfStmt(if Identifier(x) then ExprStmt(Identifier(y)))", 371)
    def test_372(self): self.check_stmt("if (x) { y; }", "IfStmt(if Identifier(x) then BlockStmt([ExprStmt(Identifier(y))]))", 372)
    def test_373(self): self.check_stmt("if (x) y; else z;", "IfStmt(if Identifier(x) then ExprStmt(Identifier(y)), else ExprStmt(Identifier(z)))", 373)
    def test_374(self): self.check_stmt("if (x) { y; } else { z; }", "IfStmt(if Identifier(x) then BlockStmt([ExprStmt(Identifier(y))]), else BlockStmt([ExprStmt(Identifier(z))]))", 374)
    def test_375(self): self.check_stmt("if (x) if (y) z;", "IfStmt(if Identifier(x) then IfStmt(if Identifier(y) then ExprStmt(Identifier(z))))", 375)
    def test_376(self): self.check_stmt("if (x) if (y) z; else w;", "IfStmt(if Identifier(x) then IfStmt(if Identifier(y) then ExprStmt(Identifier(z)), else ExprStmt(Identifier(w))))", 376)
    def test_377(self): self.check_stmt("while (x) y;", "WhileStmt(while Identifier(x) do ExprStmt(Identifier(y)))", 377)
    def test_378(self): self.check_stmt("while (x) { y; }", "WhileStmt(while Identifier(x) do BlockStmt([ExprStmt(Identifier(y))]))", 378)
    def test_379(self): self.check_stmt("while (x < 10) x++;", "WhileStmt(while BinaryOp(Identifier(x), <, IntLiteral(10)) do ExprStmt(PostfixOp(Identifier(x)++)))", 379)
    def test_380(self): self.check_stmt("if (x == 1) return;", "IfStmt(if BinaryOp(Identifier(x), ==, IntLiteral(1)) then ReturnStmt(return))", 380)
    def test_381(self): self.check_stmt("if (x) break;", "IfStmt(if Identifier(x) then BreakStmt())", 381)
    def test_382(self): self.check_stmt("if (x) continue;", "IfStmt(if Identifier(x) then ContinueStmt())", 382)
    def test_383(self): self.check_stmt("while (1) break;", "WhileStmt(while IntLiteral(1) do BreakStmt())", 383)
    def test_384(self): self.check_stmt("while (1) continue;", "WhileStmt(while IntLiteral(1) do ContinueStmt())", 384)
    def test_385(self): self.check_stmt("if (x) return 1;", "IfStmt(if Identifier(x) then ReturnStmt(return IntLiteral(1)))", 385)

    # ==========================================================================
    # GROUP 7: CONTROL FLOW - FOR & SWITCH (15 Tests)
    # ==========================================================================
    def test_386(self): self.check_stmt("for(;;) x;", "ForStmt(for None; None; None do ExprStmt(Identifier(x)))", 386)
    def test_387(self): self.check_stmt("for(i=0;;) x;", "ForStmt(for AssignStmt(AssignExpr(Identifier(i) = IntLiteral(0))); None; None do ExprStmt(Identifier(x)))", 387)
    def test_388(self): self.check_stmt("for(int i=0;;) x;", "ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); None; None do ExprStmt(Identifier(x)))", 388)
    def test_389(self): self.check_stmt("for(; i<10;) x;", "ForStmt(for None; BinaryOp(Identifier(i), <, IntLiteral(10)); None do ExprStmt(Identifier(x)))", 389)
    def test_390(self): self.check_stmt("for(;; i++) x;", "ForStmt(for None; None; PostfixOp(Identifier(i)++) do ExprStmt(Identifier(x)))", 390)
    def test_391(self): self.check_stmt("for(int i=0; i<10; i++) x;", "ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do ExprStmt(Identifier(x)))", 391)
    def test_392(self): self.check_stmt("for(i=0; i<10; i=i+1) { }", "ForStmt(for AssignStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(10)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([]))", 392)
    def test_393(self): self.check_stmt("switch(x) {}", "SwitchStmt(switch Identifier(x) cases [])", 393)
    def test_394(self): self.check_stmt("switch(x) { case 1: y; }", "SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [ExprStmt(Identifier(y))])])", 394)
    def test_395(self): self.check_stmt("switch(x) { default: y; }", "SwitchStmt(switch Identifier(x) cases [], default DefaultStmt(default: [ExprStmt(Identifier(y))]))", 395)
    def test_396(self): self.check_stmt("switch(x) { case 1: y; break; }", "SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [ExprStmt(Identifier(y)), BreakStmt()])])", 396)
    def test_397(self): self.check_stmt("switch(x) { case 1: case 2: y; }", "SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): []), CaseStmt(case IntLiteral(2): [ExprStmt(Identifier(y))])])", 397)
    def test_398(self): self.check_stmt("switch(x) { case 1: y; default: z; }", "SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [ExprStmt(Identifier(y))])], default DefaultStmt(default: [ExprStmt(Identifier(z))]))", 398)
    def test_399(self): self.check_stmt("for(auto i=0; i<10; i++) break;", "ForStmt(for VarDecl(auto, i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do BreakStmt())", 399)
    def test_400(self): self.check_stmt("switch(1+2) { case 3: }", "SwitchStmt(switch BinaryOp(IntLiteral(1), +, IntLiteral(2)) cases [CaseStmt(case IntLiteral(3): [])])", 400)
    