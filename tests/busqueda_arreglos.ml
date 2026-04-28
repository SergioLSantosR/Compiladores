programa {
    entero[] valores = [23, 45, 12, 67, 34, 89, 56];
    entero buscar = 34;
    entero encontrado = 0;
    entero posicion = 0;
    entero i = 0;
    
    mientras (i < 7 && encontrado == 0) {
        si (valores[i] == buscar) {
            encontrado = 1;
            posicion = i;
        }
        i = i + 1;
    }
    
    si (encontrado == 1) {
        imprimir("Valor encontrado en la posición:");
        imprimir(posicion);
    } sino {
        imprimir("Valor no encontrado");
    }
}