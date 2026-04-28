programa {
    imprimir("Break: Mostrar números hasta encontrar 5");
    entero i = 1;
    mientras (i <= 10) {
        imprimir(i);
        si (i == 5) {
            romper;
        }
        i = i + 1;
    }
    
    imprimir("Continue: Mostrar números excepto el 5");
    entero j = 0;
    mientras (j < 6) {
        j = j + 1;
        si (j == 5) {
            continuar;
        }
        imprimir(j);
    }
}