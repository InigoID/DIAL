#!/usr/bin/env python3
# -*- coding: utf-8 -*-



'''

    PRÁCTICA 1 (PARTE 2): ANÁLISIS DE LA EFICIENCIA DE ALGORITMOS DE 
                          ORDENACIÓN Y DE BÚSQUEDA EN PYTHON

    ASIGNATURA: DISEÑO DE ALGORITMOS
    CURSO:      2022-2023
    SUBGRUPO:   U1

    APELLIDOS: IRIONDO DELGADO
    NOMBRE:    ÍÑIGO

'''



import matplotlib.pyplot as plt
import numpy as np
import timeit
import time
import random



# ALGORITMOS DE ORDENACION (SELECCIÓN E INSERCIÓN)



'''

EJERCICIO 1: Programa en Python los algoritmos de ordenación por selección y
ordenación por inserción estudiados en las clases de teoría. Usa el código 
visto en las sesiones de laboratorio para visualizar los tiempos de ejecución
de estos dos programas, para determinar cuál es más eficiente en la práctica, 
así como para visualizar la función de coste que define, para cada algoritmo, 
su orden de complejidad.

'''



def ord_seleccion(v): # Ordenación por selección (visto en clase) O(N^2)
    n = len(v)
    for i in range(n - 1):
        pmin = i
        for j in range(i + 1, n):
            if v[j] < v[pmin]:
                pmin = j
        v[i], v[pmin] = v[pmin], v[i]
    return v




def ord_insercion(v): # Ordenación por inserción (visto en clase) O(N^2)
    n = len(v)
    for i in range(1, n):
        elem = v[i]
        j = i - 1
        while j >= 0 and elem < v[j]:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = elem
    return v




def main1():
    
    MAX_LEN = 1000  # Maximum length of input list

    # Initialise results containers
    
    lengths_sort_sel  = []
    times_sort_sel    = []

    lengths_sort_ins  = []
    times_sort_ins    = []

    for length in range(0, MAX_LEN, 5) :
        
        # Generate random lists
        
        v  = [random.randint(-99, 99) for _ in range(length)]
        w = []
        for elem in v :
            w.append(elem)

        # Time execution (algoritmo de ordenacion por selección)
        
        start = time.perf_counter()
        ord_seleccion(v)
        end = time.perf_counter()

        # Store results
        
        lengths_sort_sel.append(length)
        times_sort_sel.append(end - start)

        # Time execution (algoritmo de ordenacion por inserción)
        
        start = time.perf_counter()
        ord_insercion(w)
        end = time.perf_counter()

        # Store results
        
        lengths_sort_ins.append(length)
        times_sort_ins.append(end - start)
        
        

    # Plot results
    
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Algoritmos de ordenacion - Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_sort_sel, times_sort_sel, label="ord_seleccion()")
    plt.plot(lengths_sort_ins, times_sort_ins, label="ord_insercion()")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    
    ns = np.linspace(1, 3000, 100, dtype = int)
    ts = [timeit.timeit('ord_insercion(lst)',
                    setup='lst=list(range({})); random.shuffle(lst)'.format(n),
                    globals=globals(),
                    number=1000)
          for n in ns]

    plt.plot(ns, ts, 'or')

    degree = 5
    coeffs = np.polyfit(ns, ts, degree)
    p = np.poly1d(coeffs)
    plt.plot(ns, [p(n) for n in ns], '-b')
    


# ALGORITMOS DE ORDENACION (QUICKSORT Y MERGESORT)


    
'''

EJERCICIO 2: Programa en Python los algoritmos de ordenación "quicksort" 
y "mergesort", y compara su eficiencia con los algoritmos de ordenación 
anteriores.

'''   



def quickSort(v): # Ordenación por el método quicksort O(N*logN)
    return quicksort1(v,0,len(v)-1)

def quicksort1(V, c, f):
    if c < f:
        p = particion(V, c, f)
        quicksort1(V, c, p-1)
        quicksort1(V, p+1, f)

def particion(V, c, f):
    piv = V[c]
    i = c+1
    d = f
    while i != d+1:
        while i <= d and V[i] <= piv:
            i += 1
        while i <= d and V[d] >= piv:
            d -= 1
        if i < d:
            V[i], V[d] = V[d], V[i]
            i += 1
            d -= 1
    V[c], V[d] = V[d], V[c]
    return d




def mergeSort(myList): # Ordenación por el método mergesort O(N*logN)
    return mergesort1(myList,0,len(myList)-1)

def mergesort1(V, c, f):
    if c < f:
        m = (c + f) // 2
        mergesort1(V, c, m)
        mergesort1(V, m + 1, f)
        mezclar(V, c, m, f)

def mezclar(V, c, m, f):
    W = [0] * len(V)
    i = c
    j = m + 1
    k = c
    while i <= m and j <= f:
        if V[i] <= V[j]:
            W[k] = V[i]
            i += 1
        else:
            W[k] = V[j]
            j += 1
        k += 1
    if i > m:
        for l in range(j, f + 1):
            W[k] = V[l]
            k += 1
    else:
        for l in range(i, m + 1):
            W[k] = V[l]
            k += 1
    for l in range(c, f + 1):
        V[l] = W[l]



def main2():
    
    MAX_LEN = 1000  # Maximum length of input list
    
    # Initialise results containers
    
    lengths_sort_sel = []
    times_sort_sel   = []

    lengths_sort_ins = []
    times_sort_ins   = []
    
    lengths_quick = []
    times_quick   = []
    
    lengths_merge = []
    times_merge   = []

    for length in range(0, MAX_LEN, 100) :
        
        # Generate random list
        
        v = [random.randint(-99, 99) for _ in range(length)]
        v1 = []
        v2 = []
        v3 = []
        for elem in v :
            v1.append(elem)
            v2.append(elem)
            v3.append(elem)

        # Time execution (algoritmo de ordenacion por selección)
        
        start = time.perf_counter()
        ord_seleccion(v)
        end = time.perf_counter()

        # Store results
        
        lengths_sort_sel.append(length)
        times_sort_sel.append(end - start)

        # Time execution (algoritmo de ordenacion por inserción)
        
        start = time.perf_counter()
        ord_insercion(v1)
        end = time.perf_counter()

        # Store results
        
        lengths_sort_ins.append(length)
        times_sort_ins.append(end - start)

        # Time execution (algoritmo de ordenacion quicksort)

        start = time.perf_counter()
        quickSort(v2)
        end = time.perf_counter()
        
        # Store results
        
        lengths_quick.append(length)
        times_quick.append(end - start)
        
        # Time execution (algoritmo de ordenacion mergesort)

        start = time.perf_counter()
        mergeSort(v3)
        end = time.perf_counter()
        
        # Store results
        
        lengths_merge.append(length)
        times_merge.append(end - start)

        

    # Plot results
    
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Algoritmos de ordenacion - Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_sort_sel, times_sort_sel, label="ord_seleccion()")
    plt.plot(lengths_sort_ins, times_sort_ins, label="ord_insercion()")
    plt.plot(lengths_merge, times_merge, label="mergeSort()")
    plt.plot(lengths_quick, times_quick, label="quickSort()")
    plt.legend()
    plt.tight_layout()
    plt.show()
    


# ALGORITMOS DE BÚSQUEDA (SECUENCIAL Y BINARIA)



'''

EJERCICIO 3: Programa en Python los algoritmos de búsqueda secuencial y 
búsqueda binaria, y compara su eficiencia. Visualiza sus ordenes de 
complejidad.

'''  



def busq_sec(lst, x): # Búsqueda secuencial O(N)
    n = len(lst)
    i = 0
    while i < n and lst[i] != x:
        i = i + 1
    return 0 <= i < n



def busq_bin(lst, x): # Búsqueda binaria (o dicotómica) O(logN)
    lo = 0
    hi = len(lst) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if x < lst[mid]:
            hi = mid - 1
        elif x > lst[mid]:
            lo = mid + 1
        else:
            return True
    else:
        return False
    
        
        



def main3():
    
    MAX_LEN = 1000  # Maximum length of input list
    
    # Initialise results containers
    
    lengths_busq_sec = []
    times_busq_sec   = []

    lengths_busq_bin = []
    times_busq_bin   = []

    for length in range(0, MAX_LEN, 10) :
        
        # Generate random list
        
        v = [random.randint(-99, 99) for _ in range(length)]
        x = random.randint(-99, 99)
        
        # Sort the list
        
        ord_insercion(v)

        # Time execution (algoritmo de búsqueda secuencial)
        
        start = time.perf_counter()
        busq_sec(v, x)
        end = time.perf_counter()

        # Store results
        
        lengths_busq_sec.append(length)
        times_busq_sec.append(end - start)

        # Time execution (algoritmo de búsqueda binaria)
        
        start = time.perf_counter()
        busq_bin(v, x)
        end = time.perf_counter()

        # Store results
        
        lengths_busq_bin.append(length)
        times_busq_bin.append(end - start)



    # Plot results
    
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Algoritmos de búsqueda - Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_busq_sec, times_busq_sec, label="busq_sec()")
    plt.plot(lengths_busq_bin, times_busq_bin, label="busq_bin()")
    plt.legend()
    plt.tight_layout()
    plt.show()

    ns = np.linspace(1, 10000, 100, dtype = int) 
    # ts = [timeit.timeit('busq_sec(lst, random.randint(lst[0], lst[len(lst)-1]))',
    #                 setup='lst=list(range({}))'.format(n),
    #                 globals=globals(),
    #                 number=1000)
    #       for n in ns]
    ts = [timeit.timeit('busq_bin(lst, random.randint(lst[0], lst[len(lst)-1]))',
                    setup='lst=list(range({}))'.format(n),
                    globals=globals(),
                    number=1000)
          for n in ns]
    

    plt.plot(ns, ts, 'or')

    degree = 10
    coeffs = np.polyfit(ns, ts, degree)
    p = np.poly1d(coeffs)
    plt.plot(ns, [p(n) for n in ns], '-b')
