grammar MiniLang;

// ==================== Reglas del Parser ====================

programa
 : PROGRAMA bloque EOF
 ;

bloque
 : LLAVE_IZQ sentencia* LLAVE_DER
 ;

sentencia
 : declaracionVariable
 | asignacion
 | condicionalSi
 | imprimir
 ;

declaracionVariable
 : tipo IDENTIFICADOR PUNTO_COMA
 ;

tipo
 : TIPO_ENTERO
 | TIPO_BOOL
 ;

asignacion
 : IDENTIFICADOR ASIGNACION expresion PUNTO_COMA
 ;

condicionalSi
 : SI PAREN_IZQ expresion PAREN_DER bloque (SINO bloque)?
 ;

imprimir
 : IMPRIMIR PAREN_IZQ expresion PAREN_DER PUNTO_COMA
 ;

// ==================== Expresiones  ====================


expresion
 : NEGACION expresion                                                            #NegacionLogica
 | RESTA expresion                                                               #MenosUnario
 | PAREN_IZQ expresion PAREN_DER                                                 #Parentesis
 | izq=expresion op=(MULTIPLICACION|DIVISION) der=expresion                      #MultiplicacionDivision
 | izq=expresion op=(SUMA|RESTA) der=expresion                                   #SumaResta
 | izq=expresion op=(MENOR_QUE|MENOR_IGUAL|MAYOR_QUE|MAYOR_IGUAL) der=expresion #Comparacion
 | izq=expresion op=(IGUAL|DIFERENTE) der=expresion                              #Igualdad
 | izq=expresion Y_LOGICO der=expresion                                          #YLogico
 | izq=expresion O_LOGICO der=expresion                                          #OLogico
 | ENTERO                                                                        #LiteralEntero
 | VERDADERO                                                                     #LiteralVerdadero
 | FALSO                                                                         #LiteralFalso
 | IDENTIFICADOR                                                                 #ReferenciaVariable
 ;

// ==================== Reglas del Lexer ====================

// Palabras clave
PROGRAMA : 'program';
SI       : 'if';
SINO     : 'else';
IMPRIMIR : 'print';
TIPO_ENTERO : 'int';
TIPO_BOOL   : 'bool';
VERDADERO   : 'true';
FALSO       : 'false';

// Operadores lógicos
Y_LOGICO  : '&&';
O_LOGICO  : '||';
NEGACION  : '!';

// Operadores de igualdad
IGUAL     : '==';
DIFERENTE : '!=' | '<>';

// Operadores relacionales
MENOR_IGUAL : '<=';
MAYOR_IGUAL : '>=';
MENOR_QUE   : '<';
MAYOR_QUE   : '>';

// Asignación y aritméticos
ASIGNACION    : '=';
SUMA          : '+';
RESTA         : '-';
MULTIPLICACION: '*';
DIVISION      : '/';

// Símbolos de agrupación y puntuación
PAREN_IZQ    : '(';
PAREN_DER    : ')';
LLAVE_IZQ    : '{';
LLAVE_DER    : '}';
CORCHETE_IZQ : '[';
CORCHETE_DER : ']';
PUNTO_COMA   : ';';
COMA         : ',';

// Identificadores y literales numéricos
IDENTIFICADOR : [a-zA-Z_][a-zA-Z_0-9]*;
ENTERO        : [0-9]+;

// Espacios en blanco y comentarios (se ignoran)
ESPACIO           : [ \t\r\n]+ -> skip;
COMENTARIO_LINEA  : '//' ~[\r\n]* -> skip;
COMENTARIO_BLOQUE : '/*' .*? '*/' -> skip;
