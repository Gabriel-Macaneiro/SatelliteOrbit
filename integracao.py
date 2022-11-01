# Recebe uma função, um intervalo e retorna a integral
# Será utilizado o método de Gauss Legendre

import numpy as np


def integral(f, a, b):
    n = 5  # Definindo o grau de integração para uma boa precisão
    # Valores de r e c tabelados
    soma = 0
    r = [-(1 / 21) * np.sqrt(245 + 14 * np.sqrt(70)), -(1 / 21) * np.sqrt(245 - 14 * np.sqrt(70)), 0,
         (1 / 21) * np.sqrt(245 - 14 * np.sqrt(70)), (1 / 21) * np.sqrt(245 + 14 * np.sqrt(70))]
    c = [(1 / 900) * (322 - 13 * np.sqrt(70)), (1 / 900) * (322 + 13 * np.sqrt(70)), 128 / 225,
         (1 / 900) * (322 + 13 * np.sqrt(70)), (1 / 900) * (322 - 13 * np.sqrt(70))]
    for i in range(n):
        x = ((b - a) * r[i] + a + b) / 2.0
        soma += c[i] * f(x)
    result = (b - a) * soma / 2.0
    return result
