programa {
    // Variables
    entero x = 10;
    entero y = 5;
    entero z;
    
    // Operaciones aritméticas
    z = x + y;
    imprimir("Suma:");
    imprimir(z);
    
    z = x - y;
    imprimir("Resta:");
    imprimir(z);
    
    z = x * y;
    imprimir("Multiplicación:");
    imprimir(z);
    
    z = x / y;
    imprimir("División:");
    imprimir(z);
    
    z = x % y;
    imprimir("Módulo:");
    imprimir(z);
    
    // Arreglos
    entero[] numeros = [10, 20, 30, 40, 50];
    imprimir("Primer elemento del arreglo:");
    imprimir(numeros[0]);
    
    numeros[2] = 99;
    imprimir("Arreglo modificado:");
    imprimir(numeros[2]);
    
    // Condicionales
    si (x > y) {
        imprimir("x es mayor que y");
    } sino {
        imprimir("x no es mayor que y");
    }
    
    // Ciclo mientras
    imprimir("Ciclo mientras (i < 3):");
    entero i = 0;
    mientras (i < 3) {
        imprimir(i);
        i = i + 1;
    }
    
    // Ciclo para
    imprimir("Ciclo para (j = 0 hasta 3):");
    para (entero j = 0; j < 3; j = j + 1) {
        imprimir(j);
    }
}