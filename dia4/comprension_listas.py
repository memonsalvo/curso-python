# palabra = 'python'

# lista = []

# for letra in palabra:
#     lista.append(letra)

# print(lista)

# apartir de aqui viene la comprension de lista
# lista = [letra for letra in palabra]

# lista = [ff for ff in 'python']
# print(lista)

# lista = [n for n in range (0,21,2)]
# lista por medio de rango

# lista = [n/2 for n in range (0,21,2)]
# condicional por medio de rango

# lista = [n for n in range(0,21,2) if n * 2 > 10]
# lista por medio de condicional if

pies = [10,20,30,40,50]
metros = [p / 3.281 for p in pies]
# donde se hizo una lista con el metodo de conversion sacando datos de otra lista