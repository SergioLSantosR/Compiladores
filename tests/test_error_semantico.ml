// Errores semánticos: tipos, variable no declarada, llamada con argumentos incorrectos
program {
  func int doble(int x) {
    return x + x;
  }
  int a;
  bool b;
  a = 1;
  b = true;
  a = b;
  y = 3;
  print(doble(1));
  print(doble(1, 2));
  print(doble(true));
}
