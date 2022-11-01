# Recebe os parâmetros da elipse e constrói a visualização das áreas da segunda lei de Kepler

from matplotlib import pyplot as plt
import numpy as np


def calculoDaArea(xc, a, b, f, t, x, y):
    plt.figure(figsize=(14, 8))

    plt.plot(xc, 0, 'ko', markersize=5)
    plt.annotate('Centro', xy=(xc, 0), xytext=(xc - 1e6, 1.3e5))

    plt.plot(xc + a * np.cos(t), b * np.sin(t), color='black', label='Órbita do satélite')
    plt.plot(x[1], y[1], 'ro', label='Pontos equidistantes em tempo')
    plt.annotate('x1', xy=(x[1], y[1]), xytext=(x[1], y[1] + 120000))
    plt.plot(x[2], y[2], 'ro')
    plt.annotate('x2', xy=(x[2], y[2]), xytext=(x[2], y[2] + 120000))
    for i in [1, 2]:
        plt.plot([xc + f, x[i]], [0, y[i]], color='red')
    plt.vlines(x=x[2], ymin=0, ymax=y[2], color='black', linestyle='--')
    plt.hlines(y=0, xmin=x[2], xmax=xc + f, color='black', linestyle='--')
    plt.vlines(x=x[1], ymin=0, ymax=y[1], color='black', linestyle='--')
    plt.plot(xc + f, 0, 'bo', markersize=15, label='Terra')
    plt.annotate('T', xy=(xc + f, 0), xytext=(xc + f - 800000, -250000))

    plt.plot(x[1], 0, 'ko', markersize='5')
    plt.annotate('b', xy=(x[1], 0), xytext=(x[1] - 120000, -320000))
    plt.plot(x[2], 0, 'ko', markersize='5')
    plt.annotate('a', xy=(x[2], 0), xytext=(x[2] - 170000, -280000))

    plt.grid(linestyle='--', color='lightgray')
    plt.title("Como calcular a área de uma seção")
    plt.legend(loc='upper right')
    plt.ylabel("Distância(m)")
    plt.xlabel("Distância(m)")
    plt.savefig('calculodaarea.png')
    plt.show()


def areaDasSecoes(xc, a, b, f, t, x, y, ABC):
    plt.figure(figsize=(14, 8))

    plt.plot(xc, 0, 'ko', markersize=5)
    plt.annotate('Centro', xy=(xc, 0), xytext=(xc - 1e6, 1.3e5))

    plt.plot(xc + a * np.cos(t), b * np.sin(t), color='black', label='Órbita do satélite')
    plt.plot(x[1], y[1], 'ro', label='Pontos equidistantes em tempo')
    for i in [2, 7, 8]:
        plt.plot(x[i], y[i], 'ro')
    for i in [1, 2, 7, 8]:
        plt.plot([xc + f, x[i]], [0, y[i]], color='red', linestyle='--')
    plt.plot(xc + f, 0, 'bo', markersize=15)
    plt.annotate('Terra', xy=(xc+f, 0), xytext=(xc+f-1900000, -250000))

    A = (x[1]+x[2])/2.0
    B = np.sqrt(ABC[0]*A*A + ABC[1]*1e3*A + ABC[2]*1e6)
    X = np.array([xc+f, x[1], A, x[2]])
    Y = np.array([0, y[1], B, y[2]])
    plt.fill(X, Y, color='lightcoral')

    A = (x[7] + x[8]) / 2.0
    B = np.sqrt(ABC[0] * A * A + ABC[1] * 1e3 * A + ABC[2] * 1e6)
    X = np.array([xc + f, x[7], A, x[8]])
    Y = np.array([0, y[7], B, y[8]])
    plt.fill(X, Y, color='lightcoral', label='Áreas das seções')

    plt.grid(linestyle='--', color='lightgray')
    plt.title("Área das seções")
    plt.legend(loc='upper right')
    plt.ylabel("Distância(m)")
    plt.xlabel("Distância(m)")
    plt.savefig('areadassecoes.png')
    plt.show()
