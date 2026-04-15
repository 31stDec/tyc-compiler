grammar TyC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:
        result = super().emit()
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit()
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        result = super().emit()
        raise ErrorToken(result.text)
    else:
        return super().emit()
}

options {
    language=Python3;
}

// ======================================================
// PARSER RULES
// ======================================================

// Program Structure (Modified: allow empty program)
program: (structDecl | funcDecl)* EOF;

// Struct Declaration
structDecl: K_STRUCT ID LBRACE structMember* RBRACE SEMI;
structMember: type ID SEMI;

// Function Declaration
funcDecl:
    (type | K_VOID) ID LPAR paramList? RPAR blockStmt  # ExplicitFuncDecl
  | ID LPAR paramList? RPAR blockStmt                  # InferredFuncDecl
  ;

paramList: param (COMMA param)*;
param: type ID;

// Types
type: K_INT | K_FLOAT | K_STRING | ID;

// Statements
stmt:
    blockStmt
  | varDeclStmt
  | ifStmt
  | whileStmt
  | forStmt
  | switchStmt
  | breakStmt
  | continueStmt
  | returnStmt
  | exprStmt
  | SEMI
  ;

blockStmt: LBRACE stmt* RBRACE;

// Variable Declaration
varDeclStmt:
    K_AUTO ID (ASSIGN expr)? SEMI  # AutoDecl
  | type ID (ASSIGN expr)? SEMI    # ExplicitDecl
  ;

// Control Flow
ifStmt: K_IF LPAR expr RPAR stmt (K_ELSE stmt)?;

whileStmt: K_WHILE LPAR expr RPAR stmt;

forStmt: K_FOR LPAR forInit expr? SEMI expr? RPAR stmt;

forInit: varDeclStmt | exprStmt | SEMI;

// Switch Case
switchStmt: K_SWITCH LPAR expr RPAR LBRACE switchBody RBRACE;
switchBody: (caseLabel stmt*)*;
caseLabel: K_CASE expr COLON | K_DEFAULT COLON;

// Jump Statements
breakStmt: K_BREAK SEMI;
continueStmt: K_CONTINUE SEMI;
returnStmt: K_RETURN expr? SEMI;

// Expression Statement
exprStmt: expr SEMI;

// Expressions
expr:
    expr DOT ID                         # MemberAccessExpr
  | expr LPAR argList? RPAR             # FuncCallExpr
  | expr (INC | DEC)                    # PostfixExpr
  | (NOT | SUB | ADD | INC | DEC) expr  # UnaryExpr
  | expr (MUL | DIV | MOD) expr         # MultiplicativeExpr
  | expr (ADD | SUB) expr               # AdditiveExpr
  | expr (LT | LE | GT | GE) expr       # RelationalExpr
  | expr (EQ | NEQ) expr                # EqualityExpr
  | expr AND expr                       # LogicalAndExpr
  | expr OR expr                        # LogicalOrExpr
  | <assoc=right> expr ASSIGN expr                    # AssignExpr
  | primary                             # PrimaryExpr
  ;

primary:
    LPAR expr RPAR
  | ID
  | INT_LIT
  | FLOAT_LIT
  | STRING_LIT
  | structLiteral
  ;

structLiteral: LBRACE argList? RBRACE;
argList: expr (COMMA expr)*;

// ======================================================
// LEXER RULES
// ======================================================

BLOCK_COMMENT : '/*' .*? '*/' -> skip ;
LINE_COMMENT  : '//' ~[\r\n]* -> skip ;
WS            : [ \t\r\n\f]+ -> skip ; 

K_AUTO   : 'auto';
K_BREAK  : 'break';
K_CASE   : 'case';
K_CONTINUE : 'continue';
K_DEFAULT: 'default';
K_ELSE   : 'else';
K_FLOAT  : 'float';
K_FOR    : 'for';
K_IF     : 'if';
K_INT    : 'int';
K_RETURN : 'return';
K_STRING : 'string';
K_STRUCT : 'struct';
K_SWITCH : 'switch';
K_VOID   : 'void';
K_WHILE  : 'while';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';

EQ : '==';
NEQ: '!=';
LT : '<';
GT : '>';
LE : '<=';
GE : '>=';

AND: '&&';
OR : '||';
NOT: '!';

INC: '++';
DEC: '--';
ASSIGN: '=';
DOT: '.';

LPAR   : '(';
RPAR   : ')';
LBRA   : '[';
RBRA   : ']';
LBRACE : '{';
RBRACE : '}';
COMMA  : ',';
SEMI   : ';';
COLON  : ':';

FLOAT_LIT : [0-9]+ '.' [0-9]* ([eE] [+-]? [0-9]+)? 
          | '.' [0-9]+ ([eE] [+-]? [0-9]+)? 
          | [0-9]+ [eE] [+-]? [0-9]+ ; 

INT_LIT   : [0-9]+ ;

ID : [a-zA-Z_] [a-zA-Z0-9_]* ;

STRING_LIT : '"' (ESC_SEQ | ~["\\\r\n])* '"' { self.text = self.text[1:-1] } ;

ILLEGAL_ESCAPE : '"' (ESC_SEQ | ~["\\\r\n])* '\\' ~[bfrnt"\\\r\n] ;

UNCLOSE_STRING : '"' (ESC_SEQ | ~["\\\r\n])* ;

ERROR_CHAR : . ;

fragment ESC_SEQ : '\\' [bfrnt"\\\\] ;