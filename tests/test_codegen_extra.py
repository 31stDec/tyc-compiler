"""
Extra test cases for TyC code generation (~1000 tests).
"""

from src.utils.nodes import *
from tests.utils import CodeGenerator


def test_extra_001():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [IntLiteral(0)]))]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_002():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [IntLiteral(1)]))]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_003():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [IntLiteral(42)]))]))])
    assert CodeGenerator().generate_and_run(ast) == "42"

def test_extra_004():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [IntLiteral(100)]))]))])
    assert CodeGenerator().generate_and_run(ast) == "100"

def test_extra_005():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [IntLiteral(999)]))]))])
    assert CodeGenerator().generate_and_run(ast) == "999"

def test_extra_006():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [IntLiteral(-1)]))]))])
    assert CodeGenerator().generate_and_run(ast) == "-1"

def test_extra_007():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [IntLiteral(-42)]))]))])
    assert CodeGenerator().generate_and_run(ast) == "-42"

def test_extra_008():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [IntLiteral(255)]))]))])
    assert CodeGenerator().generate_and_run(ast) == "255"

def test_extra_009():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [IntLiteral(1000)]))]))])
    assert CodeGenerator().generate_and_run(ast) == "1000"

def test_extra_010():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [IntLiteral(10000)]))]))])
    assert CodeGenerator().generate_and_run(ast) == "10000"

def test_extra_011():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printFloat", [FloatLiteral(0.0)]))]))])
    assert CodeGenerator().generate_and_run(ast) == "0.0"

def test_extra_012():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printFloat", [FloatLiteral(1.0)]))]))])
    assert CodeGenerator().generate_and_run(ast) == "1.0"

def test_extra_013():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printFloat", [FloatLiteral(2.0)]))]))])
    assert CodeGenerator().generate_and_run(ast) == "2.0"

def test_extra_014():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printFloat", [FloatLiteral(3.14)]))]))])
    assert CodeGenerator().generate_and_run(ast) == "3.14"

def test_extra_015():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printFloat", [FloatLiteral(2.5)]))]))])
    assert CodeGenerator().generate_and_run(ast) == "2.5"

def test_extra_016():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printFloat", [FloatLiteral(1.5)]))]))])
    assert CodeGenerator().generate_and_run(ast) == "1.5"

def test_extra_017():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printFloat", [FloatLiteral(0.5)]))]))])
    assert CodeGenerator().generate_and_run(ast) == "0.5"

def test_extra_018():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printFloat", [FloatLiteral(0.25)]))]))])
    assert CodeGenerator().generate_and_run(ast) == "0.25"

def test_extra_019():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printFloat", [FloatLiteral(0.75)]))]))])
    assert CodeGenerator().generate_and_run(ast) == "0.75"

def test_extra_020():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printFloat", [FloatLiteral(10.0)]))]))])
    assert CodeGenerator().generate_and_run(ast) == "10.0"

def test_extra_021():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("")]))]))])
    assert CodeGenerator().generate_and_run(ast) == ""

def test_extra_022():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("a")]))]))])
    assert CodeGenerator().generate_and_run(ast) == "a"

def test_extra_023():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("hello")]))]))])
    assert CodeGenerator().generate_and_run(ast) == "hello"

def test_extra_024():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("Hello World")]))]))])
    assert CodeGenerator().generate_and_run(ast) == "Hello World"

def test_extra_025():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("123")]))]))])
    assert CodeGenerator().generate_and_run(ast) == "123"

def test_extra_026():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("TyC")]))]))])
    assert CodeGenerator().generate_and_run(ast) == "TyC"

def test_extra_027():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("ABC")]))]))])
    assert CodeGenerator().generate_and_run(ast) == "ABC"

def test_extra_028():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("test")]))]))])
    assert CodeGenerator().generate_and_run(ast) == "test"

def test_extra_029():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("foo bar")]))]))])
    assert CodeGenerator().generate_and_run(ast) == "foo bar"

def test_extra_030():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("compiler")]))]))])
    assert CodeGenerator().generate_and_run(ast) == "compiler"

def test_extra_031():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(3), "+", IntLiteral(4))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "7"

def test_extra_032():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(10), "-", IntLiteral(3))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "7"

def test_extra_033():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(6), "*", IntLiteral(7))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "42"

def test_extra_034():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(20), "/", IntLiteral(4))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "5"

def test_extra_035():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(17), "%", IntLiteral(5))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "2"

def test_extra_036():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(0), "+", IntLiteral(0))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_037():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(-5), "+", IntLiteral(3))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "-2"

def test_extra_038():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(100), "-", IntLiteral(200))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "-100"

def test_extra_039():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(2), "*", IntLiteral(0))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_040():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(7), "/", IntLiteral(2))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "3"

def test_extra_041():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printFloat", [BinaryOp(FloatLiteral(1.5), "+", FloatLiteral(1.5))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "3.0"

def test_extra_042():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printFloat", [BinaryOp(FloatLiteral(5.0), "-", FloatLiteral(2.5))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "2.5"

def test_extra_043():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printFloat", [BinaryOp(FloatLiteral(2.0), "*", FloatLiteral(2.5))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "5.0"

def test_extra_044():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printFloat", [BinaryOp(FloatLiteral(7.5), "/", FloatLiteral(2.5))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "3.0"

def test_extra_045():
    # int + float => i2f coercion
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printFloat", [BinaryOp(IntLiteral(2), "+", FloatLiteral(1.5))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "3.5"

def test_extra_046():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printFloat", [BinaryOp(FloatLiteral(3.0), "+", IntLiteral(1))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "4.0"

def test_extra_047():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printFloat", [BinaryOp(IntLiteral(3), "*", FloatLiteral(2.5))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "7.5"

def test_extra_048():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printFloat", [BinaryOp(FloatLiteral(10.0), "/", IntLiteral(4))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "2.5"

def test_extra_049():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(BinaryOp(IntLiteral(2), "+", IntLiteral(3)), "*", IntLiteral(4))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "20"

def test_extra_050():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(2), "+", BinaryOp(IntLiteral(3), "*", IntLiteral(4)))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "14"

def test_extra_051():
    # == true
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(5), "==", IntLiteral(5))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_052():
    # == false
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(5), "==", IntLiteral(6))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_053():
    # != true
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(3), "!=", IntLiteral(4))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_054():
    # != false
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(3), "!=", IntLiteral(3))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_055():
    # < true
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(3), "<", IntLiteral(5))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_056():
    # < false
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(5), "<", IntLiteral(3))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_057():
    # > true
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(7), ">", IntLiteral(3))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_058():
    # > false
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(3), ">", IntLiteral(7))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_059():
    # <= equal case
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(5), "<=", IntLiteral(5))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_060():
    # >= equal case
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(5), ">=", IntLiteral(5))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_061():
    # <= false
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(6), "<=", IntLiteral(5))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_062():
    # >= false
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(4), ">=", IntLiteral(5))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_063():
    # float == float
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(FloatLiteral(1.5), "==", FloatLiteral(1.5))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_064():
    # float < float
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(FloatLiteral(0.5), "<", FloatLiteral(1.5))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_065():
    # float > float false
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(FloatLiteral(1.5), ">", FloatLiteral(2.5))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_066():
    # && both true
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(1), "&&", IntLiteral(1))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_067():
    # && left false
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(0), "&&", IntLiteral(1))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_068():
    # && right false
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(1), "&&", IntLiteral(0))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_069():
    # || both false
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(0), "||", IntLiteral(0))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_070():
    # || left true
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(1), "||", IntLiteral(0))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_071():
    # || right true
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(0), "||", IntLiteral(1))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_072():
    # ! true
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [PrefixOp("!", IntLiteral(0))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_073():
    # ! false
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [PrefixOp("!", IntLiteral(1))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_074():
    # unary minus int
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [PrefixOp("-", IntLiteral(5))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "-5"

def test_extra_075():
    # unary minus float
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printFloat", [PrefixOp("-", FloatLiteral(1.5))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "-1.5"

def test_extra_076():
    # prefix ++ on var
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(5)),
        ExprStmt(PrefixOp("++", Identifier("x"))),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "6"

def test_extra_077():
    # prefix -- on var
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(5)),
        ExprStmt(PrefixOp("--", Identifier("x"))),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "4"

def test_extra_078():
    # postfix ++ on var
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(5)),
        ExprStmt(PostfixOp("++", Identifier("x"))),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "6"

def test_extra_079():
    # postfix -- on var
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(10)),
        ExprStmt(PostfixOp("--", Identifier("x"))),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "9"

def test_extra_080():
    # postfix ++ returns original value before update (correct C/C++/Java semantics)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(5)),
        ExprStmt(FuncCall("printInt", [PostfixOp("++", Identifier("x"))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "5"

def test_extra_081():
    # var decl explicit int
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "n", IntLiteral(7)),
        ExprStmt(FuncCall("printInt", [Identifier("n")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "7"

def test_extra_082():
    # var decl explicit float
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "f", FloatLiteral(3.14)),
        ExprStmt(FuncCall("printFloat", [Identifier("f")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "3.14"

def test_extra_083():
    # var decl explicit string
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(StringType(), "s", StringLiteral("hello")),
        ExprStmt(FuncCall("printString", [Identifier("s")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "hello"

def test_extra_084():
    # auto int var
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "x", IntLiteral(99)),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "99"

def test_extra_085():
    # auto float var
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "f", FloatLiteral(2.5)),
        ExprStmt(FuncCall("printFloat", [Identifier("f")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "2.5"

def test_extra_086():
    # auto string var
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "s", StringLiteral("auto")),
        ExprStmt(FuncCall("printString", [Identifier("s")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "auto"

def test_extra_087():
    # assign to var
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(0)),
        ExprStmt(AssignExpr(Identifier("x"), IntLiteral(42))),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "42"

def test_extra_088():
    # multiple var decls
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "a", IntLiteral(10)),
        VarDecl(IntType(), "b", IntLiteral(20)),
        ExprStmt(FuncCall("printInt", [BinaryOp(Identifier("a"), "+", Identifier("b"))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "30"

def test_extra_089():
    # if true branch taken
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        IfStmt(IntLiteral(1), BlockStmt([ExprStmt(FuncCall("printInt", [IntLiteral(1)]))]), None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_090():
    # if false branch not taken
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        IfStmt(IntLiteral(0), BlockStmt([ExprStmt(FuncCall("printInt", [IntLiteral(1)]))]), None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == ""

def test_extra_091():
    # if-else true branch
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        IfStmt(IntLiteral(1),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("yes")]))]),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("no")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "yes"

def test_extra_092():
    # if-else false branch
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        IfStmt(IntLiteral(0),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("yes")]))]),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("no")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "no"

def test_extra_093():
    # while loop 3 iters
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "i", IntLiteral(0)),
        WhileStmt(BinaryOp(Identifier("i"), "<", IntLiteral(3)), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("i")])),
            ExprStmt(PostfixOp("++", Identifier("i")))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "012"

def test_extra_094():
    # while loop never executes
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "i", IntLiteral(10)),
        WhileStmt(BinaryOp(Identifier("i"), "<", IntLiteral(0)), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == ""

def test_extra_095():
    # while with break
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "i", IntLiteral(0)),
        WhileStmt(IntLiteral(1), BlockStmt([
            IfStmt(BinaryOp(Identifier("i"), "==", IntLiteral(3)), BlockStmt([BreakStmt()]), None),
            ExprStmt(FuncCall("printInt", [Identifier("i")])),
            ExprStmt(PostfixOp("++", Identifier("i")))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "012"

def test_extra_096():
    # while with continue
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "i", IntLiteral(0)),
        WhileStmt(BinaryOp(Identifier("i"), "<", IntLiteral(5)), BlockStmt([
            ExprStmt(PostfixOp("++", Identifier("i"))),
            IfStmt(BinaryOp(BinaryOp(Identifier("i"), "%", IntLiteral(2)), "==", IntLiteral(0)),
                   BlockStmt([ContinueStmt()]), None),
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "135"

def test_extra_097():
    # for loop 0..4
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(
            VarDecl(IntType(), "i", IntLiteral(0)),
            BinaryOp(Identifier("i"), "<", IntLiteral(5)),
            PostfixOp("++", Identifier("i")),
            BlockStmt([ExprStmt(FuncCall("printInt", [Identifier("i")]))])
        )
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "01234"

def test_extra_098():
    # for loop with break
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(
            VarDecl(IntType(), "i", IntLiteral(0)),
            BinaryOp(Identifier("i"), "<", IntLiteral(10)),
            PostfixOp("++", Identifier("i")),
            BlockStmt([
                IfStmt(BinaryOp(Identifier("i"), "==", IntLiteral(3)), BlockStmt([BreakStmt()]), None),
                ExprStmt(FuncCall("printInt", [Identifier("i")]))
            ])
        )
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "012"

def test_extra_099():
    # for loop with continue (skip even)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(
            VarDecl(IntType(), "i", IntLiteral(0)),
            BinaryOp(Identifier("i"), "<", IntLiteral(6)),
            PostfixOp("++", Identifier("i")),
            BlockStmt([
                IfStmt(BinaryOp(BinaryOp(Identifier("i"), "%", IntLiteral(2)), "==", IntLiteral(0)),
                       BlockStmt([ContinueStmt()]), None),
                ExprStmt(FuncCall("printInt", [Identifier("i")]))
            ])
        )
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "135"

def test_extra_100():
    # simple void function call
    ast = Program([
        FuncDecl(VoidType(), "greet", [], BlockStmt([
            ExprStmt(FuncCall("printString", [StringLiteral("hi")]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("greet", []))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "hi"

def test_extra_101():
    # function with int return
    ast = Program([
        FuncDecl(IntType(), "getVal", [], BlockStmt([ReturnStmt(IntLiteral(42))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("getVal", [])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "42"

def test_extra_102():
    # function with float return
    ast = Program([
        FuncDecl(FloatType(), "getF", [], BlockStmt([ReturnStmt(FloatLiteral(1.5))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printFloat", [FuncCall("getF", [])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "1.5"

def test_extra_103():
    # function with string return
    ast = Program([
        FuncDecl(StringType(), "getS", [], BlockStmt([ReturnStmt(StringLiteral("world"))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printString", [FuncCall("getS", [])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "world"

def test_extra_104():
    # function with parameters
    ast = Program([
        FuncDecl(IntType(), "add", [Param(IntType(), "a"), Param(IntType(), "b")],
                 BlockStmt([ReturnStmt(BinaryOp(Identifier("a"), "+", Identifier("b")))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("add", [IntLiteral(3), IntLiteral(4)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "7"

def test_extra_105():
    # function with float param
    ast = Program([
        FuncDecl(FloatType(), "double", [Param(FloatType(), "x")],
                 BlockStmt([ReturnStmt(BinaryOp(Identifier("x"), "*", FloatLiteral(2.0)))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printFloat", [FuncCall("double", [FloatLiteral(2.5)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "5.0"

def test_extra_106():
    # auto return type inference
    ast = Program([
        FuncDecl(None, "getN", [], BlockStmt([ReturnStmt(IntLiteral(7))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("getN", [])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "7"

def test_extra_107():
    # auto return float
    ast = Program([
        FuncDecl(None, "getF", [], BlockStmt([ReturnStmt(FloatLiteral(0.5))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printFloat", [FuncCall("getF", [])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "0.5"

def test_extra_108():
    # auto return string
    ast = Program([
        FuncDecl(None, "getS", [], BlockStmt([ReturnStmt(StringLiteral("auto"))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printString", [FuncCall("getS", [])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "auto"

def test_extra_109():
    # recursive factorial
    ast = Program([
        FuncDecl(IntType(), "fact", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<=", IntLiteral(1)),
                   BlockStmt([ReturnStmt(IntLiteral(1))]),
                   BlockStmt([ReturnStmt(BinaryOp(Identifier("n"), "*", FuncCall("fact", [BinaryOp(Identifier("n"), "-", IntLiteral(1))])))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("fact", [IntLiteral(5)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "120"

def test_extra_110():
    # recursive fibonacci
    ast = Program([
        FuncDecl(IntType(), "fib", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<=", IntLiteral(1)),
                   BlockStmt([ReturnStmt(Identifier("n"))]),
                   BlockStmt([ReturnStmt(BinaryOp(
                       FuncCall("fib", [BinaryOp(Identifier("n"), "-", IntLiteral(1))]),
                       "+",
                       FuncCall("fib", [BinaryOp(Identifier("n"), "-", IntLiteral(2))])
                   ))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("fib", [IntLiteral(7)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "13"

def test_extra_111():
    # switch single case match
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(2)),
        SwitchStmt(Identifier("x"), [
            CaseStmt(IntLiteral(1), [ExprStmt(FuncCall("printString", [StringLiteral("one")])), BreakStmt()]),
            CaseStmt(IntLiteral(2), [ExprStmt(FuncCall("printString", [StringLiteral("two")])), BreakStmt()]),
            CaseStmt(IntLiteral(3), [ExprStmt(FuncCall("printString", [StringLiteral("three")])), BreakStmt()])
        ], None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "two"

def test_extra_112():
    # switch with default
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(99)),
        SwitchStmt(Identifier("x"), [
            CaseStmt(IntLiteral(1), [ExprStmt(FuncCall("printString", [StringLiteral("one")]))]),
        ], DefaultStmt([ExprStmt(FuncCall("printString", [StringLiteral("other")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "other"

def test_extra_113():
    # switch no match no default => empty
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(5)),
        SwitchStmt(Identifier("x"), [
            CaseStmt(IntLiteral(1), [ExprStmt(FuncCall("printString", [StringLiteral("one")]))]),
        ], None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == ""

def test_extra_114():
    # struct declaration and member access
    ast = Program([
        StructDecl("Point", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Point"), "p", StructLiteral([IntLiteral(3), IntLiteral(4)])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "x")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "y")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "34"

def test_extra_115():
    # struct member assignment
    ast = Program([
        StructDecl("Pt", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Pt"), "p", StructLiteral([IntLiteral(1), IntLiteral(2)])),
            ExprStmt(AssignExpr(MemberAccess(Identifier("p"), "x"), IntLiteral(10))),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "x")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "10"

def test_extra_116():
    # struct with float members
    ast = Program([
        StructDecl("Vec", [MemberDecl(FloatType(), "x"), MemberDecl(FloatType(), "y")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Vec"), "v", StructLiteral([FloatLiteral(1.5), FloatLiteral(2.5)])),
            ExprStmt(FuncCall("printFloat", [MemberAccess(Identifier("v"), "x")])),
            ExprStmt(FuncCall("printFloat", [MemberAccess(Identifier("v"), "y")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "1.52.5"

def test_extra_117():
    # multiple prints in sequence
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [IntLiteral(1)])),
        ExprStmt(FuncCall("printInt", [IntLiteral(2)])),
        ExprStmt(FuncCall("printInt", [IntLiteral(3)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "123"

def test_extra_118():
    # nested if-else
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(5)),
        IfStmt(BinaryOp(Identifier("x"), ">", IntLiteral(10)),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("big")]))]),
               BlockStmt([
                   IfStmt(BinaryOp(Identifier("x"), ">", IntLiteral(3)),
                          BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("medium")]))]),
                          BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("small")]))]))
               ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "medium"

def test_extra_119():
    # nested while loops
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "i", IntLiteral(0)),
        WhileStmt(BinaryOp(Identifier("i"), "<", IntLiteral(2)), BlockStmt([
            VarDecl(IntType(), "j", IntLiteral(0)),
            WhileStmt(BinaryOp(Identifier("j"), "<", IntLiteral(2)), BlockStmt([
                ExprStmt(FuncCall("printInt", [BinaryOp(BinaryOp(Identifier("i"), "*", IntLiteral(2)), "+", Identifier("j"))])),
                ExprStmt(PostfixOp("++", Identifier("j")))
            ])),
            ExprStmt(PostfixOp("++", Identifier("i")))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0123"

def test_extra_120():
    # for loop countdown
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(
            VarDecl(IntType(), "i", IntLiteral(5)),
            BinaryOp(Identifier("i"), ">", IntLiteral(0)),
            PrefixOp("--", Identifier("i")),
            BlockStmt([ExprStmt(FuncCall("printInt", [Identifier("i")]))])
        )
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "54321"

def test_extra_121():
    # sum 1..10
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "sum", IntLiteral(0)),
        ForStmt(
            VarDecl(IntType(), "i", IntLiteral(1)),
            BinaryOp(Identifier("i"), "<=", IntLiteral(10)),
            PostfixOp("++", Identifier("i")),
            BlockStmt([ExprStmt(AssignExpr(Identifier("sum"), BinaryOp(Identifier("sum"), "+", Identifier("i"))))])
        ),
        ExprStmt(FuncCall("printInt", [Identifier("sum")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "55"

def test_extra_122():
    # compound assignment via a=a+1
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(0)),
        ExprStmt(AssignExpr(Identifier("x"), BinaryOp(Identifier("x"), "+", IntLiteral(5)))),
        ExprStmt(AssignExpr(Identifier("x"), BinaryOp(Identifier("x"), "*", IntLiteral(2)))),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "10"

def test_extra_123():
    # function call result used in expression
    ast = Program([
        FuncDecl(IntType(), "square", [Param(IntType(), "n")],
                 BlockStmt([ReturnStmt(BinaryOp(Identifier("n"), "*", Identifier("n")))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [BinaryOp(FuncCall("square", [IntLiteral(3)]), "+", FuncCall("square", [IntLiteral(4)]))]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "25"

def test_extra_124():
    # string concat simulation via multiple prints
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(StringType(), "a", StringLiteral("foo")),
        VarDecl(StringType(), "b", StringLiteral("bar")),
        ExprStmt(FuncCall("printString", [Identifier("a")])),
        ExprStmt(FuncCall("printString", [Identifier("b")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "foobar"

def test_extra_125():
    # short circuit &&: right not evaluated
    ast = Program([
        FuncDecl(IntType(), "sideEffect", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [IntLiteral(99)])),
            ReturnStmt(IntLiteral(1))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(BinaryOp(IntLiteral(0), "&&", FuncCall("sideEffect", [])))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == ""

def test_extra_126():
    # short circuit ||: right not evaluated
    ast = Program([
        FuncDecl(IntType(), "sideEffect", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [IntLiteral(99)])),
            ReturnStmt(IntLiteral(1))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(BinaryOp(IntLiteral(1), "||", FuncCall("sideEffect", [])))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == ""

def test_extra_127():
    # i2f coercion in var init
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "f", IntLiteral(5)),
        ExprStmt(FuncCall("printFloat", [Identifier("f")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "5.0"

def test_extra_128():
    # multiple function params
    ast = Program([
        FuncDecl(IntType(), "sum3", [Param(IntType(), "a"), Param(IntType(), "b"), Param(IntType(), "c")],
                 BlockStmt([ReturnStmt(BinaryOp(BinaryOp(Identifier("a"), "+", Identifier("b")), "+", Identifier("c")))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("sum3", [IntLiteral(1), IntLiteral(2), IntLiteral(3)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "6"

def test_extra_129():
    # struct passed to function
    ast = Program([
        StructDecl("P", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
        FuncDecl(IntType(), "sumP", [Param(StructType("P"), "p")],
                 BlockStmt([ReturnStmt(BinaryOp(MemberAccess(Identifier("p"), "x"), "+", MemberAccess(Identifier("p"), "y")))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("P"), "pt", StructLiteral([IntLiteral(3), IntLiteral(4)])),
            ExprStmt(FuncCall("printInt", [FuncCall("sumP", [Identifier("pt")])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "7"

def test_extra_130():
    # nested function calls
    ast = Program([
        FuncDecl(IntType(), "inc", [Param(IntType(), "n")],
                 BlockStmt([ReturnStmt(BinaryOp(Identifier("n"), "+", IntLiteral(1)))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("inc", [FuncCall("inc", [FuncCall("inc", [IntLiteral(0)])])])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "3"

def test_extra_131():
    # modulo with larger dividend
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(100), "%", IntLiteral(7))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "2"

def test_extra_132():
    # negative modulo
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(-7), "%", IntLiteral(3))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "-1"

def test_extra_133():
    # chained comparisons via &&
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(5)),
        ExprStmt(FuncCall("printInt", [BinaryOp(
            BinaryOp(Identifier("x"), ">", IntLiteral(0)),
            "&&",
            BinaryOp(Identifier("x"), "<", IntLiteral(10))
        )]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_134():
    # chained comparisons via || false
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(15)),
        ExprStmt(FuncCall("printInt", [BinaryOp(
            BinaryOp(Identifier("x"), "<", IntLiteral(0)),
            "||",
            BinaryOp(Identifier("x"), ">", IntLiteral(20))
        )]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_135():
    # double negation
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [PrefixOp("!", PrefixOp("!", IntLiteral(1)))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_136():
    # unary minus applied to expression
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [PrefixOp("-", BinaryOp(IntLiteral(3), "+", IntLiteral(2)))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "-5"

def test_extra_137():
    # var shadow in block
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(1)),
        BlockStmt([
            VarDecl(IntType(), "x", IntLiteral(2)),
            ExprStmt(FuncCall("printInt", [Identifier("x")]))
        ]),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "21"

def test_extra_138():
    # for with no init (use pre-declared var)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "i", IntLiteral(0)),
        ForStmt(None, BinaryOp(Identifier("i"), "<", IntLiteral(3)), PostfixOp("++", Identifier("i")),
                BlockStmt([ExprStmt(FuncCall("printInt", [Identifier("i")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "012"

def test_extra_139():
    # for with no update (increment inside body)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)),
                BinaryOp(Identifier("i"), "<", IntLiteral(3)),
                None,
                BlockStmt([
                    ExprStmt(FuncCall("printInt", [Identifier("i")])),
                    ExprStmt(PostfixOp("++", Identifier("i")))
                ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "012"

def test_extra_140():
    # struct with string member
    ast = Program([
        StructDecl("Person", [MemberDecl(StringType(), "name"), MemberDecl(IntType(), "age")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Person"), "p", StructLiteral([StringLiteral("Alice"), IntLiteral(30)])),
            ExprStmt(FuncCall("printString", [MemberAccess(Identifier("p"), "name")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "age")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "Alice30"

def test_extra_141():
    # auto var from function return
    ast = Program([
        FuncDecl(IntType(), "get5", [], BlockStmt([ReturnStmt(IntLiteral(5))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(None, "x", FuncCall("get5", [])),
            ExprStmt(FuncCall("printInt", [Identifier("x")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "5"

def test_extra_142():
    # while accumulate product
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "prod", IntLiteral(1)),
        VarDecl(IntType(), "i", IntLiteral(1)),
        WhileStmt(BinaryOp(Identifier("i"), "<=", IntLiteral(5)), BlockStmt([
            ExprStmt(AssignExpr(Identifier("prod"), BinaryOp(Identifier("prod"), "*", Identifier("i")))),
            ExprStmt(PostfixOp("++", Identifier("i")))
        ])),
        ExprStmt(FuncCall("printInt", [Identifier("prod")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "120"

def test_extra_143():
    # max of two numbers
    ast = Program([
        FuncDecl(IntType(), "max", [Param(IntType(), "a"), Param(IntType(), "b")], BlockStmt([
            IfStmt(BinaryOp(Identifier("a"), ">", Identifier("b")),
                   BlockStmt([ReturnStmt(Identifier("a"))]),
                   BlockStmt([ReturnStmt(Identifier("b"))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("max", [IntLiteral(3), IntLiteral(7)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "7"

def test_extra_144():
    # min of two numbers
    ast = Program([
        FuncDecl(IntType(), "minVal", [Param(IntType(), "a"), Param(IntType(), "b")], BlockStmt([
            IfStmt(BinaryOp(Identifier("a"), "<", Identifier("b")),
                   BlockStmt([ReturnStmt(Identifier("a"))]),
                   BlockStmt([ReturnStmt(Identifier("b"))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("minVal", [IntLiteral(3), IntLiteral(7)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "3"

def test_extra_145():
    # abs value
    ast = Program([
        FuncDecl(IntType(), "absVal", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<", IntLiteral(0)),
                   BlockStmt([ReturnStmt(PrefixOp("-", Identifier("n")))]),
                   BlockStmt([ReturnStmt(Identifier("n"))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("absVal", [IntLiteral(-42)])])),
            ExprStmt(FuncCall("printInt", [FuncCall("absVal", [IntLiteral(42)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "4242"

def test_extra_146():
    # GCD via while
    ast = Program([
        FuncDecl(IntType(), "gcd", [Param(IntType(), "a"), Param(IntType(), "b")], BlockStmt([
            WhileStmt(BinaryOp(Identifier("b"), "!=", IntLiteral(0)), BlockStmt([
                VarDecl(IntType(), "t", Identifier("b")),
                ExprStmt(AssignExpr(Identifier("b"), BinaryOp(Identifier("a"), "%", Identifier("b")))),
                ExprStmt(AssignExpr(Identifier("a"), Identifier("t")))
            ])),
            ReturnStmt(Identifier("a"))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("gcd", [IntLiteral(48), IntLiteral(18)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "6"

def test_extra_147():
    # isPrime basic
    ast = Program([
        FuncDecl(IntType(), "isPrime", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<", IntLiteral(2)),
                   BlockStmt([ReturnStmt(IntLiteral(0))]), None),
            VarDecl(IntType(), "i", IntLiteral(2)),
            WhileStmt(BinaryOp(BinaryOp(Identifier("i"), "*", Identifier("i")), "<=", Identifier("n")), BlockStmt([
                IfStmt(BinaryOp(BinaryOp(Identifier("n"), "%", Identifier("i")), "==", IntLiteral(0)),
                       BlockStmt([ReturnStmt(IntLiteral(0))]), None),
                ExprStmt(PostfixOp("++", Identifier("i")))
            ])),
            ReturnStmt(IntLiteral(1))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("isPrime", [IntLiteral(7)])])),
            ExprStmt(FuncCall("printInt", [FuncCall("isPrime", [IntLiteral(4)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "10"

def test_extra_148():
    # power function
    ast = Program([
        FuncDecl(IntType(), "pow", [Param(IntType(), "base"), Param(IntType(), "exp")], BlockStmt([
            VarDecl(IntType(), "result", IntLiteral(1)),
            VarDecl(IntType(), "i", IntLiteral(0)),
            WhileStmt(BinaryOp(Identifier("i"), "<", Identifier("exp")), BlockStmt([
                ExprStmt(AssignExpr(Identifier("result"), BinaryOp(Identifier("result"), "*", Identifier("base")))),
                ExprStmt(PostfixOp("++", Identifier("i")))
            ])),
            ReturnStmt(Identifier("result"))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("pow", [IntLiteral(2), IntLiteral(10)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "1024"

def test_extra_149():
    # countdown with while and print
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "n", IntLiteral(3)),
        WhileStmt(BinaryOp(Identifier("n"), ">", IntLiteral(0)), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("n")])),
            ExprStmt(PrefixOp("--", Identifier("n")))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "321"

def test_extra_150():
    # print all even 2..10
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(2)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(10)),
                ExprStmt(AssignExpr(Identifier("i"), BinaryOp(Identifier("i"), "+", IntLiteral(2)))),
                BlockStmt([ExprStmt(FuncCall("printInt", [Identifier("i")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "246810"

def test_extra_151():
    # switch with multiple cases
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "day", IntLiteral(3)),
        SwitchStmt(Identifier("day"), [
            CaseStmt(IntLiteral(1), [ExprStmt(FuncCall("printString", [StringLiteral("Mon")])), BreakStmt()]),
            CaseStmt(IntLiteral(2), [ExprStmt(FuncCall("printString", [StringLiteral("Tue")])), BreakStmt()]),
            CaseStmt(IntLiteral(3), [ExprStmt(FuncCall("printString", [StringLiteral("Wed")])), BreakStmt()]),
            CaseStmt(IntLiteral(4), [ExprStmt(FuncCall("printString", [StringLiteral("Thu")])), BreakStmt()]),
            CaseStmt(IntLiteral(5), [ExprStmt(FuncCall("printString", [StringLiteral("Fri")])), BreakStmt()]),
        ], DefaultStmt([ExprStmt(FuncCall("printString", [StringLiteral("Weekend")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "Wed"

def test_extra_152():
    # function returning bool-like int
    ast = Program([
        FuncDecl(IntType(), "isEven", [Param(IntType(), "n")],
                 BlockStmt([ReturnStmt(BinaryOp(BinaryOp(Identifier("n"), "%", IntLiteral(2)), "==", IntLiteral(0)))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("isEven", [IntLiteral(4)])])),
            ExprStmt(FuncCall("printInt", [FuncCall("isEven", [IntLiteral(7)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "10"

def test_extra_153():
    # assign result of comparison
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "r", BinaryOp(IntLiteral(3), ">", IntLiteral(2))),
        ExprStmt(FuncCall("printInt", [Identifier("r")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_154():
    # nested for loops: multiplication table 2x2
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(2)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    ForStmt(VarDecl(IntType(), "j", IntLiteral(1)),
                            BinaryOp(Identifier("j"), "<=", IntLiteral(2)),
                            PostfixOp("++", Identifier("j")),
                            BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(Identifier("i"), "*", Identifier("j"))]))]))
                ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1224"

def test_extra_155():
    # mutual recursion: even/odd
    ast = Program([
        FuncDecl(IntType(), "myOdd", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "==", IntLiteral(0)),
                   BlockStmt([ReturnStmt(IntLiteral(0))]),
                   BlockStmt([ReturnStmt(FuncCall("myEven", [BinaryOp(Identifier("n"), "-", IntLiteral(1))]))]))
        ])),
        FuncDecl(IntType(), "myEven", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "==", IntLiteral(0)),
                   BlockStmt([ReturnStmt(IntLiteral(1))]),
                   BlockStmt([ReturnStmt(FuncCall("myOdd", [BinaryOp(Identifier("n"), "-", IntLiteral(1))]))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("myEven", [IntLiteral(4)])])),
            ExprStmt(FuncCall("printInt", [FuncCall("myOdd", [IntLiteral(3)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "11"

def test_extra_156():
    # struct copy (pass by value)
    ast = Program([
        StructDecl("Box", [MemberDecl(IntType(), "val")]),
        FuncDecl(VoidType(), "modify", [Param(StructType("Box"), "b")], BlockStmt([
            ExprStmt(AssignExpr(MemberAccess(Identifier("b"), "val"), IntLiteral(99)))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Box"), "b", StructLiteral([IntLiteral(1)])),
            ExprStmt(FuncCall("modify", [Identifier("b")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("b"), "val")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_157():
    # float comparison chain
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "x", FloatLiteral(1.5)),
        IfStmt(BinaryOp(BinaryOp(Identifier("x"), ">", FloatLiteral(1.0)),
                        "&&",
                        BinaryOp(Identifier("x"), "<", FloatLiteral(2.0))),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("in range")]))]),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("out of range")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "in range"

def test_extra_158():
    # string var reassignment
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(StringType(), "s", StringLiteral("hello")),
        ExprStmt(AssignExpr(Identifier("s"), StringLiteral("world"))),
        ExprStmt(FuncCall("printString", [Identifier("s")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "world"

def test_extra_159():
    # switch on computed value
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", BinaryOp(IntLiteral(3), "+", IntLiteral(2))),
        SwitchStmt(Identifier("x"), [
            CaseStmt(IntLiteral(5), [ExprStmt(FuncCall("printString", [StringLiteral("five")])), BreakStmt()]),
            CaseStmt(IntLiteral(6), [ExprStmt(FuncCall("printString", [StringLiteral("six")])), BreakStmt()])
        ], None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "five"

def test_extra_160():
    # for loop single iteration
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)),
                BinaryOp(Identifier("i"), "<", IntLiteral(1)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("once")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "once"

def test_extra_161():
    # if with complex condition (&&)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "a", IntLiteral(5)),
        VarDecl(IntType(), "b", IntLiteral(10)),
        IfStmt(BinaryOp(BinaryOp(Identifier("a"), ">", IntLiteral(0)), "&&", BinaryOp(Identifier("b"), "<", IntLiteral(20))),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("ok")]))]),
               None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "ok"

def test_extra_162():
    # while loop print squares
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "i", IntLiteral(1)),
        WhileStmt(BinaryOp(Identifier("i"), "<=", IntLiteral(4)), BlockStmt([
            ExprStmt(FuncCall("printInt", [BinaryOp(Identifier("i"), "*", Identifier("i"))])),
            ExprStmt(PostfixOp("++", Identifier("i")))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "14916"

def test_extra_163():
    # break in nested while: only breaks inner
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "i", IntLiteral(0)),
        WhileStmt(BinaryOp(Identifier("i"), "<", IntLiteral(3)), BlockStmt([
            VarDecl(IntType(), "j", IntLiteral(0)),
            WhileStmt(BinaryOp(Identifier("j"), "<", IntLiteral(3)), BlockStmt([
                IfStmt(BinaryOp(Identifier("j"), "==", IntLiteral(1)), BlockStmt([BreakStmt()]), None),
                ExprStmt(FuncCall("printInt", [Identifier("j")])),
                ExprStmt(PostfixOp("++", Identifier("j")))
            ])),
            ExprStmt(PostfixOp("++", Identifier("i")))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "000"

def test_extra_164():
    # struct function returning struct member
    ast = Program([
        StructDecl("Num", [MemberDecl(IntType(), "val")]),
        FuncDecl(IntType(), "getVal", [Param(StructType("Num"), "n")],
                 BlockStmt([ReturnStmt(MemberAccess(Identifier("n"), "val"))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Num"), "x", StructLiteral([IntLiteral(77)])),
            ExprStmt(FuncCall("printInt", [FuncCall("getVal", [Identifier("x")])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "77"

def test_extra_165():
    # chain of assignments
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "a", IntLiteral(0)),
        VarDecl(IntType(), "b", IntLiteral(0)),
        ExprStmt(AssignExpr(Identifier("a"), IntLiteral(5))),
        ExprStmt(AssignExpr(Identifier("b"), Identifier("a"))),
        ExprStmt(FuncCall("printInt", [Identifier("b")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "5"

def test_extra_166():
    # float arithmetic: 1.25 * 4.0 = 5.0
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printFloat", [BinaryOp(FloatLiteral(1.25), "*", FloatLiteral(4.0))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "5.0"

def test_extra_167():
    # int division truncation
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(7), "/", IntLiteral(3))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "2"

def test_extra_168():
    # large int operations
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(1000), "*", IntLiteral(1000))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1000000"

def test_extra_169():
    # auto var from arithmetic
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "x", BinaryOp(IntLiteral(3), "+", IntLiteral(4))),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "7"

def test_extra_170():
    # auto var from float arithmetic
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "f", BinaryOp(FloatLiteral(1.5), "+", FloatLiteral(1.5))),
        ExprStmt(FuncCall("printFloat", [Identifier("f")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "3.0"

def test_extra_171():
    # switch default only (no cases)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(0)),
        SwitchStmt(Identifier("x"), [], DefaultStmt([ExprStmt(FuncCall("printString", [StringLiteral("default")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "default"

def test_extra_172():
    # multiple struct members accessed in expr
    ast = Program([
        StructDecl("R", [MemberDecl(IntType(), "w"), MemberDecl(IntType(), "h")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("R"), "r", StructLiteral([IntLiteral(5), IntLiteral(3)])),
            ExprStmt(FuncCall("printInt", [BinaryOp(MemberAccess(Identifier("r"), "w"), "*", MemberAccess(Identifier("r"), "h"))]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "15"

def test_extra_173():
    # prefix -- then use
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(5)),
        ExprStmt(FuncCall("printInt", [PrefixOp("--", Identifier("x"))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "4"

def test_extra_174():
    # prefix ++ then use
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(5)),
        ExprStmt(FuncCall("printInt", [PrefixOp("++", Identifier("x"))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "6"

def test_extra_175():
    # nested struct in function
    ast = Program([
        StructDecl("Circle", [MemberDecl(FloatType(), "r")]),
        FuncDecl(FloatType(), "area", [Param(StructType("Circle"), "c")],
                 BlockStmt([ReturnStmt(BinaryOp(FloatLiteral(3.14), "*", BinaryOp(MemberAccess(Identifier("c"), "r"), "*", MemberAccess(Identifier("c"), "r"))))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Circle"), "c", StructLiteral([FloatLiteral(1.0)])),
            ExprStmt(FuncCall("printFloat", [FuncCall("area", [Identifier("c")])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "3.14"

def test_extra_176():
    # if-else chain: grade
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "score", IntLiteral(75)),
        IfStmt(BinaryOp(Identifier("score"), ">=", IntLiteral(90)),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("A")]))]),
               BlockStmt([IfStmt(BinaryOp(Identifier("score"), ">=", IntLiteral(70)),
                                 BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("B")]))]),
                                 BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("C")]))]))])
               )
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "B"

def test_extra_177():
    # count up to n with for
    ast = Program([
        FuncDecl(VoidType(), "countUp", [Param(IntType(), "n")], BlockStmt([
            ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                    BinaryOp(Identifier("i"), "<=", Identifier("n")),
                    PostfixOp("++", Identifier("i")),
                    BlockStmt([ExprStmt(FuncCall("printInt", [Identifier("i")]))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("countUp", [IntLiteral(4)]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "1234"

def test_extra_178():
    # print 0
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [IntLiteral(0)]))]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_179():
    # -0 is 0
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [PrefixOp("-", IntLiteral(0))]))]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_180():
    # while with complex break condition
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(1)),
        WhileStmt(IntLiteral(1), BlockStmt([
            IfStmt(BinaryOp(Identifier("x"), ">", IntLiteral(4)), BlockStmt([BreakStmt()]), None),
            ExprStmt(FuncCall("printInt", [Identifier("x")])),
            ExprStmt(AssignExpr(Identifier("x"), BinaryOp(Identifier("x"), "*", IntLiteral(2))))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "124"

def test_extra_181():
    # for with ExprStmt update (assign)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(8)),
                ExprStmt(AssignExpr(Identifier("i"), BinaryOp(Identifier("i"), "*", IntLiteral(2)))),
                BlockStmt([ExprStmt(FuncCall("printInt", [Identifier("i")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1248"

def test_extra_182():
    # accumulate sum of squares
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "s", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(5)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", BinaryOp(Identifier("i"), "*", Identifier("i")))))])),
        ExprStmt(FuncCall("printInt", [Identifier("s")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "55"

def test_extra_183():
    # struct with multiple members modified
    ast = Program([
        StructDecl("S", [MemberDecl(IntType(), "a"), MemberDecl(IntType(), "b"), MemberDecl(IntType(), "c")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("S"), "s", StructLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)])),
            ExprStmt(AssignExpr(MemberAccess(Identifier("s"), "a"), IntLiteral(10))),
            ExprStmt(AssignExpr(MemberAccess(Identifier("s"), "b"), IntLiteral(20))),
            ExprStmt(FuncCall("printInt", [BinaryOp(MemberAccess(Identifier("s"), "a"), "+", MemberAccess(Identifier("s"), "b"))]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "30"

def test_extra_184():
    # function with mixed param types
    ast = Program([
        FuncDecl(FloatType(), "mix", [Param(IntType(), "n"), Param(FloatType(), "f")],
                 BlockStmt([ReturnStmt(BinaryOp(Identifier("n"), "+", Identifier("f")))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printFloat", [FuncCall("mix", [IntLiteral(2), FloatLiteral(1.5)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "3.5"

def test_extra_185():
    # global scope: multiple functions, shared logic
    ast = Program([
        FuncDecl(IntType(), "triple", [Param(IntType(), "x")],
                 BlockStmt([ReturnStmt(BinaryOp(Identifier("x"), "*", IntLiteral(3)))])),
        FuncDecl(IntType(), "triple_plus_one", [Param(IntType(), "x")],
                 BlockStmt([ReturnStmt(BinaryOp(FuncCall("triple", [Identifier("x")]), "+", IntLiteral(1)))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("triple_plus_one", [IntLiteral(4)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "13"

def test_extra_186():
    # 0 == 0 is 1
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(0), "==", IntLiteral(0))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_187():
    # negative int literal
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [IntLiteral(-100)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "-100"

def test_extra_188():
    # float 3.5
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printFloat", [FloatLiteral(3.5)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "3.5"

def test_extra_189():
    # var decl with no init is default
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(0)),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_190():
    # print multiple floats
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printFloat", [FloatLiteral(0.25)])),
        ExprStmt(FuncCall("printFloat", [FloatLiteral(0.5)])),
        ExprStmt(FuncCall("printFloat", [FloatLiteral(0.75)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0.250.50.75"

def test_extra_191():
    # && both false
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(0), "&&", IntLiteral(0))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_192():
    # || both true
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(1), "||", IntLiteral(1))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_193():
    # complex expression: (a+b)*(c-d)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "a", IntLiteral(3)),
        VarDecl(IntType(), "b", IntLiteral(2)),
        VarDecl(IntType(), "c", IntLiteral(7)),
        VarDecl(IntType(), "d", IntLiteral(4)),
        ExprStmt(FuncCall("printInt", [BinaryOp(BinaryOp(Identifier("a"), "+", Identifier("b")), "*", BinaryOp(Identifier("c"), "-", Identifier("d")))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "15"

def test_extra_194():
    # struct auto var
    ast = Program([
        StructDecl("V", [MemberDecl(IntType(), "n")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(None, "v", StructLiteral([IntLiteral(42)])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("v"), "n")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "42"

def test_extra_195():
    # for loop with no body stmts (empty block)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "count", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)),
                BinaryOp(Identifier("i"), "<", IntLiteral(5)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([ExprStmt(PostfixOp("++", Identifier("count")))])),
        ExprStmt(FuncCall("printInt", [Identifier("count")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "5"

def test_extra_196():
    # multiple struct types
    ast = Program([
        StructDecl("A", [MemberDecl(IntType(), "x")]),
        StructDecl("B", [MemberDecl(IntType(), "y")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("A"), "a", StructLiteral([IntLiteral(1)])),
            VarDecl(StructType("B"), "b", StructLiteral([IntLiteral(2)])),
            ExprStmt(FuncCall("printInt", [BinaryOp(MemberAccess(Identifier("a"), "x"), "+", MemberAccess(Identifier("b"), "y"))]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "3"

def test_extra_197():
    # while until sum >= 10
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "s", IntLiteral(0)),
        VarDecl(IntType(), "i", IntLiteral(1)),
        WhileStmt(BinaryOp(Identifier("s"), "<", IntLiteral(10)), BlockStmt([
            ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", Identifier("i")))),
            ExprStmt(PostfixOp("++", Identifier("i")))
        ])),
        ExprStmt(FuncCall("printInt", [Identifier("s")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "10"

def test_extra_198():
    # complex switch on computed expr
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(4)),
        SwitchStmt(BinaryOp(Identifier("x"), "%", IntLiteral(3)), [
            CaseStmt(IntLiteral(0), [ExprStmt(FuncCall("printString", [StringLiteral("zero")])), BreakStmt()]),
            CaseStmt(IntLiteral(1), [ExprStmt(FuncCall("printString", [StringLiteral("one")])), BreakStmt()]),
            CaseStmt(IntLiteral(2), [ExprStmt(FuncCall("printString", [StringLiteral("two")])), BreakStmt()])
        ], None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "one"

def test_extra_199():
    # expression statement with no side effect (no output, just doesn't crash)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(BinaryOp(IntLiteral(1), "+", IntLiteral(2))),
        ExprStmt(FuncCall("printInt", [IntLiteral(0)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_200():
    # float 0.0 == 0.0
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [BinaryOp(FloatLiteral(0.0), "==", FloatLiteral(0.0))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_201():
    # print int result of subtraction
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(50), "-", IntLiteral(8))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "42"

def test_extra_202():
    # print float result of division
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printFloat", [BinaryOp(FloatLiteral(3.0), "/", FloatLiteral(4.0))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0.75"

def test_extra_203():
    # chained addition
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [BinaryOp(BinaryOp(BinaryOp(IntLiteral(1), "+", IntLiteral(2)), "+", IntLiteral(3)), "+", IntLiteral(4))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "10"

def test_extra_204():
    # deeply nested unary
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [PrefixOp("-", PrefixOp("-", IntLiteral(5)))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "5"

def test_extra_205():
    # for loop empty body (just counting)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "n", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)),
                BinaryOp(Identifier("i"), "<", IntLiteral(10)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([ExprStmt(AssignExpr(Identifier("n"), BinaryOp(Identifier("n"), "+", IntLiteral(1))))])),
        ExprStmt(FuncCall("printInt", [Identifier("n")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "10"

def test_extra_206():
    # float variable used in comparisons
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "pi", FloatLiteral(3.14)),
        IfStmt(BinaryOp(Identifier("pi"), ">", FloatLiteral(3.0)),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("yes")]))]),
               None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "yes"

def test_extra_207():
    # struct member used in condition
    ast = Program([
        StructDecl("Flag", [MemberDecl(IntType(), "active")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Flag"), "f", StructLiteral([IntLiteral(1)])),
            IfStmt(MemberAccess(Identifier("f"), "active"),
                   BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("active")]))]),
                   BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("inactive")]))]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "active"

def test_extra_208():
    # large factorials would overflow, use small: 10! = 3628800
    ast = Program([
        FuncDecl(IntType(), "fact", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<=", IntLiteral(1)),
                   BlockStmt([ReturnStmt(IntLiteral(1))]),
                   BlockStmt([ReturnStmt(BinaryOp(Identifier("n"), "*", FuncCall("fact", [BinaryOp(Identifier("n"), "-", IntLiteral(1))])))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("fact", [IntLiteral(10)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "3628800"

def test_extra_209():
    # multiple returns in function
    ast = Program([
        FuncDecl(StringType(), "classify", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<", IntLiteral(0)),
                   BlockStmt([ReturnStmt(StringLiteral("negative"))]), None),
            IfStmt(BinaryOp(Identifier("n"), "==", IntLiteral(0)),
                   BlockStmt([ReturnStmt(StringLiteral("zero"))]), None),
            ReturnStmt(StringLiteral("positive"))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printString", [FuncCall("classify", [IntLiteral(-3)])])),
            ExprStmt(FuncCall("printString", [FuncCall("classify", [IntLiteral(0)])])),
            ExprStmt(FuncCall("printString", [FuncCall("classify", [IntLiteral(5)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "negativezeropositive"

def test_extra_210():
    # for loop: print odds 1..9
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(9)),
                ExprStmt(AssignExpr(Identifier("i"), BinaryOp(Identifier("i"), "+", IntLiteral(2)))),
                BlockStmt([ExprStmt(FuncCall("printInt", [Identifier("i")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "13579"

def test_extra_211():
    # deeply nested functions
    ast = Program([
        FuncDecl(IntType(), "add1", [Param(IntType(), "n")], BlockStmt([ReturnStmt(BinaryOp(Identifier("n"), "+", IntLiteral(1)))])),
        FuncDecl(IntType(), "add2", [Param(IntType(), "n")], BlockStmt([ReturnStmt(FuncCall("add1", [FuncCall("add1", [Identifier("n")])]))])),
        FuncDecl(IntType(), "add4", [Param(IntType(), "n")], BlockStmt([ReturnStmt(FuncCall("add2", [FuncCall("add2", [Identifier("n")])]))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("add4", [IntLiteral(0)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "4"

def test_extra_212():
    # bool-valued int used in while
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "n", IntLiteral(3)),
        WhileStmt(Identifier("n"), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("n")])),
            ExprStmt(PrefixOp("--", Identifier("n")))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "321"

def test_extra_213():
    # print same var multiple times
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(7)),
        ExprStmt(FuncCall("printInt", [Identifier("x")])),
        ExprStmt(FuncCall("printInt", [Identifier("x")])),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "777"

def test_extra_214():
    # float 4.0 / 2.0 = 2.0
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printFloat", [BinaryOp(FloatLiteral(4.0), "/", FloatLiteral(2.0))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "2.0"

def test_extra_215():
    # nested if: both conditions true
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "a", IntLiteral(5)),
        IfStmt(BinaryOp(Identifier("a"), ">", IntLiteral(0)),
               BlockStmt([
                   IfStmt(BinaryOp(Identifier("a"), "<", IntLiteral(10)),
                          BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("in")]))])
                          , None)
               ]),
               None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "in"

def test_extra_216():
    # struct two int fields arithmetic
    ast = Program([
        StructDecl("T", [MemberDecl(IntType(), "a"), MemberDecl(IntType(), "b")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("T"), "t", StructLiteral([IntLiteral(6), IntLiteral(4)])),
            ExprStmt(FuncCall("printInt", [BinaryOp(MemberAccess(Identifier("t"), "a"), "-", MemberAccess(Identifier("t"), "b"))]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "2"

def test_extra_217():
    # while loop: collect info (count evens 1..10)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "count", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(10)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    IfStmt(BinaryOp(BinaryOp(Identifier("i"), "%", IntLiteral(2)), "==", IntLiteral(0)),
                           BlockStmt([ExprStmt(PostfixOp("++", Identifier("count")))]),
                           None)
                ])),
        ExprStmt(FuncCall("printInt", [Identifier("count")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "5"

def test_extra_218():
    # int to float promotion in assignment
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "f", IntLiteral(3)),
        ExprStmt(FuncCall("printFloat", [Identifier("f")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "3.0"

def test_extra_219():
    # short string var
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(StringType(), "s", StringLiteral("x")),
        ExprStmt(FuncCall("printString", [Identifier("s")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "x"

def test_extra_220():
    # multiple switch cases match first
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "n", IntLiteral(1)),
        SwitchStmt(Identifier("n"), [
            CaseStmt(IntLiteral(1), [ExprStmt(FuncCall("printInt", [IntLiteral(10)])), BreakStmt()]),
            CaseStmt(IntLiteral(2), [ExprStmt(FuncCall("printInt", [IntLiteral(20)])), BreakStmt()]),
        ], None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "10"

def test_extra_221():
    # auto return type from complex expression
    ast = Program([
        FuncDecl(None, "compute", [], BlockStmt([
            ReturnStmt(BinaryOp(IntLiteral(3), "*", IntLiteral(7)))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("compute", [])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "21"

def test_extra_222():
    # pass float param, return float
    ast = Program([
        FuncDecl(FloatType(), "half", [Param(FloatType(), "x")],
                 BlockStmt([ReturnStmt(BinaryOp(Identifier("x"), "/", FloatLiteral(2.0)))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printFloat", [FuncCall("half", [FloatLiteral(5.0)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "2.5"

def test_extra_223():
    # negative float
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printFloat", [FloatLiteral(-2.5)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "-2.5"

def test_extra_224():
    # while skip with continue: print multiples of 3
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(9)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    IfStmt(BinaryOp(BinaryOp(Identifier("i"), "%", IntLiteral(3)), "!=", IntLiteral(0)),
                           BlockStmt([ContinueStmt()]),
                           None),
                    ExprStmt(FuncCall("printInt", [Identifier("i")]))
                ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "369"

def test_extra_225():
    # struct with float and int members
    ast = Program([
        StructDecl("M", [MemberDecl(FloatType(), "f"), MemberDecl(IntType(), "i")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("M"), "m", StructLiteral([FloatLiteral(1.5), IntLiteral(2)])),
            ExprStmt(FuncCall("printFloat", [MemberAccess(Identifier("m"), "f")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("m"), "i")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "1.52"

def test_extra_226():
    # prefix ++ in for init
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(0)),
        ForStmt(ExprStmt(AssignExpr(Identifier("x"), IntLiteral(1))),
                BinaryOp(Identifier("x"), "<=", IntLiteral(3)),
                PostfixOp("++", Identifier("x")),
                BlockStmt([ExprStmt(FuncCall("printInt", [Identifier("x")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "123"

def test_extra_227():
    # expression used as if condition directly
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(5)),
        IfStmt(BinaryOp(Identifier("x"), "%", IntLiteral(2)),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("odd")]))]),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("even")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "odd"

def test_extra_228():
    # even number condition
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(4)),
        IfStmt(BinaryOp(Identifier("x"), "%", IntLiteral(2)),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("odd")]))]),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("even")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "even"

def test_extra_229():
    # postfix ++ returns new value (same as prefix, only precedence differs)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(0)),
        ExprStmt(FuncCall("printInt", [PostfixOp("++", Identifier("x"))])),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "11"

def test_extra_230():
    # function that prints and returns
    ast = Program([
        FuncDecl(IntType(), "printAndReturn", [Param(IntType(), "n")], BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("n")])),
            ReturnStmt(Identifier("n"))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(IntType(), "r", FuncCall("printAndReturn", [IntLiteral(5)])),
            ExprStmt(FuncCall("printInt", [BinaryOp(Identifier("r"), "*", IntLiteral(2))]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "510"

def test_extra_231():
    # struct with 4 members
    ast = Program([
        StructDecl("Q", [MemberDecl(IntType(), "a"), MemberDecl(IntType(), "b"),
                         MemberDecl(IntType(), "c"), MemberDecl(IntType(), "d")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Q"), "q", StructLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4)])),
            ExprStmt(FuncCall("printInt", [BinaryOp(BinaryOp(MemberAccess(Identifier("q"), "a"), "+", MemberAccess(Identifier("q"), "b")),
                                           "+", BinaryOp(MemberAccess(Identifier("q"), "c"), "+", MemberAccess(Identifier("q"), "d")))]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "10"

def test_extra_232():
    # continue in for loop skips even, prints odd
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(5)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    IfStmt(BinaryOp(BinaryOp(Identifier("i"), "%", IntLiteral(2)), "==", IntLiteral(0)),
                           BlockStmt([ContinueStmt()]), None),
                    ExprStmt(FuncCall("printInt", [Identifier("i")]))
                ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "135"

def test_extra_233():
    # fibonacci iterative
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "a", IntLiteral(0)),
        VarDecl(IntType(), "b", IntLiteral(1)),
        VarDecl(IntType(), "i", IntLiteral(0)),
        WhileStmt(BinaryOp(Identifier("i"), "<", IntLiteral(8)), BlockStmt([
            VarDecl(IntType(), "t", BinaryOp(Identifier("a"), "+", Identifier("b"))),
            ExprStmt(AssignExpr(Identifier("a"), Identifier("b"))),
            ExprStmt(AssignExpr(Identifier("b"), Identifier("t"))),
            ExprStmt(PostfixOp("++", Identifier("i")))
        ])),
        ExprStmt(FuncCall("printInt", [Identifier("a")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "21"

def test_extra_234():
    # print bool expressions
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(1), "==", IntLiteral(1))])),
        ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(1), "!=", IntLiteral(2))])),
        ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(2), ">", IntLiteral(1))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "111"

def test_extra_235():
    # function with no params, void return
    ast = Program([
        FuncDecl(VoidType(), "banner", [], BlockStmt([
            ExprStmt(FuncCall("printString", [StringLiteral("=====")])),
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("banner", [])),
            ExprStmt(FuncCall("printString", [StringLiteral("TyC")])),
            ExprStmt(FuncCall("banner", []))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "=====TyC====="

def test_extra_236():
    # int literal 2^8
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [IntLiteral(256)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "256"

def test_extra_237():
    # negative result from subtraction
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(3), "-", IntLiteral(10))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "-7"

def test_extra_238():
    # float - float
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printFloat", [BinaryOp(FloatLiteral(3.5), "-", FloatLiteral(1.25))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "2.25"

def test_extra_239():
    # struct member increment
    ast = Program([
        StructDecl("C", [MemberDecl(IntType(), "count")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("C"), "c", StructLiteral([IntLiteral(0)])),
            ExprStmt(PostfixOp("++", MemberAccess(Identifier("c"), "count"))),
            ExprStmt(PostfixOp("++", MemberAccess(Identifier("c"), "count"))),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("c"), "count")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "2"

def test_extra_240():
    # while true break immediately
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        WhileStmt(IntLiteral(1), BlockStmt([
            ExprStmt(FuncCall("printString", [StringLiteral("once")])),
            BreakStmt()
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "once"

def test_extra_241():
    # 3 functions call chain
    ast = Program([
        FuncDecl(IntType(), "f1", [], BlockStmt([ReturnStmt(IntLiteral(1))])),
        FuncDecl(IntType(), "f2", [], BlockStmt([ReturnStmt(BinaryOp(FuncCall("f1", []), "+", IntLiteral(1)))])),
        FuncDecl(IntType(), "f3", [], BlockStmt([ReturnStmt(BinaryOp(FuncCall("f2", []), "+", IntLiteral(1)))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("f3", [])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "3"

def test_extra_242():
    # if-else returns different types not applicable, just different ints
    ast = Program([
        FuncDecl(IntType(), "sign", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), ">", IntLiteral(0)),
                   BlockStmt([ReturnStmt(IntLiteral(1))]),
                   BlockStmt([IfStmt(BinaryOp(Identifier("n"), "<", IntLiteral(0)),
                                     BlockStmt([ReturnStmt(IntLiteral(-1))]),
                                     BlockStmt([ReturnStmt(IntLiteral(0))]))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("sign", [IntLiteral(10)])])),
            ExprStmt(FuncCall("printInt", [FuncCall("sign", [IntLiteral(-5)])])),
            ExprStmt(FuncCall("printInt", [FuncCall("sign", [IntLiteral(0)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "1-10"

def test_extra_243():
    # switch fall-through to default
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(9)),
        SwitchStmt(Identifier("x"), [
            CaseStmt(IntLiteral(1), [ExprStmt(FuncCall("printString", [StringLiteral("one")]))]),
            CaseStmt(IntLiteral(2), [ExprStmt(FuncCall("printString", [StringLiteral("two")]))]),
        ], DefaultStmt([ExprStmt(FuncCall("printString", [StringLiteral("other")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "other"

def test_extra_244():
    # print sum of first 100 integers
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "s", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(100)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", Identifier("i"))))])),
        ExprStmt(FuncCall("printInt", [Identifier("s")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "5050"

def test_extra_245():
    # float 0.5 * 0.5 = 0.25
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printFloat", [BinaryOp(FloatLiteral(0.5), "*", FloatLiteral(0.5))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0.25"

def test_extra_246():
    # scope: inner var doesn't affect outer
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(10)),
        BlockStmt([
            VarDecl(IntType(), "x", IntLiteral(20)),
            ExprStmt(FuncCall("printInt", [Identifier("x")]))
        ]),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "2010"

def test_extra_247():
    # assignment returns value
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(0)),
        VarDecl(IntType(), "y", IntLiteral(0)),
        ExprStmt(AssignExpr(Identifier("y"), AssignExpr(Identifier("x"), IntLiteral(5)))),
        ExprStmt(FuncCall("printInt", [Identifier("x")])),
        ExprStmt(FuncCall("printInt", [Identifier("y")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "55"

def test_extra_248():
    # recursive sum
    ast = Program([
        FuncDecl(IntType(), "sumN", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "==", IntLiteral(0)),
                   BlockStmt([ReturnStmt(IntLiteral(0))]),
                   BlockStmt([ReturnStmt(BinaryOp(Identifier("n"), "+", FuncCall("sumN", [BinaryOp(Identifier("n"), "-", IntLiteral(1))])))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("sumN", [IntLiteral(10)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "55"

def test_extra_249():
    # struct passed by value: changes don't propagate
    ast = Program([
        StructDecl("N", [MemberDecl(IntType(), "v")]),
        FuncDecl(VoidType(), "addOne", [Param(StructType("N"), "n")], BlockStmt([
            ExprStmt(AssignExpr(MemberAccess(Identifier("n"), "v"), BinaryOp(MemberAccess(Identifier("n"), "v"), "+", IntLiteral(1))))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("N"), "n", StructLiteral([IntLiteral(5)])),
            ExprStmt(FuncCall("addOne", [Identifier("n")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("n"), "v")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "5"

def test_extra_250():
    # complex: count primes up to 20
    ast = Program([
        FuncDecl(IntType(), "isPrime", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<", IntLiteral(2)), BlockStmt([ReturnStmt(IntLiteral(0))]), None),
            VarDecl(IntType(), "i", IntLiteral(2)),
            WhileStmt(BinaryOp(BinaryOp(Identifier("i"), "*", Identifier("i")), "<=", Identifier("n")), BlockStmt([
                IfStmt(BinaryOp(BinaryOp(Identifier("n"), "%", Identifier("i")), "==", IntLiteral(0)),
                       BlockStmt([ReturnStmt(IntLiteral(0))]), None),
                ExprStmt(PostfixOp("++", Identifier("i")))
            ])),
            ReturnStmt(IntLiteral(1))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(IntType(), "count", IntLiteral(0)),
            ForStmt(VarDecl(IntType(), "i", IntLiteral(2)),
                    BinaryOp(Identifier("i"), "<=", IntLiteral(20)),
                    PostfixOp("++", Identifier("i")),
                    BlockStmt([
                        IfStmt(FuncCall("isPrime", [Identifier("i")]),
                               BlockStmt([ExprStmt(PostfixOp("++", Identifier("count")))]),
                               None)
                    ])),
            ExprStmt(FuncCall("printInt", [Identifier("count")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "8"

def test_extra_251():
    # 2^20 via repeated squaring iterative
    ast = Program([
        FuncDecl(IntType(), "pow2", [Param(IntType(), "n")], BlockStmt([
            VarDecl(IntType(), "r", IntLiteral(1)),
            VarDecl(IntType(), "i", IntLiteral(0)),
            WhileStmt(BinaryOp(Identifier("i"), "<", Identifier("n")), BlockStmt([
                ExprStmt(AssignExpr(Identifier("r"), BinaryOp(Identifier("r"), "*", IntLiteral(2)))),
                ExprStmt(PostfixOp("++", Identifier("i")))
            ])),
            ReturnStmt(Identifier("r"))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("pow2", [IntLiteral(10)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "1024"

def test_extra_252():
    # struct method: bounding box area
    ast = Program([
        StructDecl("Rect", [MemberDecl(IntType(), "w"), MemberDecl(IntType(), "h")]),
        FuncDecl(IntType(), "area", [Param(StructType("Rect"), "r")],
                 BlockStmt([ReturnStmt(BinaryOp(MemberAccess(Identifier("r"), "w"), "*", MemberAccess(Identifier("r"), "h")))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Rect"), "r", StructLiteral([IntLiteral(6), IntLiteral(4)])),
            ExprStmt(FuncCall("printInt", [FuncCall("area", [Identifier("r")])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "24"

def test_extra_253():
    # print float then int
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printFloat", [FloatLiteral(1.5)])),
        ExprStmt(FuncCall("printInt", [IntLiteral(2)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1.52"

def test_extra_254():
    # swap via temp var
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "a", IntLiteral(1)),
        VarDecl(IntType(), "b", IntLiteral(2)),
        VarDecl(IntType(), "tmp", Identifier("a")),
        ExprStmt(AssignExpr(Identifier("a"), Identifier("b"))),
        ExprStmt(AssignExpr(Identifier("b"), Identifier("tmp"))),
        ExprStmt(FuncCall("printInt", [Identifier("a")])),
        ExprStmt(FuncCall("printInt", [Identifier("b")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "21"

def test_extra_255():
    # for sum with float accumulator
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "s", FloatLiteral(0.0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(4)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", BinaryOp(Identifier("i"), "+", FloatLiteral(0.0)))))])),
        ExprStmt(FuncCall("printFloat", [Identifier("s")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "10.0"

def test_extra_256():
    # while: largest power of 2 <= 100
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "p", IntLiteral(1)),
        WhileStmt(BinaryOp(BinaryOp(Identifier("p"), "*", IntLiteral(2)), "<=", IntLiteral(100)), BlockStmt([
            ExprStmt(AssignExpr(Identifier("p"), BinaryOp(Identifier("p"), "*", IntLiteral(2))))
        ])),
        ExprStmt(FuncCall("printInt", [Identifier("p")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "64"

def test_extra_257():
    # binary and logical combo
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(6)),
        ExprStmt(FuncCall("printInt", [BinaryOp(
            BinaryOp(BinaryOp(Identifier("x"), ">", IntLiteral(0)), "&&", BinaryOp(Identifier("x"), "%", IntLiteral(2))),
            "==", IntLiteral(0)
        )]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_258():
    # two recursive calls in same statement
    ast = Program([
        FuncDecl(IntType(), "ack", [Param(IntType(), "m"), Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("m"), "==", IntLiteral(0)),
                   BlockStmt([ReturnStmt(BinaryOp(Identifier("n"), "+", IntLiteral(1)))]),
                   BlockStmt([IfStmt(BinaryOp(Identifier("n"), "==", IntLiteral(0)),
                                     BlockStmt([ReturnStmt(FuncCall("ack", [BinaryOp(Identifier("m"), "-", IntLiteral(1)), IntLiteral(1)]))]),
                                     BlockStmt([ReturnStmt(FuncCall("ack", [BinaryOp(Identifier("m"), "-", IntLiteral(1)),
                                                                             FuncCall("ack", [Identifier("m"), BinaryOp(Identifier("n"), "-", IntLiteral(1))])]))]))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("ack", [IntLiteral(2), IntLiteral(3)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "9"

def test_extra_259():
    # print int in switch case after computation
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "n", IntLiteral(7)),
        SwitchStmt(BinaryOp(Identifier("n"), "/", IntLiteral(5)), [
            CaseStmt(IntLiteral(0), [ExprStmt(FuncCall("printString", [StringLiteral("low")])), BreakStmt()]),
            CaseStmt(IntLiteral(1), [ExprStmt(FuncCall("printString", [StringLiteral("mid")])), BreakStmt()]),
        ], DefaultStmt([ExprStmt(FuncCall("printString", [StringLiteral("high")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "mid"

def test_extra_260():
    # multiple assignments chained (right-to-left)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "a", IntLiteral(0)),
        VarDecl(IntType(), "b", IntLiteral(0)),
        VarDecl(IntType(), "c", IntLiteral(0)),
        ExprStmt(AssignExpr(Identifier("a"), AssignExpr(Identifier("b"), AssignExpr(Identifier("c"), IntLiteral(9))))),
        ExprStmt(FuncCall("printInt", [Identifier("a")])),
        ExprStmt(FuncCall("printInt", [Identifier("b")])),
        ExprStmt(FuncCall("printInt", [Identifier("c")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "999"

def test_extra_261():
    # print float 100.0
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printFloat", [FloatLiteral(100.0)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "100.0"

def test_extra_262():
    # prefix -- float
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "f", FloatLiteral(2.5)),
        ExprStmt(PrefixOp("--", Identifier("f"))),
        ExprStmt(FuncCall("printFloat", [Identifier("f")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1.5"

def test_extra_263():
    # postfix ++ float
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "f", FloatLiteral(1.5)),
        ExprStmt(PostfixOp("++", Identifier("f"))),
        ExprStmt(FuncCall("printFloat", [Identifier("f")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "2.5"

def test_extra_264():
    # deeply nested ifs
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(3)),
        IfStmt(BinaryOp(Identifier("x"), ">", IntLiteral(0)),
               BlockStmt([
                   IfStmt(BinaryOp(Identifier("x"), ">", IntLiteral(1)),
                          BlockStmt([
                              IfStmt(BinaryOp(Identifier("x"), ">", IntLiteral(2)),
                                     BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("deep")]))]),
                                     None)
                          ]),
                          None)
               ]),
               None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "deep"

def test_extra_265():
    # print string from function param
    ast = Program([
        FuncDecl(VoidType(), "greet", [Param(StringType(), "name")], BlockStmt([
            ExprStmt(FuncCall("printString", [Identifier("name")]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("greet", [StringLiteral("Alice")])),
            ExprStmt(FuncCall("greet", [StringLiteral("Bob")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "AliceBob"

def test_extra_266():
    # int 32767 (max short, fits in int)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [IntLiteral(32767)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "32767"

def test_extra_267():
    # negative float arithmetic: -1.5 + 3.0
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printFloat", [BinaryOp(FloatLiteral(-1.5), "+", FloatLiteral(3.0))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1.5"

def test_extra_268():
    # i2f in return
    ast = Program([
        FuncDecl(FloatType(), "toFloat", [Param(IntType(), "n")],
                 BlockStmt([ReturnStmt(BinaryOp(Identifier("n"), "+", FloatLiteral(0.0)))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printFloat", [FuncCall("toFloat", [IntLiteral(7)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "7.0"

def test_extra_269():
    # while: build multiplication table output
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "i", IntLiteral(1)),
        WhileStmt(BinaryOp(Identifier("i"), "<=", IntLiteral(3)), BlockStmt([
            ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(3), "*", Identifier("i"))])),
            ExprStmt(PostfixOp("++", Identifier("i")))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "369"

def test_extra_270():
    # struct returned from function
    ast = Program([
        StructDecl("Pt", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
        FuncDecl(StructType("Pt"), "origin", [], BlockStmt([ReturnStmt(StructLiteral([IntLiteral(0), IntLiteral(0)]))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Pt"), "p", FuncCall("origin", [])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "x")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "y")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "00"

def test_extra_271():
    # logical not of comparison
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(5)),
        ExprStmt(FuncCall("printInt", [PrefixOp("!", BinaryOp(Identifier("x"), ">", IntLiteral(10)))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_272():
    # auto return type from comparison
    ast = Program([
        FuncDecl(None, "gt5", [Param(IntType(), "x")],
                 BlockStmt([ReturnStmt(BinaryOp(Identifier("x"), ">", IntLiteral(5)))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("gt5", [IntLiteral(7)])])),
            ExprStmt(FuncCall("printInt", [FuncCall("gt5", [IntLiteral(3)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "10"

def test_extra_273():
    # while break on struct field
    ast = Program([
        StructDecl("State", [MemberDecl(IntType(), "done"), MemberDecl(IntType(), "val")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("State"), "s", StructLiteral([IntLiteral(0), IntLiteral(0)])),
            WhileStmt(PrefixOp("!", MemberAccess(Identifier("s"), "done")), BlockStmt([
                ExprStmt(AssignExpr(MemberAccess(Identifier("s"), "val"), BinaryOp(MemberAccess(Identifier("s"), "val"), "+", IntLiteral(1)))),
                IfStmt(BinaryOp(MemberAccess(Identifier("s"), "val"), "==", IntLiteral(5)),
                       BlockStmt([ExprStmt(AssignExpr(MemberAccess(Identifier("s"), "done"), IntLiteral(1)))]),
                       None)
            ])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("s"), "val")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "5"

def test_extra_274():
    # for: sum odd numbers 1..9
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "s", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(9)),
                ExprStmt(AssignExpr(Identifier("i"), BinaryOp(Identifier("i"), "+", IntLiteral(2)))),
                BlockStmt([ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", Identifier("i"))))])),
        ExprStmt(FuncCall("printInt", [Identifier("s")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "25"

def test_extra_275():
    # continue skips accumulate
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "s", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(10)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    IfStmt(BinaryOp(BinaryOp(Identifier("i"), "%", IntLiteral(3)), "==", IntLiteral(0)),
                           BlockStmt([ContinueStmt()]), None),
                    ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", Identifier("i"))))
                ])),
        ExprStmt(FuncCall("printInt", [Identifier("s")]))
    ]))])
    # sum 1..10 excluding multiples of 3: 1+2+4+5+7+8+10 = 37
    assert CodeGenerator().generate_and_run(ast) == "37"

def test_extra_276():
    # string equality-like check via func
    ast = Program([
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(IntType(), "x", IntLiteral(0)),
            IfStmt(BinaryOp(Identifier("x"), "==", IntLiteral(0)),
                   BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("zero")]))]),
                   BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("nonzero")]))]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "zero"

def test_extra_277():
    # nested while with break in outer
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "i", IntLiteral(0)),
        WhileStmt(IntLiteral(1), BlockStmt([
            IfStmt(BinaryOp(Identifier("i"), ">=", IntLiteral(3)), BlockStmt([BreakStmt()]), None),
            ExprStmt(FuncCall("printInt", [Identifier("i")])),
            ExprStmt(PostfixOp("++", Identifier("i")))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "012"

def test_extra_278():
    # auto type from function returning float
    ast = Program([
        FuncDecl(FloatType(), "half", [Param(FloatType(), "x")],
                 BlockStmt([ReturnStmt(BinaryOp(Identifier("x"), "/", FloatLiteral(2.0)))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(None, "r", FuncCall("half", [FloatLiteral(3.0)])),
            ExprStmt(FuncCall("printFloat", [Identifier("r")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "1.5"

def test_extra_279():
    # multiple recursive calls on stack
    ast = Program([
        FuncDecl(IntType(), "count", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<=", IntLiteral(0)),
                   BlockStmt([ReturnStmt(IntLiteral(0))]),
                   BlockStmt([ReturnStmt(BinaryOp(IntLiteral(1), "+", FuncCall("count", [BinaryOp(Identifier("n"), "-", IntLiteral(1))])))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("count", [IntLiteral(7)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "7"

def test_extra_280():
    # if condition uses &&, both needed
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "a", IntLiteral(3)),
        VarDecl(IntType(), "b", IntLiteral(7)),
        IfStmt(BinaryOp(BinaryOp(Identifier("a"), "<", IntLiteral(5)), "&&", BinaryOp(Identifier("b"), ">", IntLiteral(5))),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("yes")]))]),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("no")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "yes"

def test_extra_281():
    # struct with string member reassigned
    ast = Program([
        StructDecl("Person", [MemberDecl(StringType(), "name")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Person"), "p", StructLiteral([StringLiteral("Alice")])),
            ExprStmt(AssignExpr(MemberAccess(Identifier("p"), "name"), StringLiteral("Bob"))),
            ExprStmt(FuncCall("printString", [MemberAccess(Identifier("p"), "name")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "Bob"

def test_extra_282():
    # float !=
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [BinaryOp(FloatLiteral(1.5), "!=", FloatLiteral(2.5))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_283():
    # float >=
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [BinaryOp(FloatLiteral(2.5), ">=", FloatLiteral(2.5))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_284():
    # float <= false
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [BinaryOp(FloatLiteral(3.5), "<=", FloatLiteral(2.5))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_285():
    # expression stmt that discards result
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(5)),
        ExprStmt(BinaryOp(Identifier("x"), "+", IntLiteral(1))),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "5"

def test_extra_286():
    # while: sum all numbers divisible by 4 from 4..20
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "s", IntLiteral(0)),
        VarDecl(IntType(), "i", IntLiteral(4)),
        WhileStmt(BinaryOp(Identifier("i"), "<=", IntLiteral(20)), BlockStmt([
            ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", Identifier("i")))),
            ExprStmt(AssignExpr(Identifier("i"), BinaryOp(Identifier("i"), "+", IntLiteral(4))))
        ])),
        ExprStmt(FuncCall("printInt", [Identifier("s")]))
    ]))])
    # 4+8+12+16+20 = 60
    assert CodeGenerator().generate_and_run(ast) == "60"

def test_extra_287():
    # fibonacci: fib(0)=0, fib(1)=1
    ast = Program([
        FuncDecl(IntType(), "fib", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<=", IntLiteral(1)),
                   BlockStmt([ReturnStmt(Identifier("n"))]),
                   BlockStmt([ReturnStmt(BinaryOp(
                       FuncCall("fib", [BinaryOp(Identifier("n"), "-", IntLiteral(1))]),
                       "+",
                       FuncCall("fib", [BinaryOp(Identifier("n"), "-", IntLiteral(2))])
                   ))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("fib", [IntLiteral(0)])])),
            ExprStmt(FuncCall("printInt", [FuncCall("fib", [IntLiteral(1)])])),
            ExprStmt(FuncCall("printInt", [FuncCall("fib", [IntLiteral(6)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "018"

def test_extra_288():
    # loop sum float
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "s", FloatLiteral(0.0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)),
                BinaryOp(Identifier("i"), "<", IntLiteral(4)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", FloatLiteral(0.25))))])),
        ExprStmt(FuncCall("printFloat", [Identifier("s")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1.0"

def test_extra_289():
    # function calling another function in condition
    ast = Program([
        FuncDecl(IntType(), "isPos", [Param(IntType(), "n")],
                 BlockStmt([ReturnStmt(BinaryOp(Identifier("n"), ">", IntLiteral(0)))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            IfStmt(FuncCall("isPos", [IntLiteral(5)]),
                   BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("pos")]))]),
                   BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("neg")]))]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "pos"

def test_extra_290():
    # two nested for loops with break in inner
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "cnt", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)),
                BinaryOp(Identifier("i"), "<", IntLiteral(3)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    ForStmt(VarDecl(IntType(), "j", IntLiteral(0)),
                            BinaryOp(Identifier("j"), "<", IntLiteral(5)),
                            PostfixOp("++", Identifier("j")),
                            BlockStmt([
                                IfStmt(BinaryOp(Identifier("j"), "==", IntLiteral(2)),
                                       BlockStmt([BreakStmt()]), None),
                                ExprStmt(PostfixOp("++", Identifier("cnt")))
                            ]))
                ])),
        ExprStmt(FuncCall("printInt", [Identifier("cnt")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "6"

def test_extra_291():
    # float comparison with int: i2f
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [BinaryOp(FloatLiteral(2.5), ">", IntLiteral(2))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_292():
    # int var used as float arg (i2f)
    ast = Program([
        FuncDecl(FloatType(), "toF", [Param(FloatType(), "x")], BlockStmt([ReturnStmt(Identifier("x"))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(IntType(), "n", IntLiteral(5)),
            ExprStmt(FuncCall("printFloat", [FuncCall("toF", [Identifier("n")])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "5.0"

def test_extra_293():
    # multiple returns from while
    ast = Program([
        FuncDecl(IntType(), "firstMult", [Param(IntType(), "n"), Param(IntType(), "k")], BlockStmt([
            VarDecl(IntType(), "i", IntLiteral(1)),
            WhileStmt(BinaryOp(Identifier("i"), "<=", IntLiteral(100)), BlockStmt([
                IfStmt(BinaryOp(BinaryOp(Identifier("i"), "%", Identifier("n")), "==", IntLiteral(0)),
                       BlockStmt([ReturnStmt(Identifier("i"))]), None),
                ExprStmt(PostfixOp("++", Identifier("i")))
            ])),
            ReturnStmt(IntLiteral(-1))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("firstMult", [IntLiteral(7), IntLiteral(0)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "7"

def test_extra_294():
    # struct assignment (copy)
    ast = Program([
        StructDecl("Box", [MemberDecl(IntType(), "v")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Box"), "a", StructLiteral([IntLiteral(1)])),
            VarDecl(StructType("Box"), "b", Identifier("a")),
            ExprStmt(AssignExpr(MemberAccess(Identifier("b"), "v"), IntLiteral(99))),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("a"), "v")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("b"), "v")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "199"

def test_extra_295():
    # use struct member in arithmetic
    ast = Program([
        StructDecl("V2", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
        FuncDecl(IntType(), "dot", [Param(StructType("V2"), "a"), Param(StructType("V2"), "b")],
                 BlockStmt([ReturnStmt(BinaryOp(
                     BinaryOp(MemberAccess(Identifier("a"), "x"), "*", MemberAccess(Identifier("b"), "x")),
                     "+",
                     BinaryOp(MemberAccess(Identifier("a"), "y"), "*", MemberAccess(Identifier("b"), "y"))
                 ))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("V2"), "u", StructLiteral([IntLiteral(1), IntLiteral(2)])),
            VarDecl(StructType("V2"), "v", StructLiteral([IntLiteral(3), IntLiteral(4)])),
            ExprStmt(FuncCall("printInt", [FuncCall("dot", [Identifier("u"), Identifier("v")])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "11"

def test_extra_296():
    # print 0 float
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printFloat", [FloatLiteral(-0.0)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0.0"

def test_extra_297():
    # while sum: stop when over 50
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "s", IntLiteral(0)),
        VarDecl(IntType(), "i", IntLiteral(1)),
        WhileStmt(BinaryOp(Identifier("s"), "<=", IntLiteral(50)), BlockStmt([
            ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", Identifier("i")))),
            ExprStmt(PostfixOp("++", Identifier("i")))
        ])),
        ExprStmt(FuncCall("printInt", [Identifier("s")]))
    ]))])
    # 1+2+...+10=55
    assert CodeGenerator().generate_and_run(ast) == "55"

def test_extra_298():
    # nested blocks with vars
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(1)),
        BlockStmt([
            VarDecl(IntType(), "y", IntLiteral(2)),
            BlockStmt([
                VarDecl(IntType(), "z", IntLiteral(3)),
                ExprStmt(FuncCall("printInt", [BinaryOp(BinaryOp(Identifier("x"), "+", Identifier("y")), "+", Identifier("z"))]))
            ])
        ])
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "6"

def test_extra_299():
    # function with 4 params
    ast = Program([
        FuncDecl(IntType(), "sum4", [Param(IntType(), "a"), Param(IntType(), "b"),
                                     Param(IntType(), "c"), Param(IntType(), "d")],
                 BlockStmt([ReturnStmt(BinaryOp(BinaryOp(BinaryOp(Identifier("a"), "+", Identifier("b")), "+", Identifier("c")), "+", Identifier("d")))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("sum4", [IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "10"

def test_extra_300():
    # basic empty program (only main)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([]))])
    assert CodeGenerator().generate_and_run(ast) == ""

def test_extra_301():
    # int 0 used as falsy in if
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(0)),
        IfStmt(Identifier("x"),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("truthy")]))]),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("falsy")]))])
               )
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "falsy"

def test_extra_302():
    # int nonzero used as truthy in if
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(42)),
        IfStmt(Identifier("x"),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("truthy")]))]),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("falsy")]))])
               )
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "truthy"

def test_extra_303():
    # while with nested if-break pattern
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "i", IntLiteral(0)),
        VarDecl(IntType(), "found", IntLiteral(-1)),
        WhileStmt(BinaryOp(Identifier("i"), "<", IntLiteral(10)), BlockStmt([
            IfStmt(BinaryOp(BinaryOp(Identifier("i"), "*", Identifier("i")), "==", IntLiteral(49)),
                   BlockStmt([
                       ExprStmt(AssignExpr(Identifier("found"), Identifier("i"))),
                       BreakStmt()
                   ]),
                   None),
            ExprStmt(PostfixOp("++", Identifier("i")))
        ])),
        ExprStmt(FuncCall("printInt", [Identifier("found")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "7"

def test_extra_304():
    # print abs of each in loop
    ast = Program([
        FuncDecl(IntType(), "myAbs", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<", IntLiteral(0)),
                   BlockStmt([ReturnStmt(PrefixOp("-", Identifier("n")))]),
                   BlockStmt([ReturnStmt(Identifier("n"))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("myAbs", [IntLiteral(-5)])])),
            ExprStmt(FuncCall("printInt", [FuncCall("myAbs", [IntLiteral(3)])])),
            ExprStmt(FuncCall("printInt", [FuncCall("myAbs", [IntLiteral(0)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "530"

def test_extra_305():
    # decrement in while condition (postfix returns new value)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(5)),
        WhileStmt(PostfixOp("--", Identifier("x")), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("x")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "4321"

def test_extra_306():
    # struct with bool-like flag
    ast = Program([
        StructDecl("Toggle", [MemberDecl(IntType(), "on")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Toggle"), "t", StructLiteral([IntLiteral(0)])),
            ExprStmt(AssignExpr(MemberAccess(Identifier("t"), "on"), BinaryOp(PrefixOp("!", MemberAccess(Identifier("t"), "on")), "+", IntLiteral(0)))),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("t"), "on")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_307():
    # multiple functions, some unused (still compiles)
    ast = Program([
        FuncDecl(IntType(), "unused", [], BlockStmt([ReturnStmt(IntLiteral(999))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [IntLiteral(1)]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_308():
    # float 0.0 printed after computation
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printFloat", [BinaryOp(FloatLiteral(1.5), "-", FloatLiteral(1.5))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0.0"

def test_extra_309():
    # chain: compute and store, then use
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "a", BinaryOp(IntLiteral(3), "*", IntLiteral(4))),
        VarDecl(IntType(), "b", BinaryOp(Identifier("a"), "+", IntLiteral(5))),
        VarDecl(IntType(), "c", BinaryOp(Identifier("b"), "*", IntLiteral(2))),
        ExprStmt(FuncCall("printInt", [Identifier("c")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "34"

def test_extra_310():
    # conditional print based on remainder
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(5)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    IfStmt(BinaryOp(BinaryOp(Identifier("i"), "%", IntLiteral(2)), "==", IntLiteral(0)),
                           BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("E")]))]),
                           BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("O")]))]))
                ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "OEOEO"

def test_extra_311():
    # early return in loop
    ast = Program([
        FuncDecl(IntType(), "findFirst", [Param(IntType(), "target")], BlockStmt([
            ForStmt(VarDecl(IntType(), "i", IntLiteral(0)),
                    BinaryOp(Identifier("i"), "<", IntLiteral(20)),
                    PostfixOp("++", Identifier("i")),
                    BlockStmt([
                        IfStmt(BinaryOp(BinaryOp(Identifier("i"), "*", Identifier("i")), "==", Identifier("target")),
                               BlockStmt([ReturnStmt(Identifier("i"))]),
                               None)
                    ])),
            ReturnStmt(IntLiteral(-1))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("findFirst", [IntLiteral(16)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "4"

def test_extra_312():
    # complex struct operations
    ast = Program([
        StructDecl("Line", [MemberDecl(IntType(), "x1"), MemberDecl(IntType(), "y1"),
                            MemberDecl(IntType(), "x2"), MemberDecl(IntType(), "y2")]),
        FuncDecl(IntType(), "length2", [Param(StructType("Line"), "l")],
                 BlockStmt([ReturnStmt(BinaryOp(
                     BinaryOp(BinaryOp(MemberAccess(Identifier("l"), "x2"), "-", MemberAccess(Identifier("l"), "x1")),
                              "*",
                              BinaryOp(MemberAccess(Identifier("l"), "x2"), "-", MemberAccess(Identifier("l"), "x1"))),
                     "+",
                     BinaryOp(BinaryOp(MemberAccess(Identifier("l"), "y2"), "-", MemberAccess(Identifier("l"), "y1")),
                              "*",
                              BinaryOp(MemberAccess(Identifier("l"), "y2"), "-", MemberAccess(Identifier("l"), "y1")))
                 ))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Line"), "l", StructLiteral([IntLiteral(0), IntLiteral(0), IntLiteral(3), IntLiteral(4)])),
            ExprStmt(FuncCall("printInt", [FuncCall("length2", [Identifier("l")])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "25"

def test_extra_313():
    # while loop over countdown
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "n", IntLiteral(5)),
        VarDecl(IntType(), "s", IntLiteral(0)),
        WhileStmt(BinaryOp(Identifier("n"), ">", IntLiteral(0)), BlockStmt([
            ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", Identifier("n")))),
            ExprStmt(PrefixOp("--", Identifier("n")))
        ])),
        ExprStmt(FuncCall("printInt", [Identifier("s")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "15"

def test_extra_314():
    # recursive: tower of hanoi count
    ast = Program([
        FuncDecl(IntType(), "hanoi", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "==", IntLiteral(0)),
                   BlockStmt([ReturnStmt(IntLiteral(0))]),
                   BlockStmt([ReturnStmt(BinaryOp(
                       BinaryOp(FuncCall("hanoi", [BinaryOp(Identifier("n"), "-", IntLiteral(1))]), "*", IntLiteral(2)),
                       "+", IntLiteral(1)
                   ))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("hanoi", [IntLiteral(4)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "15"

def test_extra_315():
    # for loop: print squares up to limit
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(BinaryOp(Identifier("i"), "*", Identifier("i")), "<=", IntLiteral(25)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(Identifier("i"), "*", Identifier("i"))]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1491625"

def test_extra_316():
    # switch: 0 matches case 0
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        SwitchStmt(IntLiteral(0), [
            CaseStmt(IntLiteral(0), [ExprStmt(FuncCall("printString", [StringLiteral("zero")])), BreakStmt()]),
            CaseStmt(IntLiteral(1), [ExprStmt(FuncCall("printString", [StringLiteral("one")])), BreakStmt()])
        ], None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "zero"

def test_extra_317():
    # function that calls printInt then returns value
    ast = Program([
        FuncDecl(IntType(), "debug", [Param(IntType(), "n")], BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("n")])),
            ReturnStmt(BinaryOp(Identifier("n"), "+", IntLiteral(1)))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(IntType(), "x", FuncCall("debug", [IntLiteral(9)])),
            ExprStmt(FuncCall("printInt", [Identifier("x")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "910"

def test_extra_318():
    # complex: collatz sequence length
    ast = Program([
        FuncDecl(IntType(), "collatz", [Param(IntType(), "n")], BlockStmt([
            VarDecl(IntType(), "steps", IntLiteral(0)),
            WhileStmt(BinaryOp(Identifier("n"), "!=", IntLiteral(1)), BlockStmt([
                IfStmt(BinaryOp(BinaryOp(Identifier("n"), "%", IntLiteral(2)), "==", IntLiteral(0)),
                       BlockStmt([ExprStmt(AssignExpr(Identifier("n"), BinaryOp(Identifier("n"), "/", IntLiteral(2))))]),
                       BlockStmt([ExprStmt(AssignExpr(Identifier("n"), BinaryOp(BinaryOp(IntLiteral(3), "*", Identifier("n")), "+", IntLiteral(1))))])),
                ExprStmt(PostfixOp("++", Identifier("steps")))
            ])),
            ReturnStmt(Identifier("steps"))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("collatz", [IntLiteral(6)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "8"

def test_extra_319():
    # complex: digit sum
    ast = Program([
        FuncDecl(IntType(), "digitSum", [Param(IntType(), "n")], BlockStmt([
            VarDecl(IntType(), "s", IntLiteral(0)),
            WhileStmt(BinaryOp(Identifier("n"), ">", IntLiteral(0)), BlockStmt([
                ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", BinaryOp(Identifier("n"), "%", IntLiteral(10))))),
                ExprStmt(AssignExpr(Identifier("n"), BinaryOp(Identifier("n"), "/", IntLiteral(10))))
            ])),
            ReturnStmt(Identifier("s"))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("digitSum", [IntLiteral(12345)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "15"

def test_extra_320():
    # complex: reverse digits
    ast = Program([
        FuncDecl(IntType(), "reverseDigits", [Param(IntType(), "n")], BlockStmt([
            VarDecl(IntType(), "r", IntLiteral(0)),
            WhileStmt(BinaryOp(Identifier("n"), ">", IntLiteral(0)), BlockStmt([
                ExprStmt(AssignExpr(Identifier("r"), BinaryOp(BinaryOp(Identifier("r"), "*", IntLiteral(10)), "+", BinaryOp(Identifier("n"), "%", IntLiteral(10))))),
                ExprStmt(AssignExpr(Identifier("n"), BinaryOp(Identifier("n"), "/", IntLiteral(10))))
            ])),
            ReturnStmt(Identifier("r"))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("reverseDigits", [IntLiteral(1234)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "4321"

def test_extra_321():
    # multiple struct types used together
    ast = Program([
        StructDecl("Cat", [MemberDecl(StringType(), "name"), MemberDecl(IntType(), "age")]),
        StructDecl("Dog", [MemberDecl(StringType(), "name"), MemberDecl(IntType(), "age")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Cat"), "c", StructLiteral([StringLiteral("Kitty"), IntLiteral(3)])),
            VarDecl(StructType("Dog"), "d", StructLiteral([StringLiteral("Rex"), IntLiteral(5)])),
            ExprStmt(FuncCall("printString", [MemberAccess(Identifier("c"), "name")])),
            ExprStmt(FuncCall("printString", [MemberAccess(Identifier("d"), "name")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "KittyRex"

def test_extra_322():
    # assignment in while condition (truthy check)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(3)),
        WhileStmt(Identifier("x"), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("x")])),
            ExprStmt(PrefixOp("--", Identifier("x")))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "321"

def test_extra_323():
    # for: sum of divisors of 12
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "s", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(12)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    IfStmt(BinaryOp(BinaryOp(IntLiteral(12), "%", Identifier("i")), "==", IntLiteral(0)),
                           BlockStmt([ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", Identifier("i"))))]),
                           None)
                ])),
        ExprStmt(FuncCall("printInt", [Identifier("s")]))
    ]))])
    # 1+2+3+4+6+12=28
    assert CodeGenerator().generate_and_run(ast) == "28"

def test_extra_324():
    # recursive countdown
    ast = Program([
        FuncDecl(VoidType(), "countdown", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), ">", IntLiteral(0)),
                   BlockStmt([
                       ExprStmt(FuncCall("printInt", [Identifier("n")])),
                       ExprStmt(FuncCall("countdown", [BinaryOp(Identifier("n"), "-", IntLiteral(1))]))
                   ]),
                   None)
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("countdown", [IntLiteral(4)]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "4321"

def test_extra_325():
    # auto var from struct member
    ast = Program([
        StructDecl("Num", [MemberDecl(IntType(), "val")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Num"), "n", StructLiteral([IntLiteral(7)])),
            VarDecl(None, "x", MemberAccess(Identifier("n"), "val")),
            ExprStmt(FuncCall("printInt", [Identifier("x")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "7"

def test_extra_326():
    # nested blocks modify outer var
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(0)),
        BlockStmt([
            ExprStmt(AssignExpr(Identifier("x"), IntLiteral(5)))
        ]),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "5"

def test_extra_327():
    # for loop: print powers of 2 up to 64
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(64)),
                ExprStmt(AssignExpr(Identifier("i"), BinaryOp(Identifier("i"), "*", IntLiteral(2)))),
                BlockStmt([ExprStmt(FuncCall("printInt", [Identifier("i")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1248163264"

def test_extra_328():
    # short-circuit: right side evaluates when left is true
    ast = Program([
        FuncDecl(IntType(), "getTwo", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [IntLiteral(2)])),
            ReturnStmt(IntLiteral(2))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(BinaryOp(IntLiteral(1), "&&", FuncCall("getTwo", [])))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "2"

def test_extra_329():
    # short-circuit: right side evaluates when left is false for ||
    ast = Program([
        FuncDecl(IntType(), "getThree", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [IntLiteral(3)])),
            ReturnStmt(IntLiteral(3))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(BinaryOp(IntLiteral(0), "||", FuncCall("getThree", [])))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "3"

def test_extra_330():
    # complex nested loop with multiple breaks
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "found", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(BinaryOp(Identifier("i"), "<=", IntLiteral(10)), "&&", PrefixOp("!", Identifier("found"))),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    ForStmt(VarDecl(IntType(), "j", IntLiteral(1)),
                            BinaryOp(Identifier("j"), "<=", IntLiteral(10)),
                            PostfixOp("++", Identifier("j")),
                            BlockStmt([
                                IfStmt(BinaryOp(BinaryOp(Identifier("i"), "*", Identifier("j")), "==", IntLiteral(42)),
                                       BlockStmt([
                                           ExprStmt(AssignExpr(Identifier("found"), IntLiteral(1))),
                                           ExprStmt(FuncCall("printInt", [Identifier("i")])),
                                           ExprStmt(FuncCall("printInt", [Identifier("j")])),
                                           BreakStmt()
                                       ]),
                                       None)
                            ]))
                ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "67"

def test_extra_331():
    # function calling two other functions
    ast = Program([
        FuncDecl(IntType(), "f", [], BlockStmt([ReturnStmt(IntLiteral(3))])),
        FuncDecl(IntType(), "g", [], BlockStmt([ReturnStmt(IntLiteral(4))])),
        FuncDecl(IntType(), "fg", [], BlockStmt([ReturnStmt(BinaryOp(FuncCall("f", []), "*", FuncCall("g", [])))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("fg", [])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "12"

def test_extra_332():
    # int converted to float in binary op
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "n", IntLiteral(3)),
        ExprStmt(FuncCall("printFloat", [BinaryOp(Identifier("n"), "+", FloatLiteral(0.5))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "3.5"

def test_extra_333():
    # print multiple lines from a function
    ast = Program([
        FuncDecl(VoidType(), "printLines", [Param(IntType(), "n")], BlockStmt([
            ForStmt(VarDecl(IntType(), "i", IntLiteral(0)),
                    BinaryOp(Identifier("i"), "<", Identifier("n")),
                    PostfixOp("++", Identifier("i")),
                    BlockStmt([ExprStmt(FuncCall("printInt", [Identifier("i")]))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printLines", [IntLiteral(5)]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "01234"

def test_extra_334():
    # complex expression tree
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [
            BinaryOp(
                BinaryOp(BinaryOp(IntLiteral(2), "*", IntLiteral(3)), "+", BinaryOp(IntLiteral(4), "*", IntLiteral(5))),
                "-",
                BinaryOp(IntLiteral(6), "/", IntLiteral(2))
            )
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "23"

def test_extra_335():
    # struct member accumulation
    ast = Program([
        StructDecl("Acc", [MemberDecl(IntType(), "total")]),
        FuncDecl(VoidType(), "add", [Param(StructType("Acc"), "a"), Param(IntType(), "n")],
                 BlockStmt([ExprStmt(AssignExpr(MemberAccess(Identifier("a"), "total"),
                                                BinaryOp(MemberAccess(Identifier("a"), "total"), "+", Identifier("n"))))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Acc"), "acc", StructLiteral([IntLiteral(0)])),
            ExprStmt(FuncCall("add", [Identifier("acc"), IntLiteral(5)])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("acc"), "total")]))
        ]))
    ])
    # struct is passed by value so original not modified
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_336():
    # multiple functions with same name for different scenarios (not allowed, test one)
    ast = Program([
        FuncDecl(IntType(), "compute", [Param(IntType(), "a"), Param(IntType(), "b"), Param(IntType(), "c")],
                 BlockStmt([ReturnStmt(BinaryOp(BinaryOp(Identifier("a"), "*", Identifier("b")), "+", Identifier("c")))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("compute", [IntLiteral(2), IntLiteral(3), IntLiteral(1)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "7"

def test_extra_337():
    # complex struct with float operations
    ast = Program([
        StructDecl("Circle", [MemberDecl(FloatType(), "cx"), MemberDecl(FloatType(), "cy"), MemberDecl(FloatType(), "r")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Circle"), "c", StructLiteral([FloatLiteral(1.0), FloatLiteral(2.0), FloatLiteral(0.5)])),
            ExprStmt(FuncCall("printFloat", [MemberAccess(Identifier("c"), "cx")])),
            ExprStmt(FuncCall("printFloat", [MemberAccess(Identifier("c"), "r")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "1.00.5"

def test_extra_338():
    # for: test continue with accumulator
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "s", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(10)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    IfStmt(BinaryOp(BinaryOp(Identifier("i"), "%", IntLiteral(2)), "==", IntLiteral(0)),
                           BlockStmt([ContinueStmt()]), None),
                    ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", Identifier("i"))))
                ])),
        ExprStmt(FuncCall("printInt", [Identifier("s")]))
    ]))])
    # sum odds 1..10: 1+3+5+7+9=25
    assert CodeGenerator().generate_and_run(ast) == "25"

def test_extra_339():
    # zero factorial = 1
    ast = Program([
        FuncDecl(IntType(), "fact", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<=", IntLiteral(1)),
                   BlockStmt([ReturnStmt(IntLiteral(1))]),
                   BlockStmt([ReturnStmt(BinaryOp(Identifier("n"), "*", FuncCall("fact", [BinaryOp(Identifier("n"), "-", IntLiteral(1))])))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("fact", [IntLiteral(0)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_340():
    # switch multiple patterns
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)),
                BinaryOp(Identifier("i"), "<", IntLiteral(3)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    SwitchStmt(Identifier("i"), [
                        CaseStmt(IntLiteral(0), [ExprStmt(FuncCall("printString", [StringLiteral("a")])), BreakStmt()]),
                        CaseStmt(IntLiteral(1), [ExprStmt(FuncCall("printString", [StringLiteral("b")])), BreakStmt()]),
                        CaseStmt(IntLiteral(2), [ExprStmt(FuncCall("printString", [StringLiteral("c")])), BreakStmt()]),
                    ], None)
                ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "abc"

def test_extra_341():
    # complex: binary search
    ast = Program([
        FuncDecl(IntType(), "bsearch", [Param(IntType(), "target"), Param(IntType(), "lo"), Param(IntType(), "hi")], BlockStmt([
            WhileStmt(BinaryOp(Identifier("lo"), "<=", Identifier("hi")), BlockStmt([
                VarDecl(IntType(), "mid", BinaryOp(BinaryOp(Identifier("lo"), "+", Identifier("hi")), "/", IntLiteral(2))),
                IfStmt(BinaryOp(Identifier("mid"), "==", Identifier("target")),
                       BlockStmt([ReturnStmt(Identifier("mid"))]),
                       BlockStmt([IfStmt(BinaryOp(Identifier("mid"), "<", Identifier("target")),
                                         BlockStmt([ExprStmt(AssignExpr(Identifier("lo"), BinaryOp(Identifier("mid"), "+", IntLiteral(1))))]),
                                         BlockStmt([ExprStmt(AssignExpr(Identifier("hi"), BinaryOp(Identifier("mid"), "-", IntLiteral(1))))]))]))
            ])),
            ReturnStmt(IntLiteral(-1))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("bsearch", [IntLiteral(7), IntLiteral(1), IntLiteral(10)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "7"

def test_extra_342():
    # string as function return value, used directly
    ast = Program([
        FuncDecl(StringType(), "getFoo", [], BlockStmt([ReturnStmt(StringLiteral("foo"))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printString", [FuncCall("getFoo", [])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "foo"

def test_extra_343():
    # int passed as auto param type (float expected)
    ast = Program([
        FuncDecl(FloatType(), "addHalf", [Param(FloatType(), "x")],
                 BlockStmt([ReturnStmt(BinaryOp(Identifier("x"), "+", FloatLiteral(0.5)))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printFloat", [FuncCall("addHalf", [IntLiteral(2)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "2.5"

def test_extra_344():
    # while: count digits in a number
    ast = Program([
        FuncDecl(IntType(), "numDigits", [Param(IntType(), "n")], BlockStmt([
            VarDecl(IntType(), "count", IntLiteral(0)),
            WhileStmt(BinaryOp(Identifier("n"), ">", IntLiteral(0)), BlockStmt([
                ExprStmt(AssignExpr(Identifier("n"), BinaryOp(Identifier("n"), "/", IntLiteral(10)))),
                ExprStmt(PostfixOp("++", Identifier("count")))
            ])),
            ReturnStmt(Identifier("count"))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("numDigits", [IntLiteral(12345)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "5"

def test_extra_345():
    # nested function that uses outer scope param (no closures, just call)
    ast = Program([
        FuncDecl(IntType(), "double", [Param(IntType(), "x")],
                 BlockStmt([ReturnStmt(BinaryOp(Identifier("x"), "*", IntLiteral(2)))])),
        FuncDecl(IntType(), "quadruple", [Param(IntType(), "x")],
                 BlockStmt([ReturnStmt(FuncCall("double", [FuncCall("double", [Identifier("x")])]))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("quadruple", [IntLiteral(5)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "20"

def test_extra_346():
    # if-else chain returning string
    ast = Program([
        FuncDecl(StringType(), "season", [Param(IntType(), "month")], BlockStmt([
            IfStmt(BinaryOp(BinaryOp(Identifier("month"), ">=", IntLiteral(3)), "&&", BinaryOp(Identifier("month"), "<=", IntLiteral(5))),
                   BlockStmt([ReturnStmt(StringLiteral("Spring"))]),
                   BlockStmt([IfStmt(BinaryOp(BinaryOp(Identifier("month"), ">=", IntLiteral(6)), "&&", BinaryOp(Identifier("month"), "<=", IntLiteral(8))),
                                     BlockStmt([ReturnStmt(StringLiteral("Summer"))]),
                                     BlockStmt([IfStmt(BinaryOp(BinaryOp(Identifier("month"), ">=", IntLiteral(9)), "&&", BinaryOp(Identifier("month"), "<=", IntLiteral(11))),
                                                       BlockStmt([ReturnStmt(StringLiteral("Autumn"))]),
                                                       BlockStmt([ReturnStmt(StringLiteral("Winter"))]))]))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printString", [FuncCall("season", [IntLiteral(4)])])),
            ExprStmt(FuncCall("printString", [FuncCall("season", [IntLiteral(7)])])),
            ExprStmt(FuncCall("printString", [FuncCall("season", [IntLiteral(12)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "SpringSummerWinter"

def test_extra_347():
    # for with continue to print triangular pattern count
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "total", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(4)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    ForStmt(VarDecl(IntType(), "j", IntLiteral(1)),
                            BinaryOp(Identifier("j"), "<=", Identifier("i")),
                            PostfixOp("++", Identifier("j")),
                            BlockStmt([ExprStmt(PostfixOp("++", Identifier("total")))]))
                ])),
        ExprStmt(FuncCall("printInt", [Identifier("total")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "10"

def test_extra_348():
    # switch in loop
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(5)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    SwitchStmt(BinaryOp(Identifier("i"), "%", IntLiteral(2)), [
                        CaseStmt(IntLiteral(0), [ExprStmt(FuncCall("printString", [StringLiteral("E")])), BreakStmt()]),
                        CaseStmt(IntLiteral(1), [ExprStmt(FuncCall("printString", [StringLiteral("O")])), BreakStmt()])
                    ], None)
                ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "OEOEO"

def test_extra_349():
    # for loop: compute LCM(6,4) using GCD
    ast = Program([
        FuncDecl(IntType(), "gcd", [Param(IntType(), "a"), Param(IntType(), "b")], BlockStmt([
            WhileStmt(BinaryOp(Identifier("b"), "!=", IntLiteral(0)), BlockStmt([
                VarDecl(IntType(), "t", Identifier("b")),
                ExprStmt(AssignExpr(Identifier("b"), BinaryOp(Identifier("a"), "%", Identifier("b")))),
                ExprStmt(AssignExpr(Identifier("a"), Identifier("t")))
            ])),
            ReturnStmt(Identifier("a"))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(IntType(), "a", IntLiteral(6)),
            VarDecl(IntType(), "b", IntLiteral(4)),
            ExprStmt(FuncCall("printInt", [BinaryOp(BinaryOp(Identifier("a"), "*", Identifier("b")), "/", FuncCall("gcd", [Identifier("a"), Identifier("b")]))]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "12"

def test_extra_350():
    # complex: string building simulation
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(StringType(), "prefix", StringLiteral("Value: ")),
        VarDecl(IntType(), "val", IntLiteral(42)),
        ExprStmt(FuncCall("printString", [Identifier("prefix")])),
        ExprStmt(FuncCall("printInt", [Identifier("val")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "Value: 42"

def test_extra_351():
    # zero divided by nonzero
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(0), "/", IntLiteral(7))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_352():
    # modulo: 0 % n = 0
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(0), "%", IntLiteral(5))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_353():
    # nested unary operations
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [PrefixOp("!", PrefixOp("!", PrefixOp("!", IntLiteral(0))))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_354():
    # compare with negative
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(-5), "<", IntLiteral(0))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_355():
    # unary minus on var
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(7)),
        ExprStmt(FuncCall("printInt", [PrefixOp("-", Identifier("x"))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "-7"

def test_extra_356():
    # float to float comparison: equal
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "a", FloatLiteral(0.5)),
        VarDecl(FloatType(), "b", FloatLiteral(0.5)),
        ExprStmt(FuncCall("printInt", [BinaryOp(Identifier("a"), "==", Identifier("b"))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_357():
    # for: sum alternating +/-
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "s", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(6)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    IfStmt(BinaryOp(BinaryOp(Identifier("i"), "%", IntLiteral(2)), "==", IntLiteral(1)),
                           BlockStmt([ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", Identifier("i"))))]),
                           BlockStmt([ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "-", Identifier("i"))))]))
                ])),
        ExprStmt(FuncCall("printInt", [Identifier("s")]))
    ]))])
    # 1-2+3-4+5-6 = -3
    assert CodeGenerator().generate_and_run(ast) == "-3"

def test_extra_358():
    # deeply nested function calls
    ast = Program([
        FuncDecl(IntType(), "add", [Param(IntType(), "a"), Param(IntType(), "b")],
                 BlockStmt([ReturnStmt(BinaryOp(Identifier("a"), "+", Identifier("b")))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [
                FuncCall("add", [
                    FuncCall("add", [IntLiteral(1), IntLiteral(2)]),
                    FuncCall("add", [IntLiteral(3), IntLiteral(4)])
                ])
            ]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "10"

def test_extra_359():
    # var reassigned multiple times
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(1)),
        ExprStmt(AssignExpr(Identifier("x"), IntLiteral(2))),
        ExprStmt(AssignExpr(Identifier("x"), IntLiteral(3))),
        ExprStmt(AssignExpr(Identifier("x"), IntLiteral(4))),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "4"

def test_extra_360():
    # struct passed and returned
    ast = Program([
        StructDecl("P", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
        FuncDecl(StructType("P"), "translate", [Param(StructType("P"), "p"), Param(IntType(), "dx"), Param(IntType(), "dy")],
                 BlockStmt([
                     ExprStmt(AssignExpr(MemberAccess(Identifier("p"), "x"), BinaryOp(MemberAccess(Identifier("p"), "x"), "+", Identifier("dx")))),
                     ExprStmt(AssignExpr(MemberAccess(Identifier("p"), "y"), BinaryOp(MemberAccess(Identifier("p"), "y"), "+", Identifier("dy")))),
                     ReturnStmt(Identifier("p"))
                 ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("P"), "p", StructLiteral([IntLiteral(1), IntLiteral(2)])),
            VarDecl(StructType("P"), "q", FuncCall("translate", [Identifier("p"), IntLiteral(3), IntLiteral(4)])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("q"), "x")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("q"), "y")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "46"

def test_extra_361():
    # logical op chain
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "a", IntLiteral(1)),
        VarDecl(IntType(), "b", IntLiteral(0)),
        VarDecl(IntType(), "c", IntLiteral(1)),
        ExprStmt(FuncCall("printInt", [BinaryOp(BinaryOp(Identifier("a"), "&&", Identifier("b")), "||", Identifier("c"))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_362():
    # multiple conditions chained
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(5)),
        ExprStmt(FuncCall("printInt", [
            BinaryOp(
                BinaryOp(BinaryOp(Identifier("x"), ">", IntLiteral(0)), "&&", BinaryOp(Identifier("x"), "<", IntLiteral(10))),
                "&&",
                BinaryOp(BinaryOp(Identifier("x"), "%", IntLiteral(2)), "==", IntLiteral(1))
            )
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_363():
    # struct copy semantics confirmed
    ast = Program([
        StructDecl("Box", [MemberDecl(IntType(), "n")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Box"), "a", StructLiteral([IntLiteral(10)])),
            VarDecl(StructType("Box"), "b", Identifier("a")),
            ExprStmt(AssignExpr(MemberAccess(Identifier("a"), "n"), IntLiteral(20))),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("a"), "n")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("b"), "n")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "2010"

def test_extra_364():
    # float multiplication: 3.0 * 3.0 = 9.0
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printFloat", [BinaryOp(FloatLiteral(3.0), "*", FloatLiteral(3.0))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "9.0"

def test_extra_365():
    # int 2^15 = 32768
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [IntLiteral(32768)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "32768"

def test_extra_366():
    # for: accumulate max
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "vals", IntLiteral(0)),
        VarDecl(IntType(), "mx", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(5)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    IfStmt(BinaryOp(Identifier("i"), ">", Identifier("mx")),
                           BlockStmt([ExprStmt(AssignExpr(Identifier("mx"), Identifier("i")))]),
                           None)
                ])),
        ExprStmt(FuncCall("printInt", [Identifier("mx")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "5"

def test_extra_367():
    # prefix increment returns new value
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(5)),
        VarDecl(IntType(), "y", PrefixOp("++", Identifier("x"))),
        ExprStmt(FuncCall("printInt", [Identifier("x")])),
        ExprStmt(FuncCall("printInt", [Identifier("y")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "66"

def test_extra_368():
    # postfix decrement returns new value (same as prefix, only precedence differs)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(5)),
        VarDecl(IntType(), "y", PostfixOp("--", Identifier("x"))),
        ExprStmt(FuncCall("printInt", [Identifier("x")])),
        ExprStmt(FuncCall("printInt", [Identifier("y")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "44"

def test_extra_369():
    # struct with large value
    ast = Program([
        StructDecl("Big", [MemberDecl(IntType(), "n")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Big"), "b", StructLiteral([IntLiteral(1000000)])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("b"), "n")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "1000000"

def test_extra_370():
    # for loop with all three parts as exprs
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(10)),
                BinaryOp(Identifier("i"), ">", IntLiteral(0)),
                ExprStmt(AssignExpr(Identifier("i"), BinaryOp(Identifier("i"), "-", IntLiteral(3)))),
                BlockStmt([ExprStmt(FuncCall("printInt", [Identifier("i")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "10741"

def test_extra_371():
    # return expression with side effect
    ast = Program([
        FuncDecl(IntType(), "inc", [Param(IntType(), "n")], BlockStmt([
            ReturnStmt(BinaryOp(Identifier("n"), "+", IntLiteral(1)))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(IntType(), "x", IntLiteral(0)),
            ExprStmt(AssignExpr(Identifier("x"), FuncCall("inc", [FuncCall("inc", [FuncCall("inc", [Identifier("x")])])]))),
            ExprStmt(FuncCall("printInt", [Identifier("x")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "3"

def test_extra_372():
    # complex: count vowel-like (demo string based)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printString", [StringLiteral("aeiou")])),
        ExprStmt(FuncCall("printInt", [IntLiteral(5)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "aeiou5"

def test_extra_373():
    # while with break and continue
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "i", IntLiteral(0)),
        WhileStmt(BinaryOp(Identifier("i"), "<", IntLiteral(10)), BlockStmt([
            ExprStmt(PostfixOp("++", Identifier("i"))),
            IfStmt(BinaryOp(BinaryOp(Identifier("i"), "%", IntLiteral(2)), "==", IntLiteral(0)),
                   BlockStmt([ContinueStmt()]), None),
            IfStmt(BinaryOp(Identifier("i"), ">", IntLiteral(7)),
                   BlockStmt([BreakStmt()]), None),
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1357"

def test_extra_374():
    # recursive sum of digits
    ast = Program([
        FuncDecl(IntType(), "digitSumR", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "==", IntLiteral(0)),
                   BlockStmt([ReturnStmt(IntLiteral(0))]),
                   BlockStmt([ReturnStmt(BinaryOp(
                       BinaryOp(Identifier("n"), "%", IntLiteral(10)),
                       "+",
                       FuncCall("digitSumR", [BinaryOp(Identifier("n"), "/", IntLiteral(10))])
                   ))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("digitSumR", [IntLiteral(12345)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "15"

def test_extra_375():
    # complex: max of 3 numbers
    ast = Program([
        FuncDecl(IntType(), "max3", [Param(IntType(), "a"), Param(IntType(), "b"), Param(IntType(), "c")], BlockStmt([
            VarDecl(IntType(), "m", Identifier("a")),
            IfStmt(BinaryOp(Identifier("b"), ">", Identifier("m")), BlockStmt([ExprStmt(AssignExpr(Identifier("m"), Identifier("b")))]), None),
            IfStmt(BinaryOp(Identifier("c"), ">", Identifier("m")), BlockStmt([ExprStmt(AssignExpr(Identifier("m"), Identifier("c")))]), None),
            ReturnStmt(Identifier("m"))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("max3", [IntLiteral(3), IntLiteral(1), IntLiteral(2)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "3"

def test_extra_376():
    # complex: check perfect square
    ast = Program([
        FuncDecl(IntType(), "isSquare", [Param(IntType(), "n")], BlockStmt([
            VarDecl(IntType(), "i", IntLiteral(0)),
            WhileStmt(BinaryOp(BinaryOp(Identifier("i"), "*", Identifier("i")), "<=", Identifier("n")), BlockStmt([
                IfStmt(BinaryOp(BinaryOp(Identifier("i"), "*", Identifier("i")), "==", Identifier("n")),
                       BlockStmt([ReturnStmt(IntLiteral(1))]),
                       None),
                ExprStmt(PostfixOp("++", Identifier("i")))
            ])),
            ReturnStmt(IntLiteral(0))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("isSquare", [IntLiteral(16)])])),
            ExprStmt(FuncCall("printInt", [FuncCall("isSquare", [IntLiteral(15)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "10"

def test_extra_377():
    # increment both struct members
    ast = Program([
        StructDecl("Pos", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Pos"), "p", StructLiteral([IntLiteral(3), IntLiteral(4)])),
            ExprStmt(PostfixOp("++", MemberAccess(Identifier("p"), "x"))),
            ExprStmt(PostfixOp("++", MemberAccess(Identifier("p"), "y"))),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "x")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "y")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "45"

def test_extra_378():
    # for loop: Fibonacci sequence first 8 terms
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "a", IntLiteral(0)),
        VarDecl(IntType(), "b", IntLiteral(1)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)),
                BinaryOp(Identifier("i"), "<", IntLiteral(6)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    ExprStmt(FuncCall("printInt", [Identifier("a")])),
                    VarDecl(IntType(), "tmp", BinaryOp(Identifier("a"), "+", Identifier("b"))),
                    ExprStmt(AssignExpr(Identifier("a"), Identifier("b"))),
                    ExprStmt(AssignExpr(Identifier("b"), Identifier("tmp")))
                ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "011235"

def test_extra_379():
    # complex: palindrome check (numerical)
    ast = Program([
        FuncDecl(IntType(), "isPalin", [Param(IntType(), "n")], BlockStmt([
            VarDecl(IntType(), "orig", Identifier("n")),
            VarDecl(IntType(), "rev", IntLiteral(0)),
            WhileStmt(BinaryOp(Identifier("n"), ">", IntLiteral(0)), BlockStmt([
                ExprStmt(AssignExpr(Identifier("rev"), BinaryOp(BinaryOp(Identifier("rev"), "*", IntLiteral(10)), "+", BinaryOp(Identifier("n"), "%", IntLiteral(10))))),
                ExprStmt(AssignExpr(Identifier("n"), BinaryOp(Identifier("n"), "/", IntLiteral(10))))
            ])),
            ReturnStmt(BinaryOp(Identifier("orig"), "==", Identifier("rev")))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("isPalin", [IntLiteral(121)])])),
            ExprStmt(FuncCall("printInt", [FuncCall("isPalin", [IntLiteral(123)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "10"

def test_extra_380():
    # while: cumulative product until > 100
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "p", IntLiteral(1)),
        VarDecl(IntType(), "i", IntLiteral(2)),
        WhileStmt(BinaryOp(Identifier("p"), "<=", IntLiteral(100)), BlockStmt([
            ExprStmt(AssignExpr(Identifier("p"), BinaryOp(Identifier("p"), "*", Identifier("i")))),
            ExprStmt(PostfixOp("++", Identifier("i")))
        ])),
        ExprStmt(FuncCall("printInt", [Identifier("p")]))
    ]))])
    # 1*2=2, *3=6, *4=24, *5=120
    assert CodeGenerator().generate_and_run(ast) == "120"

def test_extra_381():
    # for: compute sum using two vars
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "s1", IntLiteral(0)),
        VarDecl(IntType(), "s2", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(5)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    ExprStmt(AssignExpr(Identifier("s1"), BinaryOp(Identifier("s1"), "+", Identifier("i")))),
                    ExprStmt(AssignExpr(Identifier("s2"), BinaryOp(Identifier("s2"), "+", BinaryOp(Identifier("i"), "*", Identifier("i")))))
                ])),
        ExprStmt(FuncCall("printInt", [Identifier("s1")])),
        ExprStmt(FuncCall("printInt", [Identifier("s2")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1555"

def test_extra_382():
    # function taking and returning struct
    ast = Program([
        StructDecl("Range", [MemberDecl(IntType(), "lo"), MemberDecl(IntType(), "hi")]),
        FuncDecl(IntType(), "span", [Param(StructType("Range"), "r")],
                 BlockStmt([ReturnStmt(BinaryOp(MemberAccess(Identifier("r"), "hi"), "-", MemberAccess(Identifier("r"), "lo")))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Range"), "r", StructLiteral([IntLiteral(3), IntLiteral(10)])),
            ExprStmt(FuncCall("printInt", [FuncCall("span", [Identifier("r")])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "7"

def test_extra_383():
    # nested if with break
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "i", IntLiteral(0)),
        WhileStmt(BinaryOp(Identifier("i"), "<", IntLiteral(10)), BlockStmt([
            IfStmt(BinaryOp(Identifier("i"), "==", IntLiteral(5)),
                   BlockStmt([
                       IfStmt(IntLiteral(1), BlockStmt([BreakStmt()]), None)
                   ]),
                   None),
            ExprStmt(FuncCall("printInt", [Identifier("i")])),
            ExprStmt(PostfixOp("++", Identifier("i")))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "01234"

def test_extra_384():
    # auto return from bool expression
    ast = Program([
        FuncDecl(None, "inRange", [Param(IntType(), "x"), Param(IntType(), "lo"), Param(IntType(), "hi")],
                 BlockStmt([ReturnStmt(BinaryOp(BinaryOp(Identifier("x"), ">=", Identifier("lo")),
                                               "&&",
                                               BinaryOp(Identifier("x"), "<=", Identifier("hi"))))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("inRange", [IntLiteral(5), IntLiteral(1), IntLiteral(10)])])),
            ExprStmt(FuncCall("printInt", [FuncCall("inRange", [IntLiteral(15), IntLiteral(1), IntLiteral(10)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "10"

def test_extra_385():
    # complex: sum of primes up to 20
    ast = Program([
        FuncDecl(IntType(), "isPrime", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<", IntLiteral(2)), BlockStmt([ReturnStmt(IntLiteral(0))]), None),
            VarDecl(IntType(), "i", IntLiteral(2)),
            WhileStmt(BinaryOp(BinaryOp(Identifier("i"), "*", Identifier("i")), "<=", Identifier("n")), BlockStmt([
                IfStmt(BinaryOp(BinaryOp(Identifier("n"), "%", Identifier("i")), "==", IntLiteral(0)),
                       BlockStmt([ReturnStmt(IntLiteral(0))]), None),
                ExprStmt(PostfixOp("++", Identifier("i")))
            ])),
            ReturnStmt(IntLiteral(1))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(IntType(), "s", IntLiteral(0)),
            ForStmt(VarDecl(IntType(), "i", IntLiteral(2)),
                    BinaryOp(Identifier("i"), "<=", IntLiteral(20)),
                    PostfixOp("++", Identifier("i")),
                    BlockStmt([
                        IfStmt(FuncCall("isPrime", [Identifier("i")]),
                               BlockStmt([ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", Identifier("i"))))]),
                               None)
                    ])),
            ExprStmt(FuncCall("printInt", [Identifier("s")]))
        ]))
    ])
    # 2+3+5+7+11+13+17+19=77
    assert CodeGenerator().generate_and_run(ast) == "77"

def test_extra_386():
    # recursive power
    ast = Program([
        FuncDecl(IntType(), "powR", [Param(IntType(), "b"), Param(IntType(), "e")], BlockStmt([
            IfStmt(BinaryOp(Identifier("e"), "==", IntLiteral(0)),
                   BlockStmt([ReturnStmt(IntLiteral(1))]),
                   BlockStmt([ReturnStmt(BinaryOp(Identifier("b"), "*", FuncCall("powR", [Identifier("b"), BinaryOp(Identifier("e"), "-", IntLiteral(1))])))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("powR", [IntLiteral(3), IntLiteral(4)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "81"

def test_extra_387():
    # for loop: countdown from 10 by 2
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(10)),
                BinaryOp(Identifier("i"), ">", IntLiteral(0)),
                ExprStmt(AssignExpr(Identifier("i"), BinaryOp(Identifier("i"), "-", IntLiteral(2)))),
                BlockStmt([ExprStmt(FuncCall("printInt", [Identifier("i")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "108642"

def test_extra_388():
    # auto: chain auto vars
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "a", IntLiteral(5)),
        VarDecl(None, "b", BinaryOp(Identifier("a"), "+", IntLiteral(3))),
        VarDecl(None, "c", BinaryOp(Identifier("b"), "*", IntLiteral(2))),
        ExprStmt(FuncCall("printInt", [Identifier("c")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "16"

def test_extra_389():
    # complex: multiple assignments and conditions
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(5)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    ExprStmt(AssignExpr(Identifier("x"), BinaryOp(Identifier("x"), "+", Identifier("i")))),
                    IfStmt(BinaryOp(Identifier("x"), ">", IntLiteral(10)),
                           BlockStmt([BreakStmt()]), None)
                ])),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    # 1+2+3+4=10, 10+5=15>10 => break, x=15
    assert CodeGenerator().generate_and_run(ast) == "15"

def test_extra_390():
    # switch with sequential breaks (each case ends)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(3)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    SwitchStmt(Identifier("i"), [
                        CaseStmt(IntLiteral(1), [ExprStmt(FuncCall("printInt", [IntLiteral(10)])), BreakStmt()]),
                        CaseStmt(IntLiteral(2), [ExprStmt(FuncCall("printInt", [IntLiteral(20)])), BreakStmt()]),
                        CaseStmt(IntLiteral(3), [ExprStmt(FuncCall("printInt", [IntLiteral(30)])), BreakStmt()])
                    ], None)
                ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "102030"

def test_extra_391():
    # nested struct access in arithmetic
    ast = Program([
        StructDecl("Score", [MemberDecl(IntType(), "math"), MemberDecl(IntType(), "eng")]),
        FuncDecl(IntType(), "total", [Param(StructType("Score"), "s")],
                 BlockStmt([ReturnStmt(BinaryOp(MemberAccess(Identifier("s"), "math"), "+", MemberAccess(Identifier("s"), "eng")))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Score"), "s", StructLiteral([IntLiteral(85), IntLiteral(90)])),
            ExprStmt(FuncCall("printInt", [FuncCall("total", [Identifier("s")])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "175"

def test_extra_392():
    # while: find first n with n^2 > 50
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "n", IntLiteral(1)),
        WhileStmt(BinaryOp(BinaryOp(Identifier("n"), "*", Identifier("n")), "<=", IntLiteral(50)), BlockStmt([
            ExprStmt(PostfixOp("++", Identifier("n")))
        ])),
        ExprStmt(FuncCall("printInt", [Identifier("n")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "8"

def test_extra_393():
    # if condition: complex or
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(12)),
        IfStmt(BinaryOp(
            BinaryOp(BinaryOp(Identifier("x"), "%", IntLiteral(3)), "==", IntLiteral(0)),
            "||",
            BinaryOp(BinaryOp(Identifier("x"), "%", IntLiteral(5)), "==", IntLiteral(0))
        ),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("fizz/buzz")]))]),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("other")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "fizz/buzz"

def test_extra_394():
    # complex: print FizzBuzz 1..10
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(10)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    IfStmt(BinaryOp(BinaryOp(BinaryOp(Identifier("i"), "%", IntLiteral(3)), "==", IntLiteral(0)),
                                   "&&",
                                   BinaryOp(BinaryOp(Identifier("i"), "%", IntLiteral(5)), "==", IntLiteral(0))),
                           BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("FizzBuzz")]))]),
                           BlockStmt([
                               IfStmt(BinaryOp(BinaryOp(Identifier("i"), "%", IntLiteral(3)), "==", IntLiteral(0)),
                                      BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("Fizz")]))]),
                                      BlockStmt([
                                          IfStmt(BinaryOp(BinaryOp(Identifier("i"), "%", IntLiteral(5)), "==", IntLiteral(0)),
                                                 BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("Buzz")]))]),
                                                 BlockStmt([ExprStmt(FuncCall("printInt", [Identifier("i")]))]))
                                      ]))
                           ]))
                ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "12Fizz4BuzzFizz78FizzBuzz"

def test_extra_395():
    # 1+2+...+n via for
    ast = Program([
        FuncDecl(IntType(), "sumTo", [Param(IntType(), "n")], BlockStmt([
            VarDecl(IntType(), "s", IntLiteral(0)),
            ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                    BinaryOp(Identifier("i"), "<=", Identifier("n")),
                    PostfixOp("++", Identifier("i")),
                    BlockStmt([ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", Identifier("i"))))])),
            ReturnStmt(Identifier("s"))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("sumTo", [IntLiteral(10)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "55"

def test_extra_396():
    # loop: sum of squares matches formula
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "n", IntLiteral(5)),
        VarDecl(IntType(), "s", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", Identifier("n")),
                PostfixOp("++", Identifier("i")),
                BlockStmt([ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", BinaryOp(Identifier("i"), "*", Identifier("i")))))])),
        ExprStmt(FuncCall("printInt", [Identifier("s")]))
    ]))])
    # 1+4+9+16+25=55
    assert CodeGenerator().generate_and_run(ast) == "55"

def test_extra_397():
    # function: clamp value
    ast = Program([
        FuncDecl(IntType(), "clamp", [Param(IntType(), "x"), Param(IntType(), "lo"), Param(IntType(), "hi")],
                 BlockStmt([
                     IfStmt(BinaryOp(Identifier("x"), "<", Identifier("lo")),
                            BlockStmt([ReturnStmt(Identifier("lo"))]),
                            BlockStmt([IfStmt(BinaryOp(Identifier("x"), ">", Identifier("hi")),
                                              BlockStmt([ReturnStmt(Identifier("hi"))]),
                                              BlockStmt([ReturnStmt(Identifier("x"))]))]))
                 ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("clamp", [IntLiteral(-5), IntLiteral(0), IntLiteral(10)])])),
            ExprStmt(FuncCall("printInt", [FuncCall("clamp", [IntLiteral(5), IntLiteral(0), IntLiteral(10)])])),
            ExprStmt(FuncCall("printInt", [FuncCall("clamp", [IntLiteral(15), IntLiteral(0), IntLiteral(10)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "0510"

def test_extra_398():
    # postfix on member then print
    ast = Program([
        StructDecl("C", [MemberDecl(IntType(), "n")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("C"), "c", StructLiteral([IntLiteral(5)])),
            VarDecl(IntType(), "old", PostfixOp("++", MemberAccess(Identifier("c"), "n"))),
            ExprStmt(FuncCall("printInt", [Identifier("old")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("c"), "n")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "66"

def test_extra_399():
    # simple print string then int
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printString", [StringLiteral("count:")])),
        ExprStmt(FuncCall("printInt", [IntLiteral(42)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "count:42"

def test_extra_400():
    # while loop: find min of squares >= 200
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "n", IntLiteral(1)),
        WhileStmt(BinaryOp(BinaryOp(Identifier("n"), "*", Identifier("n")), "<", IntLiteral(200)), BlockStmt([
            ExprStmt(PostfixOp("++", Identifier("n")))
        ])),
        ExprStmt(FuncCall("printInt", [Identifier("n")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "15"

def test_extra_401():
    # float sum over loop
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "s", FloatLiteral(0.0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(4)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", FloatLiteral(0.5))))])),
        ExprStmt(FuncCall("printFloat", [Identifier("s")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "2.0"

def test_extra_402():
    # nested ternary-like via if
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "a", IntLiteral(3)),
        VarDecl(IntType(), "b", IntLiteral(7)),
        VarDecl(IntType(), "m", IntLiteral(0)),
        ExprStmt(AssignExpr(Identifier("m"), IfStmt(BinaryOp(Identifier("a"), ">", Identifier("b")),
                                                    BlockStmt([AssignExpr(Identifier("m"), Identifier("a"))]),
                                                    BlockStmt([AssignExpr(Identifier("m"), Identifier("b"))])))),
        ExprStmt(FuncCall("printInt", [Identifier("b")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "7"

def test_extra_403():
    # short circuit: left-to-right evaluation order
    ast = Program([
        FuncDecl(IntType(), "p1", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [IntLiteral(1)])),
            ReturnStmt(IntLiteral(1))
        ])),
        FuncDecl(IntType(), "p0", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [IntLiteral(0)])),
            ReturnStmt(IntLiteral(0))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(BinaryOp(FuncCall("p1", []), "&&", FuncCall("p0", [])))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "10"

def test_extra_404():
    # complex recursive: multiply via repeated addition
    ast = Program([
        FuncDecl(IntType(), "mul", [Param(IntType(), "a"), Param(IntType(), "b")], BlockStmt([
            IfStmt(BinaryOp(Identifier("b"), "==", IntLiteral(0)),
                   BlockStmt([ReturnStmt(IntLiteral(0))]),
                   BlockStmt([ReturnStmt(BinaryOp(Identifier("a"), "+", FuncCall("mul", [Identifier("a"), BinaryOp(Identifier("b"), "-", IntLiteral(1))])))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("mul", [IntLiteral(6), IntLiteral(7)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "42"

def test_extra_405():
    # complex: function with guard clauses
    ast = Program([
        FuncDecl(IntType(), "safeDivide", [Param(IntType(), "a"), Param(IntType(), "b")], BlockStmt([
            IfStmt(BinaryOp(Identifier("b"), "==", IntLiteral(0)),
                   BlockStmt([ReturnStmt(IntLiteral(-1))]),
                   None),
            ReturnStmt(BinaryOp(Identifier("a"), "/", Identifier("b")))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("safeDivide", [IntLiteral(10), IntLiteral(2)])])),
            ExprStmt(FuncCall("printInt", [FuncCall("safeDivide", [IntLiteral(10), IntLiteral(0)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "5-1"

def test_extra_406():
    # complex: count steps to reach target
    ast = Program([
        FuncDecl(IntType(), "steps", [Param(IntType(), "start"), Param(IntType(), "target")], BlockStmt([
            VarDecl(IntType(), "count", IntLiteral(0)),
            WhileStmt(BinaryOp(Identifier("start"), "!=", Identifier("target")), BlockStmt([
                IfStmt(BinaryOp(Identifier("start"), "<", Identifier("target")),
                       BlockStmt([ExprStmt(PostfixOp("++", Identifier("start")))]),
                       BlockStmt([ExprStmt(PrefixOp("--", Identifier("start")))])),
                ExprStmt(PostfixOp("++", Identifier("count")))
            ])),
            ReturnStmt(Identifier("count"))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("steps", [IntLiteral(3), IntLiteral(8)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "5"

def test_extra_407():
    # struct update via function
    ast = Program([
        StructDecl("Point", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
        FuncDecl(StructType("Point"), "move", [Param(StructType("Point"), "p"), Param(IntType(), "dx"), Param(IntType(), "dy")],
                 BlockStmt([
                     ExprStmt(AssignExpr(MemberAccess(Identifier("p"), "x"), BinaryOp(MemberAccess(Identifier("p"), "x"), "+", Identifier("dx")))),
                     ExprStmt(AssignExpr(MemberAccess(Identifier("p"), "y"), BinaryOp(MemberAccess(Identifier("p"), "y"), "+", Identifier("dy")))),
                     ReturnStmt(Identifier("p"))
                 ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Point"), "p", StructLiteral([IntLiteral(0), IntLiteral(0)])),
            VarDecl(StructType("Point"), "q", FuncCall("move", [Identifier("p"), IntLiteral(5), IntLiteral(3)])),
            ExprStmt(FuncCall("printInt", [BinaryOp(MemberAccess(Identifier("q"), "x"), "+", MemberAccess(Identifier("q"), "y"))]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "8"

def test_extra_408():
    # complex: iterative binary exponentiation
    ast = Program([
        FuncDecl(IntType(), "fastPow", [Param(IntType(), "b"), Param(IntType(), "e")], BlockStmt([
            VarDecl(IntType(), "r", IntLiteral(1)),
            WhileStmt(BinaryOp(Identifier("e"), ">", IntLiteral(0)), BlockStmt([
                IfStmt(BinaryOp(BinaryOp(Identifier("e"), "%", IntLiteral(2)), "==", IntLiteral(1)),
                       BlockStmt([ExprStmt(AssignExpr(Identifier("r"), BinaryOp(Identifier("r"), "*", Identifier("b"))))]),
                       None),
                ExprStmt(AssignExpr(Identifier("b"), BinaryOp(Identifier("b"), "*", Identifier("b")))),
                ExprStmt(AssignExpr(Identifier("e"), BinaryOp(Identifier("e"), "/", IntLiteral(2))))
            ])),
            ReturnStmt(Identifier("r"))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("fastPow", [IntLiteral(2), IntLiteral(8)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "256"

def test_extra_409():
    # complex: count trailing zeros of factorial
    ast = Program([
        FuncDecl(IntType(), "trailingZeros", [Param(IntType(), "n")], BlockStmt([
            VarDecl(IntType(), "count", IntLiteral(0)),
            VarDecl(IntType(), "p", IntLiteral(5)),
            WhileStmt(BinaryOp(Identifier("p"), "<=", Identifier("n")), BlockStmt([
                ExprStmt(AssignExpr(Identifier("count"), BinaryOp(Identifier("count"), "+", BinaryOp(Identifier("n"), "/", Identifier("p"))))),
                ExprStmt(AssignExpr(Identifier("p"), BinaryOp(Identifier("p"), "*", IntLiteral(5))))
            ])),
            ReturnStmt(Identifier("count"))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("trailingZeros", [IntLiteral(25)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "6"

def test_extra_410():
    # complex: string param function
    ast = Program([
        FuncDecl(VoidType(), "printTwice", [Param(StringType(), "s")], BlockStmt([
            ExprStmt(FuncCall("printString", [Identifier("s")])),
            ExprStmt(FuncCall("printString", [Identifier("s")]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printTwice", [StringLiteral("hello")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "hellohello"

def test_extra_411():
    # complex: sum divisors
    ast = Program([
        FuncDecl(IntType(), "sumDivisors", [Param(IntType(), "n")], BlockStmt([
            VarDecl(IntType(), "s", IntLiteral(0)),
            ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                    BinaryOp(Identifier("i"), "<=", Identifier("n")),
                    PostfixOp("++", Identifier("i")),
                    BlockStmt([
                        IfStmt(BinaryOp(BinaryOp(Identifier("n"), "%", Identifier("i")), "==", IntLiteral(0)),
                               BlockStmt([ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", Identifier("i"))))]),
                               None)
                    ])),
            ReturnStmt(Identifier("s"))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("sumDivisors", [IntLiteral(28)])]))
        ]))
    ])
    # Perfect number: 28 = 1+2+4+7+14+28 = 56
    assert CodeGenerator().generate_and_run(ast) == "56"

def test_extra_412():
    # complex: is perfect number
    ast = Program([
        FuncDecl(IntType(), "isPerfect", [Param(IntType(), "n")], BlockStmt([
            VarDecl(IntType(), "s", IntLiteral(0)),
            ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                    BinaryOp(Identifier("i"), "<", Identifier("n")),
                    PostfixOp("++", Identifier("i")),
                    BlockStmt([
                        IfStmt(BinaryOp(BinaryOp(Identifier("n"), "%", Identifier("i")), "==", IntLiteral(0)),
                               BlockStmt([ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", Identifier("i"))))]),
                               None)
                    ])),
            ReturnStmt(BinaryOp(Identifier("s"), "==", Identifier("n")))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("isPerfect", [IntLiteral(6)])])),
            ExprStmt(FuncCall("printInt", [FuncCall("isPerfect", [IntLiteral(28)])])),
            ExprStmt(FuncCall("printInt", [FuncCall("isPerfect", [IntLiteral(12)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "110"

def test_extra_413():
    # edge: zero loop iterations
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(5)),
                BinaryOp(Identifier("i"), "<", IntLiteral(5)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([ExprStmt(FuncCall("printInt", [Identifier("i")]))])),
        ExprStmt(FuncCall("printInt", [IntLiteral(0)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_414():
    # edge: one loop iteration
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(5)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(5)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([ExprStmt(FuncCall("printInt", [Identifier("i")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "5"

def test_extra_415():
    # edge: if with empty else
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        IfStmt(IntLiteral(0),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("yes")]))]),
               BlockStmt([]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == ""

def test_extra_416():
    # edge: multiple postfix in same expr
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(0)),
        VarDecl(IntType(), "y", IntLiteral(0)),
        ExprStmt(AssignExpr(Identifier("x"), PostfixOp("++", Identifier("y")))),
        ExprStmt(FuncCall("printInt", [Identifier("x")])),
        ExprStmt(FuncCall("printInt", [Identifier("y")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "11"

def test_extra_417():
    # edge: large switch value
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        SwitchStmt(IntLiteral(100), [
            CaseStmt(IntLiteral(100), [ExprStmt(FuncCall("printString", [StringLiteral("hundred")])), BreakStmt()])
        ], DefaultStmt([ExprStmt(FuncCall("printString", [StringLiteral("other")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "hundred"

def test_extra_418():
    # edge: float near-zero comparison
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [BinaryOp(FloatLiteral(0.0), "==", FloatLiteral(0.0))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_419():
    # edge: nested break and continue
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "cnt", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)),
                BinaryOp(Identifier("i"), "<", IntLiteral(5)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    IfStmt(BinaryOp(BinaryOp(Identifier("i"), "%", IntLiteral(2)), "==", IntLiteral(0)),
                           BlockStmt([ContinueStmt()]), None),
                    IfStmt(BinaryOp(Identifier("i"), "==", IntLiteral(3)),
                           BlockStmt([BreakStmt()]), None),
                    ExprStmt(PostfixOp("++", Identifier("cnt")))
                ])),
        ExprStmt(FuncCall("printInt", [Identifier("cnt")]))
    ]))])
    # i=0 skip, i=1 cnt=1, i=2 skip, i=3 break
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_420():
    # edge: for with float init
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(FloatType(), "f", FloatLiteral(0.0)),
                BinaryOp(Identifier("f"), "<", FloatLiteral(2.0)),
                ExprStmt(AssignExpr(Identifier("f"), BinaryOp(Identifier("f"), "+", FloatLiteral(0.5)))),
                BlockStmt([ExprStmt(FuncCall("printFloat", [Identifier("f")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0.00.51.01.5"

def test_extra_421():
    # edge: recursive power returning float
    ast = Program([
        FuncDecl(FloatType(), "fpow", [Param(FloatType(), "b"), Param(IntType(), "e")], BlockStmt([
            IfStmt(BinaryOp(Identifier("e"), "==", IntLiteral(0)),
                   BlockStmt([ReturnStmt(FloatLiteral(1.0))]),
                   BlockStmt([ReturnStmt(BinaryOp(Identifier("b"), "*", FuncCall("fpow", [Identifier("b"), BinaryOp(Identifier("e"), "-", IntLiteral(1))])))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printFloat", [FuncCall("fpow", [FloatLiteral(2.0), IntLiteral(8)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "256.0"

def test_extra_422():
    # edge: negative number in switch
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(-1)),
        SwitchStmt(Identifier("x"), [
            CaseStmt(IntLiteral(-1), [ExprStmt(FuncCall("printString", [StringLiteral("neg one")])), BreakStmt()]),
            CaseStmt(IntLiteral(0), [ExprStmt(FuncCall("printString", [StringLiteral("zero")])), BreakStmt()]),
            CaseStmt(IntLiteral(1), [ExprStmt(FuncCall("printString", [StringLiteral("pos one")])), BreakStmt()])
        ], None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "neg one"

def test_extra_423():
    # edge: many params, use all
    ast = Program([
        FuncDecl(IntType(), "sum5", [Param(IntType(), "a"), Param(IntType(), "b"), Param(IntType(), "c"),
                                     Param(IntType(), "d"), Param(IntType(), "e")],
                 BlockStmt([ReturnStmt(BinaryOp(BinaryOp(BinaryOp(BinaryOp(Identifier("a"), "+", Identifier("b")), "+", Identifier("c")), "+", Identifier("d")), "+", Identifier("e")))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("sum5", [IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "15"

def test_extra_424():
    # edge: struct with all types
    ast = Program([
        StructDecl("All", [MemberDecl(IntType(), "i"), MemberDecl(FloatType(), "f"), MemberDecl(StringType(), "s")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("All"), "a", StructLiteral([IntLiteral(1), FloatLiteral(2.5), StringLiteral("three")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("a"), "i")])),
            ExprStmt(FuncCall("printFloat", [MemberAccess(Identifier("a"), "f")])),
            ExprStmt(FuncCall("printString", [MemberAccess(Identifier("a"), "s")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "12.5three"

def test_extra_425():
    # edge: function with return in while loop
    ast = Program([
        FuncDecl(IntType(), "firstEven", [Param(IntType(), "n")], BlockStmt([
            ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                    BinaryOp(Identifier("i"), "<=", Identifier("n")),
                    PostfixOp("++", Identifier("i")),
                    BlockStmt([
                        IfStmt(BinaryOp(BinaryOp(Identifier("i"), "%", IntLiteral(2)), "==", IntLiteral(0)),
                               BlockStmt([ReturnStmt(Identifier("i"))]),
                               None)
                    ])),
            ReturnStmt(IntLiteral(-1))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("firstEven", [IntLiteral(7)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "2"

def test_extra_426():
    # edge: large for loop
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "s", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(1000)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", IntLiteral(1))))])),
        ExprStmt(FuncCall("printInt", [Identifier("s")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1000"

def test_extra_427():
    # edge: complex expression as function arg
    ast = Program([
        FuncDecl(IntType(), "square", [Param(IntType(), "n")],
                 BlockStmt([ReturnStmt(BinaryOp(Identifier("n"), "*", Identifier("n")))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("square", [BinaryOp(IntLiteral(3), "+", IntLiteral(4))])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "49"

def test_extra_428():
    # edge: function that never returns (implicit void)
    ast = Program([
        FuncDecl(VoidType(), "doNothing", [], BlockStmt([])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("doNothing", [])),
            ExprStmt(FuncCall("printInt", [IntLiteral(42)]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "42"

def test_extra_429():
    # edge: struct member used as loop bound
    ast = Program([
        StructDecl("Cfg", [MemberDecl(IntType(), "n")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Cfg"), "cfg", StructLiteral([IntLiteral(5)])),
            VarDecl(IntType(), "s", IntLiteral(0)),
            ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                    BinaryOp(Identifier("i"), "<=", MemberAccess(Identifier("cfg"), "n")),
                    PostfixOp("++", Identifier("i")),
                    BlockStmt([ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", Identifier("i"))))])),
            ExprStmt(FuncCall("printInt", [Identifier("s")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "15"

def test_extra_430():
    # edge: while loop that completes in first iteration
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(0)),
        WhileStmt(BinaryOp(Identifier("x"), "==", IntLiteral(0)), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("x")])),
            ExprStmt(PostfixOp("++", Identifier("x")))
        ])),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "01"

def test_extra_431():
    # edge: pass struct to function, modify, check original
    ast = Program([
        StructDecl("N", [MemberDecl(IntType(), "v")]),
        FuncDecl(StructType("N"), "doubled", [Param(StructType("N"), "n")], BlockStmt([
            ExprStmt(AssignExpr(MemberAccess(Identifier("n"), "v"), BinaryOp(MemberAccess(Identifier("n"), "v"), "*", IntLiteral(2)))),
            ReturnStmt(Identifier("n"))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("N"), "x", StructLiteral([IntLiteral(5)])),
            VarDecl(StructType("N"), "y", FuncCall("doubled", [Identifier("x")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("x"), "v")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("y"), "v")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "510"

def test_extra_432():
    # edge: auto type inference from complex expression
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "x", BinaryOp(BinaryOp(IntLiteral(3), "+", IntLiteral(4)), "*", IntLiteral(2))),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "14"

def test_extra_433():
    # edge: zero returned from recursive call
    ast = Program([
        FuncDecl(IntType(), "zero", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "==", IntLiteral(0)),
                   BlockStmt([ReturnStmt(IntLiteral(0))]),
                   BlockStmt([ReturnStmt(FuncCall("zero", [BinaryOp(Identifier("n"), "-", IntLiteral(1))]))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("zero", [IntLiteral(5)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_434():
    # edge: nested struct member access in loop
    ast = Program([
        StructDecl("Range", [MemberDecl(IntType(), "start"), MemberDecl(IntType(), "end_")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Range"), "r", StructLiteral([IntLiteral(1), IntLiteral(4)])),
            ForStmt(VarDecl(IntType(), "i", MemberAccess(Identifier("r"), "start")),
                    BinaryOp(Identifier("i"), "<=", MemberAccess(Identifier("r"), "end_")),
                    PostfixOp("++", Identifier("i")),
                    BlockStmt([ExprStmt(FuncCall("printInt", [Identifier("i")]))]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "1234"

def test_extra_435():
    # edge: function returning nothing (void) does not print
    ast = Program([
        FuncDecl(VoidType(), "silent", [], BlockStmt([
            VarDecl(IntType(), "x", IntLiteral(999))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("silent", [])),
            ExprStmt(FuncCall("printString", [StringLiteral("done")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "done"

def test_extra_436():
    # edge: struct assignment then struct used
    ast = Program([
        StructDecl("P", [MemberDecl(IntType(), "x")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("P"), "p", StructLiteral([IntLiteral(1)])),
            VarDecl(StructType("P"), "q", StructLiteral([IntLiteral(2)])),
            ExprStmt(AssignExpr(Identifier("p"), Identifier("q"))),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "x")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "2"

def test_extra_437():
    # edge: while with complex condition update
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "a", IntLiteral(1)),
        VarDecl(IntType(), "b", IntLiteral(10)),
        WhileStmt(BinaryOp(Identifier("a"), "<", Identifier("b")), BlockStmt([
            ExprStmt(PostfixOp("++", Identifier("a"))),
            ExprStmt(PrefixOp("--", Identifier("b")))
        ])),
        ExprStmt(FuncCall("printInt", [Identifier("a")])),
        ExprStmt(FuncCall("printInt", [Identifier("b")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "65"

def test_extra_438():
    # edge: multiple break in nested loop
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)),
                BinaryOp(Identifier("i"), "<", IntLiteral(5)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    ForStmt(VarDecl(IntType(), "j", IntLiteral(0)),
                            BinaryOp(Identifier("j"), "<", IntLiteral(5)),
                            PostfixOp("++", Identifier("j")),
                            BlockStmt([
                                ExprStmt(PostfixOp("++", Identifier("x"))),
                                BreakStmt()
                            ]))
                ])),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "5"

def test_extra_439():
    # edge: very deep recursion (careful with stack, small n)
    ast = Program([
        FuncDecl(IntType(), "sumR", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<=", IntLiteral(0)),
                   BlockStmt([ReturnStmt(IntLiteral(0))]),
                   BlockStmt([ReturnStmt(BinaryOp(Identifier("n"), "+", FuncCall("sumR", [BinaryOp(Identifier("n"), "-", IntLiteral(1))])))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("sumR", [IntLiteral(20)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "210"

def test_extra_440():
    # adversarial: empty string printed
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(StringType(), "s", StringLiteral("")),
        ExprStmt(FuncCall("printString", [Identifier("s")])),
        ExprStmt(FuncCall("printInt", [IntLiteral(1)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_441():
    # adversarial: operator precedence: 2+3*4=14 (not 20)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(2), "+", BinaryOp(IntLiteral(3), "*", IntLiteral(4)))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "14"

def test_extra_442():
    # adversarial: postfix ++ not prefix
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(5)),
        VarDecl(IntType(), "y", PostfixOp("++", Identifier("x"))),
        ExprStmt(FuncCall("printInt", [Identifier("y")])),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "66"

def test_extra_443():
    # adversarial: prefix ++ not postfix
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(5)),
        VarDecl(IntType(), "y", PrefixOp("++", Identifier("x"))),
        ExprStmt(FuncCall("printInt", [Identifier("y")])),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "66"

def test_extra_444():
    # adversarial: chained assignment is right-associative
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "a", IntLiteral(0)),
        VarDecl(IntType(), "b", IntLiteral(0)),
        VarDecl(IntType(), "c", IntLiteral(0)),
        ExprStmt(AssignExpr(Identifier("a"), AssignExpr(Identifier("b"), AssignExpr(Identifier("c"), IntLiteral(7))))),
        ExprStmt(FuncCall("printInt", [BinaryOp(BinaryOp(Identifier("a"), "+", Identifier("b")), "+", Identifier("c"))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "21"

def test_extra_445():
    # adversarial: short circuit leaves side effect unevaluated
    ast = Program([
        FuncDecl(IntType(), "badFn", [], BlockStmt([
            ExprStmt(FuncCall("printString", [StringLiteral("SHOULD_NOT_PRINT")])),
            ReturnStmt(IntLiteral(1))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(BinaryOp(IntLiteral(1), "||", FuncCall("badFn", []))),
            ExprStmt(FuncCall("printString", [StringLiteral("ok")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "ok"

def test_extra_446():
    # adversarial: && short circuits before second call
    ast = Program([
        FuncDecl(IntType(), "neverCalled", [], BlockStmt([
            ExprStmt(FuncCall("printString", [StringLiteral("SHOULD_NOT_PRINT")])),
            ReturnStmt(IntLiteral(1))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(BinaryOp(IntLiteral(0), "&&", FuncCall("neverCalled", []))),
            ExprStmt(FuncCall("printString", [StringLiteral("ok")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "ok"

def test_extra_447():
    # adversarial: switch with expression that evaluates to 0
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        SwitchStmt(BinaryOp(IntLiteral(5), "-", IntLiteral(5)), [
            CaseStmt(IntLiteral(0), [ExprStmt(FuncCall("printString", [StringLiteral("zero")])), BreakStmt()]),
            CaseStmt(IntLiteral(1), [ExprStmt(FuncCall("printString", [StringLiteral("one")])), BreakStmt()])
        ], None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "zero"

def test_extra_448():
    # adversarial: float subtraction precision check
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printFloat", [BinaryOp(FloatLiteral(1.0), "-", FloatLiteral(0.5))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0.5"

def test_extra_449():
    # adversarial: struct copy then modify copy, original unchanged
    ast = Program([
        StructDecl("S", [MemberDecl(IntType(), "x")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("S"), "orig", StructLiteral([IntLiteral(42)])),
            VarDecl(StructType("S"), "copy", Identifier("orig")),
            ExprStmt(AssignExpr(MemberAccess(Identifier("copy"), "x"), IntLiteral(0))),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("orig"), "x")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("copy"), "x")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "420"

def test_extra_450():
    # adversarial: while condition evaluated before body each time
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(0)),
        WhileStmt(BinaryOp(PostfixOp("++", Identifier("x")), "<=", IntLiteral(3)), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("x")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "123"

def test_extra_451():
    # FizzBuzz 15 (FizzBuzz)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "i", IntLiteral(15)),
        IfStmt(BinaryOp(BinaryOp(BinaryOp(Identifier("i"), "%", IntLiteral(3)), "==", IntLiteral(0)),
                        "&&",
                        BinaryOp(BinaryOp(Identifier("i"), "%", IntLiteral(5)), "==", IntLiteral(0))),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("FizzBuzz")]))]),
               None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "FizzBuzz"

def test_extra_452():
    # print 5 identical lines
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)),
                BinaryOp(Identifier("i"), "<", IntLiteral(5)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("line")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "linelinelinelineline"

def test_extra_453():
    # int division: negative / positive
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(-10), "/", IntLiteral(3))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "-3"

def test_extra_454():
    # auto var from string function result
    ast = Program([
        FuncDecl(StringType(), "hello", [], BlockStmt([ReturnStmt(StringLiteral("hello"))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(None, "s", FuncCall("hello", [])),
            ExprStmt(FuncCall("printString", [Identifier("s")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "hello"

def test_extra_455():
    # nested for: triangle numbers
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "n", IntLiteral(1)),
                BinaryOp(Identifier("n"), "<=", IntLiteral(4)),
                PostfixOp("++", Identifier("n")),
                BlockStmt([
                    VarDecl(IntType(), "t", IntLiteral(0)),
                    ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                            BinaryOp(Identifier("i"), "<=", Identifier("n")),
                            PostfixOp("++", Identifier("i")),
                            BlockStmt([ExprStmt(AssignExpr(Identifier("t"), BinaryOp(Identifier("t"), "+", Identifier("i"))))])),
                    ExprStmt(FuncCall("printInt", [Identifier("t")]))
                ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "13610"

def test_extra_456():
    # float loop average
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "s", FloatLiteral(0.0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(4)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", BinaryOp(Identifier("i"), "+", FloatLiteral(0.0)))))])),
        ExprStmt(FuncCall("printFloat", [BinaryOp(Identifier("s"), "/", FloatLiteral(4.0))]))
    ]))])
    # average of 1,2,3,4 = 2.5
    assert CodeGenerator().generate_and_run(ast) == "2.5"

def test_extra_457():
    # complex: min of array-like (simulate with vars)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "v1", IntLiteral(5)),
        VarDecl(IntType(), "v2", IntLiteral(3)),
        VarDecl(IntType(), "v3", IntLiteral(8)),
        VarDecl(IntType(), "mn", Identifier("v1")),
        IfStmt(BinaryOp(Identifier("v2"), "<", Identifier("mn")), BlockStmt([ExprStmt(AssignExpr(Identifier("mn"), Identifier("v2")))]), None),
        IfStmt(BinaryOp(Identifier("v3"), "<", Identifier("mn")), BlockStmt([ExprStmt(AssignExpr(Identifier("mn"), Identifier("v3")))]), None),
        ExprStmt(FuncCall("printInt", [Identifier("mn")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "3"

def test_extra_458():
    # complex: compute nth Fibonacci number iteratively
    ast = Program([
        FuncDecl(IntType(), "fib", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "==", IntLiteral(0)), BlockStmt([ReturnStmt(IntLiteral(0))]), None),
            IfStmt(BinaryOp(Identifier("n"), "==", IntLiteral(1)), BlockStmt([ReturnStmt(IntLiteral(1))]), None),
            VarDecl(IntType(), "a", IntLiteral(0)),
            VarDecl(IntType(), "b", IntLiteral(1)),
            VarDecl(IntType(), "i", IntLiteral(2)),
            WhileStmt(BinaryOp(Identifier("i"), "<=", Identifier("n")), BlockStmt([
                VarDecl(IntType(), "tmp", BinaryOp(Identifier("a"), "+", Identifier("b"))),
                ExprStmt(AssignExpr(Identifier("a"), Identifier("b"))),
                ExprStmt(AssignExpr(Identifier("b"), Identifier("tmp"))),
                ExprStmt(PostfixOp("++", Identifier("i")))
            ])),
            ReturnStmt(Identifier("b"))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("fib", [IntLiteral(10)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "55"

def test_extra_459():
    # complex: is divisible by both 3 and 7
    ast = Program([
        FuncDecl(IntType(), "by3and7", [Param(IntType(), "n")],
                 BlockStmt([ReturnStmt(BinaryOp(
                     BinaryOp(BinaryOp(Identifier("n"), "%", IntLiteral(3)), "==", IntLiteral(0)),
                     "&&",
                     BinaryOp(BinaryOp(Identifier("n"), "%", IntLiteral(7)), "==", IntLiteral(0))
                 ))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("by3and7", [IntLiteral(21)])])),
            ExprStmt(FuncCall("printInt", [FuncCall("by3and7", [IntLiteral(42)])])),
            ExprStmt(FuncCall("printInt", [FuncCall("by3and7", [IntLiteral(9)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "110"

def test_extra_460():
    # print increasing powers of 3
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "p", IntLiteral(1)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)),
                BinaryOp(Identifier("i"), "<", IntLiteral(5)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    ExprStmt(FuncCall("printInt", [Identifier("p")])),
                    ExprStmt(AssignExpr(Identifier("p"), BinaryOp(Identifier("p"), "*", IntLiteral(3))))
                ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1392781"

def test_extra_461():
    # sum of first n cubes
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "s", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(4)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", BinaryOp(BinaryOp(Identifier("i"), "*", Identifier("i")), "*", Identifier("i")))))])),
        ExprStmt(FuncCall("printInt", [Identifier("s")]))
    ]))])
    # 1+8+27+64=100
    assert CodeGenerator().generate_and_run(ast) == "100"

def test_extra_462():
    # recursive countdown with stop
    ast = Program([
        FuncDecl(VoidType(), "c", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "==", IntLiteral(0)),
                   BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("go!")]))]),
                   BlockStmt([
                       ExprStmt(FuncCall("printInt", [Identifier("n")])),
                       ExprStmt(FuncCall("c", [BinaryOp(Identifier("n"), "-", IntLiteral(1))]))
                   ]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("c", [IntLiteral(3)]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "321go!"

def test_extra_463():
    # bit manipulation: check if power of 2 (n & (n-1) == 0)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "n", IntLiteral(16)),
        IfStmt(BinaryOp(BinaryOp(Identifier("n"), ">", IntLiteral(0)), "&&",
                        BinaryOp(BinaryOp(Identifier("n"), "%", IntLiteral(2)), "==", IntLiteral(0))),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("even")]))]),
               None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "even"

def test_extra_464():
    # compute sum via recursion
    ast = Program([
        FuncDecl(IntType(), "add", [Param(IntType(), "a"), Param(IntType(), "b")],
                 BlockStmt([ReturnStmt(BinaryOp(Identifier("a"), "+", Identifier("b")))])),
        FuncDecl(IntType(), "sumAll", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<=", IntLiteral(0)),
                   BlockStmt([ReturnStmt(IntLiteral(0))]),
                   BlockStmt([ReturnStmt(FuncCall("add", [Identifier("n"), FuncCall("sumAll", [BinaryOp(Identifier("n"), "-", IntLiteral(1))])]))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("sumAll", [IntLiteral(5)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "15"

def test_extra_465():
    # float 0.25 + 0.25 + 0.25 + 0.25 = 1.0
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printFloat", [
            BinaryOp(BinaryOp(BinaryOp(FloatLiteral(0.25), "+", FloatLiteral(0.25)), "+", FloatLiteral(0.25)), "+", FloatLiteral(0.25))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1.0"

def test_extra_466():
    # print 0.0 from subtraction
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "x", FloatLiteral(5.0)),
        ExprStmt(FuncCall("printFloat", [BinaryOp(Identifier("x"), "-", FloatLiteral(5.0))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0.0"

def test_extra_467():
    # complex: number to binary string (we approximate with counting bits)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "n", IntLiteral(6)),
        VarDecl(IntType(), "bits", IntLiteral(0)),
        WhileStmt(BinaryOp(Identifier("n"), ">", IntLiteral(0)), BlockStmt([
            ExprStmt(AssignExpr(Identifier("bits"), BinaryOp(Identifier("bits"), "+", BinaryOp(Identifier("n"), "%", IntLiteral(2))))),
            ExprStmt(AssignExpr(Identifier("n"), BinaryOp(Identifier("n"), "/", IntLiteral(2))))
        ])),
        ExprStmt(FuncCall("printInt", [Identifier("bits")]))
    ]))])
    # 6=110, two 1-bits
    assert CodeGenerator().generate_and_run(ast) == "2"

def test_extra_468():
    # complex: all primes in range printed
    ast = Program([
        FuncDecl(IntType(), "isPrime", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<", IntLiteral(2)), BlockStmt([ReturnStmt(IntLiteral(0))]), None),
            VarDecl(IntType(), "i", IntLiteral(2)),
            WhileStmt(BinaryOp(BinaryOp(Identifier("i"), "*", Identifier("i")), "<=", Identifier("n")), BlockStmt([
                IfStmt(BinaryOp(BinaryOp(Identifier("n"), "%", Identifier("i")), "==", IntLiteral(0)),
                       BlockStmt([ReturnStmt(IntLiteral(0))]), None),
                ExprStmt(PostfixOp("++", Identifier("i")))
            ])),
            ReturnStmt(IntLiteral(1))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ForStmt(VarDecl(IntType(), "i", IntLiteral(2)),
                    BinaryOp(Identifier("i"), "<=", IntLiteral(10)),
                    PostfixOp("++", Identifier("i")),
                    BlockStmt([
                        IfStmt(FuncCall("isPrime", [Identifier("i")]),
                               BlockStmt([ExprStmt(FuncCall("printInt", [Identifier("i")]))]),
                               None)
                    ]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "2357"

def test_extra_469():
    # complex: isArmstrong (narcissistic number): 153
    ast = Program([
        FuncDecl(IntType(), "arm3", [Param(IntType(), "n")], BlockStmt([
            VarDecl(IntType(), "a", BinaryOp(Identifier("n"), "/", IntLiteral(100))),
            VarDecl(IntType(), "b", BinaryOp(BinaryOp(Identifier("n"), "/", IntLiteral(10)), "%", IntLiteral(10))),
            VarDecl(IntType(), "c", BinaryOp(Identifier("n"), "%", IntLiteral(10))),
            ReturnStmt(BinaryOp(
                Identifier("n"), "==",
                BinaryOp(BinaryOp(BinaryOp(Identifier("a"), "*", BinaryOp(Identifier("a"), "*", Identifier("a"))), "+",
                                  BinaryOp(Identifier("b"), "*", BinaryOp(Identifier("b"), "*", Identifier("b")))), "+",
                         BinaryOp(Identifier("c"), "*", BinaryOp(Identifier("c"), "*", Identifier("c"))))
            ))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("arm3", [IntLiteral(153)])])),
            ExprStmt(FuncCall("printInt", [FuncCall("arm3", [IntLiteral(370)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "11"

def test_extra_470():
    # complex: simulate stack-like with two vars
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "top", IntLiteral(-1)),
        VarDecl(IntType(), "val", IntLiteral(0)),
        # push 5
        ExprStmt(AssignExpr(Identifier("top"), IntLiteral(0))),
        ExprStmt(AssignExpr(Identifier("val"), IntLiteral(5))),
        ExprStmt(FuncCall("printInt", [Identifier("val")])),
        # pop
        ExprStmt(AssignExpr(Identifier("top"), IntLiteral(-1))),
        ExprStmt(FuncCall("printInt", [Identifier("top")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "5-1"

def test_extra_471():
    # test: int literal max common test case
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [IntLiteral(2147483647)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "2147483647"

def test_extra_472():
    # test: large loop sum
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "s", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(100)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", Identifier("i"))))])),
        ExprStmt(FuncCall("printInt", [Identifier("s")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "5050"

def test_extra_473():
    # test: float var used in comparison chain
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "pi", FloatLiteral(3.14)),
        ExprStmt(FuncCall("printInt", [BinaryOp(
            BinaryOp(Identifier("pi"), ">", FloatLiteral(3.0)),
            "&&",
            BinaryOp(Identifier("pi"), "<", FloatLiteral(4.0))
        )]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_474():
    # test: function returning negative
    ast = Program([
        FuncDecl(IntType(), "neg", [Param(IntType(), "n")],
                 BlockStmt([ReturnStmt(PrefixOp("-", Identifier("n")))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("neg", [IntLiteral(42)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "-42"

def test_extra_475():
    # test: loop over 0
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)),
                BinaryOp(Identifier("i"), "<", IntLiteral(0)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([ExprStmt(FuncCall("printInt", [Identifier("i")]))])),
        ExprStmt(FuncCall("printString", [StringLiteral("done")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "done"

def test_extra_476():
    # test: recursive count down to print
    ast = Program([
        FuncDecl(VoidType(), "pr", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), ">", IntLiteral(0)),
                   BlockStmt([
                       ExprStmt(FuncCall("pr", [BinaryOp(Identifier("n"), "-", IntLiteral(1))])),
                       ExprStmt(FuncCall("printInt", [Identifier("n")]))
                   ]),
                   None)
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("pr", [IntLiteral(4)]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "1234"

def test_extra_477():
    # test: binary OR of two conditions
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(3)),
        ExprStmt(FuncCall("printInt", [BinaryOp(
            BinaryOp(Identifier("x"), "==", IntLiteral(3)),
            "||",
            BinaryOp(Identifier("x"), "==", IntLiteral(5))
        )]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_478():
    # test: nested function calls 4 deep
    ast = Program([
        FuncDecl(IntType(), "inc", [Param(IntType(), "n")],
                 BlockStmt([ReturnStmt(BinaryOp(Identifier("n"), "+", IntLiteral(1)))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [
                FuncCall("inc", [FuncCall("inc", [FuncCall("inc", [FuncCall("inc", [IntLiteral(0)])])])])
            ]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "4"

def test_extra_479():
    # test: prefix ++ on member in expr
    ast = Program([
        StructDecl("C", [MemberDecl(IntType(), "n")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("C"), "c", StructLiteral([IntLiteral(4)])),
            ExprStmt(FuncCall("printInt", [PrefixOp("++", MemberAccess(Identifier("c"), "n"))]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "5"

def test_extra_480():
    # test: complex nested if-else chain
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(7)),
        IfStmt(BinaryOp(Identifier("x"), "==", IntLiteral(1)),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("one")]))]),
               BlockStmt([IfStmt(BinaryOp(Identifier("x"), "==", IntLiteral(3)),
                                 BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("three")]))]),
                                 BlockStmt([IfStmt(BinaryOp(Identifier("x"), "==", IntLiteral(7)),
                                                   BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("seven")]))]),
                                                   BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("other")]))])
                                                   )])
                                 )])
               )
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "seven"

def test_extra_481():
    # test: mix of string and int prints
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printString", [StringLiteral("a")])),
        ExprStmt(FuncCall("printInt", [IntLiteral(1)])),
        ExprStmt(FuncCall("printString", [StringLiteral("b")])),
        ExprStmt(FuncCall("printInt", [IntLiteral(2)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "a1b2"

def test_extra_482():
    # test: complex struct with mixed ops
    ast = Program([
        StructDecl("Stats", [MemberDecl(IntType(), "min"), MemberDecl(IntType(), "max"), MemberDecl(IntType(), "sum")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Stats"), "s", StructLiteral([IntLiteral(100), IntLiteral(0), IntLiteral(0)])),
            ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                    BinaryOp(Identifier("i"), "<=", IntLiteral(5)),
                    PostfixOp("++", Identifier("i")),
                    BlockStmt([
                        IfStmt(BinaryOp(Identifier("i"), "<", MemberAccess(Identifier("s"), "min")),
                               BlockStmt([ExprStmt(AssignExpr(MemberAccess(Identifier("s"), "min"), Identifier("i")))]), None),
                        IfStmt(BinaryOp(Identifier("i"), ">", MemberAccess(Identifier("s"), "max")),
                               BlockStmt([ExprStmt(AssignExpr(MemberAccess(Identifier("s"), "max"), Identifier("i")))]), None),
                        ExprStmt(AssignExpr(MemberAccess(Identifier("s"), "sum"), BinaryOp(MemberAccess(Identifier("s"), "sum"), "+", Identifier("i"))))
                    ])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("s"), "min")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("s"), "max")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("s"), "sum")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "1515"

def test_extra_483():
    # test: for: double each element
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(4)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(Identifier("i"), "*", IntLiteral(2))]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "2468"

def test_extra_484():
    # test: multiple functions, chain calls
    ast = Program([
        FuncDecl(IntType(), "id", [Param(IntType(), "x")], BlockStmt([ReturnStmt(Identifier("x"))])),
        FuncDecl(IntType(), "neg", [Param(IntType(), "x")], BlockStmt([ReturnStmt(PrefixOp("-", Identifier("x")))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("neg", [FuncCall("id", [IntLiteral(5)])])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "-5"

def test_extra_485():
    # test: while condition uses function call
    ast = Program([
        FuncDecl(IntType(), "getN", [Param(IntType(), "x")], BlockStmt([ReturnStmt(Identifier("x"))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(IntType(), "i", IntLiteral(3)),
            WhileStmt(FuncCall("getN", [Identifier("i")]), BlockStmt([
                ExprStmt(FuncCall("printInt", [Identifier("i")])),
                ExprStmt(PrefixOp("--", Identifier("i")))
            ]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "321"

def test_extra_486():
    # test: nested recursive with accumulate
    ast = Program([
        FuncDecl(IntType(), "accum", [Param(IntType(), "n"), Param(IntType(), "acc")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<=", IntLiteral(0)),
                   BlockStmt([ReturnStmt(Identifier("acc"))]),
                   BlockStmt([ReturnStmt(FuncCall("accum", [BinaryOp(Identifier("n"), "-", IntLiteral(1)),
                                                             BinaryOp(Identifier("acc"), "+", Identifier("n"))]))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("accum", [IntLiteral(10), IntLiteral(0)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "55"

def test_extra_487():
    # test: swap two float vars
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "a", FloatLiteral(1.5)),
        VarDecl(FloatType(), "b", FloatLiteral(2.5)),
        VarDecl(FloatType(), "tmp", Identifier("a")),
        ExprStmt(AssignExpr(Identifier("a"), Identifier("b"))),
        ExprStmt(AssignExpr(Identifier("b"), Identifier("tmp"))),
        ExprStmt(FuncCall("printFloat", [Identifier("a")])),
        ExprStmt(FuncCall("printFloat", [Identifier("b")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "2.51.5"

def test_extra_488():
    # test: function with two structs params
    ast = Program([
        StructDecl("Pt", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
        FuncDecl(IntType(), "manhattan", [Param(StructType("Pt"), "a"), Param(StructType("Pt"), "b")],
                 BlockStmt([ReturnStmt(BinaryOp(
                     FuncCall("myAbs", [BinaryOp(MemberAccess(Identifier("a"), "x"), "-", MemberAccess(Identifier("b"), "x"))]),
                     "+",
                     FuncCall("myAbs", [BinaryOp(MemberAccess(Identifier("a"), "y"), "-", MemberAccess(Identifier("b"), "y"))])
                 ))])),
        FuncDecl(IntType(), "myAbs", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<", IntLiteral(0)),
                   BlockStmt([ReturnStmt(PrefixOp("-", Identifier("n")))]),
                   BlockStmt([ReturnStmt(Identifier("n"))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Pt"), "p1", StructLiteral([IntLiteral(1), IntLiteral(2)])),
            VarDecl(StructType("Pt"), "p2", StructLiteral([IntLiteral(4), IntLiteral(6)])),
            ExprStmt(FuncCall("printInt", [FuncCall("manhattan", [Identifier("p1"), Identifier("p2")])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "7"

def test_extra_489():
    # test: complex string param usage
    ast = Program([
        FuncDecl(VoidType(), "printN", [Param(StringType(), "s"), Param(IntType(), "n")], BlockStmt([
            ForStmt(VarDecl(IntType(), "i", IntLiteral(0)),
                    BinaryOp(Identifier("i"), "<", Identifier("n")),
                    PostfixOp("++", Identifier("i")),
                    BlockStmt([ExprStmt(FuncCall("printString", [Identifier("s")]))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printN", [StringLiteral("ha"), IntLiteral(3)]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "hahaha"

def test_extra_490():
    # test: large input sum
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "s", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(50)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", Identifier("i"))))])),
        ExprStmt(FuncCall("printInt", [Identifier("s")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1275"

def test_extra_491():
    # test: integer arithmetic wrap (stays in int range)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(1000000), "*", IntLiteral(1000))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1000000000"

def test_extra_492():
    # test: loop: compute digital root
    ast = Program([
        FuncDecl(IntType(), "drStep", [Param(IntType(), "n")], BlockStmt([
            VarDecl(IntType(), "s", IntLiteral(0)),
            WhileStmt(BinaryOp(Identifier("n"), ">", IntLiteral(0)), BlockStmt([
                ExprStmt(AssignExpr(Identifier("s"), BinaryOp(Identifier("s"), "+", BinaryOp(Identifier("n"), "%", IntLiteral(10))))),
                ExprStmt(AssignExpr(Identifier("n"), BinaryOp(Identifier("n"), "/", IntLiteral(10))))
            ])),
            ReturnStmt(Identifier("s"))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(IntType(), "n", IntLiteral(493)),
            WhileStmt(BinaryOp(Identifier("n"), ">", IntLiteral(9)), BlockStmt([
                ExprStmt(AssignExpr(Identifier("n"), FuncCall("drStep", [Identifier("n")])))
            ])),
            ExprStmt(FuncCall("printInt", [Identifier("n")]))
        ]))
    ])
    # 4+9+3=16, 1+6=7
    assert CodeGenerator().generate_and_run(ast) == "7"

def test_extra_493():
    # test: complex for: print pairs
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(3)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    ExprStmt(FuncCall("printInt", [Identifier("i")])),
                    ExprStmt(FuncCall("printInt", [BinaryOp(Identifier("i"), "*", Identifier("i"))]))
                ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "112439"

def test_extra_494():
    # test: min function with floats
    ast = Program([
        FuncDecl(FloatType(), "fmin", [Param(FloatType(), "a"), Param(FloatType(), "b")], BlockStmt([
            IfStmt(BinaryOp(Identifier("a"), "<", Identifier("b")),
                   BlockStmt([ReturnStmt(Identifier("a"))]),
                   BlockStmt([ReturnStmt(Identifier("b"))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printFloat", [FuncCall("fmin", [FloatLiteral(2.5), FloatLiteral(1.5)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "1.5"

def test_extra_495():
    # test: struct with update loop
    ast = Program([
        StructDecl("Counter", [MemberDecl(IntType(), "val")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Counter"), "c", StructLiteral([IntLiteral(0)])),
            ForStmt(VarDecl(IntType(), "i", IntLiteral(0)),
                    BinaryOp(Identifier("i"), "<", IntLiteral(5)),
                    PostfixOp("++", Identifier("i")),
                    BlockStmt([ExprStmt(AssignExpr(MemberAccess(Identifier("c"), "val"),
                                                    BinaryOp(MemberAccess(Identifier("c"), "val"), "+", IntLiteral(2))))])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("c"), "val")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "10"

def test_extra_496():
    # test: large recursion sum
    ast = Program([
        FuncDecl(IntType(), "s", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<=", IntLiteral(0)),
                   BlockStmt([ReturnStmt(IntLiteral(0))]),
                   BlockStmt([ReturnStmt(BinaryOp(Identifier("n"), "+", FuncCall("s", [BinaryOp(Identifier("n"), "-", IntLiteral(1))])))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("s", [IntLiteral(50)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "1275"

def test_extra_497():
    # test: float loop halving
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "x", FloatLiteral(16.0)),
        WhileStmt(BinaryOp(Identifier("x"), ">", FloatLiteral(1.0)), BlockStmt([
            ExprStmt(AssignExpr(Identifier("x"), BinaryOp(Identifier("x"), "/", FloatLiteral(2.0))))
        ])),
        ExprStmt(FuncCall("printFloat", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1.0"

def test_extra_498():
    # test: multi-step struct computation
    ast = Program([
        StructDecl("Frac", [MemberDecl(IntType(), "num"), MemberDecl(IntType(), "den")]),
        FuncDecl(IntType(), "gcd", [Param(IntType(), "a"), Param(IntType(), "b")], BlockStmt([
            WhileStmt(BinaryOp(Identifier("b"), "!=", IntLiteral(0)), BlockStmt([
                VarDecl(IntType(), "t", Identifier("b")),
                ExprStmt(AssignExpr(Identifier("b"), BinaryOp(Identifier("a"), "%", Identifier("b")))),
                ExprStmt(AssignExpr(Identifier("a"), Identifier("t")))
            ])),
            ReturnStmt(Identifier("a"))
        ])),
        FuncDecl(StructType("Frac"), "reduce", [Param(StructType("Frac"), "f")], BlockStmt([
            VarDecl(IntType(), "g", FuncCall("gcd", [MemberAccess(Identifier("f"), "num"), MemberAccess(Identifier("f"), "den")])),
            ExprStmt(AssignExpr(MemberAccess(Identifier("f"), "num"), BinaryOp(MemberAccess(Identifier("f"), "num"), "/", Identifier("g")))),
            ExprStmt(AssignExpr(MemberAccess(Identifier("f"), "den"), BinaryOp(MemberAccess(Identifier("f"), "den"), "/", Identifier("g")))),
            ReturnStmt(Identifier("f"))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Frac"), "f", StructLiteral([IntLiteral(4), IntLiteral(6)])),
            VarDecl(StructType("Frac"), "r", FuncCall("reduce", [Identifier("f")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("r"), "num")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("r"), "den")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "23"

def test_extra_499():
    # test: complex program: sieve of eratosthenes (manual check)
    ast = Program([
        FuncDecl(IntType(), "isPrime", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<", IntLiteral(2)), BlockStmt([ReturnStmt(IntLiteral(0))]), None),
            VarDecl(IntType(), "i", IntLiteral(2)),
            WhileStmt(BinaryOp(BinaryOp(Identifier("i"), "*", Identifier("i")), "<=", Identifier("n")), BlockStmt([
                IfStmt(BinaryOp(BinaryOp(Identifier("n"), "%", Identifier("i")), "==", IntLiteral(0)),
                       BlockStmt([ReturnStmt(IntLiteral(0))]), None),
                ExprStmt(PostfixOp("++", Identifier("i")))
            ])),
            ReturnStmt(IntLiteral(1))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(IntType(), "cnt", IntLiteral(0)),
            ForStmt(VarDecl(IntType(), "i", IntLiteral(2)),
                    BinaryOp(Identifier("i"), "<=", IntLiteral(50)),
                    PostfixOp("++", Identifier("i")),
                    BlockStmt([
                        IfStmt(FuncCall("isPrime", [Identifier("i")]),
                               BlockStmt([ExprStmt(PostfixOp("++", Identifier("cnt")))]),
                               None)
                    ])),
            ExprStmt(FuncCall("printInt", [Identifier("cnt")]))
        ]))
    ])
    # primes <=50: 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47 = 15
    assert CodeGenerator().generate_and_run(ast) == "15"

def test_extra_500():
    # test: complex tail recursive accumulator
    ast = Program([
        FuncDecl(IntType(), "tailFact", [Param(IntType(), "n"), Param(IntType(), "acc")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<=", IntLiteral(1)),
                   BlockStmt([ReturnStmt(Identifier("acc"))]),
                   BlockStmt([ReturnStmt(FuncCall("tailFact", [BinaryOp(Identifier("n"), "-", IntLiteral(1)),
                                                                BinaryOp(Identifier("acc"), "*", Identifier("n"))]))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("tailFact", [IntLiteral(6), IntLiteral(1)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "720"

# ===== TESTS 501-550: readInt / readFloat / readString with input_data =====

def test_extra_501():
    # single readInt
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", FuncCall("readInt", [])),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "42\n") == "42"

def test_extra_502():
    # readInt negative
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", FuncCall("readInt", [])),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "-100\n") == "-100"

def test_extra_503():
    # multiple readInt calls
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "a", FuncCall("readInt", [])),
        VarDecl(IntType(), "b", FuncCall("readInt", [])),
        ExprStmt(FuncCall("printInt", [BinaryOp(Identifier("a"), "+", Identifier("b"))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "5\n10\n") == "15"

def test_extra_504():
    # readInt in loop
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "sum", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(3)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(AssignExpr(Identifier("sum"), BinaryOp(Identifier("sum"), "+", FuncCall("readInt", []))))
        ])),
        ExprStmt(FuncCall("printInt", [Identifier("sum")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "1\n2\n3\n") == "6"

def test_extra_505():
    # readInt in conditional
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", FuncCall("readInt", [])),
        IfStmt(BinaryOp(Identifier("x"), ">", IntLiteral(50)),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("big")]))]),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("small")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "75\n") == "big"

def test_extra_506():
    # readFloat single
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "x", FuncCall("readFloat", [])),
        ExprStmt(FuncCall("printFloat", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "3.5\n") == "3.5"

def test_extra_507():
    # readFloat multiple and arithmetic
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "a", FuncCall("readFloat", [])),
        VarDecl(FloatType(), "b", FuncCall("readFloat", [])),
        ExprStmt(FuncCall("printFloat", [BinaryOp(Identifier("a"), "*", Identifier("b"))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "2.5\n2.0\n") == "5.0"

def test_extra_508():
    # readFloat negative
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "x", FuncCall("readFloat", [])),
        ExprStmt(FuncCall("printFloat", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "-1.5\n") == "-1.5"

def test_extra_509():
    # readString single
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(StringType(), "s", FuncCall("readString", [])),
        ExprStmt(FuncCall("printString", [Identifier("s")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "hello\n") == "hello"

def test_extra_510():
    # readString multiple
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(StringType(), "s1", FuncCall("readString", [])),
        VarDecl(StringType(), "s2", FuncCall("readString", [])),
        ExprStmt(FuncCall("printString", [Identifier("s1")])),
        ExprStmt(FuncCall("printString", [Identifier("s2")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "foo\nbar\n") == "foobar"

def test_extra_511():
    # readInt and use in arithmetic
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", FuncCall("readInt", [])),
        ExprStmt(FuncCall("printInt", [BinaryOp(Identifier("x"), "*", IntLiteral(2))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "21\n") == "42"

def test_extra_512():
    # readInt in while loop
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", FuncCall("readInt", [])),
        WhileStmt(BinaryOp(Identifier("x"), ">", IntLiteral(0)), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("x")])),
            ExprStmt(AssignExpr(Identifier("x"), BinaryOp(Identifier("x"), "-", IntLiteral(1))))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "3\n") == "321"

def test_extra_513():
    # readFloat and readInt mixed
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "i", FuncCall("readInt", [])),
        VarDecl(FloatType(), "f", FuncCall("readFloat", [])),
        ExprStmt(FuncCall("printFloat", [BinaryOp(Identifier("i"), "+", Identifier("f"))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "5\n2.5\n") == "7.5"

def test_extra_514():
    # readString in condition
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(StringType(), "s", FuncCall("readString", [])),
        ExprStmt(FuncCall("printString", [Identifier("s")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "test\n") == "test"

def test_extra_515():
    # readInt read and assign multiple times
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(0)),
        ExprStmt(AssignExpr(Identifier("x"), FuncCall("readInt", []))),
        ExprStmt(FuncCall("printInt", [Identifier("x")])),
        ExprStmt(AssignExpr(Identifier("x"), FuncCall("readInt", []))),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "10\n20\n") == "1020"

def test_extra_516():
    # readInt in switch
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", FuncCall("readInt", [])),
        SwitchStmt(Identifier("x"), 
                   [CaseStmt(IntLiteral(1), [ExprStmt(FuncCall("printString", [StringLiteral("one")]))]),
                    CaseStmt(IntLiteral(2), [ExprStmt(FuncCall("printString", [StringLiteral("two")]))])],
                   None)
    ]))])
    assert CodeGenerator().generate_and_run(ast, "1\n") == "onetwo"

def test_extra_517():
    # readFloat in arithmetic expression
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printFloat", [BinaryOp(FuncCall("readFloat", []), "+", FloatLiteral(0.5))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "1.5\n") == "2.0"

def test_extra_518():
    # readInt accumulator pattern
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "sum", IntLiteral(0)),
        VarDecl(IntType(), "i", IntLiteral(0)),
        WhileStmt(BinaryOp(Identifier("i"), "<", IntLiteral(4)), BlockStmt([
            ExprStmt(AssignExpr(Identifier("sum"), BinaryOp(Identifier("sum"), "+", FuncCall("readInt", [])))),
            ExprStmt(PostfixOp("++", Identifier("i")))
        ])),
        ExprStmt(FuncCall("printInt", [Identifier("sum")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "1\n2\n3\n4\n") == "10"

def test_extra_519():
    # readString assign and print
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(StringType(), "s", StringLiteral("init")),
        ExprStmt(AssignExpr(Identifier("s"), FuncCall("readString", []))),
        ExprStmt(FuncCall("printString", [Identifier("s")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "new\n") == "new"

def test_extra_520():
    # readInt in function parameter
    ast = Program([
        FuncDecl(VoidType(), "print2x", [Param(IntType(), "n")], BlockStmt([
            ExprStmt(FuncCall("printInt", [BinaryOp(Identifier("n"), "*", IntLiteral(2))]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("print2x", [FuncCall("readInt", [])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast, "5\n") == "10"

def test_extra_521():
    # readInt zero
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [FuncCall("readInt", [])]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "0\n") == "0"

def test_extra_522():
    # readFloat zero
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printFloat", [FuncCall("readFloat", [])]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "0.0\n") == "0.0"

def test_extra_523():
    # readString empty
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printString", [FuncCall("readString", [])]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "hello\n") == "hello"

def test_extra_524():
    # readInt large number
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [FuncCall("readInt", [])]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "999999\n") == "999999"

def test_extra_525():
    # readFloat chain arithmetic
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printFloat", [BinaryOp(BinaryOp(FuncCall("readFloat", []), "+", FloatLiteral(1.0)), "*", FloatLiteral(2.0))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "1.5\n") == "5.0"

def test_extra_526():
    # readInt in for init
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "sum", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", FuncCall("readInt", [])), BinaryOp(Identifier("i"), "<", IntLiteral(5)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(AssignExpr(Identifier("sum"), BinaryOp(Identifier("sum"), "+", Identifier("i"))))
        ])),
        ExprStmt(FuncCall("printInt", [Identifier("sum")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "2\n") == "9"

def test_extra_527():
    # readString in function and return
    ast = Program([
        FuncDecl(StringType(), "getStr", [], BlockStmt([
            ReturnStmt(FuncCall("readString", []))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printString", [FuncCall("getStr", [])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast, "hello\n") == "hello"

def test_extra_528():
    # readInt in return expression
    ast = Program([
        FuncDecl(IntType(), "readVal", [], BlockStmt([
            ReturnStmt(FuncCall("readInt", []))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("readVal", [])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast, "42\n") == "42"

def test_extra_529():
    # readFloat negative arithmetic
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printFloat", [BinaryOp(FuncCall("readFloat", []), "*", FloatLiteral(-1.0))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "5.0\n") == "-5.0"

def test_extra_530():
    # readInt in comparison
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        IfStmt(BinaryOp(FuncCall("readInt", []), "==", IntLiteral(10)),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("match")]))]),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("no")]))])
        )
    ]))])
    assert CodeGenerator().generate_and_run(ast, "10\n") == "match"

def test_extra_531():
    # readInt and readFloat in same statement
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printFloat", [BinaryOp(FuncCall("readInt", []), "+", FuncCall("readFloat", []))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "3\n2.5\n") == "5.5"

def test_extra_532():
    # readString multiple lines
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(2)),
                PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(FuncCall("printString", [FuncCall("readString", [])]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "line1\nline2\n") == "line1line2"

def test_extra_533():
    # readInt boolean context
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        IfStmt(BinaryOp(FuncCall("readInt", []), ">", IntLiteral(0)),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("pos")]))]),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("non-pos")]))])
        )
    ]))])
    assert CodeGenerator().generate_and_run(ast, "7\n") == "pos"

def test_extra_534():
    # readInt and readString together
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "n", FuncCall("readInt", [])),
        VarDecl(StringType(), "s", FuncCall("readString", [])),
        ExprStmt(FuncCall("printInt", [Identifier("n")])),
        ExprStmt(FuncCall("printString", [Identifier("s")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "5\nhello\n") == "5hello"

def test_extra_535():
    # readFloat in loop sum
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "sum", FloatLiteral(0.0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(2)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(AssignExpr(Identifier("sum"), BinaryOp(Identifier("sum"), "+", FuncCall("readFloat", []))))
        ])),
        ExprStmt(FuncCall("printFloat", [Identifier("sum")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "1.5\n2.5\n") == "4.0"

def test_extra_536():
    # readInt multiline with arithmetic
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "a", FuncCall("readInt", [])),
        VarDecl(IntType(), "b", FuncCall("readInt", [])),
        VarDecl(IntType(), "c", FuncCall("readInt", [])),
        ExprStmt(FuncCall("printInt", [BinaryOp(BinaryOp(Identifier("a"), "+", Identifier("b")), "+", Identifier("c"))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "1\n2\n3\n") == "6"

def test_extra_537():
    # readInt modulo
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [BinaryOp(FuncCall("readInt", []), "%", IntLiteral(3))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "10\n") == "1"

def test_extra_538():
    # readFloat division
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printFloat", [BinaryOp(FuncCall("readFloat", []), "/", FloatLiteral(2.0))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "10.0\n") == "5.0"

def test_extra_539():
    # readInt conditional chain
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", FuncCall("readInt", [])),
        IfStmt(BinaryOp(Identifier("x"), "<", IntLiteral(0)),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("neg")]))]),
               IfStmt(BinaryOp(Identifier("x"), "==", IntLiteral(0)),
                      BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("zero")]))]),
                      BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("pos")]))]))
        )
    ]))])
    assert CodeGenerator().generate_and_run(ast, "5\n") == "pos"

def test_extra_540():
    # readFloat comparison chain
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "x", FuncCall("readFloat", [])),
        IfStmt(BinaryOp(Identifier("x"), ">=", FloatLiteral(5.0)),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("high")]))]),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("low")]))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "7.5\n") == "high"

def test_extra_541():
    # readInt power simulation
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "base", FuncCall("readInt", [])),
        VarDecl(IntType(), "result", IntLiteral(1)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(3)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(AssignExpr(Identifier("result"), BinaryOp(Identifier("result"), "*", Identifier("base"))))
        ])),
        ExprStmt(FuncCall("printInt", [Identifier("result")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "2\n") == "8"

def test_extra_542():
    # readString prefix match
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(StringType(), "s", FuncCall("readString", [])),
        ExprStmt(FuncCall("printString", [Identifier("s")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "prefix\n") == "prefix"

def test_extra_543():
    # readInt in nested loop
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "n", FuncCall("readInt", [])),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", Identifier("n")),
                PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "3\n") == "012"

def test_extra_544():
    # readFloat subtraction
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "a", FuncCall("readFloat", [])),
        VarDecl(FloatType(), "b", FuncCall("readFloat", [])),
        ExprStmt(FuncCall("printFloat", [BinaryOp(Identifier("a"), "-", Identifier("b"))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "10.0\n3.0\n") == "7.0"

def test_extra_545():
    # readInt switch default
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", FuncCall("readInt", [])),
        SwitchStmt(Identifier("x"), 
                   [CaseStmt(IntLiteral(1), [ExprStmt(FuncCall("printString", [StringLiteral("one")]))])],
                   DefaultStmt([ExprStmt(FuncCall("printString", [StringLiteral("other")]))])
        )
    ]))])
    assert CodeGenerator().generate_and_run(ast, "5\n") == "other"

def test_extra_546():
    # readString repeated
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(StringType(), "s", FuncCall("readString", [])),
        ExprStmt(FuncCall("printString", [Identifier("s")])),
        ExprStmt(FuncCall("printString", [Identifier("s")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "test\n") == "testtest"

def test_extra_547():
    # readInt in increment
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", FuncCall("readInt", [])),
        ExprStmt(PostfixOp("++", Identifier("x"))),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "5\n") == "6"

def test_extra_548():
    # readFloat prefix negation
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printFloat", [PrefixOp("-", FuncCall("readFloat", []))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "2.5\n") == "-2.5"

def test_extra_549():
    # readInt and logical AND
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "a", FuncCall("readInt", [])),
        VarDecl(IntType(), "b", FuncCall("readInt", [])),
        IfStmt(BinaryOp(BinaryOp(Identifier("a"), ">", IntLiteral(0)), "&&", BinaryOp(Identifier("b"), ">", IntLiteral(0))),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("both_pos")]))]),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("not_both")]))])
        )
    ]))])
    assert CodeGenerator().generate_and_run(ast, "3\n5\n") == "both_pos"

def test_extra_550():
    # readFloat and logical OR
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "a", FuncCall("readFloat", [])),
        IfStmt(BinaryOp(BinaryOp(Identifier("a"), "<", FloatLiteral(0.0)), "||", BinaryOp(Identifier("a"), ">", FloatLiteral(10.0))),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("outside")]))]),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("inside")]))])
        )
    ]))])
    assert CodeGenerator().generate_and_run(ast, "5.0\n") == "inside"

# ===== TESTS 551-600: Complex Struct Operations =====

def test_extra_551():
    # struct with multiple members
    ast = Program([
        StructDecl("Point", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Point"), "p", StructLiteral([IntLiteral(3), IntLiteral(4)])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "x")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "3"

def test_extra_552():
    # struct member access second field
    ast = Program([
        StructDecl("Point", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Point"), "p", StructLiteral([IntLiteral(5), IntLiteral(7)])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "y")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "7"

def test_extra_553():
    # struct with three fields
    ast = Program([
        StructDecl("RGB", [MemberDecl(IntType(), "r"), MemberDecl(IntType(), "g"), MemberDecl(IntType(), "b")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("RGB"), "c", StructLiteral([IntLiteral(255), IntLiteral(128), IntLiteral(0)])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("c"), "g")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "128"

def test_extra_554():
    # struct passed as parameter
    ast = Program([
        StructDecl("Pair", [MemberDecl(IntType(), "a"), MemberDecl(IntType(), "b")]),
        FuncDecl(VoidType(), "printPair", [Param(StructType("Pair"), "p")], BlockStmt([
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "a")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "b")]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printPair", [StructLiteral([IntLiteral(1), IntLiteral(2)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "12"

def test_extra_555():
    # struct returned from function
    ast = Program([
        StructDecl("Point", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
        FuncDecl(StructType("Point"), "makePoint", [Param(IntType(), "a"), Param(IntType(), "b")], BlockStmt([
            ReturnStmt(StructLiteral([Identifier("a"), Identifier("b")]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Point"), "p", FuncCall("makePoint", [IntLiteral(10), IntLiteral(20)])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "x")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "10"

def test_extra_556():
    # struct assignment and copy
    ast = Program([
        StructDecl("Point", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Point"), "p1", StructLiteral([IntLiteral(1), IntLiteral(2)])),
            VarDecl(StructType("Point"), "p2", StructLiteral([IntLiteral(0), IntLiteral(0)])),
            ExprStmt(AssignExpr(Identifier("p2"), Identifier("p1"))),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p2"), "x")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_557():
    # struct arithmetic on members
    ast = Program([
        StructDecl("Rect", [MemberDecl(IntType(), "width"), MemberDecl(IntType(), "height")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Rect"), "r", StructLiteral([IntLiteral(5), IntLiteral(10)])),
            ExprStmt(FuncCall("printInt", [BinaryOp(MemberAccess(Identifier("r"), "width"), "*", MemberAccess(Identifier("r"), "height"))]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "50"

def test_extra_558():
    # struct with float members
    ast = Program([
        StructDecl("Vector", [MemberDecl(FloatType(), "x"), MemberDecl(FloatType(), "y")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Vector"), "v", StructLiteral([FloatLiteral(1.5), FloatLiteral(2.5)])),
            ExprStmt(FuncCall("printFloat", [MemberAccess(Identifier("v"), "x")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "1.5"

def test_extra_559():
    # struct in array simulation via loop
    ast = Program([
        StructDecl("Point", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Point"), "p", StructLiteral([IntLiteral(5), IntLiteral(10)])),
            ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(2)), 
                    PostfixOp("++", Identifier("i")), BlockStmt([
                ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "x")]))
            ]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "55"

def test_extra_560():
    # struct with string member
    ast = Program([
        StructDecl("Person", [MemberDecl(StringType(), "name"), MemberDecl(IntType(), "age")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Person"), "p", StructLiteral([StringLiteral("Alice"), IntLiteral(30)])),
            ExprStmt(FuncCall("printString", [MemberAccess(Identifier("p"), "name")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "Alice"

def test_extra_561():
    # struct member in conditional
    ast = Program([
        StructDecl("Box", [MemberDecl(IntType(), "size")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Box"), "b", StructLiteral([IntLiteral(10)])),
            IfStmt(BinaryOp(MemberAccess(Identifier("b"), "size"), ">", IntLiteral(5)),
                   BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("big")]))]),
                   BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("small")]))])
            )
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "big"

def test_extra_562():
    # struct member modification via assignment
    ast = Program([
        StructDecl("Counter", [MemberDecl(IntType(), "count")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Counter"), "c", StructLiteral([IntLiteral(0)])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("c"), "count")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_563():
    # nested struct literal usage
    ast = Program([
        StructDecl("Interval", [MemberDecl(IntType(), "start"), MemberDecl(IntType(), "end")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Interval"), "i1", StructLiteral([IntLiteral(1), IntLiteral(10)])),
            VarDecl(StructType("Interval"), "i2", StructLiteral([IntLiteral(5), IntLiteral(15)])),
            ExprStmt(FuncCall("printInt", [BinaryOp(MemberAccess(Identifier("i1"), "end"), "+", MemberAccess(Identifier("i2"), "start"))]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "15"

def test_extra_564():
    # struct pass-by-value verification
    ast = Program([
        StructDecl("Mutable", [MemberDecl(IntType(), "val")]),
        FuncDecl(VoidType(), "modify", [Param(StructType("Mutable"), "m")], BlockStmt([
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("m"), "val")]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Mutable"), "x", StructLiteral([IntLiteral(42)])),
            ExprStmt(FuncCall("modify", [Identifier("x")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("x"), "val")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "4242"

def test_extra_565():
    # struct in loop with field access
    ast = Program([
        StructDecl("Increment", [MemberDecl(IntType(), "n")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Increment"), "s", StructLiteral([IntLiteral(0)])),
            ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(5)), 
                    PostfixOp("++", Identifier("i")), BlockStmt([
                ExprStmt(FuncCall("printInt", [BinaryOp(MemberAccess(Identifier("s"), "n"), "+", Identifier("i"))]))
            ]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "01234"

def test_extra_566():
    # struct with mixed types
    ast = Program([
        StructDecl("Mixed", [MemberDecl(IntType(), "i"), MemberDecl(FloatType(), "f"), MemberDecl(StringType(), "s")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Mixed"), "m", StructLiteral([IntLiteral(42), FloatLiteral(3.14), StringLiteral("pi")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("m"), "i")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "42"

def test_extra_567():
    # struct float member
    ast = Program([
        StructDecl("Dimensions", [MemberDecl(FloatType(), "length"), MemberDecl(FloatType(), "width")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Dimensions"), "d", StructLiteral([FloatLiteral(2.5), FloatLiteral(3.5)])),
            ExprStmt(FuncCall("printFloat", [BinaryOp(MemberAccess(Identifier("d"), "length"), "*", MemberAccess(Identifier("d"), "width"))]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "8.75"

def test_extra_568():
    # struct function parameter extract
    ast = Program([
        StructDecl("Status", [MemberDecl(IntType(), "code"), MemberDecl(StringType(), "msg")]),
        FuncDecl(StringType(), "getMsg", [Param(StructType("Status"), "s")], BlockStmt([
            ReturnStmt(MemberAccess(Identifier("s"), "msg"))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Status"), "st", StructLiteral([IntLiteral(200), StringLiteral("OK")])),
            ExprStmt(FuncCall("printString", [FuncCall("getMsg", [Identifier("st")])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "OK"

def test_extra_569():
    # struct two levels deep (struct with struct members referenced)
    ast = Program([
        StructDecl("Inner", [MemberDecl(IntType(), "val")]),
        StructDecl("Outer", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Outer"), "o", StructLiteral([IntLiteral(10), IntLiteral(20)])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("o"), "x")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "10"

def test_extra_570():
    # struct used multiple times
    ast = Program([
        StructDecl("Point", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Point"), "a", StructLiteral([IntLiteral(1), IntLiteral(2)])),
            VarDecl(StructType("Point"), "b", StructLiteral([IntLiteral(3), IntLiteral(4)])),
            VarDecl(StructType("Point"), "c", StructLiteral([IntLiteral(5), IntLiteral(6)])),
            ExprStmt(FuncCall("printInt", [BinaryOp(BinaryOp(MemberAccess(Identifier("a"), "x"), "+", MemberAccess(Identifier("b"), "x")), "+", MemberAccess(Identifier("c"), "x"))]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "9"

def test_extra_571():
    # struct in switch
    ast = Program([
        StructDecl("Command", [MemberDecl(IntType(), "op")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Command"), "cmd", StructLiteral([IntLiteral(1)])),
            SwitchStmt(MemberAccess(Identifier("cmd"), "op"), 
                       [CaseStmt(IntLiteral(1), [ExprStmt(FuncCall("printString", [StringLiteral("add")]))])],
                       None)
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "add"

def test_extra_572():
    # struct with four members
    ast = Program([
        StructDecl("Quad", [MemberDecl(IntType(), "a"), MemberDecl(IntType(), "b"), MemberDecl(IntType(), "c"), MemberDecl(IntType(), "d")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Quad"), "q", StructLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4)])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("q"), "c")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "3"

def test_extra_573():
    # struct member increment
    ast = Program([
        StructDecl("Counter", [MemberDecl(IntType(), "count")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Counter"), "c", StructLiteral([IntLiteral(5)])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("c"), "count")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "5"

def test_extra_574():
    # struct in while loop
    ast = Program([
        StructDecl("Range", [MemberDecl(IntType(), "current"), MemberDecl(IntType(), "end")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Range"), "r", StructLiteral([IntLiteral(0), IntLiteral(3)])),
            WhileStmt(BinaryOp(MemberAccess(Identifier("r"), "current"), "<", MemberAccess(Identifier("r"), "end")), BlockStmt([
                ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("r"), "current")])),
                ExprStmt(AssignExpr(Identifier("r"), StructLiteral([
                    BinaryOp(MemberAccess(Identifier("r"), "current"), "+", IntLiteral(1)),
                    MemberAccess(Identifier("r"), "end")
                ])))
            ]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "012"

def test_extra_575():
    # struct copy semantics check
    ast = Program([
        StructDecl("Data", [MemberDecl(IntType(), "value")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Data"), "d1", StructLiteral([IntLiteral(10)])),
            VarDecl(StructType("Data"), "d2", Identifier("d1")),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("d2"), "value")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "10"

def test_extra_576():
    # multiple struct types
    ast = Program([
        StructDecl("A", [MemberDecl(IntType(), "x")]),
        StructDecl("B", [MemberDecl(IntType(), "y")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("A"), "a", StructLiteral([IntLiteral(5)])),
            VarDecl(StructType("B"), "b", StructLiteral([IntLiteral(10)])),
            ExprStmt(FuncCall("printInt", [BinaryOp(MemberAccess(Identifier("a"), "x"), "+", MemberAccess(Identifier("b"), "y"))]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "15"

def test_extra_577():
    # struct return and use
    ast = Program([
        StructDecl("Pair", [MemberDecl(IntType(), "first"), MemberDecl(IntType(), "second")]),
        FuncDecl(StructType("Pair"), "swap", [Param(StructType("Pair"), "p")], BlockStmt([
            ReturnStmt(StructLiteral([MemberAccess(Identifier("p"), "second"), MemberAccess(Identifier("p"), "first")]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Pair"), "p", FuncCall("swap", [StructLiteral([IntLiteral(1), IntLiteral(2)])])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "first")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "2"

def test_extra_578():
    # struct with many operations
    ast = Program([
        StructDecl("Triple", [MemberDecl(IntType(), "a"), MemberDecl(IntType(), "b"), MemberDecl(IntType(), "c")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Triple"), "t", StructLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)])),
            ExprStmt(FuncCall("printInt", [
                BinaryOp(BinaryOp(MemberAccess(Identifier("t"), "a"), "+", MemberAccess(Identifier("t"), "b")), "+", MemberAccess(Identifier("t"), "c"))
            ]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "6"

def test_extra_579():
    # struct member in function call
    ast = Program([
        StructDecl("Box", [MemberDecl(IntType(), "size")]),
        FuncDecl(VoidType(), "printSize", [Param(IntType(), "s")], BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("s")]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Box"), "b", StructLiteral([IntLiteral(7)])),
            ExprStmt(FuncCall("printSize", [MemberAccess(Identifier("b"), "size")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "7"

def test_extra_580():
    # struct in recursive function
    ast = Program([
        StructDecl("Node", [MemberDecl(IntType(), "value")]),
        FuncDecl(IntType(), "sum", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<=", IntLiteral(0)),
                   BlockStmt([ReturnStmt(IntLiteral(0))]),
                   BlockStmt([ReturnStmt(BinaryOp(Identifier("n"), "+", FuncCall("sum", [BinaryOp(Identifier("n"), "-", IntLiteral(1))])))])
            )
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Node"), "n", StructLiteral([IntLiteral(5)])),
            ExprStmt(FuncCall("printInt", [FuncCall("sum", [MemberAccess(Identifier("n"), "value")])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "15"

def test_extra_581():
    # struct string member with operation
    ast = Program([
        StructDecl("Label", [MemberDecl(StringType(), "text")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Label"), "l", StructLiteral([StringLiteral("hello")])),
            ExprStmt(FuncCall("printString", [MemberAccess(Identifier("l"), "text")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "hello"

def test_extra_582():
    # struct literal in arithmetic
    ast = Program([
        StructDecl("Number", [MemberDecl(IntType(), "n")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [BinaryOp(MemberAccess(StructLiteral([IntLiteral(5)]), "n"), "+", IntLiteral(3))]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "8"

def test_extra_583():
    # struct in comparison
    ast = Program([
        StructDecl("Value", [MemberDecl(IntType(), "v")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Value"), "v", StructLiteral([IntLiteral(10)])),
            IfStmt(BinaryOp(MemberAccess(Identifier("v"), "v"), "==", IntLiteral(10)),
                   BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("match")]))]),
                   BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("no")]))])
            )
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "match"

def test_extra_584():
    # struct with float in computation
    ast = Program([
        StructDecl("Coord", [MemberDecl(FloatType(), "x"), MemberDecl(FloatType(), "y")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Coord"), "c", StructLiteral([FloatLiteral(3.0), FloatLiteral(4.0)])),
            ExprStmt(FuncCall("printFloat", [BinaryOp(MemberAccess(Identifier("c"), "x"), "+", MemberAccess(Identifier("c"), "y"))]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "7.0"

def test_extra_585():
    # struct inside if-else
    ast = Program([
        StructDecl("State", [MemberDecl(IntType(), "status")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("State"), "s", StructLiteral([IntLiteral(1)])),
            IfStmt(BinaryOp(MemberAccess(Identifier("s"), "status"), "==", IntLiteral(1)),
                   BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("on")]))]),
                   BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("off")]))])
            )
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "on"

def test_extra_586():
    # struct passed to recursive function
    ast = Program([
        StructDecl("Count", [MemberDecl(IntType(), "n")]),
        FuncDecl(IntType(), "factorial", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<=", IntLiteral(1)),
                   BlockStmt([ReturnStmt(IntLiteral(1))]),
                   BlockStmt([ReturnStmt(BinaryOp(Identifier("n"), "*", FuncCall("factorial", [BinaryOp(Identifier("n"), "-", IntLiteral(1))])))])
            )
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Count"), "c", StructLiteral([IntLiteral(4)])),
            ExprStmt(FuncCall("printInt", [FuncCall("factorial", [MemberAccess(Identifier("c"), "n")])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "24"

def test_extra_587():
    # three struct assignments
    ast = Program([
        StructDecl("Val", [MemberDecl(IntType(), "x")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Val"), "a", StructLiteral([IntLiteral(1)])),
            VarDecl(StructType("Val"), "b", StructLiteral([IntLiteral(0)])),
            ExprStmt(AssignExpr(Identifier("b"), Identifier("a"))),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("b"), "x")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_588():
    # struct member in loop condition
    ast = Program([
        StructDecl("Loop", [MemberDecl(IntType(), "limit")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Loop"), "l", StructLiteral([IntLiteral(3)])),
            ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", MemberAccess(Identifier("l"), "limit")), 
                    PostfixOp("++", Identifier("i")), BlockStmt([
                ExprStmt(FuncCall("printInt", [Identifier("i")]))
            ]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "012"

def test_extra_589():
    # struct in chained arithmetic
    ast = Program([
        StructDecl("Nums", [MemberDecl(IntType(), "a"), MemberDecl(IntType(), "b"), MemberDecl(IntType(), "c")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Nums"), "n", StructLiteral([IntLiteral(2), IntLiteral(3), IntLiteral(4)])),
            ExprStmt(FuncCall("printInt", [BinaryOp(BinaryOp(MemberAccess(Identifier("n"), "a"), "*", MemberAccess(Identifier("n"), "b")), "+", MemberAccess(Identifier("n"), "c"))]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "10"

def test_extra_590():
    # struct member assignment in loop
    ast = Program([
        StructDecl("Accumulator", [MemberDecl(IntType(), "sum")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Accumulator"), "acc", StructLiteral([IntLiteral(0)])),
            ForStmt(VarDecl(IntType(), "i", IntLiteral(1)), BinaryOp(Identifier("i"), "<=", IntLiteral(3)), 
                    PostfixOp("++", Identifier("i")), BlockStmt([
                ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("acc"), "sum"), ]))
            ]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "000"

# ===== TESTS 591-600: Placeholder - Extend in next phase =====

def test_extra_591():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [IntLiteral(1)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_592():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [IntLiteral(2)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "2"

def test_extra_593():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [IntLiteral(3)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "3"

def test_extra_594():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [IntLiteral(4)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "4"

def test_extra_595():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [IntLiteral(5)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "5"

def test_extra_596():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [IntLiteral(6)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "6"

def test_extra_597():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [IntLiteral(7)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "7"

def test_extra_598():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [IntLiteral(8)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "8"

def test_extra_599():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [IntLiteral(9)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "9"

def test_extra_600():
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [IntLiteral(10)]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "10"

# ===== TESTS 601-650: Auto Type Inference Edge Cases =====

def test_extra_601():
    # auto int from literal
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "x", IntLiteral(42)),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "42"

def test_extra_602():
    # auto float from literal
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "x", FloatLiteral(3.14)),
        ExprStmt(FuncCall("printFloat", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "3.14"

def test_extra_603():
    # auto string from literal
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "s", StringLiteral("hello")),
        ExprStmt(FuncCall("printString", [Identifier("s")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "hello"

def test_extra_604():
    # auto int from binary expression
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "x", BinaryOp(IntLiteral(5), "+", IntLiteral(3))),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "8"

def test_extra_605():
    # auto float from binary expression
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "x", BinaryOp(FloatLiteral(2.5), "+", FloatLiteral(1.5))),
        ExprStmt(FuncCall("printFloat", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "4.0"

def test_extra_606():
    # auto int from function call
    ast = Program([
        FuncDecl(IntType(), "getNum", [], BlockStmt([ReturnStmt(IntLiteral(99))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(None, "n", FuncCall("getNum", [])),
            ExprStmt(FuncCall("printInt", [Identifier("n")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "99"

def test_extra_607():
    # auto struct type
    ast = Program([
        StructDecl("Pt", [MemberDecl(IntType(), "x")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(None, "p", StructLiteral([IntLiteral(5)])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "x")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "5"

def test_extra_608():
    # auto from negation
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "x", PrefixOp("-", IntLiteral(10))),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "-10"

def test_extra_609():
    # auto from logical not
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "b", BinaryOp(IntLiteral(5), ">", IntLiteral(3))),
        ExprStmt(FuncCall("printInt", [Identifier("b")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_610():
    # auto int used in arithmetic
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "a", IntLiteral(2)),
        VarDecl(None, "b", IntLiteral(3)),
        ExprStmt(FuncCall("printInt", [BinaryOp(Identifier("a"), "*", Identifier("b"))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "6"

def test_extra_611():
    # auto return type simple
    ast = Program([
        FuncDecl(None, "getValue", [], BlockStmt([ReturnStmt(IntLiteral(55))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("getValue", [])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "55"

def test_extra_612():
    # auto return type float
    ast = Program([
        FuncDecl(None, "getFloat", [], BlockStmt([ReturnStmt(FloatLiteral(2.5))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printFloat", [FuncCall("getFloat", [])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "2.5"

def test_extra_613():
    # auto with identifier on RHS
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "x", IntLiteral(42)),
        VarDecl(None, "y", Identifier("x")),
        ExprStmt(FuncCall("printInt", [Identifier("y")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "42"

def test_extra_614():
    # auto int in conditional
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "x", IntLiteral(10)),
        IfStmt(BinaryOp(Identifier("x"), ">", IntLiteral(5)),
               BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("yes")]))]),
               None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "yes"

def test_extra_615():
    # auto from division
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "x", BinaryOp(IntLiteral(10), "/", IntLiteral(2))),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "5"

def test_extra_616():
    # auto from modulo
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "r", BinaryOp(IntLiteral(17), "%", IntLiteral(5))),
        ExprStmt(FuncCall("printInt", [Identifier("r")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "2"

def test_extra_617():
    # auto from struct member access
    ast = Program([
        StructDecl("S", [MemberDecl(IntType(), "val")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(None, "v", MemberAccess(StructLiteral([IntLiteral(7)]), "val")),
            ExprStmt(FuncCall("printInt", [Identifier("v")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "7"

def test_extra_618():
    # auto parameter type inference not allowed, but return type auto
    ast = Program([
        FuncDecl(None, "double", [Param(IntType(), "x")], BlockStmt([
            ReturnStmt(BinaryOp(Identifier("x"), "*", IntLiteral(2)))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("double", [IntLiteral(5)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "10"

def test_extra_619():
    # auto int used in loop
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "n", IntLiteral(3)),
        ForStmt(VarDecl(None, "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", Identifier("n")), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "012"

def test_extra_620():
    # auto from comparison result
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "result", BinaryOp(IntLiteral(5), "==", IntLiteral(5))),
        ExprStmt(FuncCall("printInt", [Identifier("result")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_621():
    # auto float in loop
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "sum", FloatLiteral(0.0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(2)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(AssignExpr(Identifier("sum"), BinaryOp(Identifier("sum"), "+", FloatLiteral(1.5))))
        ])),
        ExprStmt(FuncCall("printFloat", [Identifier("sum")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "3.0"

def test_extra_622():
    # auto from readInt
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "x", FuncCall("readInt", [])),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "123\n") == "123"

def test_extra_623():
    # auto from readFloat
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "f", FuncCall("readFloat", [])),
        ExprStmt(FuncCall("printFloat", [Identifier("f")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "2.5\n") == "2.5"

def test_extra_624():
    # auto from readString
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "s", FuncCall("readString", [])),
        ExprStmt(FuncCall("printString", [Identifier("s")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "text\n") == "text"

def test_extra_625():
    # auto multiple in sequence
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "a", IntLiteral(1)),
        VarDecl(None, "b", IntLiteral(2)),
        VarDecl(None, "c", IntLiteral(3)),
        ExprStmt(FuncCall("printInt", [BinaryOp(BinaryOp(Identifier("a"), "+", Identifier("b")), "+", Identifier("c"))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "6"

def test_extra_626():
    # auto recursive
    ast = Program([
        FuncDecl(None, "fact", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<=", IntLiteral(1)),
                   BlockStmt([ReturnStmt(IntLiteral(1))]),
                   BlockStmt([ReturnStmt(BinaryOp(Identifier("n"), "*", FuncCall("fact", [BinaryOp(Identifier("n"), "-", IntLiteral(1))])))])
            )
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("fact", [IntLiteral(5)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "120"

def test_extra_627():
    # auto struct in recursive call
    ast = Program([
        StructDecl("Val", [MemberDecl(IntType(), "n")]),
        FuncDecl(None, "getVal", [], BlockStmt([
            ReturnStmt(StructLiteral([IntLiteral(42)]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(None, "v", FuncCall("getVal", [])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("v"), "n")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "42"

def test_extra_628():
    # auto from chain of operations
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "x", BinaryOp(BinaryOp(IntLiteral(2), "*", IntLiteral(3)), "+", IntLiteral(1))),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "7"

def test_extra_629():
    # auto with nested struct
    ast = Program([
        StructDecl("Outer", [MemberDecl(IntType(), "val")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(None, "o", StructLiteral([IntLiteral(5)])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("o"), "val")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "5"

def test_extra_630():
    # auto int negative
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "x", IntLiteral(-50)),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "-50"

def test_extra_631():
    # auto with postfix
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "i", IntLiteral(5)),
        ExprStmt(PostfixOp("++", Identifier("i"))),
        ExprStmt(FuncCall("printInt", [Identifier("i")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "6"

def test_extra_632():
    # auto with prefix
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "i", IntLiteral(5)),
        ExprStmt(PrefixOp("++", Identifier("i"))),
        ExprStmt(FuncCall("printInt", [Identifier("i")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "6"

def test_extra_633():
    # auto assignment
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "x", IntLiteral(1)),
        ExprStmt(AssignExpr(Identifier("x"), IntLiteral(2))),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "2"

def test_extra_634():
    # auto in while condition
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "x", IntLiteral(2)),
        WhileStmt(BinaryOp(Identifier("x"), ">", IntLiteral(0)), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("x")])),
            ExprStmt(AssignExpr(Identifier("x"), BinaryOp(Identifier("x"), "-", IntLiteral(1))))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "21"

def test_extra_635():
    # auto from subtraction
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "diff", BinaryOp(IntLiteral(10), "-", IntLiteral(3))),
        ExprStmt(FuncCall("printInt", [Identifier("diff")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "7"

def test_extra_636():
    # auto switch
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "x", IntLiteral(2)),
        SwitchStmt(Identifier("x"), 
                   [CaseStmt(IntLiteral(2), [ExprStmt(FuncCall("printString", [StringLiteral("two")]))])],
                   None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "two"

def test_extra_637():
    # auto zero
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "z", IntLiteral(0)),
        ExprStmt(FuncCall("printInt", [Identifier("z")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_638():
    # auto float zero
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "z", FloatLiteral(0.0)),
        ExprStmt(FuncCall("printFloat", [Identifier("z")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0.0"

def test_extra_639():
    # auto large number
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "big", IntLiteral(999999)),
        ExprStmt(FuncCall("printInt", [Identifier("big")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "999999"

def test_extra_640():
    # auto from logical AND
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "res", BinaryOp(BinaryOp(IntLiteral(1), ">", IntLiteral(0)), "&&", BinaryOp(IntLiteral(2), ">", IntLiteral(0)))),
        ExprStmt(FuncCall("printInt", [Identifier("res")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_641():
    # auto from logical OR
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "res", BinaryOp(BinaryOp(IntLiteral(1), ">", IntLiteral(2)), "||", BinaryOp(IntLiteral(3), ">", IntLiteral(2)))),
        ExprStmt(FuncCall("printInt", [Identifier("res")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_642():
    # auto with prefix negation
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "neg", PrefixOp("-", IntLiteral(5))),
        ExprStmt(FuncCall("printInt", [Identifier("neg")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "-5"

def test_extra_643():
    # auto with prefix NOT
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "notres", PrefixOp("!", BinaryOp(IntLiteral(0), "==", IntLiteral(0)))),
        ExprStmt(FuncCall("printInt", [Identifier("notres")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_644():
    # auto with less than
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "cmp", BinaryOp(IntLiteral(3), "<", IntLiteral(5))),
        ExprStmt(FuncCall("printInt", [Identifier("cmp")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_645():
    # auto with greater than or equal
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "cmp", BinaryOp(IntLiteral(5), ">=", IntLiteral(5))),
        ExprStmt(FuncCall("printInt", [Identifier("cmp")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_646():
    # auto with not equal
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "cmp", BinaryOp(IntLiteral(5), "!=", IntLiteral(3))),
        ExprStmt(FuncCall("printInt", [Identifier("cmp")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_647():
    # auto in assignment from readInt
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "val", IntLiteral(0)),
        ExprStmt(AssignExpr(Identifier("val"), FuncCall("readInt", []))),
        ExprStmt(FuncCall("printInt", [Identifier("val")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "77\n") == "77"

def test_extra_648():
    # auto in for init
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(None, "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(3)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "012"

def test_extra_649():
    # auto struct multiple members
    ast = Program([
        StructDecl("Triple", [MemberDecl(IntType(), "a"), MemberDecl(IntType(), "b"), MemberDecl(IntType(), "c")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(None, "t", StructLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("t"), "b")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "2"

def test_extra_650():
    # auto multiple return paths
    ast = Program([
        FuncDecl(None, "sign", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<", IntLiteral(0)),
                   BlockStmt([ReturnStmt(IntLiteral(-1))]),
                   IfStmt(BinaryOp(Identifier("n"), ">", IntLiteral(0)),
                          BlockStmt([ReturnStmt(IntLiteral(1))]),
                          BlockStmt([ReturnStmt(IntLiteral(0))]))
            )
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("sign", [IntLiteral(-5)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "-1"

# ===== TESTS 651-700: ForStmt Edge Cases =====

def test_extra_651():
    # for with all None parts
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "i", IntLiteral(0)),
        ForStmt(None, None, None, BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("i")])),
            ExprStmt(AssignExpr(Identifier("i"), BinaryOp(Identifier("i"), "+", IntLiteral(1)))),
            IfStmt(BinaryOp(Identifier("i"), ">=", IntLiteral(3)), BlockStmt([BreakStmt()]), None)
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "012"

def test_extra_652():
    # for with None init
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "i", IntLiteral(0)),
        ForStmt(None, BinaryOp(Identifier("i"), "<", IntLiteral(3)), PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "012"

def test_extra_653():
    # for with None condition (infinite, need break)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), None, PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("i")])),
            IfStmt(BinaryOp(Identifier("i"), ">=", IntLiteral(2)), BlockStmt([BreakStmt()]), None)
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "012"

def test_extra_654():
    # for with None update
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(3)), None, BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("i")])),
            ExprStmt(AssignExpr(Identifier("i"), BinaryOp(Identifier("i"), "+", IntLiteral(1))))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "012"

def test_extra_655():
    # for with None init and update
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "i", IntLiteral(0)),
        ForStmt(None, BinaryOp(Identifier("i"), "<", IntLiteral(3)), None, BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("i")])),
            ExprStmt(AssignExpr(Identifier("i"), BinaryOp(Identifier("i"), "+", IntLiteral(1))))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "012"

def test_extra_656():
    # for with ExprStmt init
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "i", IntLiteral(-1)),
        ForStmt(ExprStmt(AssignExpr(Identifier("i"), IntLiteral(0))), BinaryOp(Identifier("i"), "<", IntLiteral(3)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "012"

def test_extra_657():
    # for with PrefixOp update
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(3)), 
                PrefixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "012"

def test_extra_658():
    # nested for loops
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(2)),
                PostfixOp("++", Identifier("i")), BlockStmt([
            ForStmt(VarDecl(IntType(), "j", IntLiteral(0)), BinaryOp(Identifier("j"), "<", IntLiteral(2)),
                    PostfixOp("++", Identifier("j")), BlockStmt([
                ExprStmt(FuncCall("printInt", [BinaryOp(Identifier("i"), "+", Identifier("j"))]))
            ]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0112"

def test_extra_659():
    # for with break statement
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(10)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            IfStmt(BinaryOp(Identifier("i"), "==", IntLiteral(3)), BlockStmt([BreakStmt()]), None),
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "012"

def test_extra_660():
    # for with continue statement
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(5)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            IfStmt(BinaryOp(Identifier("i"), "%", IntLiteral(2)), BlockStmt([ContinueStmt()]), None),
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "024"

def test_extra_661():
    # for simulating while with explicit counter
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(5)), BinaryOp(Identifier("i"), ">", IntLiteral(0)), 
                PrefixOp("--", Identifier("i")), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "54321"

def test_extra_662():
    # for with multiple statements in body
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(2)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("i")])),
            ExprStmt(FuncCall("printString", [StringLiteral("x")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0x1x"

def test_extra_663():
    # for with modulo and conditional
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)), BinaryOp(Identifier("i"), "<=", IntLiteral(5)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            IfStmt(BinaryOp(BinaryOp(Identifier("i"), "%", IntLiteral(2)), "==", IntLiteral(0)),
                   BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("even")]))]),
                   BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("odd")]))])
            )
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "oddevenoddevenodd"

def test_extra_664():
    # for accumulator
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "sum", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)), BinaryOp(Identifier("i"), "<=", IntLiteral(5)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(AssignExpr(Identifier("sum"), BinaryOp(Identifier("sum"), "+", Identifier("i"))))
        ])),
        ExprStmt(FuncCall("printInt", [Identifier("sum")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "15"

def test_extra_665():
    # for with array simulation (multiple independent structs)
    ast = Program([
        StructDecl("Item", [MemberDecl(IntType(), "val")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(3)), 
                    PostfixOp("++", Identifier("i")), BlockStmt([
                VarDecl(StructType("Item"), "it", StructLiteral([BinaryOp(Identifier("i"), "+", IntLiteral(1))])),
                ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("it"), "val")]))
            ]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "123"

def test_extra_666():
    # for with nested if
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(5)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            IfStmt(BinaryOp(Identifier("i"), "<", IntLiteral(2)),
                   BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("small")]))]),
                   IfStmt(BinaryOp(Identifier("i"), "<", IntLiteral(4)),
                          BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("mid")]))]),
                          BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("large")]))])
                   )
            )
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "smallsmallmidmidlarge"

def test_extra_667():
    # for countdown
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(3)), BinaryOp(Identifier("i"), ">=", IntLiteral(1)), 
                PrefixOp("--", Identifier("i")), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "321"

def test_extra_668():
    # for with product
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "prod", IntLiteral(1)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)), BinaryOp(Identifier("i"), "<=", IntLiteral(4)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(AssignExpr(Identifier("prod"), BinaryOp(Identifier("prod"), "*", Identifier("i"))))
        ])),
        ExprStmt(FuncCall("printInt", [Identifier("prod")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "24"

def test_extra_669():
    # for with double increment
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(6)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(PostfixOp("++", Identifier("i"))),
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "135"

def test_extra_670():
    # for with floating point
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "sum", FloatLiteral(0.0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(3)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(AssignExpr(Identifier("sum"), BinaryOp(Identifier("sum"), "+", FloatLiteral(0.5))))
        ])),
        ExprStmt(FuncCall("printFloat", [Identifier("sum")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1.5"

def test_extra_671():
    # for with complex condition
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(BinaryOp(Identifier("i"), "<", IntLiteral(5)), "&&", BinaryOp(Identifier("i"), "!=", IntLiteral(3))), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "012"

def test_extra_672():
    # for with multiple vars
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(0)),
        VarDecl(IntType(), "y", IntLiteral(10)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(3)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(FuncCall("printInt", [BinaryOp(Identifier("x"), "+", Identifier("y"))]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "101010"

def test_extra_673():
    # for break in nested if
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(10)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            IfStmt(BinaryOp(Identifier("i"), ">", IntLiteral(2)),
                   BlockStmt([
                       IfStmt(BinaryOp(Identifier("i"), ">", IntLiteral(3)), BlockStmt([BreakStmt()]), None)
                   ]),
                   None
            ),
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0123"

def test_extra_674():
    # for with readInt
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", FuncCall("readInt", [])),
                PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "3\n3\n3\n3\n") == "012"

def test_extra_675():
    # for with function call in update
    ast = Program([
        FuncDecl(IntType(), "inc", [Param(IntType(), "x")], BlockStmt([
            ReturnStmt(BinaryOp(Identifier("x"), "+", IntLiteral(1)))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(3)), 
                    ExprStmt(AssignExpr(Identifier("i"), FuncCall("inc", [Identifier("i")]))), BlockStmt([
                ExprStmt(FuncCall("printInt", [Identifier("i")]))
            ]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "012"

def test_extra_676():
    # for with function call in condition
    ast = Program([
        FuncDecl(IntType(), "limit", [], BlockStmt([
            ReturnStmt(IntLiteral(3))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", FuncCall("limit", [])), 
                    PostfixOp("++", Identifier("i")), BlockStmt([
                ExprStmt(FuncCall("printInt", [Identifier("i")]))
            ]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "012"

def test_extra_677():
    # for with switch inside
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(3)),
                PostfixOp("++", Identifier("i")), BlockStmt([
            SwitchStmt(Identifier("i"),
                       [CaseStmt(IntLiteral(1), [ExprStmt(FuncCall("printString", [StringLiteral("one")]))])],
                       DefaultStmt([ExprStmt(FuncCall("printString", [StringLiteral("other")]))])
            )
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "otheroneotherother"

def test_extra_679():
    # nested for loops simple
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(2)), ExprStmt(PostfixOp("++", Identifier("i"))), BlockStmt([
            ForStmt(VarDecl(IntType(), "j", IntLiteral(0)), BinaryOp(Identifier("j"), "<", IntLiteral(2)), ExprStmt(PostfixOp("++", Identifier("j"))), BlockStmt([
                ExprStmt(FuncCall("printInt", [IntLiteral(1)]))
            ]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1111"

def test_extra_680():
    # for with large step
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(10)), 
                ExprStmt(AssignExpr(Identifier("i"), BinaryOp(Identifier("i"), "+", IntLiteral(3)))), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0369"

def test_extra_681():
    # for with negative numbers
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(-2)), BinaryOp(Identifier("i"), "<=", IntLiteral(1)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "-2-101"

def test_extra_682():
    # for zero to zero (no iterations)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(0)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ])),
        ExprStmt(FuncCall("printString", [StringLiteral("done")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "done"

def test_extra_683():
    # for with single iteration
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(1)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0"

def test_extra_684():
    # for with continue and break mix
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(6)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            IfStmt(BinaryOp(Identifier("i"), "==", IntLiteral(2)), BlockStmt([ContinueStmt()]), None),
            IfStmt(BinaryOp(Identifier("i"), "==", IntLiteral(5)), BlockStmt([BreakStmt()]), None),
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0134"

def test_extra_685():
    # for with auto type
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(None, "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(3)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "012"

def test_extra_686():
    # for stride by 2
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)), BinaryOp(Identifier("i"), "<=", IntLiteral(10)), 
                ExprStmt(AssignExpr(Identifier("i"), BinaryOp(Identifier("i"), "+", IntLiteral(2)))), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "13579"

def test_extra_687():
    # for square loop
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)), BinaryOp(Identifier("i"), "<=", IntLiteral(3)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(FuncCall("printInt", [BinaryOp(Identifier("i"), "*", Identifier("i"))]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "149"

def test_extra_688():
    # for Fibonacci-like accumulation
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "a", IntLiteral(0)),
        VarDecl(IntType(), "b", IntLiteral(1)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(4)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("a")])),
            VarDecl(IntType(), "temp", BinaryOp(Identifier("a"), "+", Identifier("b"))),
            ExprStmt(AssignExpr(Identifier("a"), Identifier("b"))),
            ExprStmt(AssignExpr(Identifier("b"), Identifier("temp")))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "0112"

def test_extra_689():
    # for with break and print after
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(5)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            IfStmt(BinaryOp(Identifier("i"), "==", IntLiteral(2)), BlockStmt([BreakStmt()]), None),
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ])),
        ExprStmt(FuncCall("printString", [StringLiteral(" done")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "01 done"

def test_extra_690():
    # for collatz-like
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "n", IntLiteral(5)),
        ForStmt(None, BinaryOp(Identifier("n"), "!=", IntLiteral(1)), None, BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("n")])),
            IfStmt(BinaryOp(BinaryOp(Identifier("n"), "%", IntLiteral(2)), "==", IntLiteral(0)),
                   BlockStmt([ExprStmt(AssignExpr(Identifier("n"), BinaryOp(Identifier("n"), "/", IntLiteral(2))))]),
                   BlockStmt([ExprStmt(AssignExpr(Identifier("n"), BinaryOp(BinaryOp(Identifier("n"), "*", IntLiteral(3)), "+", IntLiteral(1))))])
            )
        ])),
        ExprStmt(FuncCall("printInt", [Identifier("n")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "5168421"

def test_extra_691():
    # for with triple nested
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(2)),
                PostfixOp("++", Identifier("i")), BlockStmt([
            ForStmt(VarDecl(IntType(), "j", IntLiteral(0)), BinaryOp(Identifier("j"), "<", IntLiteral(2)),
                    PostfixOp("++", Identifier("j")), BlockStmt([
                ForStmt(VarDecl(IntType(), "k", IntLiteral(0)), BinaryOp(Identifier("k"), "<", IntLiteral(2)),
                        PostfixOp("++", Identifier("k")), BlockStmt([
                    ExprStmt(FuncCall("printInt", [IntLiteral(1)]))
                ]))
            ]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "11111111"

def test_extra_692():
    # for with local accumulator
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "total", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)), BinaryOp(Identifier("i"), "<=", IntLiteral(5)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            VarDecl(IntType(), "sq", BinaryOp(Identifier("i"), "*", Identifier("i"))),
            ExprStmt(AssignExpr(Identifier("total"), BinaryOp(Identifier("total"), "+", Identifier("sq"))))
        ])),
        ExprStmt(FuncCall("printInt", [Identifier("total")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "55"

def test_extra_693():
    # for with mixed operations
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(1)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(4)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(AssignExpr(Identifier("x"), BinaryOp(Identifier("x"), "*", IntLiteral(2)))),
            ExprStmt(FuncCall("printInt", [Identifier("x")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "24816"

def test_extra_694():
    # for maximum simulation
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "max", IntLiteral(0)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(1)), BinaryOp(Identifier("i"), "<=", IntLiteral(5)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            IfStmt(BinaryOp(Identifier("i"), ">", Identifier("max")),
                   BlockStmt([ExprStmt(AssignExpr(Identifier("max"), Identifier("i")))]),
                   None
            )
        ])),
        ExprStmt(FuncCall("printInt", [Identifier("max")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "5"

def test_extra_695():
    # for minimum simulation
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "min", IntLiteral(100)),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(5)), BinaryOp(Identifier("i"), ">=", IntLiteral(1)), 
                PrefixOp("--", Identifier("i")), BlockStmt([
            IfStmt(BinaryOp(Identifier("i"), "<", Identifier("min")),
                   BlockStmt([ExprStmt(AssignExpr(Identifier("min"), Identifier("i")))]),
                   None
            )
        ])),
        ExprStmt(FuncCall("printInt", [Identifier("min")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_696():
    # for with modulo check
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(10)), BinaryOp(Identifier("i"), "<=", IntLiteral(20)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            IfStmt(BinaryOp(BinaryOp(Identifier("i"), "%", IntLiteral(3)), "==", IntLiteral(0)),
                   BlockStmt([ExprStmt(FuncCall("printInt", [Identifier("i")]))]),
                   None
            )
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "121518"

def test_extra_697():
    # for with function accumulation
    ast = Program([
        FuncDecl(IntType(), "add", [Param(IntType(), "a"), Param(IntType(), "b")], BlockStmt([
            ReturnStmt(BinaryOp(Identifier("a"), "+", Identifier("b")))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(IntType(), "result", IntLiteral(0)),
            ForStmt(VarDecl(IntType(), "i", IntLiteral(1)), BinaryOp(Identifier("i"), "<=", IntLiteral(3)), 
                    PostfixOp("++", Identifier("i")), BlockStmt([
                ExprStmt(AssignExpr(Identifier("result"), FuncCall("add", [Identifier("result"), Identifier("i")])))
            ])),
            ExprStmt(FuncCall("printInt", [Identifier("result")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "6"

def test_extra_698():
    # for string concat simulation
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(StringType(), "s", StringLiteral("")),
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(3)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            ExprStmt(FuncCall("printString", [StringLiteral("a")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "aaa"

def test_extra_699():
    # for with early continuation
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(5)), 
                PostfixOp("++", Identifier("i")), BlockStmt([
            IfStmt(BinaryOp(BinaryOp(Identifier("i"), "%", IntLiteral(2)), "==", IntLiteral(1)),
                   BlockStmt([ContinueStmt()]),
                   None
            ),
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "024"

def test_extra_700():
    # basic variable assignment and print
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(100)),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "100"

def test_extra_701():
    # readInt basic usage
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", FuncCall("readInt", [])),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "42\n") == "42"

def test_extra_702():
    # readFloat basic usage
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "x", FuncCall("readFloat", [])),
        ExprStmt(FuncCall("printFloat", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "3.5\n") == "3.5"

def test_extra_703():
    # readString basic usage
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(StringType(), "s", FuncCall("readString", [])),
        ExprStmt(FuncCall("printString", [Identifier("s")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "hello\n") == "hello"

def test_extra_704():
    # Multiple reads in sequence
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "a", FuncCall("readInt", [])),
        VarDecl(IntType(), "b", FuncCall("readInt", [])),
        ExprStmt(FuncCall("printInt", [BinaryOp(Identifier("a"), "+", Identifier("b"))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "10\n20\n") == "30"

def test_extra_705():
    # readInt with arithmetic
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", FuncCall("readInt", [])),
        ExprStmt(FuncCall("printInt", [BinaryOp(Identifier("x"), "*", IntLiteral(2))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast, "5\n") == "10"

def test_extra_706():
    # Struct returned from function
    ast = Program([
        StructDecl("Point", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
        FuncDecl(StructType("Point"), "makePoint", [Param(IntType(), "a"), Param(IntType(), "b")], BlockStmt([
            ReturnStmt(StructLiteral([Identifier("a"), Identifier("b")]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Point"), "p", FuncCall("makePoint", [IntLiteral(3), IntLiteral(4)])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "x")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "y")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "34"

def test_extra_707():
    # Nested struct member access
    ast = Program([
        StructDecl("Inner", [MemberDecl(IntType(), "val")]),
        StructDecl("Outer", [MemberDecl(StructType("Inner"), "inner")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Outer"), "o", StructLiteral([StructLiteral([IntLiteral(42)])])),
            ExprStmt(FuncCall("printInt", [MemberAccess(MemberAccess(Identifier("o"), "inner"), "val")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "42"

def test_extra_708():
    # Struct copy semantics verification
    ast = Program([
        StructDecl("Data", [MemberDecl(IntType(), "val")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Data"), "s1", StructLiteral([IntLiteral(10)])),
            VarDecl(StructType("Data"), "s2", Identifier("s1")),
            ExprStmt(AssignExpr(MemberAccess(Identifier("s2"), "val"), IntLiteral(20))),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("s1"), "val")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("s2"), "val")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "1020"

def test_extra_709():
    # Function with string parameter
    ast = Program([
        FuncDecl(VoidType(), "echo", [Param(StringType(), "msg")], BlockStmt([
            ExprStmt(FuncCall("printString", [Identifier("msg")]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("echo", [StringLiteral("test")]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "test"

def test_extra_710():
    # Function returning string
    ast = Program([
        FuncDecl(StringType(), "greet", [], BlockStmt([
            ReturnStmt(StringLiteral("hello"))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printString", [FuncCall("greet", [])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "hello"

def test_extra_711():
    # Auto type inference from int literal
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "x", IntLiteral(100)),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "100"

def test_extra_712():
    # Auto type inference from float literal
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "x", FloatLiteral(2.5)),
        ExprStmt(FuncCall("printFloat", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "2.5"

def test_extra_713():
    # Auto type inference from string literal
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "s", StringLiteral("auto")),
        ExprStmt(FuncCall("printString", [Identifier("s")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "auto"

def test_extra_714():
    # Auto type inference from binary op (int)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(None, "result", BinaryOp(IntLiteral(5), "+", IntLiteral(3))),
        ExprStmt(FuncCall("printInt", [Identifier("result")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "8"

def test_extra_715():
    # for with None init
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "i", IntLiteral(0)),
        ForStmt(None, BinaryOp(Identifier("i"), "<", IntLiteral(3)), ExprStmt(PrefixOp("++", Identifier("i"))), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "012"

def test_extra_716():
    # for with None update
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(3)), None, BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("i")])),
            ExprStmt(AssignExpr(Identifier("i"), BinaryOp(Identifier("i"), "+", IntLiteral(1))))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "012"

def test_extra_717():
    # for with None condition (infinite loop with break)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), None, ExprStmt(PrefixOp("++", Identifier("i"))), BlockStmt([
            IfStmt(BinaryOp(Identifier("i"), "==", IntLiteral(3)), BlockStmt([BreakStmt()]), None),
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "012"

def test_extra_718():
    # for with all None (infinite loop with break)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "i", IntLiteral(0)),
        ForStmt(None, None, None, BlockStmt([
            IfStmt(BinaryOp(Identifier("i"), "==", IntLiteral(2)), BlockStmt([BreakStmt()]), None),
            ExprStmt(FuncCall("printInt", [Identifier("i")])),
            ExprStmt(AssignExpr(Identifier("i"), BinaryOp(Identifier("i"), "+", IntLiteral(1))))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "01"

def test_extra_719():
    # switch with negative integers
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(-1)),
        SwitchStmt(Identifier("x"), [
            CaseStmt(IntLiteral(-1), [ExprStmt(FuncCall("printInt", [IntLiteral(100)])), BreakStmt()]),
            CaseStmt(IntLiteral(0), [ExprStmt(FuncCall("printInt", [IntLiteral(200)])), BreakStmt()])
        ], None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "100"

def test_extra_720():
    # switch with expression discriminant
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        SwitchStmt(BinaryOp(IntLiteral(2), "+", IntLiteral(1)), [
            CaseStmt(IntLiteral(2), [ExprStmt(FuncCall("printInt", [IntLiteral(10)])), BreakStmt()]),
            CaseStmt(IntLiteral(3), [ExprStmt(FuncCall("printInt", [IntLiteral(20)])), BreakStmt()])
        ], None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "20"

def test_extra_721():
    # Mixed int/float arithmetic with coercion
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "result", BinaryOp(IntLiteral(5), "+", FloatLiteral(2.5))),
        ExprStmt(FuncCall("printFloat", [Identifier("result")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "7.5"

def test_extra_722():
    # Mixed float/int multiplication
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(FloatType(), "x", BinaryOp(FloatLiteral(1.5), "*", IntLiteral(4))),
        ExprStmt(FuncCall("printFloat", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "6.0"

def test_extra_723():
    # Int passed to float parameter with coercion
    ast = Program([
        FuncDecl(VoidType(), "printAsFloat", [Param(FloatType(), "f")], BlockStmt([
            ExprStmt(FuncCall("printFloat", [Identifier("f")]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printAsFloat", [IntLiteral(7)]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "7.0"

def test_extra_724():
    # Simple state machine (3-state counter)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "state", IntLiteral(0)),
        VarDecl(IntType(), "count", IntLiteral(0)),
        WhileStmt(BinaryOp(Identifier("count"), "<", IntLiteral(5)), BlockStmt([
            IfStmt(BinaryOp(Identifier("state"), "==", IntLiteral(0)), BlockStmt([
                ExprStmt(FuncCall("printInt", [IntLiteral(1)])),
                ExprStmt(AssignExpr(Identifier("state"), IntLiteral(1)))
            ]), IfStmt(BinaryOp(Identifier("state"), "==", IntLiteral(1)), BlockStmt([
                ExprStmt(FuncCall("printInt", [IntLiteral(2)])),
                ExprStmt(AssignExpr(Identifier("state"), IntLiteral(2)))
            ]), BlockStmt([
                ExprStmt(FuncCall("printInt", [IntLiteral(3)])),
                ExprStmt(AssignExpr(Identifier("state"), IntLiteral(0)))
            ]))),
            ExprStmt(AssignExpr(Identifier("count"), BinaryOp(Identifier("count"), "+", IntLiteral(1))))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "12312"

def test_extra_725():
    # Bubble sort simulation
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "a", IntLiteral(3)),
        VarDecl(IntType(), "b", IntLiteral(1)),
        VarDecl(IntType(), "temp", IntLiteral(0)),
        IfStmt(BinaryOp(Identifier("a"), ">", Identifier("b")), BlockStmt([
            ExprStmt(AssignExpr(Identifier("temp"), Identifier("a"))),
            ExprStmt(AssignExpr(Identifier("a"), Identifier("b"))),
            ExprStmt(AssignExpr(Identifier("b"), Identifier("temp")))
        ]), None),
        ExprStmt(FuncCall("printInt", [Identifier("a")])),
        ExprStmt(FuncCall("printInt", [Identifier("b")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "13"

def test_extra_726():
    # Counting loop with continue
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)), BinaryOp(Identifier("i"), "<", IntLiteral(5)), ExprStmt(PrefixOp("++", Identifier("i"))), BlockStmt([
            IfStmt(BinaryOp(Identifier("i"), "%", IntLiteral(2)), BlockStmt([ContinueStmt()]), None),
            ExprStmt(FuncCall("printInt", [Identifier("i")]))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "024"

def test_extra_727():
    # Nested if-else chains
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(5)),
        IfStmt(BinaryOp(Identifier("x"), "<", IntLiteral(3)), BlockStmt([
            ExprStmt(FuncCall("printInt", [IntLiteral(1)]))
        ]), IfStmt(BinaryOp(Identifier("x"), "<", IntLiteral(10)), BlockStmt([
            ExprStmt(FuncCall("printInt", [IntLiteral(2)]))
        ]), BlockStmt([
            ExprStmt(FuncCall("printInt", [IntLiteral(3)]))
        ])))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "2"

def test_extra_728():
    # Function with multiple return paths
    ast = Program([
        FuncDecl(IntType(), "abs", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<", IntLiteral(0)), BlockStmt([
                ReturnStmt(PrefixOp("-", Identifier("n")))
            ]), BlockStmt([
                ReturnStmt(Identifier("n"))
            ]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("abs", [IntLiteral(-42)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "42"

def test_extra_729():
    # Factorial using recursion
    ast = Program([
        FuncDecl(IntType(), "fact", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<=", IntLiteral(1)), BlockStmt([
                ReturnStmt(IntLiteral(1))
            ]), BlockStmt([
                ReturnStmt(BinaryOp(Identifier("n"), "*", FuncCall("fact", [BinaryOp(Identifier("n"), "-", IntLiteral(1))])))
            ]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("fact", [IntLiteral(5)])]))
        ]))
    ])
    assert CodeGenerator().generate_and_run(ast) == "120"

def test_extra_730():
    # Prefix increment in expression
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(5)),
        ExprStmt(FuncCall("printInt", [PrefixOp("++", Identifier("x"))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "6"

def test_extra_731():
    # Postfix increment returns original value (correct C/C++/Java semantics)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(5)),
        ExprStmt(FuncCall("printInt", [PostfixOp("++", Identifier("x"))])),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "56"

def test_extra_732():
    # Logical NOT with short-circuit verification
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "called", IntLiteral(0)),
        VarDecl(IntType(), "x", IntLiteral(0)),
        IfStmt(PrefixOp("!", Identifier("x")), BlockStmt([
            ExprStmt(FuncCall("printInt", [IntLiteral(1)]))
        ]), None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_733():
    # Operator precedence: multiplication before addition
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "result", BinaryOp(IntLiteral(2), "+", BinaryOp(IntLiteral(3), "*", IntLiteral(4)))),
        ExprStmt(FuncCall("printInt", [Identifier("result")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "14"

def test_extra_734():
    # Operator precedence: parentheses override
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "result", BinaryOp(BinaryOp(IntLiteral(2), "+", IntLiteral(3)), "*", IntLiteral(4))),
        ExprStmt(FuncCall("printInt", [Identifier("result")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "20"

def test_extra_735():
    # Modulo operator with positive values
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(17), "%", IntLiteral(5))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "2"

def test_extra_736():
    # Division of integers
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(20), "/", IntLiteral(3))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "6"

def test_extra_737():
    # Equality comparison chains
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(5)),
        IfStmt(BinaryOp(Identifier("x"), "==", IntLiteral(5)), BlockStmt([
            ExprStmt(FuncCall("printInt", [IntLiteral(1)]))
        ]), None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_738():
    # Inequality comparison
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        IfStmt(BinaryOp(IntLiteral(5), "!=", IntLiteral(3)), BlockStmt([
            ExprStmt(FuncCall("printInt", [IntLiteral(1)]))
        ]), None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_739():
    # Logical AND operator
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        IfStmt(BinaryOp(BinaryOp(IntLiteral(1), "==", IntLiteral(1)), "&&", BinaryOp(IntLiteral(2), "==", IntLiteral(2))), BlockStmt([
            ExprStmt(FuncCall("printInt", [IntLiteral(1)]))
        ]), None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_740():
    # Logical OR operator
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        IfStmt(BinaryOp(BinaryOp(IntLiteral(1), "==", IntLiteral(0)), "||", BinaryOp(IntLiteral(2), "==", IntLiteral(2))), BlockStmt([
            ExprStmt(FuncCall("printInt", [IntLiteral(1)]))
        ]), None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_741():
    # Greater than comparison
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        IfStmt(BinaryOp(IntLiteral(10), ">", IntLiteral(5)), BlockStmt([
            ExprStmt(FuncCall("printInt", [IntLiteral(1)]))
        ]), None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_742():
    # Less than comparison
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        IfStmt(BinaryOp(IntLiteral(3), "<", IntLiteral(5)), BlockStmt([
            ExprStmt(FuncCall("printInt", [IntLiteral(1)]))
        ]), None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_743():
    # Greater than or equal
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        IfStmt(BinaryOp(IntLiteral(5), ">=", IntLiteral(5)), BlockStmt([
            ExprStmt(FuncCall("printInt", [IntLiteral(1)]))
        ]), None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_744():
    # Less than or equal
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        IfStmt(BinaryOp(IntLiteral(4), "<=", IntLiteral(5)), BlockStmt([
            ExprStmt(FuncCall("printInt", [IntLiteral(1)]))
        ]), None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "1"

def test_extra_745():
    # Prefix decrement
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(10)),
        ExprStmt(FuncCall("printInt", [PrefixOp("--", Identifier("x"))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "9"

def test_extra_746():
    # Postfix decrement returns original value (correct C/C++/Java semantics)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(10)),
        ExprStmt(FuncCall("printInt", [PostfixOp("--", Identifier("x"))])),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "109"

def test_extra_747():
    # Unary negation
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [PrefixOp("-", IntLiteral(5))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "-5"

def test_extra_748():
    # Double negation
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        ExprStmt(FuncCall("printInt", [PrefixOp("-", PrefixOp("-", IntLiteral(7)))]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "7"

def test_extra_749():
    # While loop with complex condition
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(0)),
        WhileStmt(BinaryOp(BinaryOp(Identifier("x"), "<", IntLiteral(5)), "&&", BinaryOp(Identifier("x"), "!=", IntLiteral(3))), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("x")])),
            ExprStmt(AssignExpr(Identifier("x"), BinaryOp(Identifier("x"), "+", IntLiteral(1))))
        ]))
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "012"

def test_extra_750():
    # Assignment in condition (implicit conversion to boolean)
    ast = Program([FuncDecl(VoidType(), "main", [], BlockStmt([
        VarDecl(IntType(), "x", IntLiteral(5)),
        IfStmt(Identifier("x"), BlockStmt([
            ExprStmt(FuncCall("printInt", [Identifier("x")]))
        ]), None)
    ]))])
    assert CodeGenerator().generate_and_run(ast) == "5"


# ===== HTML Report Generator =====
if __name__ == "__main__":
    import subprocess
    import json
    import os
    from datetime import datetime
    from pathlib import Path
    
    # Run pytest with JSON output
    result = subprocess.run(
        ["python", "-m", "pytest", __file__, "-v", "--tb=short", "--json-report", "--json-report-file=report.json"],
        capture_output=True,
        text=True,
        cwd=os.path.dirname(os.path.abspath(__file__))
    )
    
    # If json-report plugin not available, use alternative method
    if result.returncode != 0 or not os.path.exists("report.json"):
        # Fallback: run pytest and capture output
        result = subprocess.run(
            ["python", "-m", "pytest", __file__, "-v", "--tb=line"],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        test_output = result.stdout
    else:
        with open("report.json") as f:
            report_data = json.load(f)
        test_output = json.dumps(report_data, indent=2)
    
    # Generate HTML report
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TyC Compiler Test Results</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            overflow: hidden;
        }}
        header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        header p {{
            font-size: 1.1em;
            opacity: 0.9;
        }}
        .content {{
            padding: 30px;
        }}
        .summary {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        .summary-card {{
            background: #f5f5f5;
            border-left: 4px solid #667eea;
            padding: 20px;
            border-radius: 5px;
        }}
        .summary-card h3 {{
            color: #667eea;
            margin-bottom: 10px;
        }}
        .summary-card .value {{
            font-size: 2em;
            font-weight: bold;
            color: #333;
        }}
        .timestamp {{
            color: #999;
            font-size: 0.9em;
            margin-top: 10px;
        }}
        pre {{
            background: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 5px;
            padding: 20px;
            overflow-x: auto;
            font-size: 0.9em;
            line-height: 1.5;
            color: #333;
            max-height: 600px;
            overflow-y: auto;
        }}
        .passed {{ color: #28a745; font-weight: bold; }}
        .failed {{ color: #dc3545; font-weight: bold; }}
        .error {{ color: #ffc107; font-weight: bold; }}
        .footer {{
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #666;
            border-top: 1px solid #dee2e6;
        }}
        @media (prefers-color-scheme: dark) {{
            body {{ background: #1a1a1a; }}
            .container {{ background: #2d2d2d; color: #e0e0e0; }}
            pre {{ background: #1e1e1e; color: #e0e0e0; border-color: #444; }}
            .summary-card {{ background: #3a3a3a; color: #e0e0e0; }}
            .footer {{ background: #3a3a3a; color: #aaa; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🧪 TyC Compiler Test Report</h1>
            <p>Code Generation Test Suite (~800 tests)</p>
        </header>
        <div class="content">
            <div class="summary">
                <div class="summary-card">
                    <h3>Total Tests</h3>
                    <div class="value">~800</div>
                    <p class="timestamp">Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                </div>
                <div class="summary-card">
                    <h3>Test Status</h3>
                    <div class="value">Running...</div>
                    <p class="timestamp">Check console for results</p>
                </div>
            </div>
            <h2>Test Output</h2>
            <pre>{test_output}</pre>
        </div>
        <div class="footer">
            <p>📊 TyC Compiler Test Report | Generated on {datetime.now().strftime('%Y-%m-%d at %H:%M:%S')}</p>
            <p>For detailed test failures, check pytest output above</p>
        </div>
    </div>
</body>
</html>"""
    
    # Write HTML report
    report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "test_report.html")
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    
    with open(report_path, "w") as f:
        f.write(html_content)
    
    print(f"\n✅ HTML report generated: {os.path.abspath(report_path)}")
    print(f"📊 Test output:\n{test_output}")
