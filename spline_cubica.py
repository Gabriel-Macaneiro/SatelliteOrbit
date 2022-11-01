# Faz a interpolação da função da elipse a partir das coordenadas x e y

import numpy as np


def criaH(x):
    tam = len(x)
    h = np.zeros(tam-1)
    for i in range(tam - 1):
        h[i] = x[i+1] - x[i]
    return h


def criaA(h):
    tam = len(h) + 1
    A = np.zeros(shape=(tam, tam))
    for i in range(tam):
        for j in range(tam):
            if i == j:
                if i == 0 and j == 0:
                    A[i, j] = 1
                elif i == tam - 1 and i == tam - 1:
                    A[i, j] = 1
                else:
                    A[i, j] = 2 * (h[i] + h[i-1])
            if (j + 1) == i and i != (tam - 1):
                A[i, j] = h[j]
            if (i + 1) == j and i != 0:
                A[i, j] = h[i]
    return A


def criaB(a, h):
    tam = len(a)
    B = np.zeros(tam)
    for i in range(tam):
        if i == 0 or i == (tam - 1):
            B[i] = 0
        else:
            B[i] = (3 * (a[i+1] - a[i]) / h[i]) - (3 * (a[i] - a[i-1]) / h[i-1])
    return B


def criaAB(A, B):
    tam = len(A)
    AB = np.zeros(shape=(tam, tam + 1))
    for i in range(tam):
        for j in range(tam + 1):
            if j == tam:
                AB[i, j] = B[i]
            else:
                AB[i, j] = A[i, j]
    return AB


def thomas(AB):
    tam = len(AB)
    a = np.zeros(tam)
    b = np.zeros(tam)
    c = np.zeros(tam)
    d = np.zeros(tam)
    b[0] = AB[0][0]
    c[0] = AB[0][1]
    d[0] = AB[0][-1]
    for i in range(1, tam-1):
        a[i] = AB[i][i-1]
        b[i] = AB[i][i]
        c[i] = AB[i][i+1]
        d[i] = AB[i][-1]
    a[-1] = AB[-1][-3]
    b[-1] = AB[-1][-2]
    d[-1] = AB[-1][-1]
    c[0] /= b[0]
    d[0] /= b[0]
    for i in range(1, tam):
        den = float(b[i] - a[i] * c[i-1])
        c[i] /= den
        d[i] = (d[i] - a[i] * d[i-1]) / den
    x = np.copy(d)
    for i in range(tam - 2, -1, -1):
        x[i] -= c[i] * x[i+1]
    return x


def criaBeD(a, c, h):
    tam = len(h)
    b = np.zeros(tam)
    d = np.zeros(tam)
    for i in range(tam):
        b[i] = (a[i+1] - a[i]) / h[i] - h[i] * (2 * c[i] + c[i+1]) / 3
        d[i] = (c[i+1] - c[i]) / (3 * h[i])
    return b, d


def matrizDosCoeficientes(a, b, c, d):
    tam = len(a)
    matriz = np.zeros(shape=(tam-1, 4))
    for i in range(tam-1):
        matriz[i, 0] = a[i]
        matriz[i, 1] = b[i]
        matriz[i, 2] = c[i]
        matriz[i, 3] = d[i]
    return matriz


def splineCubica(x, y):
    a = y
    h = criaH(x)
    A = criaA(h)
    B = criaB(a, h)
    AB = criaAB(A, B)
    c = thomas(AB)
    b, d = criaBeD(a, c, h)

    return matrizDosCoeficientes(a, b, c, d)
