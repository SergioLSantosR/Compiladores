// Prueba de errores léxicos: caracteres no reconocidos por el lexer

programa {
  entero x = 5;
  x = x + @;
  entero y = #10;
  cadena s = 'texto con comillas simples';
  flotante f = 3.14$;
  entero z = ~42;
}
