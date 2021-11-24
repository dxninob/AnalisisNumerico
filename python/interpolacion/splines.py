import sympy as sym
import numpy as np


x = sym.Symbol("x")

def splinesCuadraticos(X, Y):
    X = np.array(X)
    Y = np.array(Y)
    X = X.astype(np.float)
    Y = Y.astype(np.float)
    n = X.size
    y = [(Y[i//2]if i%2==0 else Y[(i)//2]) if i <= 2*(n-1) else 0 for i in range(1, 3*(n-1) + 1)]
  
    tabla = np.zeros([3*(n-1),3*(n-1)])

    for i in range(n-1):
        tabla[2*(i + 1) - 2][3*i] = tabla[2*(i + 1) - 1][3*i] = 1 
        tabla[2*(i + 1) - 2][3*i + 1] = X[i]
        tabla[2*(i + 1) - 2][3*i + 2] = X[i]**2
        tabla[2*(i + 1) - 1][3*i + 1] = X[i + 1]
        tabla[2*(i + 1) - 1][3*i + 2] = X[i + 1]**2

    for i in range(n-2):
        tabla[2*(n-1) + i][3*i + 1] = 1
        tabla[2*(n-1) + i][3*i + 4] = -1 
        tabla[2*(n-1) + i][3*i + 2] = 2*X[i + 1]
        tabla[2*(n-1) + i][3*i + 5] = -2*X[i + 1]

    tabla[3*(n-1) - 1][2] = 2

    tabla = np.linalg.inv(tabla)
    coef = np.matmul(tabla,y)
    p=[]
    cont = 0
    for j in range(n-1):
        pj = coef[cont] + coef[cont+1] * x + coef[cont+2]*x**2
        cont=cont+3
        p.append(pj)

    return p