import sympy as sp
from sympy import *
import math
from math import *


x= symbols('x')

def busquedas(fx, x0, cx, maxI):
  fx = parse_expr(fx)
  
  if fx.subs(x,x0) == 0:
    return str(x0)+ ' es raiz '

  else: 
    cont= 0
    x1= x0+cx

  while cont < maxI and float(fx.subs(x, x0) * fx.subs(x, x1)) > 0:
    cont = cont+1
    x0 = x1 
    x1 = x0+cx

  if fx.subs(x,x1) == 0:
    return str(x1) + ' es raiz '

  elif fx.subs(x,x0) * fx.subs(x, x1) < 0:
    return 'Entre ' + str(x0) + ' y ' + str(x1) + ' hay al menos una raiz'

  else: 
    return 'No hay solución'
