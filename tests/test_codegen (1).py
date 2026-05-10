"""
Test cases for TyC code generation.
"""

from src.utils.nodes import *
from tests.utils import CodeGenerator


def test_001():
    """Test 1: Hello World - print string"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printString", [StringLiteral("Hello World")]))
            ])
        )
    ])
    expected = "Hello World"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_002():
    """Test 2: Print integer"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [IntLiteral(42)]))
            ])
        )
    ])
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_003():
    """Test 3: Print float"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printFloat", [FloatLiteral(3.14)]))
            ])
        )
    ])
    expected = "3.14"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_004():
    """Test 4: Variable declaration and assignment"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "x", IntLiteral(10)),
                ExprStmt(FuncCall("printInt", [Identifier("x")]))
            ])
        )
    ])
    expected = "10"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_005():
    """Test 5: Binary operation - addition"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(IntLiteral(5), "+", IntLiteral(3))
                ]))
            ])
        )
    ])
    expected = "8"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_006():
    """Test 6: Binary operation - multiplication"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(IntLiteral(6), "*", IntLiteral(7))
                ]))
            ])
        )
    ])
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_007():
    """Test 7: If statement"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                IfStmt(
                    BinaryOp(IntLiteral(1), "<", IntLiteral(2)),
                    ExprStmt(FuncCall("printString", [StringLiteral("yes")])),
                    ExprStmt(FuncCall("printString", [StringLiteral("no")]))
                )
            ])
        )
    ])
    expected = "yes"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_008():
    """Test 8: While loop"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "i", IntLiteral(0)),
                WhileStmt(
                    BinaryOp(Identifier("i"), "<", IntLiteral(3)),
                    BlockStmt([
                        ExprStmt(FuncCall("printInt", [Identifier("i")])),
                        ExprStmt(AssignExpr(
                            Identifier("i"),
                            BinaryOp(Identifier("i"), "+", IntLiteral(1))
                        ))
                    ])
                )
            ])
        )
    ])
    expected = "012"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_009():
    """Test 9: Function call with return value"""
    ast = Program([
        FuncDecl(
            IntType(),
            "add",
            [Param(IntType(), "a"), Param(IntType(), "b")],
            BlockStmt([
                ReturnStmt(BinaryOp(Identifier("a"), "+", Identifier("b")))
            ])
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    FuncCall("add", [IntLiteral(20), IntLiteral(22)])
                ]))
            ])
        )
    ])
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_010():
    """Test 10: Multiple statements - arithmetic operations"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "x", IntLiteral(10)),
                VarDecl(IntType(), "y", IntLiteral(20)),
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(Identifier("x"), "+", Identifier("y"))
                ]))
            ])
        )
    ])
    expected = "30"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


# ---------------------------------------------------------------------------
# Extended generated cases: test_011 through test_200.
# ---------------------------------------------------------------------------

_next_codegen_case = 11


def _main(stmts):
    return Program([FuncDecl(VoidType(), "main", [], BlockStmt(stmts))])


def _pint(expr):
    return ExprStmt(FuncCall("printInt", [expr]))


def _pfloat(expr):
    return ExprStmt(FuncCall("printFloat", [expr]))


def _pstr(expr):
    return ExprStmt(FuncCall("printString", [expr]))


def _case(name, ast, expected):
    global _next_codegen_case
    idx = _next_codegen_case
    _next_codegen_case += 1

    def test():
        result = CodeGenerator().generate_and_run(ast)
        assert result == expected, f"Expected '{expected}', got '{result}'"

    test.__name__ = f"test_{idx:03d}_{name}"
    test.__doc__ = f"Generated codegen case {idx}: {name}"
    globals()[test.__name__] = test


# 20 integer literal / print cases.
for _i in range(20):
    _case(
        f"int_literal_{_i}",
        _main([_pint(IntLiteral(_i - 5))]),
        str(_i - 5),
    )


# 30 integer arithmetic cases.
for _i in range(10):
    _case(
        f"int_add_{_i}",
        _main([_pint(BinaryOp(IntLiteral(_i), "+", IntLiteral(_i + 2)))]),
        str(_i + _i + 2),
    )
for _i in range(10):
    _case(
        f"int_sub_{_i}",
        _main([_pint(BinaryOp(IntLiteral(_i + 10), "-", IntLiteral(_i)))]),
        "10",
    )
for _i in range(10):
    _case(
        f"int_mul_div_mod_{_i}",
        _main([
            _pint(BinaryOp(IntLiteral(_i + 2), "*", IntLiteral(3))),
            _pint(BinaryOp(IntLiteral((_i + 2) * 6), "/", IntLiteral(3))),
            _pint(BinaryOp(IntLiteral(_i + 10), "%", IntLiteral(4))),
        ]),
        f"{(_i + 2) * 3}{(_i + 2) * 2}{(_i + 10) % 4}",
    )


# 20 comparison cases.
_comparison_ops = [
    ("<", 1, 2, 1),
    ("<", 2, 1, 0),
    ("<=", 2, 2, 1),
    ("<=", 3, 2, 0),
    (">", 3, 2, 1),
    (">", 2, 3, 0),
    (">=", 3, 3, 1),
    (">=", 2, 3, 0),
    ("==", 4, 4, 1),
    ("==", 4, 5, 0),
    ("!=", 4, 5, 1),
    ("!=", 4, 4, 0),
    ("<", -2, -1, 1),
    (">", -2, -1, 0),
    ("<=", -1, -1, 1),
    (">=", -1, -2, 1),
    ("==", 0, 0, 1),
    ("!=", 0, 1, 1),
    ("<", 100, 20, 0),
    (">", 100, 20, 1),
]
for _idx, (_op, _lhs, _rhs, _expected) in enumerate(_comparison_ops):
    _case(
        f"comparison_{_idx}",
        _main([_pint(BinaryOp(IntLiteral(_lhs), _op, IntLiteral(_rhs)))]),
        str(_expected),
    )


# 15 logical and unary cases.
_logical_cases = [
    (BinaryOp(IntLiteral(1), "&&", IntLiteral(1)), "1"),
    (BinaryOp(IntLiteral(0), "&&", IntLiteral(1)), "0"),
    (BinaryOp(IntLiteral(3), "&&", IntLiteral(2)), "1"),
    (BinaryOp(IntLiteral(1), "||", IntLiteral(0)), "1"),
    (BinaryOp(IntLiteral(0), "||", IntLiteral(0)), "0"),
    (BinaryOp(IntLiteral(0), "||", IntLiteral(7)), "1"),
    (PrefixOp("!", IntLiteral(0)), "1"),
    (PrefixOp("!", IntLiteral(1)), "0"),
    (PrefixOp("-", IntLiteral(8)), "-8"),
    (PrefixOp("+", IntLiteral(8)), "8"),
    (BinaryOp(PrefixOp("!", IntLiteral(0)), "&&", IntLiteral(1)), "1"),
    (BinaryOp(PrefixOp("!", IntLiteral(1)), "||", IntLiteral(9)), "1"),
    (BinaryOp(IntLiteral(1), "&&", PrefixOp("!", IntLiteral(0))), "1"),
    (BinaryOp(IntLiteral(0), "||", PrefixOp("!", IntLiteral(1))), "0"),
    (BinaryOp(IntLiteral(5), "&&", PrefixOp("!", IntLiteral(0))), "1"),
]
for _idx, (_expr, _expected) in enumerate(_logical_cases):
    _case(f"logical_unary_{_idx}", _main([_pint(_expr)]), _expected)


# 20 variable, assignment, auto, shadowing, and increment cases.
for _i in range(5):
    _case(
        f"var_explicit_{_i}",
        _main([
            VarDecl(IntType(), "x", IntLiteral(_i)),
            ExprStmt(AssignExpr(Identifier("x"), BinaryOp(Identifier("x"), "+", IntLiteral(10)))),
            _pint(Identifier("x")),
        ]),
        str(_i + 10),
    )
for _i in range(5):
    _case(
        f"var_auto_init_{_i}",
        _main([
            VarDecl(None, "x", IntLiteral(_i + 1)),
            VarDecl(None, "y", BinaryOp(Identifier("x"), "*", IntLiteral(2))),
            _pint(Identifier("y")),
        ]),
        str((_i + 1) * 2),
    )
for _i in range(5):
    _case(
        f"var_auto_late_{_i}",
        _main([
            VarDecl(None, "x"),
            ExprStmt(AssignExpr(Identifier("x"), IntLiteral(_i + 3))),
            _pint(Identifier("x")),
        ]),
        str(_i + 3),
    )
for _i in range(5):
    _case(
        f"var_shadow_increment_{_i}",
        _main([
            VarDecl(IntType(), "x", IntLiteral(_i)),
            BlockStmt([
                VarDecl(IntType(), "x", IntLiteral(20 + _i)),
                ExprStmt(PrefixOp("++", Identifier("x"))),
                _pint(Identifier("x")),
            ]),
            _pint(Identifier("x")),
        ]),
        f"{21 + _i}{_i}",
    )


# 25 control-flow cases.
for _i in range(5):
    _case(
        f"if_then_{_i}",
        _main([
            IfStmt(
                BinaryOp(IntLiteral(_i), "<", IntLiteral(10)),
                _pint(IntLiteral(1)),
                _pint(IntLiteral(0)),
            )
        ]),
        "1",
    )
for _i in range(5):
    _case(
        f"if_else_{_i}",
        _main([
            IfStmt(
                BinaryOp(IntLiteral(_i + 20), "<", IntLiteral(10)),
                _pint(IntLiteral(1)),
                _pint(IntLiteral(0)),
            )
        ]),
        "0",
    )
for _i in range(5):
    _case(
        f"while_count_{_i}",
        _main([
            VarDecl(IntType(), "i", IntLiteral(0)),
            WhileStmt(
                BinaryOp(Identifier("i"), "<", IntLiteral(_i)),
                BlockStmt([
                    _pint(Identifier("i")),
                    ExprStmt(PrefixOp("++", Identifier("i"))),
                ]),
            ),
        ]),
        "".join(str(n) for n in range(_i)),
    )
for _i in range(5):
    _case(
        f"for_count_{_i}",
        _main([
            ForStmt(
                VarDecl(IntType(), "i", IntLiteral(0)),
                BinaryOp(Identifier("i"), "<", IntLiteral(_i)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([_pint(Identifier("i"))]),
            )
        ]),
        "".join(str(n) for n in range(_i)),
    )
for _i in range(5):
    _case(
        f"switch_break_{_i}",
        _main([
            VarDecl(IntType(), "x", IntLiteral(_i % 4)),
            SwitchStmt(
                Identifier("x"),
                [
                    CaseStmt(IntLiteral(0), [_pint(IntLiteral(0)), BreakStmt()]),
                    CaseStmt(IntLiteral(1), [_pint(IntLiteral(1)), BreakStmt()]),
                    CaseStmt(IntLiteral(2), [_pint(IntLiteral(2)), BreakStmt()]),
                ],
                DefaultStmt([_pint(IntLiteral(9))]),
            ),
        ]),
        str(_i % 4 if _i % 4 < 3 else 9),
    )


# 20 function call and return cases.
for _i in range(5):
    _case(
        f"func_explicit_add_{_i}",
        Program([
            FuncDecl(
                IntType(),
                "add",
                [Param(IntType(), "a"), Param(IntType(), "b")],
                BlockStmt([ReturnStmt(BinaryOp(Identifier("a"), "+", Identifier("b")))]),
            ),
            FuncDecl(
                VoidType(),
                "main",
                [],
                BlockStmt([_pint(FuncCall("add", [IntLiteral(_i), IntLiteral(_i + 10)]))]),
            ),
        ]),
        str(_i + _i + 10),
    )
for _i in range(5):
    _case(
        f"func_inferred_mul_{_i}",
        Program([
            FuncDecl(
                None,
                "mul",
                [Param(IntType(), "a"), Param(IntType(), "b")],
                BlockStmt([ReturnStmt(BinaryOp(Identifier("a"), "*", Identifier("b")))]),
            ),
            FuncDecl(
                VoidType(),
                "main",
                [],
                BlockStmt([_pint(FuncCall("mul", [IntLiteral(_i + 1), IntLiteral(3)]))]),
            ),
        ]),
        str((_i + 1) * 3),
    )
for _i in range(5):
    _case(
        f"func_void_call_{_i}",
        Program([
            FuncDecl(
                VoidType(),
                "show",
                [Param(IntType(), "x")],
                BlockStmt([_pint(Identifier("x"))]),
            ),
            FuncDecl(
                VoidType(),
                "main",
                [],
                BlockStmt([ExprStmt(FuncCall("show", [IntLiteral(_i + 4)]))]),
            ),
        ]),
        str(_i + 4),
    )
for _i in range(5):
    _case(
        f"func_forward_inferred_{_i}",
        Program([
            FuncDecl(
                None,
                "f",
                [],
                BlockStmt([ReturnStmt(FuncCall("g", []))]),
            ),
            FuncDecl(
                None,
                "g",
                [],
                BlockStmt([ReturnStmt(IntLiteral(_i + 6))]),
            ),
            FuncDecl(
                VoidType(),
                "main",
                [],
                BlockStmt([_pint(FuncCall("f", []))]),
            ),
        ]),
        str(_i + 6),
    )


# 15 float cases.
for _i in range(5):
    _case(
        f"float_literal_{_i}",
        _main([_pfloat(FloatLiteral(float(_i) + 0.5))]),
        str(float(_i) + 0.5),
    )
for _i in range(5):
    _case(
        f"float_mixed_add_{_i}",
        _main([_pfloat(BinaryOp(IntLiteral(_i), "+", FloatLiteral(2.5)))]),
        str(float(_i) + 2.5),
    )
for _i in range(5):
    _case(
        f"float_compare_{_i}",
        _main([_pint(BinaryOp(FloatLiteral(float(_i) + 0.5), ">", IntLiteral(_i)))]),
        "1",
    )


# 10 string cases.
for _i in range(5):
    _case(
        f"string_literal_{_i}",
        _main([_pstr(StringLiteral(f"s{_i}"))]),
        f"s{_i}",
    )
for _i in range(5):
    _case(
        f"string_var_{_i}",
        _main([
            VarDecl(StringType(), "s", StringLiteral(f"v{_i}")),
            _pstr(Identifier("s")),
        ]),
        f"v{_i}",
    )


# 15 struct cases.
for _i in range(5):
    _case(
        f"struct_literal_member_{_i}",
        Program([
            StructDecl("Point", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
            FuncDecl(
                VoidType(),
                "main",
                [],
                BlockStmt([
                    VarDecl(StructType("Point"), "p", StructLiteral([IntLiteral(_i), IntLiteral(_i + 1)])),
                    _pint(MemberAccess(Identifier("p"), "x")),
                    _pint(MemberAccess(Identifier("p"), "y")),
                ]),
            ),
        ]),
        f"{_i}{_i + 1}",
    )
for _i in range(5):
    _case(
        f"struct_member_assign_{_i}",
        Program([
            StructDecl("Point", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
            FuncDecl(
                VoidType(),
                "main",
                [],
                BlockStmt([
                    VarDecl(StructType("Point"), "p"),
                    ExprStmt(AssignExpr(MemberAccess(Identifier("p"), "x"), IntLiteral(_i + 7))),
                    _pint(MemberAccess(Identifier("p"), "x")),
                ]),
            ),
        ]),
        str(_i + 7),
    )
for _i in range(5):
    _case(
        f"struct_nested_{_i}",
        Program([
            StructDecl("A", [MemberDecl(IntType(), "x")]),
            StructDecl("B", [MemberDecl(StructType("A"), "a")]),
            FuncDecl(
                VoidType(),
                "main",
                [],
                BlockStmt([
                    VarDecl(StructType("B"), "b", StructLiteral([StructLiteral([IntLiteral(_i + 2)])])),
                    _pint(MemberAccess(MemberAccess(Identifier("b"), "a"), "x")),
                ]),
            ),
        ]),
        str(_i + 2),
    )


assert _next_codegen_case == 201

