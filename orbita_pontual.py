# Recebe os parâmetros e pontos equidistantes em tempo e constrói a figura da órbita do satélite

import numpy as np
from matplotlib import pyplot as plt


def orbitaPontual(xc, a, b, f, t, x, y):
    plt.figure(figsize=(14, 8))

    plt.plot(xc, 0, 'ko', markersize=5)
    plt.annotate('Centro', xy=(xc, 0), xytext=(xc - 1e6, 1.3e5))

    plt.plot(xc + a * np.cos(t), b * np.sin(t), color='black', linestyle='--', label='Órbita do satélite')
    plt.plot(x, y, 'ro', label='Pontos equidistantes em tempo')
    plt.plot(xc + f, 0, 'bo', markersize=15, label='Terra')

    plt.grid(linestyle='--', color='lightgray')
    plt.title("Órbita pontual do satélite")
    plt.legend(loc='upper right')
    plt.ylabel("Distância(m)")
    plt.xlabel("Distância(m)")
    plt.savefig('orbitapontual.png')
    plt.show()
