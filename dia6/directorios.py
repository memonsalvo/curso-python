from pathlib import Path
# import os
# ruta = os.getcwd()
# para ver en que ruta me encuentro actualmente
# ruta = os.chdir('C:\\Users\\miguel\\Desktop\\curso-python\\dia6')
# para cambiar a una ruta en especifico
# ruta = os.makedirs('C:\\Users\\miguel\\Desktop\\curso-python\\dia7')
#para crear una nueva carpeta al final de la ruta solo se pone el nombre

# print(ruta)
# archivo = open('prueba2.txt')
# print(archivo.read())
# ruta = 'C:\\Users\\miguel\\Desktop\\curso-python\\dia6\\Prueba.txt'
# elemento = os.path.basename(ruta)
# print(elemento)
carpeta = Path('C:/Users/miguel/Desktop/curso-python/dia6')
archivo = carpeta / 'Prueba2.txt'
mi_archivo = open('Prueba2.txt')
print(mi_archivo.read())