funcion entero factorial(entero n) {
    si (n <= 1) {
        retorna 1;
    }
    retorna n * factorial(n - 1);
}

programa {
    entero x = 10;
    entero y = 3;
    entero r = x % y;
    imprimir(r);

    entero i = 0;
    mientras (i < 5) {
        si (i == 3) {
            romper;
        }
        imprimir(i);
        i = i + 1;
    }

    entero f = factorial(5);
    imprimir(f);
}
