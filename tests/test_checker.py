from tests.utils import Checker

def test_001():
    source = "void main() { int x = 5; int y = x + 1; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_002():
    source = "void main() { auto x = 10; auto y = 3.14; auto z = x + y; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_003():
    source = "int add(int x, int y) { return x + y; } void main() { int sum = add(5, 3); }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_004():
    source = "struct Point { int x; int y; }; void main() { Point p; p.x = 10; p.y = 20; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_005():
    source = "void main() { int x = 10; { int y = 20; int z = x + y; } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_006():
    source = "void main() { int x = 1; float x = 2.0; }"
    assert Checker(source).check_from_source() == "Redeclared(Variable, x)"

def test_007():
    source = "int f() { return 1; } float f() { return 2.0; } void main() {}"
    assert Checker(source).check_from_source() == "Redeclared(Function, f)"

def test_008():
    source = "struct A { int x; }; struct A { float y; }; void main() {}"
    assert Checker(source).check_from_source() == "Redeclared(Struct, A)"

def test_009():
    source = "void f(int a, float a) {} void main() {}"
    assert Checker(source).check_from_source() == "Redeclared(Parameter, a)"

def test_010():
    source = "struct A { int x; float x; }; void main() {}"
    assert Checker(source).check_from_source() == "Redeclared(Member, x)"

def test_011():
    source = "void main() { int x = y + 1; }"
    assert Checker(source).check_from_source() == "UndeclaredIdentifier(y)"

def test_012():
    source = "void main() { foo(); }"
    assert Checker(source).check_from_source() == "UndeclaredFunction(foo)"

def test_013():
    source = "void main() { UnknownStruct p; }"
    assert Checker(source).check_from_source() == "UndeclaredStruct(UnknownStruct)"

def test_014():
    source = "void main() { auto x; auto y; x = y; }"
    assert "TypeCannotBeInferred" in Checker(source).check_from_source()

def test_015():
    source = "void main() { auto x; }"
    assert "TypeCannotBeInferred" in Checker(source).check_from_source()

def test_016():
    source = "void main() { auto a; auto b; int c = a + b; }"
    assert "TypeCannotBeInferred" in Checker(source).check_from_source()

def test_017():
    source = "void main() { float f = 1.0; if (f) { } }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_018():
    source = "void main() { string s = \"hi\"; while (s) { } }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_019():
    source = "void main() { int x; x = 3.14; }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_020():
    source = "void main() { return 1; }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_021():
    source = "int f() { return 3.14; } void main() {}"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_022():
    source = "void main() { string s = \"a\" + \"b\"; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_023():
    source = "void main() { int x = 5 % 1.2; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_024():
    source = "void main() { int x = 1.0 && 2.0; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_025():
    source = "void main() { int x = 1; int y = x.a; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_026():
    source = "void f(int x) {} void main() { f(3.14); }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_027():
    source = "void main() { break; }"
    assert Checker(source).check_from_source() == "MustInLoop(BreakStmt())"

def test_028():
    source = "void main() { if (1) { continue; } }"
    assert Checker(source).check_from_source() == "MustInLoop(ContinueStmt())"

def test_029():
    source = "struct A { int x; }; struct B { A a; }; void main() { B b; b.a.x = 10; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_030():
    source = "void main() { auto x = 1; auto y = 2.5; auto z = x + y; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_031():
    source = "int f() { return 1; } void main() { auto x = f(); }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_032():
    source = "void main() { int x = 0; for(auto i=0; i<10; i++) { x = x + i; } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_033():
    source = "void main() { switch(1+2) { case 3: printInt(3); break; default: break; } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_034():
    source = "void main() { int x = 5; if (x > 0) if (x < 10) x++; else x--; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_035():
    source = "int fact(int n) { if (n<=1) return 1; return n * fact(n-1); } void main() {}"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_036():
    source = "void main() { int a; int b; int c; a = b = c = 10; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_037():
    source = "void main() { auto x; x = 10; auto y; y = x + 5.5; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_038():
    source = "void main() { int x = 10; { int x = 20; { int x = 30; } } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_039():
    source = "void main() { while(1) { if (1) break; else continue; } }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_040():
    source = "struct Point { int x; int y; }; void main() { Point p = {1, 2}; }"
    assert Checker(source).check_from_source() == "Static checking passed"

def test_041():
    source = "void main() { int a; float a; }"
    assert Checker(source).check_from_source() == "Redeclared(Variable, a)"

def test_042():
    source = "void main() { string s; string s; }"
    assert Checker(source).check_from_source() == "Redeclared(Variable, s)"

def test_043():
    source = "void f(int param) { int param; }"
    assert Checker(source).check_from_source() == "Redeclared(Variable, param)"

def test_044():
    source = "struct Test { int a; float a; }; void main() {}"
    assert Checker(source).check_from_source() == "Redeclared(Member, a)"

def test_045():
    source = "int myFunc() {return 1;} float myFunc() {return 1.0;} void main() {}"
    assert Checker(source).check_from_source() == "Redeclared(Function, myFunc)"

def test_046():
    source = "struct Data {}; struct Data { int x; }; void main() {}"
    assert Checker(source).check_from_source() == "Redeclared(Struct, Data)"

def test_047():
    source = "void f(int x, int x) {} void main() {}"
    assert Checker(source).check_from_source() == "Redeclared(Parameter, x)"

def test_048():
    source = "void main() { for(int i=0; i<10; i++) { int j = 1; int j = 2; } }"
    assert Checker(source).check_from_source() == "Redeclared(Variable, j)"

def test_049():
    source = "void main() { auto x = 1; auto x = 2; }"
    assert Checker(source).check_from_source() == "Redeclared(Variable, x)"

def test_050():
    source = "void main() { int abc; float abc = 1.0; }"
    assert Checker(source).check_from_source() == "Redeclared(Variable, abc)"

def test_051():
    source = "void main() { x = 10; }"
    assert Checker(source).check_from_source() == "UndeclaredIdentifier(x)"

def test_052():
    source = "void main() { int y = x + 1; }"
    assert Checker(source).check_from_source() == "UndeclaredIdentifier(x)"

def test_053():
    source = "void main() { printInt(undefinedVar); }"
    assert Checker(source).check_from_source() == "UndeclaredIdentifier(undefinedVar)"

def test_054():
    source = "void main() { notExistFunc(); }"
    assert Checker(source).check_from_source() == "UndeclaredFunction(notExistFunc)"

def test_055():
    source = "void main() { auto x = getSomething(); }"
    assert Checker(source).check_from_source() == "UndeclaredFunction(getSomething)"

def test_056():
    source = "void f(UnknownType p) {} void main() {}"
    assert Checker(source).check_from_source() == "UndeclaredStruct(UnknownType)"

def test_057():
    source = "UnknownReturn f() {} void main() {}"
    assert Checker(source).check_from_source() == "UndeclaredStruct(UnknownReturn)"

def test_058():
    source = "struct A { MissingStruct x; }; void main() {}"
    assert Checker(source).check_from_source() == "UndeclaredStruct(MissingStruct)"

def test_059():
    source = "void main() { { int x = 1; } int y = x; }"
    assert Checker(source).check_from_source() == "UndeclaredIdentifier(x)"

def test_060():
    source = "void main() { for(int i=0; i<1; i++) {} i = 5; }"
    assert Checker(source).check_from_source() == "UndeclaredIdentifier(i)"

def test_061():
    source = "void main() { auto x; auto y = x; }"
    assert "TypeCannotBeInferred" in Checker(source).check_from_source()

def test_062():
    source = "void main() { auto a; auto b; auto c = a == b; }"
    assert "TypeCannotBeInferred" in Checker(source).check_from_source()

def test_063():
    source = "void main() { auto x; if (x) {} }"
    assert "TypeCannotBeInferred" in Checker(source).check_from_source()

def test_064():
    source = "void main() { auto x; auto y; while (x < y) {} }"
    assert "TypeCannotBeInferred" in Checker(source).check_from_source()

def test_065():
    source = "void main() { auto x; auto y; printInt(x + y); }"
    assert "TypeCannotBeInferred" in Checker(source).check_from_source()

def test_066():
    source = "f() { auto x; return x; } void main() {}"
    assert "TypeCannotBeInferred" in Checker(source).check_from_source()

def test_067():
    source = "void main() { auto i; auto j; for(; i<j;) {} }"
    assert "TypeCannotBeInferred" in Checker(source).check_from_source()

def test_068():
    source = "void main() { auto x; switch(x) {} }"
    assert "TypeCannotBeInferred" in Checker(source).check_from_source()

def test_069():
    source = "void main() { auto x; int y = -x; }"
    assert "TypeCannotBeInferred" in Checker(source).check_from_source()

def test_070():
    source = "void main() { { auto z; } }"
    assert "TypeCannotBeInferred" in Checker(source).check_from_source()

def test_071():
    source = "void main() { if (\"true\") {} }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_072():
    source = "void main() { while (3.14) {} }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_073():
    source = "void main() { for(; \"cond\";) {} }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_074():
    source = "void main() { switch(2.5) { case 1: break; } }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_075():
    source = "void main() { switch(1) { case 2.5: break; } }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_076():
    source = "void main() { int x; x = \"string\"; }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_077():
    source = "struct A {int x;}; struct B {int x;}; void main() { A a; B b; a = b; }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_078():
    source = "int f() { return 1.5; } void main() {}"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_079():
    source = "void f() { return 1; } void main() {}"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_080():
    source = "f() { return 1; return 1.5; } void main() {}"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_081():
    source = "void main() { int x = 1 + \"a\"; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_082():
    source = "void main() { float x = 2.5 % 1; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_083():
    source = "void main() { int x = 1 && 2.5; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_084():
    source = "void main() { int x = !3.14; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_085():
    source = "void main() { float x = 1.0; x++; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_086():
    source = "void main() { int x = 1; ++1; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_087():
    source = "void main() { int x = 1; (x+1)++; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_088():
    source = "void main() { string s1 = \"a\"; string s2 = \"b\"; int x = s1 == s2; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_089():
    source = "void main() { int x = 5; int y = x.member; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_090():
    source = "struct A {int x;}; void main() { A a; int y = a.notExist; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_091():
    source = "void f(int a) {} void main() { f(1.5); }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_092():
    source = "void f(int a) {} void main() { f(1, 2); }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_093():
    source = "void main() { int x; int y = (x = \"hi\") + 1; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_094():
    source = "void main() { int x = 1; int y = (x = 3.14) + 1; }"
    assert "TypeMismatchInExpression" in Checker(source).check_from_source()

def test_095():
    source = "struct A {int x;}; void main() { A a; a.x = 1.5; }"
    assert "TypeMismatchInStatement" in Checker(source).check_from_source()

def test_096():
    source = "void main() { if (1) break; }"
    assert "MustInLoop" in Checker(source).check_from_source()

def test_097():
    source = "void main() { switch(1) { case 1: continue; } }"
    assert "MustInLoop" in Checker(source).check_from_source()

def test_098():
    source = "void helper() { break; } void main() { while(1) helper(); }"
    assert "MustInLoop" in Checker(source).check_from_source()

def test_099():
    source = "void main() { { continue; } }"
    assert "MustInLoop" in Checker(source).check_from_source()

def test_100():
    source = "struct Node { int val; }; int check(int a) { return a * 2; } void main() { Node n = {10}; auto flag = 0; for(auto i = 0; i < 10; i++) { if (i % 2 == 0) continue; if (check(i) > n.val) { flag = 1; break; } } }"
    assert Checker(source).check_from_source() == "Static checking passed"



