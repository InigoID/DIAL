'''

    PRÁCTICA 3 PARTE 2 PYTHON
    EJERCICIO 1 (CERCANOS A LA MEDIANA)

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


def cercanos_med(V, N): # 0(N^2)
    m = seleccion2(V, 0, N - 1, N // 2)
    D = [0] * N
    for i in range(N):
        D[i] = abs(V[i] - m)
    y = seleccion2(D, 0, N - 1, min(N - 1, 2))
    j = 0
    W = []
    while len(W) < 3 and j < N:
        if abs(V[j] - m) <= y:
            W.append(V[j])
        j += 1
    return W


def seleccion2(V, c, f, k):
    t = f - c + 1
    if t <= 12:
        ordenar_insercion(V, c, f)
        if k >= c and k <= f:  
            return V[k]
        else:
            return None
    s = t // 5
    for l in range(1, s + 1):
        ordenar_insercion(V, c + 5 * (l - 1), c + 5 * l - 1)
        pm = c + 5 * (l - 1) + 5 // 2
        V[c + l - 1], V[pm] = V[pm], V[c + l - 1]
    mm = seleccion2(V, c, c + s - 1, c + (s - 1) // 2)
    i, j = particion2(V, c, f, mm)
    if k < i:
        return seleccion2(V, c, i - 1, k)
    elif i <= k and k <= j:
        return mm
    else:
        return seleccion2(V, j + 1, f, k)

def ordenar_insercion(V, c, f):
    for i in range(c + 1, f + 1):
        k = V[i]
        j = i - 1
        while j >= c and V[j] > k:
            V[j + 1] = V[j]
            j -= 1
        V[j + 1] = k

def particion2(V, c, f, mm):
    i = c
    j = f
    while i <= j:
        while i <= j and V[i] <= mm:
            i += 1
        while i <= j and V[j] >= mm:
            j -= 1
        if i < j:
            V[i], V[j] = V[j], V[i]
    return i, j


def main2():

    MAX_LEN = 500  # Maximum length of input list.

    # Initialise results containers:
    lengths_cercanos_med = []
    times_cercanos_med = []

    for length in range(1, MAX_LEN, 10):

        # Generate random values:
        V = [random.randint(1, 100) for _ in range(length)]
        N = random.randint(0, length)

        # Time execution (cercanos_med):
        start = time.perf_counter()
        cercanos_med(V, N)
        end = time.perf_counter()

        # Store results (cercanos_med):
        lengths_cercanos_med.append(length)
        times_cercanos_med.append(end - start)
        
        
    # Plot results
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Algoritmo cercanos_med - Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_cercanos_med, times_cercanos_med, label="cercanos_med()")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Polynomial fit
    ns = np.linspace(1, MAX_LEN, 50, dtype=int)
    ts = [timeit.timeit('cercanos_med(V, N)',
                    setup='V = [random.randint(1, 100) for _ in range({})]; N = random.randint(0, {})'.format(n, n),
                    globals=globals(),
                    number=10)
          for n in ns]

    plt.plot(ns, ts, 'or')

    degree = 5
    coeffs = np.polyfit(ns, ts, degree)
    p = np.poly1d(coeffs)
    plt.plot(ns, [p(n) for n in ns], '-b')
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.show()

