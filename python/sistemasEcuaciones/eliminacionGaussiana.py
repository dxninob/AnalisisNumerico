import numpy as np


def eliminacionGaussiana(a, n, numCol):
  A = np.array([[float(a[j][i]) for i in range(numCol-1)] for j in range(n)])
  b = np.array([[float(a[i][numCol -1]) for i in range(n)]])

  #Creamos matriz aumentada
  ab= np.concatenate((A,b.T),axis=1)
  #Primera etapa (Ax=Ux)
  for k in range(n): #n?
    for i in range(k+1,n):
      mult= ab[i,k]/ab[k,k]
      for j in range(k,n+1):
        ab[i,j]= ab[i,j]-mult*ab[k,j]

  x= np.zeros(n)
  x[n-1]= ab[n-1,n]/ab[n-1,n-1]

  #Segunda etapa (sustitución regresiva)
  for i in range(n-1,-1,-1): 
    sum=0
    for p in range(i+1,n):
      sum= sum+ab[i,p]*x[p]
    x[i]= (ab[i,n]-sum)/ab[i,i]
  return x