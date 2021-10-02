from math import e

def f(x):
    return e **(-x) -x


def df(x):
    return - e **(-x) - 1


x0 = float(input('Ingrese el X0: '))
tol = float(input('Ingrese la tolerancia: '))
maxIter = int(input('Ingrese el número máximo de iteraciones: '))

cont = 0
error = tol + 1

while True:
    fx0 = f(x0)
    dfx0 = df(x0)
    if error <= tol:
        print('Existe la raiz', x0, 'con tolerancia de', tol)
        print('f(x) = ', fx0)
        print('Error =', error)
        print('Iteración:', cont - 1)
        break
    
    if cont == maxIter:
        print('No se encontró una solución')
        break
    
    xn = x0 - fx0/dfx0
    error =  abs(xn-x0)
    x0 = xn
    cont += 1