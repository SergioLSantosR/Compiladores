// Caso válido: funciones, while, variables en bloque anidado, print
program {
  func int suma(int a, int b) {
    return a + b;
  }
  func int fact_rec(int n) {
    if (n <= 1) {
      return 1;
    } else {
      return n * fact_rec(n - 1);
    }
  }
  int n;
  int f;
  int i;
  int s;
  n = 5;
  f = 1;
  i = 1;
  while (i <= n) {
    f = f * i;
    i = i + 1;
  }
  print(f);
  s = suma(10, 20);
  print(s);
  print(fact_rec(4));
  if (n > 0) {
    int inner;
    inner = 7;
    print(inner);
  }
}
