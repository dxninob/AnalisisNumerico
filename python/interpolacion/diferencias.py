import numpy as np
import sympy as sym


x = sym.Symbol("x")

def difDivididas(X, Y):
    X = np.array(X)
    Y = np.array(Y)
    X = X.astype(np.float)
    Y = Y.astype(np.float)
    n = X.size
    p = 0
    tabla = np.zeros([n, n])
    tabla[:,0] = Y

    for j in range(1,n):
        for i in range(n-j):
            tabla[i][j] = (tabla[i+1][j-1] - tabla[i][j-1]) / (X[i+j]-X[i])

    b = np.array(tabla[0,:])
    mult = 1

    for i in range(n):
        mult =1
        for j in range(i):
            mult = mult * (x-X[j])
            p = p + b[i]*(mult)
    p = sym.simplify(sym.expand(p))

    return p