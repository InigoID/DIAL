'''

    PRÁCTICA 4 PARTE 2 PYTHON
    EJERCICIO 1 (PROBLEMA DEL CAMBIO)

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

def devolver_cambio2(M, C, R): # O(N*C*maxR)
    monedas = [float('inf')] * (C + 1)
    monedas[0] = 0
    for i in range(len(M)):
        for j in range(C, M[i] - 1, -1):
            for k in range(1, R[i] + 1):
                if k * M[i] > j:
                    break
                monedas[j] = min(monedas[j], monedas[j - k * M[i]] + k)
    return monedas[C]


def main2():

    MAX_LEN = 500  # Maximum length of input list.

    # Initialise results containers:
    lengths_devolver_cambio2 = []
    times_devolver_cambio2 = []

    for length in range(1, MAX_LEN, 10):

        # Generate random values:
        M = [random.randint(1, 10) for _ in range(length)]
        C = random.randint(0, length * 10)
        cantidad_moneda = [random.randint(1, 10) for _ in range(length)]

        # Time execution (devolver_cambio2):
        start = time.perf_counter()
        devolver_cambio2(M, C, cantidad_moneda)
        end = time.perf_counter()

        # Store results (devolver_cambio2):
        lengths_devolver_cambio2.append(length)
        times_devolver_cambio2.append(end - start)
        
        
    # Plot results
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Algoritmo devolver_cambio2 - Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_devolver_cambio2, times_devolver_cambio2, label="devolver_cambio2()")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Polynomial fit
    ns = np.linspace(1, MAX_LEN, 50, dtype=int)
    ts = [timeit.timeit('devolver_cambio2(M, C, cantidad_moneda)',
                    setup='M = [random.randint(1, 10) for _ in range({})]; C = random.randint(0, {} * 10); cantidad_moneda = [random.randint(1, 10) for _ in range({})]'.format(n, n, n),
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
