import sympy as sp
from sympy import *
import math
from math import *


x= symbols('x')

def raices(fx, x0, maxI, tol):
  fx = parse_expr(fx)
  ux= fx/diff(fx)
  uxx= diff(ux)
  cont=0
  error= tol+1

  while cont<maxI and error>tol:
    xn= x0-ux.subs(x,x0)/uxx.subs(x,x0)
    error= abs(xn-x0)
    cont= cont+1
    x0=xn

  if error<=tol:
    return str(xn) + ' es raiz con tolerancia ' + str(tol)
    
  else:
    return 'No converge'
