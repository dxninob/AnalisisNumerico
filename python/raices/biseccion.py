from sympy import *
from math import *


x = symbols('x')


def biseccion(fx, xi, xf, maxI, tol):
  fx = parse_expr(fx)

  if fx.subs(x,xi) * fx.subs(x,xf) == 0:
    return str(xi) + ' o ' + str(xf) + ' son raiz'
    lblMensaje.config(text = mensaje)

  elif fx.subs(x,xi) * fx.subs(x,xf) > 0: 
    return 'No hay raiz'
    lblMensaje.config(text = mensaje)

  else:
    xm = (xi+xf)/2
    cont = 0
    error = abs(xi-xm)

    while error > tol and maxI > cont and fx.subs(x,xm) != 0:
      if fx.subs(x,xi) * fx.subs(x,xm) < 0:
        xf = xm 
      
      else: 
        xi = xm 

      xm = (xi+xf)/2
      error = abs(xm-xi)
      cont = cont + 1

    if fx.subs(x,xm) == 0:
      return str(xm) + ' es raiz'

    elif error < tol:
      return str(xm) + ' es raiz con tolerancia ' + str(error)
      
    else:
      return 'No hay solución'
