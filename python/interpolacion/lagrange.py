import sympy as sym
import numpy as np


x = sym.Symbol("x")

def lagrange(X, Y):
    X = np.array(X)
    Y = np.array(Y)
    X = X.astype(np.float)
    Y = Y.astype(np.float)
    n = X.size
    p = 0

    for k in range(n):
        L=1
        for i in range(n):
            if i != k:
                L = L*((x-X[i])/(X[k]-X[i]))
        p = p +L*(Y[k])
    p = sym.simplify(sym.expand(p))

    return p