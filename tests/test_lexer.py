import unittest
from tests.utils import Tokenizer

try:
    import lexererr
    from lexererr import UncloseString, IllegalEscape, ErrorToken
except ImportError:
    try:
        from build.lexererr import UncloseString, IllegalEscape, ErrorToken
    except ImportError:
        class UncloseString(Exception): pass
        class IllegalEscape(Exception): pass
        class ErrorToken(Exception): pass

class LexerSuite(unittest.TestCase):

    def check(self, inp, expected, test_id):
        try:
            actual = Tokenizer(inp).get_tokens_as_string()
            self.assertEqual(actual, expected, f"Test {test_id} Failed: Exp '{expected}', Got '{actual}'")
        except UncloseString:
            self.assertEqual("<unclosed string>", expected, f"Test {test_id} Failed: Caught UncloseString")
        except IllegalEscape:
            self.assertEqual("<wrong string>", expected, f"Test {test_id} Failed: Caught IllegalEscape")
        except ErrorToken:
            if "<unrecognized char>" in expected: return
            self.fail(f"Test {test_id} Failed: Caught ErrorToken but exp '{expected}'")

    # Group 1: Keywords
    def test_001(self): self.check("auto",     "K_AUTO,auto,EOF",         101)
    def test_002(self): self.check("break",    "K_BREAK,break,EOF",       102)
    def test_003(self): self.check("case",     "K_CASE,case,EOF",         103)
    def test_004(self): self.check("continue", "K_CONTINUE,continue,EOF", 104)
    def test_005(self): self.check("default",  "K_DEFAULT,default,EOF",   105)
    def test_006(self): self.check("else",     "K_ELSE,else,EOF",         106)
    def test_007(self): self.check("float",    "K_FLOAT,float,EOF",       107)
    def test_008(self): self.check("for",      "K_FOR,for,EOF",           108)
    def test_009(self): self.check("if",       "K_IF,if,EOF",             109)
    def test_010(self): self.check("int",      "K_INT,int,EOF",           110)
    def test_011(self): self.check("return",   "K_RETURN,return,EOF",     111)
    def test_012(self): self.check("string",   "K_STRING,string,EOF",     112)
    def test_013(self): self.check("struct",   "K_STRUCT,struct,EOF",     113)
    def test_014(self): self.check("switch",   "K_SWITCH,switch,EOF",     114)
    def test_015(self): self.check("void",     "K_VOID,void,EOF",         115)
    def test_016(self): self.check("while",    "K_WHILE,while,EOF",       116)

    # Group 2: Operators & Separators
    def test_017(self): self.check("+",  "ADD,+,EOF",      117)
    def test_018(self): self.check("-",  "SUB,-,EOF",      118)
    def test_019(self): self.check("*",  "MUL,*,EOF",      119)
    def test_020(self): self.check("/",  "DIV,/,EOF",      120)
    def test_021(self): self.check("%",  "MOD,%,EOF",      121)
    def test_022(self): self.check("==", "EQ,==,EOF",      122)
    def test_023(self): self.check("!=", "NEQ,!=,EOF",     123)
    def test_024(self): self.check("<",  "LT,<,EOF",       124)
    def test_025(self): self.check(">",  "GT,>,EOF",       125)
    def test_026(self): self.check("<=", "LE,<=,EOF",      126)
    def test_027(self): self.check(">=", "GE,>=,EOF",      127)
    def test_028(self): self.check("&&", "AND,&&,EOF",     128)
    def test_029(self): self.check("||", "OR,||,EOF",      129)
    def test_030(self): self.check("!",  "NOT,!,EOF",      130)
    def test_031(self): self.check("=",  "ASSIGN,=,EOF",   131)
    def test_032(self): self.check(".",  "DOT,.,EOF",      132)
    def test_033(self): self.check("(",  "LPAR,(,EOF",     133)
    def test_034(self): self.check(")",  "RPAR,),EOF",     134)
    def test_035(self): self.check("{",  "LBRACE,{,EOF",   135)
    def test_036(self): self.check(";",  "SEMI,;,EOF",     136)

    # Group 3: Literals & Identifiers
    def test_037(self): self.check("0",       "INT_LIT,0,EOF",       137)
    def test_038(self): self.check("999",     "INT_LIT,999,EOF",     138)
    def test_039(self): self.check("1.23",    "FLOAT_LIT,1.23,EOF",  139)
    def test_040(self): self.check(".5",      "FLOAT_LIT,.5,EOF",    140)
    def test_041(self): self.check("1.",      "FLOAT_LIT,1.,EOF",    141)
    def test_042(self): self.check("1e5",     "FLOAT_LIT,1e5,EOF",   142)
    def test_043(self): self.check("1.2e-3",  "FLOAT_LIT,1.2e-3,EOF",143)
    def test_044(self): self.check("0.0",     "FLOAT_LIT,0.0,EOF",   144)
    def test_045(self): self.check("x",       "ID,x,EOF",            145)
    def test_046(self): self.check("myVar",   "ID,myVar,EOF",        146)
    def test_047(self): self.check("_start",  "ID,_start,EOF",       147)
    def test_048(self): self.check("end_",    "ID,end_,EOF",         148)
    def test_049(self): self.check("v2",      "ID,v2,EOF",           149)
    def test_050(self): self.check("MAX_LEN", "ID,MAX_LEN,EOF",      150)
    def test_051(self): self.check('"Hello"', "STRING_LIT,Hello,EOF", 151)
    def test_052(self): self.check('""',      "STRING_LIT,,EOF",      152)
    def test_053(self): self.check(r'"\n"',   r'STRING_LIT,\n,EOF',   153)
    def test_054(self): self.check(r'"\t"',   r'STRING_LIT,\t,EOF',   154)
    def test_055(self): self.check(r'"\\"',   r'STRING_LIT,\\,EOF',   155)
    def test_056(self): self.check(r'"\""',   r'STRING_LIT,\",EOF',   156)
    def test_057(self): self.check(r'"a b"',  r'STRING_LIT,a b,EOF',  157)
    def test_058(self): self.check(r'"123"',  r'STRING_LIT,123,EOF',  158)
    def test_059(self): self.check(r'"a\tb"', r'STRING_LIT,a\tb,EOF', 159)
    def test_060(self): self.check(r'"\b\f"', r'STRING_LIT,\b\f,EOF', 160)

    # Group 4: Errors
    def test_061(self): self.check('"open',    "<unclosed string>",   161)
    def test_062(self): self.check('"a\n"',    "<unclosed string>",   162)
    def test_063(self): self.check(r'"\k"',    "<wrong string>",      163)
    def test_064(self): self.check(r'"\1"',    "<wrong string>",      164)
    def test_065(self): self.check(r'"\ "',    "<wrong string>",      165)
    def test_066(self): self.check("@",        "<unrecognized char>", 166)
    def test_067(self): self.check("#",        "<unrecognized char>", 167)
    def test_068(self): self.check("$",        "<unrecognized char>", 168)
    def test_069(self): self.check("`",        "<unrecognized char>", 169)
    def test_070(self): self.check("?",        "<unrecognized char>", 170)

    # Group 5: Complex & Variations
    def test_071(self): self.check("int x;",    "K_INT,int,ID,x,SEMI,;,EOF", 171)
    def test_072(self): self.check("x = 1;",    "ID,x,ASSIGN,=,INT_LIT,1,SEMI,;,EOF", 172)
    def test_073(self): self.check("auto y=2;", "K_AUTO,auto,ID,y,ASSIGN,=,INT_LIT,2,SEMI,;,EOF", 173)
    def test_074(self): self.check("return;",   "K_RETURN,return,SEMI,;,EOF", 174)
    def test_075(self): self.check("if(x)",     "K_IF,if,LPAR,(,ID,x,RPAR,),EOF", 175)
    def test_076(self): self.check("{ }",       "LBRACE,{,RBRACE,},EOF", 176)
    def test_077(self): self.check("a+b",       "ID,a,ADD,+,ID,b,EOF", 177)
    def test_078(self): self.check("a*b",       "ID,a,MUL,*,ID,b,EOF", 178)
    def test_079(self): self.check("a/b",       "ID,a,DIV,/,ID,b,EOF", 179)
    def test_080(self): self.check("a%b",       "ID,a,MOD,%,ID,b,EOF", 180)
    def test_081(self): self.check("a==b",      "ID,a,EQ,==,ID,b,EOF", 181)
    def test_082(self): self.check("a!=b",      "ID,a,NEQ,!=,ID,b,EOF", 182)
    def test_083(self): self.check("!x",        "NOT,!,ID,x,EOF", 183)
    def test_084(self): self.check("x++",       "ID,x,INC,++,EOF", 184)
    def test_085(self): self.check("--y",       "DEC,--,ID,y,EOF", 185)
    def test_086(self): self.check("p.x",       "ID,p,DOT,.,ID,x,EOF", 186)
    def test_087(self): self.check("[1,2]",     "LBRA,[,INT_LIT,1,COMMA,,,INT_LIT,2,RBRA,],EOF", 187)
    def test_088(self): self.check("f()",       "ID,f,LPAR,(,RPAR,),EOF", 188)
    def test_089(self): self.check("s: 1",      "ID,s,COLON,:,INT_LIT,1,EOF", 189)
    def test_090(self): self.check("/*c*/",     "EOF", 190)
    def test_091(self): self.check("// c\n",    "EOF", 191)
    def test_092(self): self.check("  x  ",     "ID,x,EOF", 192)
    def test_093(self): self.check("\tx\n",     "ID,x,EOF", 193)
    def test_094(self): self.check("a >= b",    "ID,a,GE,>=,ID,b,EOF", 194)
    def test_095(self): self.check("a <= b",    "ID,a,LE,<=,ID,b,EOF", 195)
    def test_096(self): self.check("a && b",    "ID,a,AND,&&,ID,b,EOF", 196)
    def test_097(self): self.check("a || b",    "ID,a,OR,||,ID,b,EOF", 197)
    def test_098(self): self.check("struct A{}", "K_STRUCT,struct,ID,A,LBRACE,{,RBRACE,},EOF", 198)
    def test_099(self): self.check('""+""',     "STRING_LIT,,ADD,+,STRING_LIT,,EOF", 199)
    def test_100(self): self.check("1.2E+2",    "FLOAT_LIT,1.2E+2,EOF", 200)