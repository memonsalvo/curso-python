class Pajaro:
    alas = True #atributo de la clase
    #inicio del constructor o la creacion del mismo con su atributo self
    def __init__(self, color, especie): #el cual es siempre necesario al crear constructor
        self.color = color
        self.especie = especie
        # es el constructor y self es el mismo constructor y el color es atributo

mi_pajaro = Pajaro('negro', 'carpintero')#creacion de instancia y valor del atributo

print(f'mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color }')