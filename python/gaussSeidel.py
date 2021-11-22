def gauss_seidel(A,b,x0,tol,maxI):
  rows,columns = A.shape
  diagonal= np.diag(A)
  D= np.zeros((rows,columns))

  for i in range(rows):
    D[i,i]= diagonal[i]

  L= -np.tril(A)+D
  U= -np.triu(A)+D
  T= np.matmul(np.linalg.inv(D-L),U)

  autovalores, autovectores = np.linalg.eig(T)
  autovalores= abs(autovalores)

  for i in autovalores:
    if i>=1:
      print('el método no converge')

  C= np.matmul(np.linalg.inv(D-L),b)
  xant= x0
  E=1000
  cont=0

  while E>tol and cont<maxI:
    xact=np.matmul(T,xant)+C
    E= np.amax(np.array(abs(xact-xant)))
    xant=xact
    cont = cont+1

  return xact,cont,E



gauss_seidel(np.array([[1,2,3],[1,4,2],[1,3,3]]),[1,2,3],[1,2,3],1,1)