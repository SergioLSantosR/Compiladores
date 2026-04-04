func fact(int n) int {
  if (n <= 1) {
    return 1;
  }
  return n * fact(n - 1);
}

func concat_hola(string s) string {
  return "Hola, " + s;
}

program {
  int r;
  float a;
  float b;
  string msg;

  r = fact(5);
  print(r);

  a = 7.0;
  b = a / 2.0;
  print(b);

  msg = concat_hola("MiniLang");
  print(msg);

  int i;
  i = 0;
  while (i < 3) {
    print(i);
    i = i + 1;
  }

  int j;
  for (j = 0; j < 2; j = j + 1) {
    print(j);
  }
}
