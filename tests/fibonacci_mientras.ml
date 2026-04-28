programa {
    entero n = 10;
    entero a = 0;
    entero b = 1;
    entero c;
    entero i = 2;
    
    imprimir("Secuencia Fibonacci (primeros 10 términos):");
    imprimir(a);
    imprimir(b);
    
    mientras (i < n) {
        c = a + b;
        imprimir(c);
        a = b;
        b = c;
        i = i + 1;
    }
}