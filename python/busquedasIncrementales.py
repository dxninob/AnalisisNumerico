def f(x):
    return -90 * (x-45) * (x+40) * (x-27) * (x+95) - 6000000


x0 = float(input('Ingrese el X0: '))
cx = float(input('Ingrese el cambio de X: '))
maxIter = int(input('Ingrese el número máximo de iteraciones: '))

fx0 = f(x0)
if fx0 == 0:
    print('Existe la raiz', fx0)
    print('X =', x0)
    print('Iteración: 0')

else:
    cont = 1
    x1 = x0 + cx
    while True:
        fx1 = f(x1)
        if fx1 == 0:
            print('Existe la raiz', fx1)
            print('X =', x1)
            print('Iteración:', cont)
            break
        
        fx0 = f(x0)
        if fx0 * fx1 < 0:
            print('Existe al menos una raiz entre', f(x0), 'y', f(x1))
            print('X0 =', x0, '- X1 =', x1)
            print('Iteraciónes:', cont - 1, ',', cont)
            break

        if cont == maxIter:
            print('No se encontró una solución')
            break

        x0 = x1
        x1 = x0 + cx
        cont += 1