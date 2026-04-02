grammar MiniLang;

// ---------- Reglas Parser ----------

program
 : PROGRAM (funcionDecl)* grupo (funcionDecl)* EOF   // permite funciones antes y después
 ;

funcionDecl
 : FUNCION tipo? ID PARENTESIS_IZQ parametros? PARENTESIS_DER grupo
 ;

parametros
 : parametro (COMA parametro)*
 ;

parametro
 : tipo ID
 ;

grupo
 : LLAVE_IZQ sentencia* LLAVE_DER
 ;

sentencia
 : declaraVariable
 | sentenciaAsigna
 | sentenciaSI
 | sentenciaImprime
 | sentenciaMientras
 | sentenciaPara
 | sentenciaRetorna
 ;

declaraVariable
 : tipo ID PUNTO_COMA
 ;

tipo
 : INT_T 
 | BOOL_T
 | FLOAT_T 
 | STRING_T
 ;

sentenciaAsigna
 : ID ASIGNA expr PUNTO_COMA
 ;

sentenciaSI
 : SI PARENTESIS_IZQ expr PARENTESIS_DER grupo (SINO grupo)?
 ;

sentenciaImprime
 : IMPRIME PARENTESIS_IZQ expr PARENTESIS_DER PUNTO_COMA
 ;

// Nuevas reglas para el bucle for (sin punto y coma)
inicializacionPara : tipo ID ASIGNA expr;   // ej: int i = 0
asignacionPara     : ID ASIGNA expr;       // ej: i = j + 1 (sin punto y coma)
actualizacionPara  : ID ASIGNA expr;       // ej: i = i + 1 (sin punto y coma)

sentenciaMientras
 : MIENTRAS PARENTESIS_IZQ expr PARENTESIS_DER grupo
 ;

sentenciaPara 
 : PARA PARENTESIS_IZQ (inicializacionPara | asignacionPara)? PUNTO_COMA cond=expr? PUNTO_COMA (actualizacionPara)? PARENTESIS_DER grupo
 ;

sentenciaRetorna
 : RETORNA expr? PUNTO_COMA
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
 | FLOAT                                              #FloatLit
 | STRING                                             #StringLit
 | TRUE                                               #TrueLit
 | FALSE                                              #FalseLit
 | ID                                                 #IdRef
 | ID PARENTESIS_IZQ (expr (COMA expr)*)? PARENTESIS_DER   #FuncCall
 ;

// ---------- Reglas Lexer ----------

// Palabras clave
PROGRAM  : 'program';
SI       : 'si';
SINO     : 'sino';
IMPRIME  : 'imprime';
MIENTRAS : 'mientras';
PARA     : 'para';
FUNCION  : 'funcion';
RETORNA  : 'retorna';
INT_T    : 'int';
BOOL_T   : 'bool';
FLOAT_T  : 'float';
STRING_T : 'string';
TRUE     : 'true';
FALSE    : 'false';

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

// Literales
INT    : [0-9]+;
FLOAT  : [0-9]+ '.' [0-9]+;
STRING : '"' (~["\r\n])* '"';
ID     : [a-zA-Z_][a-zA-Z_0-9]*;

// Espacios y comentarios
WS            : [ \t\r\n]+ -> skip;
LINEA_COMENTARIO  : '//' ~[\r\n]* -> skip;
GRUPO_COMENTARIO : '/*' .*? '*/' -> skip;