# Escribe una función llamada contar_primos() que requiera un solo argumento numérico.
# Esta función va a mostrar en pantalla todos los números primos existentes
# en el rango que va desde cero hasta ese número incluido,
#  y va a devolver la cantidad de números primos que encontró.
# Aclaración, por convención el 0 y el 1 no se consideran primos.
def contar_primos(num):
    primos = [2]
    # 2 es el primer numero primo de mas bajo valor por eso se inicializa con ese
    iteracion = 3
    # se inicia desde el numero 3 a contar ya que no es primo y viene despues del 2
    if num < 2:
        return 0
    
    while iteracion <= num:
        for n in range(3, iteracion,2):
            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2
    print(primos)
    return len(primos)

print(contar_primos(50))