# def chequear_3_cifras(numero):
    # return numero in range(100,1000)

# def chequear_3_cifras(lista):
#     lista_3_cifras = []
#     for n in lista:
#         if n in range(100,1000):
#             lista_3_cifras.append(n)
#         else:
#             pass
#     return lista_3_cifras

# resultado = chequear_3_cifras([55,99,6000])
# print(resultado)

""" lista_numeros = []
def todos_positivos(lista_numeros):
    for n in lista_numeros:
        if n < 0:
            return False
     return True """

            
        
# resul = todos_positivos([1, -50, 502, -5000, 755, 600, 33, 61])
# print(resul)

lista_numeros = []
def suma_menores(lista_numeros):
    suma = 0
    for n in lista_numeros:
        if n in range(1,1000):
            suma += n
    return suma
