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
