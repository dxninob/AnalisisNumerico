!pip install sympy
import sympy as sp
from sympy import *
import math
from math import *
x= symbols('x')
def biseccion(fx,xi,xf, maxI, tol):
  if fx.subs(x,xi)*fx.subs(x,xf)==0:
    print(xi, 'o', xf, 'son raiz')
  elif fx.subs(x,xi)*fx.subs(x,xf)>0: 
    print('No hay raiz')
  else:
    xm=(xi+xf)/2
    cont=0
    error=abs(x0-xm)
    while error>tol and maxI>cont and fx.subs(x,xm)!=0:
      if fx.subs(x,xi)*fx.subs(x,xm)<0:
        xf=xm 
      else: 
        xi=xm 
      xm=(xi+xf)/2
      error=abs(xm-xi)
      cont=cont+1
    if fx.subs(x,xm)==0:
      print(xm,'Es raiz')
    elif error<tol:
      print(xm,'Es raiz con tolerancia',tol)
    else:
      print('No hay solución')
