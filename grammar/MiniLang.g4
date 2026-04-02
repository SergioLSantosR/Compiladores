grammar MiniLang;

// ---------- Reglas Parser ----------

program
 : PROGRAM grupo EOF
 ;

grupo
 : llave_izq sentencia* llave_der
 ;

sentencia
 : declaraVariable
 | sentenciaAsigna
 | sentenciaIf
 | sentenciaPrint
 ;

declaraVariable
 : tipo ID punto_coma
 ;

tipo
 : INT_T
 | BOOL_T
 ;

sentenciaAsigna
 : ID asigna expr punto_coma
 ;

sentenciaSi
 : SI parentesis_izq expr parentesis_der  grupo (ENTONCES grupo)?
 ;

sentenciaImprime
 : IMPRIME parentesis_izq expr parentesis_der punto_coma
 ;

expr
 : NOT expr                                           #UnaryNot
 | SUB expr                                           #UnaryMinus
 | parentesis_izq expr parentesis_der                 #Paren
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
SI      : 'si';
ENTONCES    : 'entonces';
IMPRIME   : 'imprime';
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
asigna : '=';
suma    : '+';
resta    : '-';
multi    : '*';
divide    : '/';

// Símbolos de agrupación y otros
parentesis_izq : '(';
parentesis_der : ')';
llave_izq : '{';
llave_der : '}';
corchete_izq : '[';
corchete_der : ']';
punto_coma   : ';';
coma  : ',';

// Identificadores y literales
ID  : [a-zA-Z_][a-zA-Z_0-9]*;
INT : [0-9]+;

// Espacios y comentarios
WS            : [ \t\r\n]+ -> skip;
LINEA_COMENTARIO  : '//' ~[\r\n]* -> skip;
GRUPO_COMENTARIO : '/*' .*? '*/' -> skip;
