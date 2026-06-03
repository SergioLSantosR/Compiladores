grammar gramatica_v4;

// ==================== Reglas del Parser ====================

programa
 : (funcionDeclaracion | declaracionEstructura)* PROGRAMA bloque (funcionDeclaracion | declaracionEstructura)* EOF
 ;

// Proyecto Final: declaración de structs a nivel de programa
declaracionEstructura
 : ESTRUCTURA IDENTIFICADOR LLAVE_IZQ campoEstructura* LLAVE_DER
 ;

campoEstructura
 : tipo IDENTIFICADOR PUNTO_COMA
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
 | declaracionVariableEstructura  // Proyecto Final: Punto p;
 | asignacion
 | asignacionArreglo
 | asignacionCampo                // Proyecto Final: p.x = ...;
 | condicionalSi
 | impresion
 | cicloMientras
 | cicloPara
 | sentenciaSegun                 // Proyecto Final: switch/case/default
 | sentenciaRetorna
 | llamadaFuncion
 | sentenciaBreak
 | sentenciaContinue
 | sentenciaImportar
 ;

declaracionVariable
 : tipo IDENTIFICADOR (ASIGNACION expresion)? PUNTO_COMA
 | tipo CORCHETE_IZQ CORCHETE_DER IDENTIFICADOR (ASIGNACION literalArreglo)? PUNTO_COMA
 ;

// Proyecto Final: declaración de variable de tipo struct (el tipo es un IDENTIFICADOR)
declaracionVariableEstructura
 : IDENTIFICADOR IDENTIFICADOR PUNTO_COMA
 ;

literalArreglo
 : CORCHETE_IZQ (expresion (COMA expresion)*)? CORCHETE_DER
 ;

accesoArreglo
 : IDENTIFICADOR CORCHETE_IZQ expresion CORCHETE_DER
 ;

asignacionArreglo
 : accesoArreglo ASIGNACION expresion PUNTO_COMA
 ;

// Proyecto Final: acceso a campo de struct (p.x)
accesoCampo
 : IDENTIFICADOR PUNTO IDENTIFICADOR
 ;

// Proyecto Final: asignación a campo de struct (p.x = expr;)
asignacionCampo
 : accesoCampo ASIGNACION expresion PUNTO_COMA
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

// Proyecto Final: switch/case con default
sentenciaSegun
 : SEGUN PAREN_IZQ expresion PAREN_DER LLAVE_IZQ casoSegun* casoDefecto? LLAVE_DER
 ;

casoSegun
 : CASO expresion DOS_PUNTOS sentencia*
 ;

casoDefecto
 : DEFECTO DOS_PUNTOS sentencia*
 ;

sentenciaRetorna
 : RETORNA expresion? PUNTO_COMA
 ;

sentenciaBreak
 : ROMPER PUNTO_COMA
 ;

sentenciaContinue
 : CONTINUAR PUNTO_COMA
 ;

sentenciaImportar
 : IMPORTAR CADENA PUNTO_COMA
 ;

expresion
 : NEGACION expresion                                                                      #NegacionLogica
 | RESTA expresion                                                                         #MenosUnario
 | PAREN_IZQ tipo PAREN_DER expresion                                                      #Casting   // Proyecto Final
 | PAREN_IZQ expresion PAREN_DER                                                           #Parentesis
 | izq=expresion op=(MULTIPLICACION|DIVISION|MODULO) der=expresion                         #MultiplicacionDivisionModulo
 | izq=expresion op=(SUMA|RESTA) der=expresion                                             #SumaResta
 | izq=expresion op=(IGUAL|DIFERENTE|MENOR_QUE|MENOR_IGUAL|MAYOR_QUE|MAYOR_IGUAL) der=expresion  #Relacional
 | izq=expresion op=(Y_LOGICO|O_LOGICO) der=expresion                                     #Logica
 | <assoc=right> cond=expresion INTERROGACION ent=expresion DOS_PUNTOS sino=expresion      #Ternario  // Proyecto Final
 | ENTERO                                                                                  #LiteralEntero
 | FLOTANTE                                                                                #LiteralFlotante
 | CADENA                                                                                  #LiteralCadena
 | VERDADERO                                                                               #LiteralVerdadero
 | FALSO                                                                                   #LiteralFalso
 | accesoCampo                                                                             #AccesoCampoExpr  // Proyecto Final
 | accesoArreglo                                                                           #AccesoArregloExpr
 | IDENTIFICADOR PAREN_IZQ (expresion (COMA expresion)*)? PAREN_DER                        #LlamadaFuncionExpr
 | IDENTIFICADOR                                                                           #ReferenciaVariable
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
ROMPER        : 'romper';
CONTINUAR     : 'continuar';
IMPORTAR      : 'importar';
SEGUN         : 'segun';         // Proyecto Final: switch
CASO          : 'caso';          // Proyecto Final: case
DEFECTO       : 'defecto';       // Proyecto Final: default
ESTRUCTURA    : 'estructura';    // Proyecto Final: struct

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
MODULO        : '%';

// Símbolos de agrupación y puntuación
PAREN_IZQ    : '(';
PAREN_DER    : ')';
LLAVE_IZQ    : '{';
LLAVE_DER    : '}';
CORCHETE_IZQ : '[';
CORCHETE_DER : ']';
PUNTO_COMA   : ';';
COMA         : ',';
INTERROGACION : '?';        // Proyecto Final: ternario
DOS_PUNTOS    : ':';        // Proyecto Final: case/ternario
PUNTO         : '.';        // Proyecto Final: acceso a campo

// Literales (FLOTANTE antes de ENTERO para priorizar el match más largo)
FLOTANTE      : [0-9]+ '.' [0-9]+;
ENTERO        : [0-9]+;
CADENA        : '"' (~["\r\n])* '"';
IDENTIFICADOR : [a-zA-Z_][a-zA-Z_0-9]*;

// Espacios en blanco y comentarios (se ignoran)
ESPACIO           : [ \t\r\n]+ -> skip;
COMENTARIO_LINEA  : '//' ~[\r\n]* -> skip;
COMENTARIO_BLOQUE : '/*' .*? '*/' -> skip;
