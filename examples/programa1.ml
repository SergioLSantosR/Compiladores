funcion vacio saludo(cadena nombre) {
  imprimir("Hola " + nombre);
}
funcion entero suma(entero a, entero b) {
  retorna a + b;
}

programa {
  entero x;
  flotante y;
  cadena s;
  booleano valor;

  x = 10;
  y = 3.14;
  s = "Hola";
  valor = verdadero;

  imprimir("Inicio");

  mientras (x > 0) {
    imprimir(x);
    x = x - 1;
  }

  para (entero i = 0; i < 5; i = i + 1) {
    imprimir(i);
  }

  si (valor) {
    imprimir("valor es verdadero");
  } sino {
    imprimir("valor es falso");
  }

  imprimir(s + " mundo");
  imprimir(y * 2);
  imprimir(suma(5, 3));
  saludo("Mundo");
}
