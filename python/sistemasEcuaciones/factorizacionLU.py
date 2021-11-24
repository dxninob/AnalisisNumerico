def factorizacion_LU(A):
  rows,columns= A.shape
  L= np.zeros((rows,columns))
  U= np.zeros((rows,columns))

  for j in range(rows):
    L[j,j]=1

    for i in range(j+1,rows):
      L[i,j]= A[i,j]/A[j,j]

      for k in range(j+1,rows):
        A[i,k]= A[i,k]-L[i,j]*A[j,k]

      for p in range(j,rows):
        U[j,p]= A[j,p]

  return L,U
