# lista = ['a','b','c']

# for item in enumerate(lista):
#     print(item)

# lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
# for nombre, indice in enumerate(lista_nombres):
#         print(f'{nombre} se encuentra en el índice {indice}')

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier",
                 "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombres in enumerate(lista_nombres):
    if nombres.startswith("M"):
        print(indice)
