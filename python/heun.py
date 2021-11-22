x,y = symbols('x,y')

def heun(ecu,y0,a,b,h):
  n= int((b-a)/h)
  X= np.zeros(n+1)
  Y= np.zeros(n+1)
  X[0]= a
  Y[0]= y0
  i=1

  while i<=n:
    X[i]= X[i-1]+h
    Y[i]= Y[i-1]+ (h/2)*(ecu.subs(x,X[i-1]).subs(y,Y[i-1])+ecu.subs(x,X[i]).subs(y,Y[i-1]+h*ecu.subs(x,X[i-1]).subs(y,Y[i-1])))
    i= i+1

  return X,Y



heun(x+y,1,0,1,0.25)