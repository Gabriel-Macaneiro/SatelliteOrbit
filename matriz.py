# Recebe coordenadas x e y como uma matriz, chama eliminação gaussiana para resolver o sistema linear e retorna um vetor

import numpy as np
import eliminacao_gaussiana as eg


def calculaABC():
    A = np.loadtxt("pontos.dat", dtype=float)
    print("A =", A[0], "\n    [" + str(A[1, 0]), "\t   ", str(A[1, 1]) + "0]", "\n   ", A[2])
    matrix = [[A[0, 0]**2, A[0, 0], 1, A[0, 1]**2],
              [A[1, 0]**2, A[1, 0], 1, A[1, 1]**2],
              [A[2, 0]**2, A[2, 0], 1, A[2, 1]**2]]
    print("Matrix =", matrix[0], "\n\t", matrix[1], "\n\t", matrix[2])
    parametros = eg.eliminacaoGaussiana(matrix)
    print("Parâmetros =", parametros)
    return parametros
