!pip install sympy
import sympy as sp
from sympy import *
import math
from math import *
x= symbols('x')
def busquedas_in(fx,x0,cx,maxI):
  if fx.subs(x,x0)==0:
    print(x0, 'Es raiz')
  else: 
    cont= 0
    x1= x0+cx
  while cont<maxI and float(fx.subs(x,x0)*fx.subs(x,x1))>0:
    cont= cont+1
    x0= x1 
    x1= x0+cx
  if fx.subs(x,x1)==0:
    print(x1, 'Es raiz')
  elif fx.subs(x,x0)*fx.subs(x,x1)<0:
    print('Entre', x0, 'y', x1, 'hay al menos una raiz')
  else: 
    print('no hay solución')

busquedas_in(x-1,-1,0.5,20) 
