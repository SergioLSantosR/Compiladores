funcion int suma(int a, int b) {
  retorna a + b;
}

program {
  int x;
  float y;
  string s;
  bool valor;

  x = 10;
  y = 3.14;
  s = "Hola";
  valor = true;

  imprime("Inicio");

  mientras (x > 0) {
    imprime(x);
    x = x - 1;
  }

  para (int i = 0; i < 5; i = i + 1) {
    imprime(i);
  }

  si (valor) {
    imprime("valor es verdadero");
  } sino {
    imprime("valor es falso");
  }

  imprime(s + " mundo");
  imprime(y * 2);
  imprime(suma(5, 3));   // llamada dentro del programa
}

funcion void saludo(string nombre) {
  imprime("Hola " + nombre);
}