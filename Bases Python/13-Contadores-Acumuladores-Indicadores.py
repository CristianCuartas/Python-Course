#----------------#
# Contador

cont = 0
# cont = cont + 1

for var in range(1, 4):
    numero = int(input('Ingrese un número:'))
    if numero % 2 == 0:
        cont += 1
print(f'Has introducido {cont} números pares.')

#----------------#
# Acumulador
acumulador = 0

for var in range(1, 4):
    numero = int(input('Ingrese un número:'))
    if numero % 2 == 0:
        acumulador += numero
print(f'La suma de los números pares es: {acumulador}')

#----------------#
# Indicadores
indicador = False

for var in range(1, 4):
    numero = int(input('Ingrese un número:'))
    if numero % 2 == 0:
        indicador = True
if indicador:
    print('Hay algún número par.')
else:
    print('Hay algún número impar.')
