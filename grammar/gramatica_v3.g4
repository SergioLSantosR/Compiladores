grammar gramatica_v4;

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
 | asignacionArreglo
 | condicionalSi
 | impresion
 | cicloMientras
 | cicloPara
 | sentenciaRetorna
 | llamadaFuncion
 | sentenciaBreak
 | sentenciaContinue
 | sentenciaImportar
 | sentenciaSwitch           // NUEVO v4: Switch/Case
 | sentenciaStruct           // NUEVO v4: Declaración de struct
 ;

declaracionVariable
 : tipo IDENTIFICADOR (ASIGNACION expresion)? PUNTO_COMA
 | tipo CORCHETE_IZQ CORCHETE_DER IDENTIFICADOR (ASIGNACION literalArreglo)? PUNTO_COMA
 | tipoStruct IDENTIFICADOR (ASIGNACION literalStruct)? PUNTO_COMA  // NUEVO v4: Variable de tipo struct
 ;

literalArreglo
 : CORCHETE_IZQ (expresion (COMA expresion)*)? CORCHETE_DER
 ;

// NUEVO v4: Literal para inicializar structs
literalStruct
 : LLAVE_IZQ (expresion (COMA expresion)*)? LLAVE_DER
 ;

accesoArreglo
 : IDENTIFICADOR CORCHETE_IZQ expresion CORCHETE_DER
 ;

asignacionArreglo
 : accesoArreglo ASIGNACION expresion PUNTO_COMA
 ;

tipo
 : TIPO_ENTERO
 | TIPO_BOOL
 | TIPO_FLOTANTE
 | TIPO_CADENA
 ;

// NUEVO v4: Tipo struct (puede ser usado en declaraciones)
tipoStruct
 : IDENTIFICADOR
 ;

asignacion
 : (IDENTIFICADOR | accesoStruct) ASIGNACION expresion PUNTO_COMA  // NUEVO v4: Asignación a struct
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

sentenciaBreak
 : ROMPER PUNTO_COMA
 ;

sentenciaContinue
 : CONTINUAR PUNTO_COMA
 ;

sentenciaImportar
 : IMPORTAR CADENA PUNTO_COMA
 ;

// NUEVO v4: Sentencia Switch/Case
sentenciaSwitch
 : SWITCH PAREN_IZQ expresion PAREN_DER LLAVE_IZQ (caso)* (casoDefault)? LLAVE_DER
 ;

// NUEVO v4: Caso individual
caso
 : CASE expresion DOS_PUNTOS sentencia*
 ;

// NUEVO v4: Caso default
casoDefault
 : DEFAULT DOS_PUNTOS sentencia*
 ;

// NUEVO v4: Declaración de struct
sentenciaStruct
 : STRUCT IDENTIFICADOR LLAVE_IZQ (declaracionCampoStruct)* LLAVE_DER
 ;

// NUEVO v4: Campo dentro de un struct
declaracionCampoStruct
 : tipo IDENTIFICADOR PUNTO_COMA
 ;

// NUEVO v4: Acceso a campo de struct
accesoStruct
 : IDENTIFICADOR PUNTO IDENTIFICADOR
 ;

expresion
 : NEGACION expresion                                                                      #NegacionLogica
 | RESTA expresion                                                                         #MenosUnario
 | PAREN_IZQ expresion PAREN_DER                                                           #Parentesis
 | izq=expresion op=(MULTIPLICACION|DIVISION|MODULO) der=expresion                         #MultiplicacionDivisionModulo
 | izq=expresion op=(SUMA|RESTA) der=expresion                                             #SumaResta
 | izq=expresion op=(IGUAL|DIFERENTE|MENOR_QUE|MENOR_IGUAL|MAYOR_QUE|MAYOR_IGUAL) der=expresion  #Relacional
 | izq=expresion op=(Y_LOGICO|O_LOGICO) der=expresion                                     #Logica
 | <assoc=right> condicion=expresion '?' verdadero=expresion ':' falso=expresion           #OperadorTernario   // NUEVO v4
 | <assoc=right> PAREN_IZQ tipo PAREN_DER expresion                                        #CastingExplicito   // NUEVO v4
 | ENTERO                                                                                  #LiteralEntero
 | FLOTANTE                                                                                #LiteralFlotante
 | CADENA                                                                                  #LiteralCadena
 | VERDADERO                                                                               #LiteralVerdadero
 | FALSO                                                                                   #LiteralFalso
 | IDENTIFICADOR                                                                           #ReferenciaVariable
 | accesoArreglo                                                                           #AccesoArregloExpr
 | accesoStruct                                                                           #AccesoStructExpr    // NUEVO v4
 | IDENTIFICADOR PAREN_IZQ (expresion (COMA expresion)*)? PAREN_DER                        #LlamadaFuncionExpr
 ;

// ==================== Reglas del Lexer ====================

// Palabras clave existentes
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

// NUEVAS PALABRAS CLAVE v4
STRUCT      : 'struct';
SWITCH      : 'switch';
CASE        : 'case';
DEFAULT     : 'default';

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
PUNTO        : '.';        // NUEVO v4: Para acceso a structs
DOS_PUNTOS   : ':';        // NUEVO v4: Para case y default

// Literales
FLOTANTE      : [0-9]+ '.' [0-9]+;
ENTERO        : [0-9]+;
CADENA        : '"' (~["\r\n])* '"';
IDENTIFICADOR : [a-zA-Z_][a-zA-Z_0-9]*;

// Espacios en blanco y comentarios
ESPACIO           : [ \t\r\n]+ -> skip;
COMENTARIO_LINEA  : '//' ~[\r\n]* -> skip;
COMENTARIO_BLOQUE : '/*' .*? '*/' -> skip;