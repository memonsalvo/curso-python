cliente = {'nombre':'federico',
            'edad' : 45,
            'ocupacion': 'instructor' }

pelicula = {'titulo':'matrix',
            'ficha_tecnica':{'prota':'keanu reeves',
                             'director':'lana y lilly wachowski'}}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre':nombre,
              'edad':edad,
              'ocupacion':ocupacion}:
            print('es un cliente')
            print(nombre,edad, ocupacion)
        case {'titulo':titulo,
            'ficha_tecnica':{'prota':prota,
                             'director':director}}:
            print('esto es una pelicula')
            print(titulo, prota, director)