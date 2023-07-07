import tkinter
ventana = tkinter.Tk() #constructor de tkinter
ventana.configure(bg='#000000')

titulo = tkinter.Label(ventana, text='Hola Mundo', font=('arial', 24, 'bold'), padx=20,
                    pady=40,bg='#000000', fg='#00ff00')
# se crea el label o parrafo a mostrar y en que ventana y luego su contenido
# se pueden agregar mas parametros para personalizar y dar estilo al label
# los padx y pady son para las dimensiones de los lados en pixeles
# bg == background y fg == foreground y se usa mas que todo en el label
titulo.pack()#con esto hacemos que se empaquete o ensamble el label en la ventana que se eligio

ventana.mainloop() #es el metodo que logra que la ventana siga abierta hasta dar una 
# realizar una accion o dar algun comando o info