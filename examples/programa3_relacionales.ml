// Prueba: operadores relacionales
program {
  int x;
  int y;
  bool r;

  x = 10;
  y = 20;
  r = x < y;       // true
  imprime(r);
  r = x == y;      // false
  imprime(r);
  r = x != y;      // true
  imprime(r);
  r = y >= x;      // true
  imprime(r);
}
