# Recebe os parâmetros da elipse e calcula os 30 pontos equidistantes em tempo

from scipy import constants
import numpy as np
import bisseccao


def calculaPontosEquidistantes(a, e, xc, f):
    mass_earth = 5.9722e24
    i = 0
    P = 2 * np.pi * np.sqrt(a ** 3 / (constants.G * mass_earth))
    period = P / 30
    t = np.arange(0, P, period)
    M = (2 * np.pi * t) / P
    print("Vetor tempo: ", t)
    print("Anomalia média: ", M)
    E = np.zeros(30, dtype='float')

    for Mo in M:
        E[i] = bisseccao.bisseccao(bisseccao.funcao, -1e-15, 1e15, 1e-9, e, Mo)
        i += 1

    print("Anomalia excêntrica: ", E)
    theta = 2 * np.arctan(np.sqrt((1 + e) / (1 - e)) * np.tan(E / 2))
    r = a * ((1 - e ** 2) / (1 + e * np.cos(theta)))
    print("Anomalia verdadeira: ", theta)
    print("Distância do ponto à Terra: ", r)
    x = r * np.cos(theta) + xc + f
    y = r * np.sin(theta)
    print("Coordenadas no eixo x: ", x)
    print("Coordenadas no eixo y: ", y)
    return x, y
