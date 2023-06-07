nombre = input('\ndigita tu nombre: \n')
venta = int(input('\ndigita el total en ventas: \n'))
venta = venta * 0.13
print(f'\n{nombre} tus comisiones en total son de: {round(venta, 2)}')