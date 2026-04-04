grammar MiniLang;

// ==================== Programa: funciones opcionales + bloque principal ====================

programa
 : funcion* PROGRAMA bloque EOF
 ;

funcion
 : FUNC IDENTIFICADOR PAREN_IZQ listaParametros? PAREN_DER tipoRetorno bloque
 ;

listaParametros
 : parametro (COMA parametro)*
 ;

parametro
 : tipo IDENTIFICADOR
 ;

tipoRetorno
 : tipo
 | VOID
 ;

// ==================== Bloques y sentencias ====================

bloque
 : LLAVE_IZQ sentencia* LLAVE_DER
 ;

sentencia
 : declaracionVariable
 | asignacion
 | condicionalSi
 | imprimir
 | mientras
 | para
 | retorno
 | llamadaFuncionStmt
 ;

declaracionVariable
 : tipo IDENTIFICADOR (ASIGNACION expresion)? PUNTO_COMA
 ;

tipo
 : TIPO_ENTERO
 | TIPO_BOOL
 | TIPO_FLOAT
 | TIPO_STRING
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

mientras
 : MIENTRAS PAREN_IZQ expresion PAREN_DER bloque
 ;

para
 : PARA PAREN_IZQ paraInicio? PUNTO_COMA expresion? PUNTO_COMA paraActualizacion? PAREN_DER bloque
 ;

paraInicio
 : tipo IDENTIFICADOR ASIGNACION expresion
 | IDENTIFICADOR ASIGNACION expresion
 ;

paraActualizacion
 : IDENTIFICADOR ASIGNACION expresion
 ;

retorno
 : RETORNAR expresion? PUNTO_COMA
 ;

llamadaFuncionStmt
 : IDENTIFICADOR PAREN_IZQ listaArgumentos? PAREN_DER PUNTO_COMA
 ;

listaArgumentos
 : expresion (COMA expresion)*
 ;

// ==================== Expresiones ====================

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
 | FLOTANTE                                                                      #LiteralFlotante
 | CADENA                                                                        #LiteralCadena
 | VERDADERO                                                                     #LiteralVerdadero
 | FALSO                                                                         #LiteralFalso
 | IDENTIFICADOR PAREN_IZQ listaArgumentos? PAREN_DER                            #LlamadaFuncion
 | IDENTIFICADOR                                                                 #ReferenciaVariable
 ;

// ==================== Lexer ====================

FUNC       : 'func';
MIENTRAS   : 'while';
PARA       : 'for';
RETORNAR   : 'return';
VOID       : 'void';
PROGRAMA   : 'program';
SI         : 'if';
SINO       : 'else';
IMPRIMIR   : 'print';
TIPO_ENTERO : 'int';
TIPO_BOOL   : 'bool';
TIPO_FLOAT  : 'float';
TIPO_STRING : 'string';
VERDADERO   : 'true';
FALSO       : 'false';

Y_LOGICO  : '&&';
O_LOGICO  : '||';
NEGACION  : '!';

IGUAL     : '==';
DIFERENTE : '!=' | '<>';

MENOR_IGUAL : '<=';
MAYOR_IGUAL : '>=';
MENOR_QUE   : '<';
MAYOR_QUE   : '>';

ASIGNACION    : '=';
SUMA          : '+';
RESTA         : '-';
MULTIPLICACION: '*';
DIVISION      : '/';

PAREN_IZQ    : '(';
PAREN_DER    : ')';
LLAVE_IZQ    : '{';
LLAVE_DER    : '}';
CORCHETE_IZQ : '[';
CORCHETE_DER : ']';
PUNTO_COMA   : ';';
COMA         : ',';

IDENTIFICADOR : [a-zA-Z_][a-zA-Z_0-9]*;

FLOTANTE
 : [0-9]+ '.' [0-9]*
 | [0-9]* '.' [0-9]+
 ;

ENTERO : [0-9]+;

fragment CHAR_CADENA : ~[\u0022\r\n];
CADENA : '"' CHAR_CADENA* '"';

ESPACIO           : [ \t\r\n]+ -> skip;
COMENTARIO_LINEA  : '//' ~[\r\n]* -> skip;
COMENTARIO_BLOQUE : '/*' .*? '*/' -> skip;
