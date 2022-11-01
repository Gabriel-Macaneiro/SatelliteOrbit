# Recebe os parâmetros da órbita e as funções que representam a spline e constrói a figura

import numpy as np
from matplotlib import pyplot as plt


def areaPelaSpline(xc, a, b, f, t, funcao, vetorX, vetorY, matriz):
    plt.figure(figsize=(14, 8))

    plt.plot(xc + a * np.cos(t), b * np.sin(t), color='black', label='Órbita do satélite')

    xx1 = np.linspace(vetorX[1], vetorX[0])
    yy1 = funcao(xx1, vetorX, matriz, 0)
    plt.plot(xx1, yy1, label='Spline 1')
    xx2 = np.linspace(vetorX[2], vetorX[1])
    yy2 = funcao(xx2, vetorX, matriz, 1)
    plt.plot(xx2, yy2, label='Spline 2')
    xx3 = np.linspace(vetorX[3], vetorX[2])
    yy3 = funcao(xx3, vetorX, matriz, 2)
    plt.plot(xx3, yy3, label='Spline 3')

    for i in range(4):
        plt.plot(vetorX[i], vetorY[i], 'ro')
        plt.plot(vetorX[i], 0, 'ro', markersize='5')
        plt.vlines(x=vetorX[i], ymin=0, ymax=vetorY[i], color='black', linestyle='--')
    plt.hlines(y=0, xmin=vetorX[3], xmax=xc + f, color='black', linestyle='--')

    for i in [0, 3]:
        plt.plot([xc + f, vetorX[i]], [0, vetorY[i]], color='red')

    plt.plot(xc + f, 0, 'bo', markersize=15, label='Terra')
    plt.annotate('T', xy=(xc + f, 0), xytext=(xc + f - 800000, -250000))

    plt.annotate('x1', xy=(vetorX[0], vetorY[0]), xytext=(vetorX[0], vetorY[0] + 60000))
    plt.annotate('x2', xy=(vetorX[1], vetorY[1]), xytext=(vetorX[1], vetorY[1] + 60000))
    plt.annotate('x3', xy=(vetorX[2], vetorY[2]), xytext=(vetorX[2], vetorY[2] + 60000))
    plt.annotate('x4', xy=(vetorX[3], vetorY[3]), xytext=(vetorX[3], vetorY[3] + 60000))

    plt.annotate('d', xy=(vetorX[0], 0), xytext=(vetorX[0] - 170000, -280000))
    plt.annotate('c', xy=(vetorX[1], 0), xytext=(vetorX[1] - 170000, -280000))
    plt.annotate('b', xy=(vetorX[2], 0), xytext=(vetorX[2] - 170000, -280000))
    plt.annotate('a', xy=(vetorX[3], 0), xytext=(vetorX[3] - 170000, -280000))

    plt.grid(linestyle='--', color='lightgray')
    plt.title("Funções produzidas pela Spline Cúbica")
    plt.legend(loc='upper right')
    plt.ylabel("Distância(m)")
    plt.xlabel("Distância(m)")
    plt.savefig('areadassecoesspline.png')
    plt.show()
