precios_cafe = [('capuccino', 1.5), ('Expresso', 1.2), ('moka', 1.9)]
# es un tuple

# for elemento in precios_cafe:
#     print(elemento)

""" 
otra forma de sacar la info contenida en el tuple por cafe y precio seria:
for cafe, precio in precios_cafe:
    print(cafe)
donde se aprecia que en el loop se saca primero una info luego la otra justo en 
su propio orden
 """


def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
    return (cafe_mas_caro, precio_mayor)

print(cafe_mas_caro(precios_cafe))