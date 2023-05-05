# Escribe una función (puedes ponerle cualquier nombre que quieras)
# que reciba cualquier palabra como parámetro, y que devuelva todas sus letras únicas
# (sin repetir) pero en orden alfabético.
# Por ejemplo si al invocar esta función pasamos la palabra"entretenido",
#  debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']

def palabras(palabra):
    # lista = []
    
    for i in palabra:
        lista = list(set(i))
        # recorre la palabra y se almacena letra por letra en n
        # al setear o eliminar duplicados la n comparo los datos previos recorridos 
        # y los almacena
        # en una lista con la palabra 'lista' por ende no es necesario crear una
        # lista vacia ya que justo dentro del loop se esta creando
        # lista.append(n)
        
    lista.sort()
    return lista
# luego fuera del loop se organiza el resultado con sort y se devuelve el resultado final

print(palabras('entretenido'))