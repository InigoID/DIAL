'''

    PRÁCTICA 4 PARTE 1 PYTHON
    EJERCICIO 1

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

def paradas(G, n): #G vector de km entre cada gasolinera, n km con deposito lleno  O(N)
    P = []
    d = n
    for i in range(len(G) - 1):
        if G[i] > d:
            d = n
            P.append(i)
        else:
            d -= G[i]
    return P


def main2():

    MAX_LEN = 500  # Maximum length of input list.

    # Initialise results containers:
    lengths_paradas = []
    times_paradas = []

    for length in range(1, MAX_LEN, 10):

        # Generate random values:
        G = [random.randint(1, 100) for _ in range(length)]
        n = random.randint(0, length * 10)

        # Time execution (paradas):
        start = time.perf_counter()
        paradas(G, n)
        end = time.perf_counter()

        # Store results (paradas):
        lengths_paradas.append(length)
        times_paradas.append(end - start)
        
    # Plot results
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Algoritmo paradas - Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_paradas, times_paradas, label="paradas()")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Polynomial fit
    ns = np.linspace(1, MAX_LEN, 50, dtype=int)
    ts = [timeit.timeit('paradas(G, n)',
                    setup='G = [random.randint(1, 100) for _ in range({})]; n = random.randint(0, {} * 10)'.format(n, n),
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

