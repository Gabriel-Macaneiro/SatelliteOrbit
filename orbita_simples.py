# Recebe os parâmetros da elipse e constrói a figura da órbita do satélite

import numpy as np
from matplotlib import pyplot as plt


def orbitaSimples(xc, a, b, f, t):
    plt.figure(figsize=(14, 8))

    plt.plot(xc, 0, 'ko', markersize=5)
    plt.annotate('Centro', xy=(xc, 0), xytext=(xc + 100, 100))

    plt.axhline(0, 0.02, 0.98, color='black', linestyle='--')
    plt.plot(xc + f, 0, 'bo', markersize=15, label='Terra')
    plt.axvline(xc, 0.02, 0.98, color='black', linestyle='--', label='Eixos da elipse')
    plt.plot(xc + a * np.cos(t), b * np.sin(t), color='black', label='Órbita do satélite')

    plt.plot(xc - a, 0, 'ko', markersize='5')
    plt.annotate('A1', xy=(xc - a, 0), xytext=(xc - a - 800, 100))

    plt.plot(xc, b, 'ko', markersize='5')
    plt.annotate('B1', xy=(xc, b), xytext=(xc + 200, b + 50))

    plt.plot(xc, -b, 'ko', markersize='5')
    plt.annotate('B2', xy=(xc, -b), xytext=(xc + 200, - b - 280))

    plt.plot(xc + a, 0, 'ko', markersize='5')
    plt.annotate('A2', xy=(xc + a, 0), xytext=(xc + a + 200, 100))

    plt.plot(xc - f, 0, 'ko', markersize='5')
    plt.annotate('Foco', xy=(xc - f, 0), xytext=(xc - f - 100, 100))

    plt.grid(linestyle='--', color='lightgray')
    plt.title("Órbita simples do satélite")
    plt.legend(loc='upper right')
    plt.ylabel("Distância(Km)")
    plt.xlabel("Distância(Km)")
    plt.savefig('orbitasimples.png')
    plt.show()
