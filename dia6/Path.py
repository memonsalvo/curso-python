from pathlib import Path

base = Path.home()
guia = Path(base, 'barcelona', 'sagrada_familia.txt')
# convierte los datos o strings en una ruta de windows
# guia2 = guia.with_name('la_pedrera.txt')
print(guia.parent)
# print(guia2)
