funcion entero factorial(entero n) {
  si (n <= 1) {
    retorna 1;
  } sino {
    retorna n * factorial(n - 1);
  }
}

funcion vacio saludo(cadena nombre) {
  imprimir("Hola " + nombre);
}

programa {
  entero x = 10;
  cadena prefijo = "El resultado es: ";
  flotante pi = 3.14;
  booleano activo = verdadero;

  mientras (x > 0) {
    entero temp = factorial(x);
    imprimir(prefijo);
    imprimir(temp);
    x = x - 2;
  }

  para (entero i = 0; i < 5; i = i + 1) {
    imprimir(i);
  }

  si (activo) {
    imprimir("Programa activo");
  } sino {
    imprimir("Programa inactivo");
  }

  imprimir(pi * 2.0);
  saludo("Mundo");
}
