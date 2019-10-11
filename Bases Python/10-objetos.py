jugador = {}

jugador['nombre_1'] = 'Cristian'
jugador['puntaje_1'] = '1109'
jugador['nombre_2'] = 'David'
jugador['puntaje_2'] = '2019'

print(jugador)

# Iterar en un objeto
for llav, valor in jugador.items():
    print(f'{llav} : {valor}')

# Eliminar
del jugador['nombre_2']
del jugador['puntaje_2']
print(jugador)
