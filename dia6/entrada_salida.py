# import os
#  para encontrar desde que ruta python se esta ejecutando
# cwd = os.getcwd()
# print("Current working directory: {0}".format(cwd))
# print("os.getcwd() returns an object of type: {0}".format(type(cwd)))
mi_archivo = open('prueba.txt')

# print(mi_archivo.read())
una_linea = mi_archivo.readline()
# readline solo sirve para leer una sola linea del archivo elegido a abrir
print(una_linea)





mi_archivo.close()