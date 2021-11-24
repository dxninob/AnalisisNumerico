import sympy as sp
from sympy import *
import math
from math import *


x= symbols('x')

def punto(fx, x0, maxI, tol):
  gx= fx+x
  cont=0
  xn=gx.subs(x,x0)
  error=abs(x0-xn)

  while cont<maxI and error>tol:
    fx = parse_expr(fx)
    x0=xn
    xn= gx.subs(x,x0)
    error= abs(xn-x0)
    cont= cont+1

  if error<tol:
    return str(xn) + ' es raiz con tolerancia ' + str(tol)

  else:
    return 'No hay raiz'