# Recebe uma função, seus intervalos de busca e calcula a raiz

import numpy as np


def funcao(E, e, Mo):
    M = E - e * np.sin(E)
    return M - Mo


def bisseccao(f, an, bn, tol, e, Mo):
    pn = (an + bn) / 2.0
    boolean = True
    while boolean:
        if f(an, e, Mo) * f(pn, e, Mo) < 0:
            bn = pn
        else:
            an = pn
        pn = (an + bn) / 2.0
        if (bn - an) / 2.0 <= tol:
            boolean = False
    return pn
