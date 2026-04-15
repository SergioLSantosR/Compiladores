// Prueba de errores semánticos adicionales: funciones y retorno

funcion entero sumar(entero a, entero b) {
  // Error: función con tipo de retorno que no retorna
  entero c = a + b;
}

funcion vacio nada() {
  // Error: retorna valor en función vacio
  retorna 42;
}

funcion entero identidad(entero x) {
  // Error: retorna tipo incorrecto
  retorna "texto";
}

programa {
  entero a = 5;

  // Error: usar función void como expresión
  // nada() retorna vacio, no se puede asignar
  // (este error lo detecta el semántico)

  // Error: operador relacional con tipos incompatibles
  booleano b = "hola" < 5;

  // Error: negación lógica sobre entero
  booleano c = !a;

  // Error: menos unario sobre cadena
  entero d = -"texto";

  // Error: condición del mientras no booleana
  mientras (10) {
    imprimir(a);
  }
}
