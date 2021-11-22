def pivoteoTotal(A,b):
  n = b.size
  ab =  np.concatenate((A,b.T),axis=1)
  Ab = np.array(ab,dtype=float)
  x = np.array(list(range(n)))

  for k in range(0,n):
    A = Ab[:,:-1]
    c = abs(A[k:,k:]).max()
    index = np.where(abs(A)==c)

    c_temp = Ab[:,index[1][0]].copy()
    Ab[:,index[1][0]]= Ab[:,k].copy()
    Ab[:,k] = c_temp

    x_temp= x[index[1][0]]
    x[index[1][0]]= x[k]
    x[k]= x_temp

    r_temp= Ab[index[0][0],:].copy()
    Ab[index[0][0],:]= Ab[k,:].copy()
    Ab[k,:] = r_temp
    Ab[k,:]= Ab[k,:]*(1/c)

    for i in range(0,n):
      if i != k:
        Ab[i,:]= Ab[i,:].copy()+Ab[k,:].copy()*(-Ab[i,k].copy())

  S= Ab[:,-1]
  B= []

  for i in range(0,n):
    B.append(S[np.where(x==i)])

  return B



pivoteoTotal(np.array([[2,-1,-3,2],[5,-10,2,-6],[5,-9,15,-6],[2,1,-1,10]]),np.array([[4,3,2,1]]))