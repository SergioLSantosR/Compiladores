// Prueba: operadores lógicos (&&, ||, !)
program {
  bool a;
  bool b;
  bool c;

  a = true;
  b = false;
  c = a && b;      // false
  imprime(c);
  c = a || b;      // true
  imprime(c);
  c = !b;          // true
  imprime(c);
}
