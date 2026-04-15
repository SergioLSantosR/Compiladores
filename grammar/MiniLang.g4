grammar MiniLang;

// ==================== Reglas del Parser ====================

programa
 : (funcionDeclaracion)* PROGRAMA bloque (funcionDeclaracion)* EOF
 ;

funcionDeclaracion
 : FUNCION (tipo | VOID) IDENTIFICADOR PAREN_IZQ parametros? PAREN_DER bloque
 ;

parametros
 : parametro (COMA parametro)*
 ;

parametro
 : tipo IDENTIFICADOR
 ;

bloque
 : LLAVE_IZQ sentencia* LLAVE_DER
 ;

sentencia
 : declaracionVariable
 | asignacion
 | condicionalSi
 | impresion
 | cicloMientras
 | cicloPara
 | sentenciaRetorna
 | llamadaFuncion
 ;

declaracionVariable
 : tipo IDENTIFICADOR (ASIGNACION expresion)? PUNTO_COMA
 ;

tipo
 : TIPO_ENTERO
 | TIPO_BOOL
 | TIPO_FLOTANTE
 | TIPO_CADENA
 ;

asignacion
 : IDENTIFICADOR ASIGNACION expresion PUNTO_COMA
 ;

condicionalSi
 : SI PAREN_IZQ expresion PAREN_DER bloque (SINO bloque)?
 ;

impresion
 : IMPRIMIR PAREN_IZQ expresion PAREN_DER PUNTO_COMA
 ;

llamadaFuncion
 : IDENTIFICADOR PAREN_IZQ (expresion (COMA expresion)*)? PAREN_DER PUNTO_COMA
 ;

inicializacionPara : tipo IDENTIFICADOR ASIGNACION expresion ;
asignacionPara     : IDENTIFICADOR ASIGNACION expresion ;
actualizacionPara  : IDENTIFICADOR ASIGNACION expresion ;

cicloMientras
 : MIENTRAS PAREN_IZQ expresion PAREN_DER bloque
 ;

cicloPara
 : PARA PAREN_IZQ (inicializacionPara | asignacionPara)? PUNTO_COMA cond=expresion? PUNTO_COMA (actualizacionPara)? PAREN_DER bloque
 ;

sentenciaRetorna
 : RETORNA expresion? PUNTO_COMA
 ;

expresion
 : NEGACION expresion                                                                      #NegacionLogica
 | RESTA expresion                                                                         #MenosUnario
 | PAREN_IZQ expresion PAREN_DER                                                           #Parentesis
 | izq=expresion op=(MULTIPLICACION|DIVISION) der=expresion                                #MultiplicacionDivision
 | izq=expresion op=(SUMA|RESTA) der=expresion                                             #SumaResta
 | izq=expresion op=(IGUAL|DIFERENTE|MENOR_QUE|MENOR_IGUAL|MAYOR_QUE|MAYOR_IGUAL) der=expresion  #Relacional
 | izq=expresion op=(Y_LOGICO|O_LOGICO) der=expresion                                     #Logica
 | ENTERO                                                                                  #LiteralEntero
 | FLOTANTE                                                                                #LiteralFlotante
 | CADENA                                                                                  #LiteralCadena
 | VERDADERO                                                                               #LiteralVerdadero
 | FALSO                                                                                   #LiteralFalso
 | IDENTIFICADOR                                                                           #ReferenciaVariable
 | IDENTIFICADOR PAREN_IZQ (expresion (COMA expresion)*)? PAREN_DER                        #LlamadaFuncionExpr
 ;

// ==================== Reglas del Lexer ====================

// Palabras clave
PROGRAMA    : 'programa';
SI          : 'si';
SINO        : 'sino';
IMPRIMIR    : 'imprimir';
MIENTRAS    : 'mientras';
PARA        : 'para';
FUNCION     : 'funcion';
RETORNA     : 'retorna';
VOID        : 'vacio';
TIPO_ENTERO   : 'entero';
TIPO_BOOL     : 'booleano';
TIPO_FLOTANTE : 'flotante';
TIPO_CADENA   : 'cadena';
VERDADERO     : 'verdadero';
FALSO         : 'falso';

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

// Literales (FLOTANTE antes de ENTERO para priorizar el match más largo)
FLOTANTE      : [0-9]+ '.' [0-9]+;
ENTERO        : [0-9]+;
CADENA        : '"' (~["\r\n])* '"';
IDENTIFICADOR : [a-zA-Z_][a-zA-Z_0-9]*;

// Espacios en blanco y comentarios (se ignoran)
ESPACIO           : [ \t\r\n]+ -> skip;
COMENTARIO_LINEA  : '//' ~[\r\n]* -> skip;
COMENTARIO_BLOQUE : '/*' .*? '*/' -> skip;
