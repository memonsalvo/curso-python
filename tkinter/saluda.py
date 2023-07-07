import tkinter

ventana = tkinter.Tk()

nombre_var = tkinter.StringVar()

def cambio_nombre():
    hola_nombre.configure(text='Hola ' + nombre_var.get())

hola_nombre = tkinter.Label(ventana, text='Hola nombre', font=('arial', 20), padx=20, pady=10)
hola_nombre.pack()

nombre = tkinter.Entry(ventana, font=('arial',16), textvariable=nombre_var)#para ingresar datos
nombre.pack(padx=20, pady=10)

boton_cambio = tkinter.Button(ventana, text='Cambio', font=('arial',16), command=cambio_nombre)
boton_cambio.pack(padx=20, pady=10)

ventana.mainloop()#siempre debe ir de ultimo sino se cierran las ventanas solas