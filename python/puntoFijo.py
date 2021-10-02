import math

def g(x):
    return math.log(x**2 - 2*x +2)


x0 = float(input('Ingrese el X0: '))
tol = float(input('Ingrese la tolerancia: '))
maxIter = int(input('Ingrese el número máximo de iteraciones: '))

cont = 0
error = tol + 1

while True:
    gx0 = g(x0)
    if error <= tol:
        print('Existe la raiz', x0, 'con tolerancia de', tol)
        print('g(x) = ', gx0)
        print('Error =', error)
        print('Iteración:', cont - 1)
        break
    
    if cont == maxIter:
        print('No se encontró una solución')
        break
    
    xn = gx0
    error =  abs(xn-x0)
    x0 = xn
    cont += 1