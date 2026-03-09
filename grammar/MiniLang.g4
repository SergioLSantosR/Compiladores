grammar MiniLang;

// ---------- Reglas Parser ----------

program
 : PROGRAM block EOF
 ;

block
 : LBRACE stmt* RBRACE
 ;

stmt
 : varDecl
 | assignStmt
 | ifStmt
 | printStmt
 ;

varDecl
 : type ID SEMI
 ;

type
 : INT_T
 | BOOL_T
 ;

assignStmt
 : ID ASSIGN expr SEMI
 ;

ifStmt
 : IF LPAREN expr RPAREN block (ELSE block)?
 ;

printStmt
 : PRINT LPAREN expr RPAREN SEMI
 ;

expr
 : NOT expr                                           #UnaryNot
 | SUB expr                                           #UnaryMinus
 | LPAREN expr RPAREN                                 #Paren
 | left=expr op=(MUL|DIV) right=expr                  #MulDiv
 | left=expr op=(ADD|SUB) right=expr                  #AddSub
 | left=expr op=(EQ|NEQ|LT|LE|GT|GE) right=expr       #Relational
 | left=expr op=(AND|OR) right=expr                   #Logical
 | INT                                                #IntLit
 | TRUE                                               #TrueLit
 | FALSE                                              #FalseLit
 | ID                                                 #IdRef
 ;

// ---------- Reglas Lexer ----------

// Palabras clave
PROGRAM : 'program';
IF      : 'if';
ELSE    : 'else';
PRINT   : 'print';
INT_T   : 'int';
BOOL_T  : 'bool';
TRUE    : 'true';
FALSE   : 'false';

// Operadores lógicos y relacionales
AND : '&&';
OR  : '||';
NOT : '!';
EQ  : '==';
NEQ : '!=' | '<>';
LE  : '<=';
GE  : '>=';
LT  : '<';
GT  : '>';

// Asignación y aritméticos
ASSIGN : '=';
ADD    : '+';
SUB    : '-';
MUL    : '*';
DIV    : '/';

// Símbolos de agrupación y otros
LPAREN : '(';
RPAREN : ')';
LBRACE : '{';
RBRACE : '}';
LBRACK : '[';
RBRACK : ']';
SEMI   : ';';
COMMA  : ',';

// Identificadores y literales
ID  : [a-zA-Z_][a-zA-Z_0-9]*;
INT : [0-9]+;

// Espacios y comentarios
WS            : [ \t\r\n]+ -> skip;
LINE_COMMENT  : '//' ~[\r\n]* -> skip;
BLOCK_COMMENT : '/*' .*? '*/' -> skip;
