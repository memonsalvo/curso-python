from random import *
# primero se invoca o importa la libreria random
# lista inicial
palitos = ['-', '--', '---', '----']

# mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

# pedirle intento
def probar_suerte():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input('Elige un numero del 1 al 4: ')
    # se pone en strings para identificar facilmente el input luego se
    # parsea a entero a su vez se indica que siga el loop mientras la
    # respuesta no sea uno de los 4 numeros
    return int(intento)


# comprobar intento
def chequear_intento(lista, intento):
    if lista[intento - 1] == '-':
        # donde se le resta 1 ya que en las listas empiezan desde 0 y no 1
        print('A lavar los platos compae :v')
    else:
        print('te salvaste!!!')


    print(f'te a tocado {lista[intento-1]}')

palitos_mezclados = mezclar(palitos)
# se le da como argumento la lista de palitos a la funcion para mezclarlos
seleccion = probar_suerte()
# donde se encuentra el numero de intentos
chequear_intento(palitos_mezclados,seleccion)
# ambas funciones se invocan por medio de sus respectivas variables donde se almacenan