grammar MiniLang;

// ---------- Reglas Parser ----------

program
 : PROGRAM grupo EOF
 ;

grupo
 : LBRACE sentencia* RBRACE
 ;

sentencia
 : declaraVariable
 | sentenciaAsigna
 | sentenciaIf
 | sentenciaPrint
 ;

declaraVariable
 : tipo ID SEMI
 ;

tipo
 : INT_T
 | BOOL_T
 ;

sentenciaAsigna
 : ID ASSIGN expr SEMI
 ;

sentenciaIf
 : IF LPAREN expr RPAREN grupo (ELSE grupo)?
 ;

sentenciaPrint
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
LINEA_COMENTARIO  : '//' ~[\r\n]* -> skip;
GRUPO_COMENTARIO : '/*' .*? '*/' -> skip;
