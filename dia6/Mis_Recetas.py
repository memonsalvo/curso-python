import os
from pathlib import Path
from os import system

mi_ruta = Path(Path.home(),"dia6","Recetas")

def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1

    return contador

# mostrar menu de inicio 
def inicio():
    system('cls')
    print('*' * 50)
    print('*' * 5 +'Bienvenido al admin de recetas'+ '*' * 5)
    print('*' * 50)
    print('\n')
    print(f'Las recetas se encuentran en {mi_ruta}')
    print(f'Total recetas: {contar_recetas(mi_ruta)}')
    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print('Elige una opcion: ')
        print('''
         [1] - leer receta
         [2] - crear receta nueva
         [3] - crear categoria nueva
         [4] - eliminar receta
         [5] - eliminar categoria
         [6] - salir del programa''')
        eleccion_menu = input()
    return (eleccion_menu)
    # al sobreescribir la variable eleccion_menu se logra dejar el print estatico
    # hasta que el usuario coloque alguna de las opciones a elegir correctas

menu = 0

if menu == 1:
    # mostrar categorias 
    # elegir categoria 
    # mostrar recetas
    # elegir recetas
    # leer receta
    # volver al inicio
    pass
elif menu == 2:
    # mostrar categorias 
    # elegir categoria 
    # crear receta nueva
    # volver al inicio
    pass
elif menu == 3:
    # crear categoria
    # volver al inicio
    pass
elif  menu == 4:
    # mostrar categorias 
    # elegir categoria 
    # mostrar recetas
    # elegir recetas
    # eliminar receta
    # volver al inicio
    pass
elif menu == 5:
    # mostrar categorias 
    # elegir categoria 
    # eliminar categoria
    # volver al inicio
    pass
elif menu == 6:
    # finalizar programa
    pass