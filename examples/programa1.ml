program {
  int x;
  int y;
  int w;
  int z;

  x = 10;
  y = 20;
  z = x + y * 2;  // 10 + 20*2 = 50

  si (x > 10 || y < 20) {
    w = x / 2;    // división entera -> 25
  } sino {
    w = y - 5;
  }

  imprime(z);       // imprime 50
  imprime(w);       // imprime 25
}
