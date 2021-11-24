# Importar métodos
from raices import busquedasIncrementales
from raices import biseccion
from raices import reglaFalsa
from raices import puntoFijo
from raices import newton
from raices import secante
from raices import raicesMultiples

from sistemasEcuaciones import eliminacionGaussiana
from sistemasEcuaciones import pivoteoParcial
from sistemasEcuaciones import pivoteoTotal
from sistemasEcuaciones import factorizacionLU
from sistemasEcuaciones import jacobi
from sistemasEcuaciones import gaussSeidel

from interpolacion import diferencias
from interpolacion import lagrange
from interpolacion import splines

# Importamos librerías
import tkinter as tk
from tkinter import ttk



# Metodos raices
def deshabilitarMetodos(event=None):
    opt = metodo_selec.get()
    if opt == 'Busquedas Incrementales':
        xf_entry.config(state='disabled')
        cx_entry.config(state='normal')
        tol_entry.config(state='disabled')
    elif opt == 'Bisección' or opt == 'Regla Falsa' or opt =='Secante':
        xf_entry.config(state='normal')
        cx_entry.config(state='disabled')
        tol_entry.config(state='normal')
    elif opt == 'Newton' or opt == 'Punto Fijo' or opt == 'Raices Multiples':
        xf_entry.config(state='disabled')
        cx_entry.config(state='disabled')
        tol_entry.config(state='normal')
    return opt

# Metodos raices
def ejecutarMetodo(event=None):
    mensaje = ''
    opt = metodo_selec.get()
    if opt == 'Busquedas Incrementales':
        try:
            mensaje = busquedasIncrementales.busquedas(fx.get(), xi.get(), cx.get(), maxI.get())
        except:
            mensaje = 'Se ingresó un dato erroneo'
    elif opt == 'Bisección':
        try:
            mensaje = biseccion.biseccion(fx.get(), xi.get(), xf.get(), maxI.get(), tol.get())
        except:
            mensaje = 'Se ingresó un dato erroneo'
    elif opt == 'Regla Falsa':
        try:
            mensaje = reglaFalsa.regla(fx.get(), xi.get(), xf.get(), maxI.get(), tol.get())
        except:
            mensaje = 'Se ingresó un dato erroneo'
    elif opt == 'Secante':
        try:
            mensaje = secante.secante(fx.get(), xi.get(), xf.get(), maxI.get(), tol.get())
        except:
            mensaje = 'Se ingresó un dato erroneo'
    elif opt == 'Newton':
        try:
            mensaje = newton.newton(fx.get(), xi.get(), maxI.get(), tol.get())
        except:
            mensaje = 'Se ingresó un dato erroneo'
    elif opt == 'Punto Fijo':
        try:
            mensaje = puntoFijo.punto(fx.get(), xi.get(), maxI.get(), tol.get())
        except:
            mensaje = 'Se ingresó un dato erroneo'
    elif opt == 'Raices Multiples':
        try:
            mensaje = raicesMultiples.raices(fx.get(), xi.get(), maxI.get(), tol.get())
        except:
            mensaje = 'Se ingresó un dato erroneo'
    lblMensajeM.config(text=mensaje)



#---------------------------------------------------------------------------------------------------------
# Lagrange
def anadirPLagrange():
    global lblPuntos_x
    global lblPuntos_y
    global entryPuntos_x
    global entryPuntos_y
    global cantidad
    global btnCalcularL
    global px
    global py
    global lblMensajeL

    for i in lblPuntos_x:
        i.grid_remove()
    for i in lblPuntos_y:
        i.grid_remove()
    for i in entryPuntos_x:
        i.grid_remove()
    for i in entryPuntos_y:
        i.grid_remove()

    btnCalcularL.grid_forget()
    lblMensajeL.config(text='')

    entryPuntos_x = []
    entryPuntos_y = []
    lblPuntos_x = []
    lblPuntos_y = []
    cantidad = nump.get()
    btnCalcularL = tk.Button()
    p_act = 0
    
    for i in range(4, cantidad+4):
        lbl_x = tk.Label(p_lagrange, text=f'x{p_act}: ', fg='black')
        lbl_x.grid(padx=20, pady=5, row=i, column=1)
        px = tk.DoubleVar()
        px_entry = tk.Entry(p_lagrange, textvariable=px)
        px_entry.grid(padx=20, pady=5, row=i, column=2)
        
        lbl_y = tk.Label(p_lagrange, text=f'y{p_act}: ', fg='black')
        lbl_y.grid(padx=20, pady=5, row=i, column=3)
        py = tk.DoubleVar()
        py_entry = tk.Entry(p_lagrange, textvariable=py)
        py_entry.grid(padx=20, pady=5, row=i, column=4)

        lblPuntos_x.append(lbl_x)
        lblPuntos_y.append(lbl_y)
        entryPuntos_x.append(px_entry)
        entryPuntos_y.append(py_entry)
        p_act += 1
    btnCalcularL = tk.Button(p_lagrange, text='Calcular', command=ejecutarLagrange, fg='black')
    btnCalcularL.grid(padx=20, pady=5, row=cantidad+5, column=1, columnspan=4)

#Lagrange
def ejecutarLagrange():
    global lblMensajeL
    lblMensajeL.config(text='')
    btnCalcularL.grid_forget()

    opt = inter_select.get()
    puntos_x =[]
    puntos_y =[]
    for i in range(len(entryPuntos_x)):
        puntos_x.append(entryPuntos_x[i].get())
        puntos_y.append(entryPuntos_y[i].get())

    lblMensajeL = tk.Label(p_lagrange, fg='black', wraplength=600)
    lblMensajeL.grid(padx=20, pady=5, row=cantidad+6, column=1, columnspan=4, rowspan=5, ipadx=20, ipady=20)
    mensaje = ''
    if opt == 'Diferencias':
        mensaje = diferencias.difDivididas(puntos_x, puntos_y)
    if opt == 'Lagrange':
        mensaje = lagrange.lagrange(puntos_x, puntos_y)
    if opt == 'Splines':
        mensaje = splines.splinesCuadraticos(puntos_x, puntos_y)
    lblMensajeL.config(text=mensaje)



#---------------------------------------------------------------------------------------------------------
# Sistemas de ecuaciones
def deshabilitarSistemas(event=None):
    opt = sistema_selec.get()
    if opt == 'Gauss' or opt == 'Pivoteo Parcial' or opt == 'Pivoteo Total' or opt == 'LU':
        maxI2_entry.config(state='disabled')
        tol2_entry.config(state='disabled')
    elif opt == 'Jacobi' or opt == 'Gauss Seidel':
        maxI2_entry.config(state='normal')
        tol2_entry.config(state='normal')
    return opt

# Sitemas de ecuaciones
def anadirPSistemas():
    global entryMatriz
    global valoresIniciales
    global cantidadFilas
    global cantidadCol
    global btnCalcularS
    global lblMensajeS
    opt = sistema_selec.get()

    for i in valoresIniciales:
        i.grid_remove()

    for i in entryMatriz:
        for j in i:
            j.grid_remove()
    btnCalcularS.grid_forget()

    cantidadFilas = numFilas.get()
    cantidadCol = numCol.get()
    entryMatriz = []
    valoresIniciales = []
    btnCalcularS = tk.Button()
    lblMensajeS.config(text='')

    for i in range(cantidadFilas):
        entryMatriz.append([])
        for j in range(cantidadCol):
            entryMatriz[i].append(None)

    for i in range(7, cantidadFilas+7):
        for j in range(1, cantidadCol+1):
            matriz = tk.DoubleVar()
            matriz_entry = tk.Entry(p_sistemas, textvariable=matriz)
            matriz_entry.grid(padx=20, pady=5, row=i, column=j)
            entryMatriz[i-7][j-1] = matriz_entry

    if opt == 'Jacobi' or opt == 'Gauss Seidel':
        for i in range(1, cantidadCol):
            valInicial = tk.DoubleVar()
            valInicial_entry = tk.Entry(p_sistemas, textvariable=valInicial)
            valInicial_entry.grid(padx=20, pady=5, row=cantidadFilas+8, column=i)
            valoresIniciales.append(valInicial_entry)

    btnCalcularS = tk.Button(p_sistemas, text='Calcular', command=ejecutarSistemas, fg='black')
    btnCalcularS.grid(padx=20, pady=5, row=cantidadFilas+9, column=1, columnspan=cantidadCol)

# Sistemas de ecuaciones
def ejecutarSistemas():
    global entryMatriz
    global valoresIniciales
    global cantidadFilas
    global cantidadCol
    global btnCalcularS
    global lblMensajeS

    btnCalcularS.grid_forget()
    opt = sistema_selec.get()

    A = []
    valores = []
    for i in range(cantidadFilas):
        A.append([])
        for j in range(cantidadCol):
            A[i].append(None)

    for i in range(cantidadFilas):
        for j in range(cantidadCol):
            A[i][j] = entryMatriz[i][j].get()

    for i in valoresIniciales:
        valores.append(i.get())

    lblMensajeS = tk.Label(p_sistemas, fg='black', wraplength=600)
    lblMensajeS.grid(padx=20, pady=5, row=cantidadFilas+9, column=1, columnspan=cantidadCol, rowspan=5, ipadx=20, ipady=20)
    mensaje = ''
    if opt == 'Gauss':
        mensaje = eliminacionGaussiana.eliminacionGaussiana(A, cantidadFilas, cantidadCol)
    if opt == 'Pivoteo Parcial':
        mensaje = pivoteoParcial.pivoteoParcial(A, cantidadFilas, cantidadCol)
    if opt == 'Pivoteo Total':
        mensaje = pivoteoTotal.pivoteoTotal(A, cantidadFilas, cantidadCol)
    if opt == 'LU':
        mensaje1, mensaje2 = factorizacionLU.factLU(A)
        mensaje = 'L =', mensaje1, '    -----    U=', mensaje2
    if opt == 'Jacobi':
        mensaje1, mensaje2, mensaje3 = jacobi.jacobi(A, valores, tol2_entry.get(), maxI2_entry.get(), cantidadFilas, cantidadCol)
        if mensaje2 != '':
            mensaje = 'X =', mensaje1, ' Iteración =', mensaje2, ' Error=', mensaje3
        else:
            mensaje = mensaje1
    if opt == 'Gauss Seidel':
        mensaje1, mensaje2, mensaje3 = gaussSeidel.seidel(A, valores, tol2_entry.get(), maxI2_entry.get(), cantidadFilas, cantidadCol)
        if mensaje2 != '':
            mensaje = 'X =', mensaje1, ' Iteración =', mensaje2, ' Error=', mensaje3
        else:
            mensaje = mensaje1
    lblMensajeS.config(text=mensaje)



# ---------------------------------- CONFIGURACIÓN DE LA VENTANA ----------------------------------
# Diseño venta
ventana = tk.Tk()
ventana.title("Análisis Numérico")
ventana.geometry('700x400')
ventana.configure()

# Panel para pestañas
nb = ttk.Notebook(ventana)
nb.pack(fill='both', expand='yes')

# Creamos pestañas
p_metodos = ttk.Frame(nb)
p_vander = ttk.Frame(nb)
p_lagrange = ttk.Frame(nb)
p_splines = ttk.Frame(nb)
p_sistemas = ttk.Frame(nb)

# Agregamos pestañas
nb.add(p_metodos, text='Métodos')
nb.add(p_lagrange, text='Interpolación')
nb.add(p_sistemas, text='Sistemas Ecuaciones')



# ---------------------------------- METODOS PARA ENONCTRAR RAICES ----------------------------------
# Lista métodos
metodo_selec = tk.StringVar()
lista_metodos = ttk.Combobox(p_metodos, textvariable=metodo_selec, values=['Busquedas Incrementales', 'Bisección', 'Regla Falsa', 'Punto Fijo', 'Newton', 'Secante', 'Raices Multiples'])
lista_metodos.grid(padx=20, pady=5, row=2, column=1)
# Deshabilitamos los parametros no usados
tk.Button(p_metodos, text='Elegir método', command=deshabilitarMetodos).grid(padx=20, pady=5, row=2, column=2)

# Input f(x)
tk.Label(p_metodos, text='f(x) = ', fg='black').grid(padx=20, pady=5, row=3, column=1)
fx = tk.StringVar()
fx_entry = tk.Entry(p_metodos, textvariable=fx)
fx_entry.grid(padx=20, pady=5, row=3, column=2)

# Input xi
tk.Label(p_metodos, text='x inicial = ', fg='black').grid(padx=20, pady=5, row=4, column=1)
xi = tk.DoubleVar()
xi_entry = tk.Entry(p_metodos, textvariable=xi)
xi_entry.grid(padx=20, pady=5, row=4, column=2)

# Input xf
tk.Label(p_metodos, text='x final = ', fg='black').grid(padx=20, pady=5, row=5, column=1)
xf = tk.DoubleVar()
xf_entry = tk.Entry(p_metodos, textvariable=xf)
xf_entry.grid(padx=20, pady=5, row=5, column=2)

# Input cf
tk.Label(p_metodos, text='Cambio de x = ', fg='black').grid(padx=20, pady=5, row=6, column=1)
cx = tk.DoubleVar()
cx_entry = tk.Entry(p_metodos, textvariable=cx)
cx_entry.grid(padx=20, pady=5, row=6, column=2)

# Input maxI
tk.Label(p_metodos, text='Max iteraciones = ', fg='black').grid(padx=20, pady=5, row=7, column=1)
maxI = tk.IntVar()
maxI_entry = tk.Entry(p_metodos, textvariable=maxI)
maxI_entry.grid(padx=20, pady=5, row=7, column=2)

# Input tol
tk.Label(p_metodos, text='Tolerancia máxima = ', fg='black').grid(padx=20, pady=5, row=8, column=1)
tol = tk.DoubleVar()
tol_entry = tk.Entry(p_metodos, textvariable=tol)
tol_entry.grid(padx=20, pady=5, row=8, column=2)

# Botón para calcular
btnCalcular = tk.Button(p_metodos, text='Calcular', command=ejecutarMetodo, fg='black')
btnCalcular.grid(padx=20, pady=5, row=9, column=1, columnspan = 2)

# Output
lblMensajeM = tk.Label(p_metodos, fg='black', wraplength=600)
lblMensajeM.grid(padx=20, pady=5, row=10, column=1, columnspan=2, rowspan=5, ipadx=20, ipady=20)



# ------------------------------------ METODO DE LAGRANGE ------------------------------------
# Alamcenar puntos
lblPuntos_x = []
lblPuntos_y =[]
entryPuntos_x = []
entryPuntos_y =[]
cantidad = 0
btnCalcularL = tk.Button()
px = 0.0
py = 0.0
lblMensajeL = tk.Label()

# Lista métodos
tk.Label(p_lagrange, text='Método: ', fg='black').grid(padx=20, pady=5, row=2, column=1)
inter_select = tk.StringVar()
lista_inter = ttk.Combobox(p_lagrange, textvariable=inter_select, values=['Diferencias', 'Lagrange', 'Splines'])
lista_inter.grid(padx=20, pady=5, row=2, column=2)
# Deshabilitamos los parametros no usados
#tk.Button(p_lagrange, text='Elegir', command=deshabilitarSistemas).grid(padx=20, pady=5, row=2, column=2)

# Cantidad de puntos
tk.Label(p_lagrange, text='Cantidad de puntos: ', fg='black').grid(padx=20, pady=5, row=3, column=1)
nump = tk.IntVar()
nump_entry = tk.Entry(p_lagrange, textvariable=nump)
nump_entry.grid(padx=20, pady=5, row=3, column=2)

# Botón para añadir un puntos
btnPunto = tk.Button(p_lagrange, text='Añadir puntos', command=anadirPLagrange, fg='black')
btnPunto.grid(padx=20, pady=5, row=3, column=3)



# ------------------------------------ SISTEMAS DE ECUACIONES ------------------------------------
# Lista métodos
sistema_selec = tk.StringVar()
lista_sistemas = ttk.Combobox(p_sistemas, textvariable=sistema_selec, values=['Gauss', 'Pivoteo Parcial', 'Pivoteo Total', 'LU', 'Jacobi', 'Gauss Seidel'])
lista_sistemas.grid(padx=20, pady=5, row=2, column=1)
# Deshabilitamos los parametros no usados
tk.Button(p_sistemas, text='Elegir', command=deshabilitarSistemas).grid(padx=20, pady=5, row=2, column=2)

# Input maxI
tk.Label(p_sistemas, text='Max iteraciones =', fg='black').grid(padx=20, pady=5, row=3, column=1)
maxI2 = tk.IntVar()
maxI2_entry = tk.Entry(p_sistemas, textvariable=maxI2)
maxI2_entry.grid(padx=20, pady=5, row=3, column=2)

# Input tol
tk.Label(p_sistemas, text='Tolerancia máxima =', fg='black').grid(padx=20, pady=5, row=4, column=1)
tol2 = tk.DoubleVar()
tol2_entry = tk.Entry(p_sistemas, textvariable=tol2)
tol2_entry.grid(padx=20, pady=5, row=4, column=2)

# Alamcenar puntos
entryMatriz = []
valoresIniciales = []
cantidadFilas = 0
cantidadCol = 0
btnCalcularS = tk.Button()
lblMensajeS = tk.Label()

# Cantidad de filas
tk.Label(p_sistemas, text='Variables:', fg='black').grid(padx=20, pady=5, row=5, column=1)
numFilas = tk.IntVar()
numFilas_entry = tk.Entry(p_sistemas, textvariable=numFilas)
numFilas_entry.grid(padx=20, pady=5, row=5, column=2)

# Cantidad de columnas
tk.Label(p_sistemas, text='Ecuaciones:', fg='black').grid(padx=20, pady=5, row=6, column=1)
numCol = tk.IntVar()
numCol_entry = tk.Entry(p_sistemas, textvariable=numCol)
numCol_entry.grid(padx=20, pady=5, row=6, column=2)

# Botón para añadir un puntos
btnMatriz = tk.Button(p_sistemas, text='Añadir matriz', command=anadirPSistemas, fg='black')
btnMatriz.grid(padx=20, pady=5, row=6, column=3)



ventana.mainloop()