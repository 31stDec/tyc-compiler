"""
Test cases for TyC code generation (100 cases).
"""
from src.utils.nodes import *
from tests.utils import CodeGenerator

def run_test(ast, expected):
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_001():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ExprStmt(FuncCall('printInt', [BinaryOp(IntLiteral(1), '+', IntLiteral(1))]))]))])
    run_test(ast, '2')

def test_002():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ExprStmt(FuncCall('printInt', [BinaryOp(IntLiteral(2), '+', IntLiteral(2))]))]))])
    run_test(ast, '4')

def test_003():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ExprStmt(FuncCall('printInt', [BinaryOp(IntLiteral(3), '+', IntLiteral(3))]))]))])
    run_test(ast, '6')

def test_004():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ExprStmt(FuncCall('printInt', [BinaryOp(IntLiteral(4), '+', IntLiteral(4))]))]))])
    run_test(ast, '8')

def test_005():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ExprStmt(FuncCall('printInt', [BinaryOp(IntLiteral(5), '+', IntLiteral(5))]))]))])
    run_test(ast, '10')

def test_006():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ExprStmt(FuncCall('printInt', [BinaryOp(IntLiteral(6), '+', IntLiteral(6))]))]))])
    run_test(ast, '12')

def test_007():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ExprStmt(FuncCall('printInt', [BinaryOp(IntLiteral(7), '+', IntLiteral(7))]))]))])
    run_test(ast, '14')

def test_008():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ExprStmt(FuncCall('printInt', [BinaryOp(IntLiteral(8), '+', IntLiteral(8))]))]))])
    run_test(ast, '16')

def test_009():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ExprStmt(FuncCall('printInt', [BinaryOp(IntLiteral(9), '+', IntLiteral(9))]))]))])
    run_test(ast, '18')

def test_010():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ExprStmt(FuncCall('printInt', [BinaryOp(IntLiteral(10), '+', IntLiteral(10))]))]))])
    run_test(ast, '20')

def test_011():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([IfStmt(BinaryOp(IntLiteral(11), '<', IntLiteral(16)), ExprStmt(FuncCall('printInt', [IntLiteral(1)])), ExprStmt(FuncCall('printInt', [IntLiteral(0)])))]))])
    run_test(ast, '1')

def test_012():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([IfStmt(BinaryOp(IntLiteral(12), '<', IntLiteral(17)), ExprStmt(FuncCall('printInt', [IntLiteral(1)])), ExprStmt(FuncCall('printInt', [IntLiteral(0)])))]))])
    run_test(ast, '1')

def test_013():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([IfStmt(BinaryOp(IntLiteral(13), '<', IntLiteral(18)), ExprStmt(FuncCall('printInt', [IntLiteral(1)])), ExprStmt(FuncCall('printInt', [IntLiteral(0)])))]))])
    run_test(ast, '1')

def test_014():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([IfStmt(BinaryOp(IntLiteral(14), '<', IntLiteral(19)), ExprStmt(FuncCall('printInt', [IntLiteral(1)])), ExprStmt(FuncCall('printInt', [IntLiteral(0)])))]))])
    run_test(ast, '1')

def test_015():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([IfStmt(BinaryOp(IntLiteral(15), '<', IntLiteral(20)), ExprStmt(FuncCall('printInt', [IntLiteral(1)])), ExprStmt(FuncCall('printInt', [IntLiteral(0)])))]))])
    run_test(ast, '1')

def test_016():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([IfStmt(BinaryOp(IntLiteral(16), '<', IntLiteral(21)), ExprStmt(FuncCall('printInt', [IntLiteral(1)])), ExprStmt(FuncCall('printInt', [IntLiteral(0)])))]))])
    run_test(ast, '1')

def test_017():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([IfStmt(BinaryOp(IntLiteral(17), '<', IntLiteral(22)), ExprStmt(FuncCall('printInt', [IntLiteral(1)])), ExprStmt(FuncCall('printInt', [IntLiteral(0)])))]))])
    run_test(ast, '1')

def test_018():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([IfStmt(BinaryOp(IntLiteral(18), '<', IntLiteral(23)), ExprStmt(FuncCall('printInt', [IntLiteral(1)])), ExprStmt(FuncCall('printInt', [IntLiteral(0)])))]))])
    run_test(ast, '1')

def test_019():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([IfStmt(BinaryOp(IntLiteral(19), '<', IntLiteral(24)), ExprStmt(FuncCall('printInt', [IntLiteral(1)])), ExprStmt(FuncCall('printInt', [IntLiteral(0)])))]))])
    run_test(ast, '1')

def test_020():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([IfStmt(BinaryOp(IntLiteral(20), '<', IntLiteral(25)), ExprStmt(FuncCall('printInt', [IntLiteral(1)])), ExprStmt(FuncCall('printInt', [IntLiteral(0)])))]))])
    run_test(ast, '1')

def test_021():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([IfStmt(BinaryOp(IntLiteral(21), '<', IntLiteral(26)), ExprStmt(FuncCall('printInt', [IntLiteral(1)])), ExprStmt(FuncCall('printInt', [IntLiteral(0)])))]))])
    run_test(ast, '1')

def test_022():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([IfStmt(BinaryOp(IntLiteral(22), '<', IntLiteral(27)), ExprStmt(FuncCall('printInt', [IntLiteral(1)])), ExprStmt(FuncCall('printInt', [IntLiteral(0)])))]))])
    run_test(ast, '1')

def test_023():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([IfStmt(BinaryOp(IntLiteral(23), '<', IntLiteral(28)), ExprStmt(FuncCall('printInt', [IntLiteral(1)])), ExprStmt(FuncCall('printInt', [IntLiteral(0)])))]))])
    run_test(ast, '1')

def test_024():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([IfStmt(BinaryOp(IntLiteral(24), '<', IntLiteral(29)), ExprStmt(FuncCall('printInt', [IntLiteral(1)])), ExprStmt(FuncCall('printInt', [IntLiteral(0)])))]))])
    run_test(ast, '1')

def test_025():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([IfStmt(BinaryOp(IntLiteral(25), '<', IntLiteral(30)), ExprStmt(FuncCall('printInt', [IntLiteral(1)])), ExprStmt(FuncCall('printInt', [IntLiteral(0)])))]))])
    run_test(ast, '1')

def test_026():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([IfStmt(BinaryOp(IntLiteral(26), '<', IntLiteral(31)), ExprStmt(FuncCall('printInt', [IntLiteral(1)])), ExprStmt(FuncCall('printInt', [IntLiteral(0)])))]))])
    run_test(ast, '1')

def test_027():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([IfStmt(BinaryOp(IntLiteral(27), '<', IntLiteral(32)), ExprStmt(FuncCall('printInt', [IntLiteral(1)])), ExprStmt(FuncCall('printInt', [IntLiteral(0)])))]))])
    run_test(ast, '1')

def test_028():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([IfStmt(BinaryOp(IntLiteral(28), '<', IntLiteral(33)), ExprStmt(FuncCall('printInt', [IntLiteral(1)])), ExprStmt(FuncCall('printInt', [IntLiteral(0)])))]))])
    run_test(ast, '1')

def test_029():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([IfStmt(BinaryOp(IntLiteral(29), '<', IntLiteral(34)), ExprStmt(FuncCall('printInt', [IntLiteral(1)])), ExprStmt(FuncCall('printInt', [IntLiteral(0)])))]))])
    run_test(ast, '1')

def test_030():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([IfStmt(BinaryOp(IntLiteral(30), '<', IntLiteral(35)), ExprStmt(FuncCall('printInt', [IntLiteral(1)])), ExprStmt(FuncCall('printInt', [IntLiteral(0)])))]))])
    run_test(ast, '1')

def test_031():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(0)), WhileStmt(BinaryOp(Identifier('x'), '<', IntLiteral(2)), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('x')])), ExprStmt(AssignExpr(Identifier('x'), BinaryOp(Identifier('x'), '+', IntLiteral(1))))]))]))])
    expected_str = "".join([str(n) for n in range(2)])
    run_test(ast, expected_str)

def test_032():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(0)), WhileStmt(BinaryOp(Identifier('x'), '<', IntLiteral(3)), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('x')])), ExprStmt(AssignExpr(Identifier('x'), BinaryOp(Identifier('x'), '+', IntLiteral(1))))]))]))])
    expected_str = "".join([str(n) for n in range(3)])
    run_test(ast, expected_str)

def test_033():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(0)), WhileStmt(BinaryOp(Identifier('x'), '<', IntLiteral(4)), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('x')])), ExprStmt(AssignExpr(Identifier('x'), BinaryOp(Identifier('x'), '+', IntLiteral(1))))]))]))])
    expected_str = "".join([str(n) for n in range(4)])
    run_test(ast, expected_str)

def test_034():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(0)), WhileStmt(BinaryOp(Identifier('x'), '<', IntLiteral(5)), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('x')])), ExprStmt(AssignExpr(Identifier('x'), BinaryOp(Identifier('x'), '+', IntLiteral(1))))]))]))])
    expected_str = "".join([str(n) for n in range(5)])
    run_test(ast, expected_str)

def test_035():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(0)), WhileStmt(BinaryOp(Identifier('x'), '<', IntLiteral(1)), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('x')])), ExprStmt(AssignExpr(Identifier('x'), BinaryOp(Identifier('x'), '+', IntLiteral(1))))]))]))])
    expected_str = "".join([str(n) for n in range(1)])
    run_test(ast, expected_str)

def test_036():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(0)), WhileStmt(BinaryOp(Identifier('x'), '<', IntLiteral(2)), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('x')])), ExprStmt(AssignExpr(Identifier('x'), BinaryOp(Identifier('x'), '+', IntLiteral(1))))]))]))])
    expected_str = "".join([str(n) for n in range(2)])
    run_test(ast, expected_str)

def test_037():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(0)), WhileStmt(BinaryOp(Identifier('x'), '<', IntLiteral(3)), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('x')])), ExprStmt(AssignExpr(Identifier('x'), BinaryOp(Identifier('x'), '+', IntLiteral(1))))]))]))])
    expected_str = "".join([str(n) for n in range(3)])
    run_test(ast, expected_str)

def test_038():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(0)), WhileStmt(BinaryOp(Identifier('x'), '<', IntLiteral(4)), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('x')])), ExprStmt(AssignExpr(Identifier('x'), BinaryOp(Identifier('x'), '+', IntLiteral(1))))]))]))])
    expected_str = "".join([str(n) for n in range(4)])
    run_test(ast, expected_str)

def test_039():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(0)), WhileStmt(BinaryOp(Identifier('x'), '<', IntLiteral(5)), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('x')])), ExprStmt(AssignExpr(Identifier('x'), BinaryOp(Identifier('x'), '+', IntLiteral(1))))]))]))])
    expected_str = "".join([str(n) for n in range(5)])
    run_test(ast, expected_str)

def test_040():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(0)), WhileStmt(BinaryOp(Identifier('x'), '<', IntLiteral(1)), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('x')])), ExprStmt(AssignExpr(Identifier('x'), BinaryOp(Identifier('x'), '+', IntLiteral(1))))]))]))])
    expected_str = "".join([str(n) for n in range(1)])
    run_test(ast, expected_str)

def test_041():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(0)), WhileStmt(BinaryOp(Identifier('x'), '<', IntLiteral(2)), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('x')])), ExprStmt(AssignExpr(Identifier('x'), BinaryOp(Identifier('x'), '+', IntLiteral(1))))]))]))])
    expected_str = "".join([str(n) for n in range(2)])
    run_test(ast, expected_str)

def test_042():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(0)), WhileStmt(BinaryOp(Identifier('x'), '<', IntLiteral(3)), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('x')])), ExprStmt(AssignExpr(Identifier('x'), BinaryOp(Identifier('x'), '+', IntLiteral(1))))]))]))])
    expected_str = "".join([str(n) for n in range(3)])
    run_test(ast, expected_str)

def test_043():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(0)), WhileStmt(BinaryOp(Identifier('x'), '<', IntLiteral(4)), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('x')])), ExprStmt(AssignExpr(Identifier('x'), BinaryOp(Identifier('x'), '+', IntLiteral(1))))]))]))])
    expected_str = "".join([str(n) for n in range(4)])
    run_test(ast, expected_str)

def test_044():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(0)), WhileStmt(BinaryOp(Identifier('x'), '<', IntLiteral(5)), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('x')])), ExprStmt(AssignExpr(Identifier('x'), BinaryOp(Identifier('x'), '+', IntLiteral(1))))]))]))])
    expected_str = "".join([str(n) for n in range(5)])
    run_test(ast, expected_str)

def test_045():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(0)), WhileStmt(BinaryOp(Identifier('x'), '<', IntLiteral(1)), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('x')])), ExprStmt(AssignExpr(Identifier('x'), BinaryOp(Identifier('x'), '+', IntLiteral(1))))]))]))])
    expected_str = "".join([str(n) for n in range(1)])
    run_test(ast, expected_str)

def test_046():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(0)), WhileStmt(BinaryOp(Identifier('x'), '<', IntLiteral(2)), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('x')])), ExprStmt(AssignExpr(Identifier('x'), BinaryOp(Identifier('x'), '+', IntLiteral(1))))]))]))])
    expected_str = "".join([str(n) for n in range(2)])
    run_test(ast, expected_str)

def test_047():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(0)), WhileStmt(BinaryOp(Identifier('x'), '<', IntLiteral(3)), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('x')])), ExprStmt(AssignExpr(Identifier('x'), BinaryOp(Identifier('x'), '+', IntLiteral(1))))]))]))])
    expected_str = "".join([str(n) for n in range(3)])
    run_test(ast, expected_str)

def test_048():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(0)), WhileStmt(BinaryOp(Identifier('x'), '<', IntLiteral(4)), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('x')])), ExprStmt(AssignExpr(Identifier('x'), BinaryOp(Identifier('x'), '+', IntLiteral(1))))]))]))])
    expected_str = "".join([str(n) for n in range(4)])
    run_test(ast, expected_str)

def test_049():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(0)), WhileStmt(BinaryOp(Identifier('x'), '<', IntLiteral(5)), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('x')])), ExprStmt(AssignExpr(Identifier('x'), BinaryOp(Identifier('x'), '+', IntLiteral(1))))]))]))])
    expected_str = "".join([str(n) for n in range(5)])
    run_test(ast, expected_str)

def test_050():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(0)), WhileStmt(BinaryOp(Identifier('x'), '<', IntLiteral(1)), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('x')])), ExprStmt(AssignExpr(Identifier('x'), BinaryOp(Identifier('x'), '+', IntLiteral(1))))]))]))])
    expected_str = "".join([str(n) for n in range(1)])
    run_test(ast, expected_str)

def test_051():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ForStmt(VarDecl(IntType(), 'i', IntLiteral(0)), BinaryOp(Identifier('i'), '<', IntLiteral(5)), AssignExpr(Identifier('i'), BinaryOp(Identifier('i'), '+', IntLiteral(1))), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('i')]))]))]))])
    expected_str = "".join([str(n) for n in range(5)])
    run_test(ast, expected_str)

def test_052():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ForStmt(VarDecl(IntType(), 'i', IntLiteral(0)), BinaryOp(Identifier('i'), '<', IntLiteral(2)), AssignExpr(Identifier('i'), BinaryOp(Identifier('i'), '+', IntLiteral(1))), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('i')]))]))]))])
    expected_str = "".join([str(n) for n in range(2)])
    run_test(ast, expected_str)

def test_053():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ForStmt(VarDecl(IntType(), 'i', IntLiteral(0)), BinaryOp(Identifier('i'), '<', IntLiteral(3)), AssignExpr(Identifier('i'), BinaryOp(Identifier('i'), '+', IntLiteral(1))), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('i')]))]))]))])
    expected_str = "".join([str(n) for n in range(3)])
    run_test(ast, expected_str)

def test_054():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ForStmt(VarDecl(IntType(), 'i', IntLiteral(0)), BinaryOp(Identifier('i'), '<', IntLiteral(4)), AssignExpr(Identifier('i'), BinaryOp(Identifier('i'), '+', IntLiteral(1))), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('i')]))]))]))])
    expected_str = "".join([str(n) for n in range(4)])
    run_test(ast, expected_str)

def test_055():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ForStmt(VarDecl(IntType(), 'i', IntLiteral(0)), BinaryOp(Identifier('i'), '<', IntLiteral(5)), AssignExpr(Identifier('i'), BinaryOp(Identifier('i'), '+', IntLiteral(1))), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('i')]))]))]))])
    expected_str = "".join([str(n) for n in range(5)])
    run_test(ast, expected_str)

def test_056():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ForStmt(VarDecl(IntType(), 'i', IntLiteral(0)), BinaryOp(Identifier('i'), '<', IntLiteral(2)), AssignExpr(Identifier('i'), BinaryOp(Identifier('i'), '+', IntLiteral(1))), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('i')]))]))]))])
    expected_str = "".join([str(n) for n in range(2)])
    run_test(ast, expected_str)

def test_057():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ForStmt(VarDecl(IntType(), 'i', IntLiteral(0)), BinaryOp(Identifier('i'), '<', IntLiteral(3)), AssignExpr(Identifier('i'), BinaryOp(Identifier('i'), '+', IntLiteral(1))), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('i')]))]))]))])
    expected_str = "".join([str(n) for n in range(3)])
    run_test(ast, expected_str)

def test_058():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ForStmt(VarDecl(IntType(), 'i', IntLiteral(0)), BinaryOp(Identifier('i'), '<', IntLiteral(4)), AssignExpr(Identifier('i'), BinaryOp(Identifier('i'), '+', IntLiteral(1))), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('i')]))]))]))])
    expected_str = "".join([str(n) for n in range(4)])
    run_test(ast, expected_str)

def test_059():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ForStmt(VarDecl(IntType(), 'i', IntLiteral(0)), BinaryOp(Identifier('i'), '<', IntLiteral(5)), AssignExpr(Identifier('i'), BinaryOp(Identifier('i'), '+', IntLiteral(1))), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('i')]))]))]))])
    expected_str = "".join([str(n) for n in range(5)])
    run_test(ast, expected_str)

def test_060():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ForStmt(VarDecl(IntType(), 'i', IntLiteral(0)), BinaryOp(Identifier('i'), '<', IntLiteral(2)), AssignExpr(Identifier('i'), BinaryOp(Identifier('i'), '+', IntLiteral(1))), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('i')]))]))]))])
    expected_str = "".join([str(n) for n in range(2)])
    run_test(ast, expected_str)

def test_061():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ForStmt(VarDecl(IntType(), 'i', IntLiteral(0)), BinaryOp(Identifier('i'), '<', IntLiteral(3)), AssignExpr(Identifier('i'), BinaryOp(Identifier('i'), '+', IntLiteral(1))), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('i')]))]))]))])
    expected_str = "".join([str(n) for n in range(3)])
    run_test(ast, expected_str)

def test_062():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ForStmt(VarDecl(IntType(), 'i', IntLiteral(0)), BinaryOp(Identifier('i'), '<', IntLiteral(4)), AssignExpr(Identifier('i'), BinaryOp(Identifier('i'), '+', IntLiteral(1))), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('i')]))]))]))])
    expected_str = "".join([str(n) for n in range(4)])
    run_test(ast, expected_str)

def test_063():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ForStmt(VarDecl(IntType(), 'i', IntLiteral(0)), BinaryOp(Identifier('i'), '<', IntLiteral(5)), AssignExpr(Identifier('i'), BinaryOp(Identifier('i'), '+', IntLiteral(1))), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('i')]))]))]))])
    expected_str = "".join([str(n) for n in range(5)])
    run_test(ast, expected_str)

def test_064():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ForStmt(VarDecl(IntType(), 'i', IntLiteral(0)), BinaryOp(Identifier('i'), '<', IntLiteral(2)), AssignExpr(Identifier('i'), BinaryOp(Identifier('i'), '+', IntLiteral(1))), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('i')]))]))]))])
    expected_str = "".join([str(n) for n in range(2)])
    run_test(ast, expected_str)

def test_065():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ForStmt(VarDecl(IntType(), 'i', IntLiteral(0)), BinaryOp(Identifier('i'), '<', IntLiteral(3)), AssignExpr(Identifier('i'), BinaryOp(Identifier('i'), '+', IntLiteral(1))), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('i')]))]))]))])
    expected_str = "".join([str(n) for n in range(3)])
    run_test(ast, expected_str)

def test_066():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ForStmt(VarDecl(IntType(), 'i', IntLiteral(0)), BinaryOp(Identifier('i'), '<', IntLiteral(4)), AssignExpr(Identifier('i'), BinaryOp(Identifier('i'), '+', IntLiteral(1))), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('i')]))]))]))])
    expected_str = "".join([str(n) for n in range(4)])
    run_test(ast, expected_str)

def test_067():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ForStmt(VarDecl(IntType(), 'i', IntLiteral(0)), BinaryOp(Identifier('i'), '<', IntLiteral(5)), AssignExpr(Identifier('i'), BinaryOp(Identifier('i'), '+', IntLiteral(1))), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('i')]))]))]))])
    expected_str = "".join([str(n) for n in range(5)])
    run_test(ast, expected_str)

def test_068():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ForStmt(VarDecl(IntType(), 'i', IntLiteral(0)), BinaryOp(Identifier('i'), '<', IntLiteral(2)), AssignExpr(Identifier('i'), BinaryOp(Identifier('i'), '+', IntLiteral(1))), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('i')]))]))]))])
    expected_str = "".join([str(n) for n in range(2)])
    run_test(ast, expected_str)

def test_069():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ForStmt(VarDecl(IntType(), 'i', IntLiteral(0)), BinaryOp(Identifier('i'), '<', IntLiteral(3)), AssignExpr(Identifier('i'), BinaryOp(Identifier('i'), '+', IntLiteral(1))), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('i')]))]))]))])
    expected_str = "".join([str(n) for n in range(3)])
    run_test(ast, expected_str)

def test_070():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([ForStmt(VarDecl(IntType(), 'i', IntLiteral(0)), BinaryOp(Identifier('i'), '<', IntLiteral(4)), AssignExpr(Identifier('i'), BinaryOp(Identifier('i'), '+', IntLiteral(1))), BlockStmt([ExprStmt(FuncCall('printInt', [Identifier('i')]))]))]))])
    expected_str = "".join([str(n) for n in range(4)])
    run_test(ast, expected_str)

def test_071():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(3)), SwitchStmt(Identifier('x'), [CaseStmt(IntLiteral(1), [ExprStmt(FuncCall('printInt', [IntLiteral(1)])), BreakStmt()]), CaseStmt(IntLiteral(2), [ExprStmt(FuncCall('printInt', [IntLiteral(2)])), BreakStmt()])], DefaultStmt([ExprStmt(FuncCall('printInt', [IntLiteral(0)]))]))]))])
    expected = '1' if 3 == 1 else '2' if 3 == 2 else '0'
    run_test(ast, expected)

def test_072():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(1)), SwitchStmt(Identifier('x'), [CaseStmt(IntLiteral(1), [ExprStmt(FuncCall('printInt', [IntLiteral(1)])), BreakStmt()]), CaseStmt(IntLiteral(2), [ExprStmt(FuncCall('printInt', [IntLiteral(2)])), BreakStmt()])], DefaultStmt([ExprStmt(FuncCall('printInt', [IntLiteral(0)]))]))]))])
    expected = '1' if 1 == 1 else '2' if 1 == 2 else '0'
    run_test(ast, expected)

def test_073():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(2)), SwitchStmt(Identifier('x'), [CaseStmt(IntLiteral(1), [ExprStmt(FuncCall('printInt', [IntLiteral(1)])), BreakStmt()]), CaseStmt(IntLiteral(2), [ExprStmt(FuncCall('printInt', [IntLiteral(2)])), BreakStmt()])], DefaultStmt([ExprStmt(FuncCall('printInt', [IntLiteral(0)]))]))]))])
    expected = '1' if 2 == 1 else '2' if 2 == 2 else '0'
    run_test(ast, expected)

def test_074():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(3)), SwitchStmt(Identifier('x'), [CaseStmt(IntLiteral(1), [ExprStmt(FuncCall('printInt', [IntLiteral(1)])), BreakStmt()]), CaseStmt(IntLiteral(2), [ExprStmt(FuncCall('printInt', [IntLiteral(2)])), BreakStmt()])], DefaultStmt([ExprStmt(FuncCall('printInt', [IntLiteral(0)]))]))]))])
    expected = '1' if 3 == 1 else '2' if 3 == 2 else '0'
    run_test(ast, expected)

def test_075():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(1)), SwitchStmt(Identifier('x'), [CaseStmt(IntLiteral(1), [ExprStmt(FuncCall('printInt', [IntLiteral(1)])), BreakStmt()]), CaseStmt(IntLiteral(2), [ExprStmt(FuncCall('printInt', [IntLiteral(2)])), BreakStmt()])], DefaultStmt([ExprStmt(FuncCall('printInt', [IntLiteral(0)]))]))]))])
    expected = '1' if 1 == 1 else '2' if 1 == 2 else '0'
    run_test(ast, expected)

def test_076():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(2)), SwitchStmt(Identifier('x'), [CaseStmt(IntLiteral(1), [ExprStmt(FuncCall('printInt', [IntLiteral(1)])), BreakStmt()]), CaseStmt(IntLiteral(2), [ExprStmt(FuncCall('printInt', [IntLiteral(2)])), BreakStmt()])], DefaultStmt([ExprStmt(FuncCall('printInt', [IntLiteral(0)]))]))]))])
    expected = '1' if 2 == 1 else '2' if 2 == 2 else '0'
    run_test(ast, expected)

def test_077():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(3)), SwitchStmt(Identifier('x'), [CaseStmt(IntLiteral(1), [ExprStmt(FuncCall('printInt', [IntLiteral(1)])), BreakStmt()]), CaseStmt(IntLiteral(2), [ExprStmt(FuncCall('printInt', [IntLiteral(2)])), BreakStmt()])], DefaultStmt([ExprStmt(FuncCall('printInt', [IntLiteral(0)]))]))]))])
    expected = '1' if 3 == 1 else '2' if 3 == 2 else '0'
    run_test(ast, expected)

def test_078():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(1)), SwitchStmt(Identifier('x'), [CaseStmt(IntLiteral(1), [ExprStmt(FuncCall('printInt', [IntLiteral(1)])), BreakStmt()]), CaseStmt(IntLiteral(2), [ExprStmt(FuncCall('printInt', [IntLiteral(2)])), BreakStmt()])], DefaultStmt([ExprStmt(FuncCall('printInt', [IntLiteral(0)]))]))]))])
    expected = '1' if 1 == 1 else '2' if 1 == 2 else '0'
    run_test(ast, expected)

def test_079():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(2)), SwitchStmt(Identifier('x'), [CaseStmt(IntLiteral(1), [ExprStmt(FuncCall('printInt', [IntLiteral(1)])), BreakStmt()]), CaseStmt(IntLiteral(2), [ExprStmt(FuncCall('printInt', [IntLiteral(2)])), BreakStmt()])], DefaultStmt([ExprStmt(FuncCall('printInt', [IntLiteral(0)]))]))]))])
    expected = '1' if 2 == 1 else '2' if 2 == 2 else '0'
    run_test(ast, expected)

def test_080():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(3)), SwitchStmt(Identifier('x'), [CaseStmt(IntLiteral(1), [ExprStmt(FuncCall('printInt', [IntLiteral(1)])), BreakStmt()]), CaseStmt(IntLiteral(2), [ExprStmt(FuncCall('printInt', [IntLiteral(2)])), BreakStmt()])], DefaultStmt([ExprStmt(FuncCall('printInt', [IntLiteral(0)]))]))]))])
    expected = '1' if 3 == 1 else '2' if 3 == 2 else '0'
    run_test(ast, expected)

def test_081():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(1)), SwitchStmt(Identifier('x'), [CaseStmt(IntLiteral(1), [ExprStmt(FuncCall('printInt', [IntLiteral(1)])), BreakStmt()]), CaseStmt(IntLiteral(2), [ExprStmt(FuncCall('printInt', [IntLiteral(2)])), BreakStmt()])], DefaultStmt([ExprStmt(FuncCall('printInt', [IntLiteral(0)]))]))]))])
    expected = '1' if 1 == 1 else '2' if 1 == 2 else '0'
    run_test(ast, expected)

def test_082():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(2)), SwitchStmt(Identifier('x'), [CaseStmt(IntLiteral(1), [ExprStmt(FuncCall('printInt', [IntLiteral(1)])), BreakStmt()]), CaseStmt(IntLiteral(2), [ExprStmt(FuncCall('printInt', [IntLiteral(2)])), BreakStmt()])], DefaultStmt([ExprStmt(FuncCall('printInt', [IntLiteral(0)]))]))]))])
    expected = '1' if 2 == 1 else '2' if 2 == 2 else '0'
    run_test(ast, expected)

def test_083():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(3)), SwitchStmt(Identifier('x'), [CaseStmt(IntLiteral(1), [ExprStmt(FuncCall('printInt', [IntLiteral(1)])), BreakStmt()]), CaseStmt(IntLiteral(2), [ExprStmt(FuncCall('printInt', [IntLiteral(2)])), BreakStmt()])], DefaultStmt([ExprStmt(FuncCall('printInt', [IntLiteral(0)]))]))]))])
    expected = '1' if 3 == 1 else '2' if 3 == 2 else '0'
    run_test(ast, expected)

def test_084():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(1)), SwitchStmt(Identifier('x'), [CaseStmt(IntLiteral(1), [ExprStmt(FuncCall('printInt', [IntLiteral(1)])), BreakStmt()]), CaseStmt(IntLiteral(2), [ExprStmt(FuncCall('printInt', [IntLiteral(2)])), BreakStmt()])], DefaultStmt([ExprStmt(FuncCall('printInt', [IntLiteral(0)]))]))]))])
    expected = '1' if 1 == 1 else '2' if 1 == 2 else '0'
    run_test(ast, expected)

def test_085():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(2)), SwitchStmt(Identifier('x'), [CaseStmt(IntLiteral(1), [ExprStmt(FuncCall('printInt', [IntLiteral(1)])), BreakStmt()]), CaseStmt(IntLiteral(2), [ExprStmt(FuncCall('printInt', [IntLiteral(2)])), BreakStmt()])], DefaultStmt([ExprStmt(FuncCall('printInt', [IntLiteral(0)]))]))]))])
    expected = '1' if 2 == 1 else '2' if 2 == 2 else '0'
    run_test(ast, expected)

def test_086():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(3)), SwitchStmt(Identifier('x'), [CaseStmt(IntLiteral(1), [ExprStmt(FuncCall('printInt', [IntLiteral(1)])), BreakStmt()]), CaseStmt(IntLiteral(2), [ExprStmt(FuncCall('printInt', [IntLiteral(2)])), BreakStmt()])], DefaultStmt([ExprStmt(FuncCall('printInt', [IntLiteral(0)]))]))]))])
    expected = '1' if 3 == 1 else '2' if 3 == 2 else '0'
    run_test(ast, expected)

def test_087():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(1)), SwitchStmt(Identifier('x'), [CaseStmt(IntLiteral(1), [ExprStmt(FuncCall('printInt', [IntLiteral(1)])), BreakStmt()]), CaseStmt(IntLiteral(2), [ExprStmt(FuncCall('printInt', [IntLiteral(2)])), BreakStmt()])], DefaultStmt([ExprStmt(FuncCall('printInt', [IntLiteral(0)]))]))]))])
    expected = '1' if 1 == 1 else '2' if 1 == 2 else '0'
    run_test(ast, expected)

def test_088():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(2)), SwitchStmt(Identifier('x'), [CaseStmt(IntLiteral(1), [ExprStmt(FuncCall('printInt', [IntLiteral(1)])), BreakStmt()]), CaseStmt(IntLiteral(2), [ExprStmt(FuncCall('printInt', [IntLiteral(2)])), BreakStmt()])], DefaultStmt([ExprStmt(FuncCall('printInt', [IntLiteral(0)]))]))]))])
    expected = '1' if 2 == 1 else '2' if 2 == 2 else '0'
    run_test(ast, expected)

def test_089():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(3)), SwitchStmt(Identifier('x'), [CaseStmt(IntLiteral(1), [ExprStmt(FuncCall('printInt', [IntLiteral(1)])), BreakStmt()]), CaseStmt(IntLiteral(2), [ExprStmt(FuncCall('printInt', [IntLiteral(2)])), BreakStmt()])], DefaultStmt([ExprStmt(FuncCall('printInt', [IntLiteral(0)]))]))]))])
    expected = '1' if 3 == 1 else '2' if 3 == 2 else '0'
    run_test(ast, expected)

def test_090():
    ast = Program([FuncDecl(VoidType(), 'main', [], BlockStmt([VarDecl(IntType(), 'x', IntLiteral(1)), SwitchStmt(Identifier('x'), [CaseStmt(IntLiteral(1), [ExprStmt(FuncCall('printInt', [IntLiteral(1)])), BreakStmt()]), CaseStmt(IntLiteral(2), [ExprStmt(FuncCall('printInt', [IntLiteral(2)])), BreakStmt()])], DefaultStmt([ExprStmt(FuncCall('printInt', [IntLiteral(0)]))]))]))])
    expected = '1' if 1 == 1 else '2' if 1 == 2 else '0'
    run_test(ast, expected)

def test_091():
    ast = Program([FuncDecl(IntType(), 'f', [], BlockStmt([ReturnStmt(IntLiteral(91))])), FuncDecl(VoidType(), 'main', [], BlockStmt([ExprStmt(FuncCall('printInt', [FuncCall('f', [])]))]))])
    run_test(ast, '91')

def test_092():
    ast = Program([FuncDecl(IntType(), 'f', [], BlockStmt([ReturnStmt(IntLiteral(92))])), FuncDecl(VoidType(), 'main', [], BlockStmt([ExprStmt(FuncCall('printInt', [FuncCall('f', [])]))]))])
    run_test(ast, '92')

def test_093():
    ast = Program([FuncDecl(IntType(), 'f', [], BlockStmt([ReturnStmt(IntLiteral(93))])), FuncDecl(VoidType(), 'main', [], BlockStmt([ExprStmt(FuncCall('printInt', [FuncCall('f', [])]))]))])
    run_test(ast, '93')

def test_094():
    ast = Program([FuncDecl(IntType(), 'f', [], BlockStmt([ReturnStmt(IntLiteral(94))])), FuncDecl(VoidType(), 'main', [], BlockStmt([ExprStmt(FuncCall('printInt', [FuncCall('f', [])]))]))])
    run_test(ast, '94')

def test_095():
    ast = Program([FuncDecl(IntType(), 'f', [], BlockStmt([ReturnStmt(IntLiteral(95))])), FuncDecl(VoidType(), 'main', [], BlockStmt([ExprStmt(FuncCall('printInt', [FuncCall('f', [])]))]))])
    run_test(ast, '95')

def test_096():
    ast = Program([FuncDecl(IntType(), 'f', [], BlockStmt([ReturnStmt(IntLiteral(96))])), FuncDecl(VoidType(), 'main', [], BlockStmt([ExprStmt(FuncCall('printInt', [FuncCall('f', [])]))]))])
    run_test(ast, '96')

def test_097():
    ast = Program([FuncDecl(IntType(), 'f', [], BlockStmt([ReturnStmt(IntLiteral(97))])), FuncDecl(VoidType(), 'main', [], BlockStmt([ExprStmt(FuncCall('printInt', [FuncCall('f', [])]))]))])
    run_test(ast, '97')

def test_098():
    ast = Program([FuncDecl(IntType(), 'f', [], BlockStmt([ReturnStmt(IntLiteral(98))])), FuncDecl(VoidType(), 'main', [], BlockStmt([ExprStmt(FuncCall('printInt', [FuncCall('f', [])]))]))])
    run_test(ast, '98')

def test_099():
    ast = Program([FuncDecl(IntType(), 'f', [], BlockStmt([ReturnStmt(IntLiteral(99))])), FuncDecl(VoidType(), 'main', [], BlockStmt([ExprStmt(FuncCall('printInt', [FuncCall('f', [])]))]))])
    run_test(ast, '99')

def test_100():
    ast = Program([FuncDecl(IntType(), 'f', [], BlockStmt([ReturnStmt(IntLiteral(100))])), FuncDecl(VoidType(), 'main', [], BlockStmt([ExprStmt(FuncCall('printInt', [FuncCall('f', [])]))]))])
    run_test(ast, '100')
