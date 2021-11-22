# Importar métodos
import busquedasIncrementales
import biseccion
import reglaFalsa
import puntoFijo
import newton
import secante
import raicesMultiples
# Importamos librerías
import tkinter as tk
from tkinter import ttk


def deshabilitar(event=None):
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


def anadirP():
    global lblPuntos_x
    global lblPuntos_y
    global entryPuntos_x
    global entryPuntos_y
    global cantidad
    global btnCalcularL
    global px
    global py

    for i in lblPuntos_x:
        i.grid_remove()
    for i in lblPuntos_y:
        i.grid_remove()
    for i in entryPuntos_x:
        i.grid_remove()
    for i in entryPuntos_y:
        i.grid_remove()
    btnCalcularL.grid_forget()

    entryPuntos_x = []
    entryPuntos_y = []
    lblPuntos_x = []
    lblPuntos_y = []
    cantidad = 0
    btnCalcularL = tk.Button()

    cantidad = nump.get()
    p_act = 0
    
    for i in range(3, cantidad+3):
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
    btnCalcularL.grid(padx=20, pady=5, row=cantidad+4, column=1, columnspan=4)


def ejecutarLagrange():
    puntos_x =[]
    puntos_y =[]
    for i in range(len(entryPuntos_x)):
        puntos_x.append(entryPuntos_x[i].get())
        puntos_y.append(entryPuntos_y[i].get())

    print(puntos_x)
    print(puntos_y)
    lblMensajeL = tk.Label(p_lagrange, fg='black', wraplength=600)
    lblMensajeL.grid(padx=20, pady=5, row=cantidad+6, column=1, columnspan=4, rowspan=5, ipadx=20, ipady=20)
    #mensaje = lagrange.lagrange(puntos_x, puntos_y)
    #lblMensajeL.config(text=mensaje)



# Diseño venta
ventana = tk.Tk()
ventana.title("Análisis Numérico")
ventana.geometry('700x400')
ventana.configure()

# Panel para pestañas
nb = ttk.Notebook(ventana)
nb.pack(fill='both', expand='yes')
#nb.grid(row=1, column=1)

# Creamos pestañas
p_metodos = ttk.Frame(nb)
p_vander = ttk.Frame(nb)
p_lagrange = ttk.Frame(nb)



# ---------------------------------- METODOS PARA ENONCTRAR RAICES ----------------------------------
# Lista métodos
metodo_selec = tk.StringVar()
lista_metodos = ttk.Combobox(p_metodos, textvariable=metodo_selec, values=['Busquedas Incrementales', 'Bisección', 'Regla Falsa', 'Punto Fijo', 'Newton', 'Secante', 'Raices Multiples'])
lista_metodos.grid(padx=20, pady=5, row=2, column=1)
# Deshabilitamos los parametros no usados
tk.Button(p_metodos, text='Elegir método', command=deshabilitar).grid(padx=20, pady=5, row=2, column=2)

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
tk.Label(p_metodos, text='Numero máximo de iteraciones = ', fg='black').grid(padx=20, pady=5, row=7, column=1)
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



# ---------------------------------- METODO DE VENDERMONDE ----------------------------------


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

# Cantidad de puntos
tk.Label(p_lagrange, text='Cantidad de puntos: ', fg='black').grid(padx=20, pady=5, row=2, column=1)
nump = tk.IntVar()
nump_entry = tk.Entry(p_lagrange, textvariable=nump)
nump_entry.grid(padx=20, pady=5, row=2, column=2)

# Botón para añadir un puntos
btnPunto = tk.Button(p_lagrange, text='Añadir puntos', command=anadirP, fg='black')
btnPunto.grid(padx=20, pady=5, row=2, column=3)


# Agregamos pestañas
nb.add(p_metodos, text='Métodos')
nb.add(p_vander, text='Vandermonde')
nb.add(p_lagrange, text='Lagrange')

ventana.mainloop()