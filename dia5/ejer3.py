# Escribe una función que requiera una cantidad indefinida de argumentos.
#  Lo que hará esta función es devolver
# True si en algún momento se ha ingresado al numero
# cero repetido dos veces consecutivas.
# Por ejemplo:
# (5,6,1,0,0,9,3,5) >>>
# True
# (6,0,5,1,0,3,0,1) >>>
# False

def numeros(*args):
    # veces = 2
    # repe = 0
    if args.count(0) == 2:
            return True
    else:
            return False
# no es necesario crear un loop para comparar los datos ya que el count o contador
# dara error ya que la variable donde se almacenara el contenido no seria un entero
# ni un dato tipo contador por la misma razon no se requiere recorrerlo
# sino que python lo hace de forma natural
        
print(numeros(5,6,1,0,0,9,3,5))