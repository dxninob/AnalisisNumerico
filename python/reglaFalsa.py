!pip install sympy
import sympy as sp
from sympy import *
import math
from math import *
x= symbols('x')
def regla_falsa(fx,x0,xf,maxI,tol):
  if fx.subs(x,x0)*fx.subs(x,xf)==0:
    print(x0, '0', xf, 'son raiz')
  elif fx.subs(x,x0)*fx.subs(x,xf)>0:
    print('no hay raiz')
  else:
    xm= xf- fx.subs(x,xf)*(x0-xf)/(fx.subs(x,x0)-fx.subs(x,xf))
    cont=0
    error= abs(x0-xm)
    while error>tol and maxI>cont and fx.subs(x,xm)!=0:
      if fx.subs(x,x0)*fx.subs(x,xm)<0:
        xf=xm 
      else:
        xi=xm 
      xm= xf- fx.subs(x,xf)*(x0-xf)/(fx.subs(x,x0)-fx.subs(x,xf))
      error= abs(x0-xm)
      cont= cont+1
    if fx.subs(x,xm)==0:
      print(xm,'es raiz')
    elif error<tol:
      print(xm,'es raiz con tolerancia',tol)
    else:
      print('no hay solución')
