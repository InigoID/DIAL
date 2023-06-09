#include <iostream>
#include <stdio.h>
#include <time.h>


using namespace std ;



/*

    PRÁCTICA 1 (PARTE 2): DISEÑO DE ALGORITMOS ITERATIVOS EFICIENTES EN C/C++

    ASIGNATURA: DISEÑO DE ALGORITMOS
    CURSO:      2022-2023
    SUBGRUPO:   U1 

    APELLIDOS:  IRIONDO DELGADO
    NOMBRE:     IÑIGO

 
*/



/* ALGORITMOS PARA EL PROBLEMA DE LA RAÍZ CUADRADA ENTERA */



int raiz_ent1(int n)     // O(√n)
{
    
    int r = 0 ;

    while (n >= (r + 1) * (r + 1)) {

        r = r + 1 ;

    }   

    return r ;
}



int raiz_ent2(int n)     // O(n)
{
    
    int r = n ;

    while (r * r > n) {

        r = r - 1 ;
    
    }    

    return r ;
}



int raiz_ent3(int n)  // O(log(n))
{
    int i = 0;
    while (i * i < n) {
        i++;
    }
    if (i * i == n) {
        return i;
    } else {
        return i - 1;
    }
}



int raiz_ent4(int n, int inicio, int fin)  // O(log(n))
{
    int medio = (inicio + fin) / 2;
    if (medio * medio == n || (medio * medio < n && (medio + 1) * (medio + 1) > n)) {
        return medio;
    } else if (medio * medio > n) {
        return raiz_ent4(n, inicio, medio - 1);
    } else {
        return raiz_ent4(n, medio + 1, fin);
    }
}


int main() {
    int numero;
    cout << "Introduzca un numero para calcular la raiz cuadrada: ";
    cin >> numero;
    
    /* MEDIDAS DEL TIEMPO DE EJECUCION DE LOS PROGRAMAS */

    int repeticiones = 1000000;

    cout << "Medidas del tiempo de ejecucion del programa 'raiz_ent1': " << endl;
    clock_t t1 = clock();
    for (int i = 0; i < repeticiones; i++) {
        int res = raiz_ent1(numero);
    }
    clock_t t2 = clock();
    double tiempo_raiz_ent1 = ((double)(t2 - t1) / CLOCKS_PER_SEC) * 1000;
    cout << "Tiempo promedio: " << tiempo_raiz_ent1 / repeticiones << " ms" << endl;
    cout << "Resultado: " << raiz_ent1(numero) << endl;

    cout << "Medidas del tiempo de ejecucion del programa 'raiz_ent2': " << endl;
    t1 = clock();
    for (int i = 0; i < repeticiones; i++) {
        int res = raiz_ent2(numero);
    }
    t2 = clock();
    double tiempo_raiz_ent2 = ((double)(t2 - t1) / CLOCKS_PER_SEC) * 1000;
    cout << "Tiempo promedio: " << tiempo_raiz_ent2 / repeticiones << " ms" << endl;
    cout << "Resultado: " << raiz_ent2(numero) << endl;

    cout << "Medidas del tiempo de ejecucion del programa 'raiz_ent3': " << endl;
    t1 = clock();
    for (int i = 0; i < repeticiones; i++) {
        int res = raiz_ent3(numero);
    }
    t2 = clock();
    double tiempo_raiz_ent3 = ((double)(t2 - t1) / CLOCKS_PER_SEC) * 1000;
    cout << "Tiempo promedio: " << tiempo_raiz_ent3 / repeticiones << " ms" << endl;
    cout << "Resultado: " << raiz_ent3(numero) << endl;

    /* TIEMPOS DE EJECUCIÓN DE LOS ALGORITMOS DE RAIZ CUADRADA ENTERA */

    cout << "Medidas del tiempo de ejecucion del programa 'raiz_ent4': " << endl;
    t1 = clock();
    for (int i = 0; i < repeticiones; i++) {
        int res = raiz_ent4(numero, 0, numero);
    }
    t2 = clock();
    double tiempo_raiz_ent4 = ((double)(t2 - t1) / CLOCKS_PER_SEC) * 1000;
    cout << "Tiempo promedio: " << tiempo_raiz_ent4 / repeticiones << " ms" << endl;
    cout << "Resultado: " << raiz_ent4(numero, 0, numero) << endl;

    return 0;
}