!pip install sympy
import sympy as sp
from sympy import *
import math
from math import *
x= symbols('x')
def punto_fijo(fx,x0,maxI,tol):
  gx= fx+x
  cont=0
  xn=gx.subs(x,x0)
  error=abs(x0-xn)
  while cont<maxI and error>tol:
    x0=xn
    xn= gx.subs(x,x0)
    error= abs(xn-x0)
    cont= cont+1
  if error<tol:
    print(xn,'es raiz con tolerancia',tol)
  else:
    print('no hay raiz')
