def f(x):
    return (x**3) - 7.51 * (x**2) + 18.4239 * x - 14.8331


xi = float(input('Ingrese el Xi: '))
xf = float(input('Ingrese el Xf: '))
tol = float(input('Ingrese la tolerancia: '))
maxIter = int(input('Ingrese el número máximo de iteraciones: '))

fxi = f(xi)
fxf = f(xf)
if fxi * fxf == 0:
    if fxi == 0:
        print('Existe la raiz', xi)
        print('f(x) = ', fxi)
    else:
        print('Existe la raiz', xf)
        print('f(x) = ', fxf)
    print('Iteración: 0')

elif fxi * fxf > 0:
    print('No hay una raiz')

else:
    cont = 0
    xm = fxf * (xi-xf) / (fxi-fxf)
    fxm = f(xm)
    error = abs(xi-xm)
    while True:
        if error <= tol:
            print('Existe la raiz', xm, 'con tolerancia de', tol)
            print('f(x) = ', fxf)
            print('Xi =', xi, '- Xf =', xf)
            print('Iteración:', cont)
            break

        if fxm == 0:
            print('Existe la raiz', xm)
            print('f(xm) = ', fxf)
            print('Xi =', xi, '- Xf =', xf)
            print('Iteración:', cont)
            break
        
        if cont == maxIter:
            print('No se encontró una solución')
            break

        if fxi * fxm < 0:
            xf = xm
        else:
            xi = xm

        fxi = f(xi)
        fxf = f(xf)

        xm = fxf * (xi-xf) / (fxi-fxf)
        fxm = f(xm)
        error = abs(xi-xm)
        cont += 1