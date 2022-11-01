# Recebe uma matriz de um sistema linear e retona um vetor com as soluções desse sistema


def eliminacaoGaussiana(matrix):
    n = len(matrix)
    x = [0.0] * n
    for i in range(0, n - 1):
        c = i + 1
        for j in range(i + 1, n):
            while matrix[i][i] == 0:
                aux = matrix[i]
                matrix[i] = matrix[c]
                matrix[c] = aux
                c += 1
            a = matrix[j][i] / matrix[i][i]
            for k in range(0, n + 1):
                matrix[j][k] = float(matrix[j][k]) - a * matrix[i][k]

    x[n - 1] = matrix[n - 1][n] / matrix[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        soma = 0
        for j in range(i + 1, n):
            soma += matrix[i][j] * x[j]
        x[i] = (matrix[i][n] - soma) / matrix[i][i]
    return x
