# Crea una función llamada devolver_distintos()
# que reciba 3 integers como parámetros.
# Si la suma de los 3 numeros es mayor a 15
# , va a devolver el número mayor.
# Si la suma de los 3 numeros es menor a 10 , va a
# devolver elnúmero menor.
# Si la suma de los 3 números es un valor
# entre 10 y 15(incluidos) va a devolver el número de
# valor intermedio.
a = int(input('digita el 1er numero:\n'))
b = int(input('digita el 2do numero:\n'))
c = int(input('digita el 3er numero:\n'))
def devolver_distintos(a,b,c):
    suma = a+b+c
    lista = [a,b,c]
    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]
# al poner la lista en orden se puede elegir facilmente el valor de
# en medio ya que son solo 3 valores 0 , 1 y 2
print('\n',devolver_distintos(a,b,c))