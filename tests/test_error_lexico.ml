// Error léxico: símbolos no reconocidos (@, #)
program {
  int x;
  x = 1 @ 2;
  # esto no es comentario válido en MiniLang
  print(x);
}
