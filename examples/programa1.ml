program {
  int x;
  int y;
  int w;
  int z;

  x = 10;
  y = 20;
  z = x + y * 2;  // 10 + 20*2 = 50

  if (z > 30) {
    w = z / 2;    // división entera -> 25
  } else {
    w = z - 5;
  }

  print(z);       // imprime 50
  print(w);       // imprime 25
}
