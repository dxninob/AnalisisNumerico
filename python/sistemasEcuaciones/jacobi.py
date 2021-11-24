import numpy as np


def jacobi(a, x0, tol, maxI, rows, columns):
  tol = float(tol)
  maxI = int(maxI)
  A = np.array([[float(a[j][i]) for i in range(columns-1)] for j in range(rows)])
  b = np.array([float(a[i][columns -1]) for i in range(rows)])
  x0 = np.array(x0)
  x0 = x0.astype(np.float)
  print(A)
  print(b)
  print(x0)
  diagonal= np.diag(A)
  D= np.zeros((rows,columns-1))
  for i in range(rows):
    D[i,i]= diagonal[i]
  print(D)

  L= -np.tril(A)+D
  U= -np.triu(A)+D
  T= np.matmul(np.linalg.inv(D),(L+U))

  autovalores,autovectores= np.linalg.eig(T)
  autovalores= abs(autovalores)

  for i in autovalores:
    if i>=1:
      return 'El metodo no converge', '', ''

  C= np.matmul(np.linalg.inv(D),b)
  xant= x0
  E=1000
  cont=0

  while E>tol and cont<maxI:
    xact= np.matmul(T,xant)+C
    E= np.amax(np.array(abs(xact-xant)))
    xant=xact
    cont= cont+1

  return xact, cont, E