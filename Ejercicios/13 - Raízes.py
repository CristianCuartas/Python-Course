import math
print('Raíz cuadrada y raíz cúbica')
numero = input('Ingrese un número:')
numero = float(numero)

raiz_cuadrada = math.sqrt(numero)
raizCubica = numero**(1/3)

print(f'La raíz cuadrada de {numero} es de: {raiz_cuadrada}')
print(f'La raíz cúbica de {numero} es de: {raizCubica}')
