// Prueba: operadores lógicos (&&, ||, !)
program {
  bool a;
  bool b;
  bool c;

  a = true;
  b = false;
  c = a && b;      // false
  print(c);
  c = a || b;      // true
  print(c);
  c = !b;          // true
  print(c);
}
