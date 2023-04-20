from random import *
estimado = 0
intentos = 0
numero_secreto = randint(1, 100)
nombre = input('dime tu nombre')
print(f'bueno {nombre}, he pensado un numero entre 1 y 100\nTienes 8 intentos para adivinar')

while intentos < 8:
    estimado = int(input('cual es el numero?: '))
    intentos += 1

    if estimado not in range(1,101):
        print('tu numero no se encuentra en el rango que va de 1 a 100')
        # de esta forma se puede hacer condicional de rangos
    elif estimado < numero_secreto:
        print('mi numero es mas alto')
    elif estimado > numero_secreto:
        print('mi numero es mas bajo')
    else:
        print(f'Felicitaciones {nombre}! Has adivinado en {intentos} intentos')
        break
if estimado != numero_secreto:
    print(f'lo siento, se han agotado los intentos. El numero secreto era {numero_secreto}')