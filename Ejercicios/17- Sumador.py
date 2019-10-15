print('Sumar los valores que se introduzcan.')
print('Presione el número 0 para terminar.')
sumador = 0
numero = int(input('Introzduca un numero:'))
while numero != 0:
    sumador += numero
    numero = int(input('Introzduca un numero:'))
print(f'La suma de los números introducidos es de {sumador}')
