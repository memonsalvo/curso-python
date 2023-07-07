import tkinter

ventana = tkinter.Tk()

def login():
    nombre = nombre_var.get()
    contra = pass_var.get()
    
    if nombre == 'admin' and contra == '123':
        msm_label.configure(text='Bienvenido profesor')
    else:
        msm_label.configure(text='usuario o contraseña invalido')
# variables
nombre_var = tkinter.StringVar()
pass_var = tkinter.StringVar()



nombre_label = tkinter.Label(ventana, text='Nombre Usuario',
                              font=('arial', 18),).pack(padx=20, pady=10)
nombre_entry = tkinter.Entry(ventana, 
                             font=('arial', 16), textvariable=nombre_var).pack(padx=20, pady=10)

contra_label = tkinter.Label(ventana, text='Contraseña',
                              font=('arial', 18)).pack(padx=20, pady=10)
contra_entry = tkinter.Entry(ventana,
                              font=('arial', 16), textvariable=pass_var).pack(padx=20, pady=10)

boton_ingresar = tkinter.Button(ventana, text='ingresar',
                                 font=('arial', 18), command=login).pack(padx=20, pady=10)


msm_label = tkinter.Label(ventana, text='', font=('arial', 18),)
msm_label.pack(padx=20, pady=5)

ventana.mainloop()