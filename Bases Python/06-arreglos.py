lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript']

print(lenguajes[3])

# Ordenar los elementos
lenguajes.sort()
print(lenguajes)

# Acceder un elemento dentro de un texto
aprendiendo = f'Estoy aprendiendo {lenguajes[3]}.'
print(aprendiendo)

# Modificando valores
lenguajes[2] = 'PHP'

# Agregar elementos
lenguajes.append('Ruby')

# Eliminar
del lenguajes[0]

print(lenguajes)

tabla = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(tabla[0][2], tabla[1][1], tabla[2][2])
tabla_2 = [[0, 10]]
tabla.extend(tabla_2)
print(tabla)
tabla_2.insert(1, [11, 20])
print(tabla_2)
print(tabla.pop())
print(tabla.pop(0))
print(tabla.reverse())
