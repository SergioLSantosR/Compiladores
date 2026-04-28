programa {
    entero x = 10;
    entero y = 20;
    entero z;
    
    z = x + y * 2;
    imprimir(z);
    
    si (x > 10 || y < 20) {
        z = x / 2;
    } sino {
        z = y - 5;
    }
    
    imprimir(z);
    
    entero i = 0;
    mientras (i < 5) {
        imprimir(i);
        i = i + 1;
    }
    
    para (entero j = 0; j < 3; j = j + 1) {
        imprimir(j);
    }
}