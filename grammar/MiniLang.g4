grammar MiniLang;

// ---------- Reglas Parser ----------

program
 : PROGRAM grupo EOF
 ;

grupo
 : LLAVE_IZQ sentencia* LLAVE_DER
 ;

sentencia
 : declaraVariable
 | sentenciaAsigna
 | sentenciaSI
 | sentenciaImprime
 ;

declaraVariable
 : tipo ID PUNTO_COMA
 ;

tipo
 : INT_T
 | BOOL_T
 ;

sentenciaAsigna
 : ID ASIGNA expr PUNTO_COMA
 ;

sentenciaSI
 : SI PARENTESIS_IZQ expr PARENTESIS_DER  grupo (SINO grupo)?
 ;

sentenciaImprime
 : IMPRIME PARENTESIS_IZQ expr PARENTESIS_DER PUNTO_COMA
 ;

expr
 : NOT expr                                           #UnaryNot
 | RESTA expr                                         #UnaryMinus
 | PARENTESIS_IZQ expr PARENTESIS_DER                 #Paren
 | left=expr op=(MULTI|DIVIDE) right=expr             #MulDiv
 | left=expr op=(SUMA|RESTA) right=expr               #AddSub
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
SI      : 'si';
SINO    : 'sino';
IMPRIME : 'imprime';
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
ASIGNA   : '=';
SUMA     : '+';
RESTA    : '-';
MULTI    : '*';
DIVIDE   : '/';

// Símbolos de agrupación y otros
PARENTESIS_IZQ : '(';
PARENTESIS_DER : ')';
LLAVE_IZQ : '{';
LLAVE_DER : '}';
CORCHETE_IZQ : '[';
CORCHETE_DER : ']';
PUNTO_COMA   : ';';
COMA  : ',';

// Identificadores y literales
ID  : [a-zA-Z_][a-zA-Z_0-9]*;
INT : [0-9]+;

// Espacios y comentarios
WS            : [ \t\r\n]+ -> skip;
LINEA_COMENTARIO  : '//' ~[\r\n]* -> skip;
GRUPO_COMENTARIO : '/*' .*? '*/' -> skip;
