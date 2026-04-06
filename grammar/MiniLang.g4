grammar MiniLang;

// ==================== Reglas del Parser ====================

programa
 : PROGRAMA cuerpoPrincipal EOF
 ;

cuerpoPrincipal
 : LLAVE_IZQ declaracionFuncion* sentencia* LLAVE_DER
 ;

declaracionFuncion
 : FUNC tipo IDENTIFICADOR PAREN_IZQ listaParametros? PAREN_DER bloque
 ;

listaParametros
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
 | cicloMientras
 | imprimir
 | retorno
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

cicloMientras
 : MIENTRAS PAREN_IZQ expresion PAREN_DER bloque
 ;

imprimir
 : IMPRIMIR PAREN_IZQ expresion PAREN_DER PUNTO_COMA
 ;

retorno
 : RETORNO expresion PUNTO_COMA
 ;

// ==================== Expresiones  ====================

expresion
 : NEGACION expresion                                                            #NegacionLogica
 | RESTA expresion                                                               #MenosUnario
 | IDENTIFICADOR PAREN_IZQ listaArgumentos? PAREN_DER                            #LlamadaFuncion
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

listaArgumentos
 : expresion (COMA expresion)*
 ;

// ==================== Reglas del Lexer ====================

PROGRAMA    : 'program';
SI          : 'if';
SINO        : 'else';
IMPRIMIR    : 'print';
TIPO_ENTERO : 'int';
TIPO_BOOL   : 'bool';
VERDADERO   : 'true';
FALSO       : 'false';
MIENTRAS    : 'while';
FUNC        : 'func';
RETORNO     : 'return';

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
ENTERO        : [0-9]+;

ESPACIO           : [ \t\r\n]+ -> skip;
COMENTARIO_LINEA  : '//' ~[\r\n]* -> skip;
COMENTARIO_BLOQUE : '/*' .*? '*/' -> skip;
