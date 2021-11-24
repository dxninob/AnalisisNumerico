import sympy as sp
from sympy import *
import math
from math import *


x= symbols('x')

def secante(fx,x0,xf,maxI,tol):
  fx = parse_expr(fx)
  cont=0
  error=tol+1

  while cont<maxI and error>tol:
    xn= x0-fx.subs(x,x0)*(xf-x0)/(fx.subs(x,xf)-fx.subs(x,x0))
    error= abs(xn-x0)
    xf=x0
    x0=xc
    cont= cont+1

  if error<tol:
    return str(xn) + ' es raiz con tolerancia ' + str(tol)

  else:
    return 'No hay raiz'
