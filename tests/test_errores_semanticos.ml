// Prueba de errores semánticos: tipos, declaraciones y ámbitos

funcion entero duplicar(entero n) {
  retorna n * 2;
}

programa {
  // Error: asignar cadena a entero
  entero x = "hola";

  // Error: variable no declarada
  y = 10;

  // Error: redeclaración en el mismo ámbito
  entero z = 1;
  entero z = 2;

  // Error: condición no booleana
  si (42) {
    imprimir(0);
  }

  // Error: operación aritmética con booleano
  entero w = verdadero + 1;

  // Error: llamada con número incorrecto de argumentos
  entero r = duplicar(1, 2);

  // Error: usar función vacio como expresión
  // (nota: duplicar retorna entero, así que creamos una vacio)
}

funcion vacio saludar() {
  imprimir("hola");
}

// Se necesita otro programa para probar error de función vacio como expresión
