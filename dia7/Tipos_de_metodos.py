class Pajaro:
    alas = True 
    def __init__(self, color, especie): 
        self.color = color
        self.especie = especie

    def piar(self):  
        print(f'pio, mi color es {self.color}')#.format(self.color))
        

    def volar(self, metros):
        print(f'El pajaro a volado {metros} metros')

    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es {self.color}')
         
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'puso {cantidad} huevos')#no necesita una instancia para ser invocado
    
# Pajaro.poner_huevos(3)

    @staticmethod
    def mirar():
        print('El pajaro mira')
# Pajaro.mirar()

piolin = Pajaro('amarillo', 'canario')
# piolin.pintar_negro()
        