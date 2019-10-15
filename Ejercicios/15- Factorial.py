print('Calcular el factorial de un número.')
factorial = 1
numero = int(input('Introduzca un número:'))
for numeros in range(1, numero+1):
    factorial = factorial*numeros

print(f'El factorial de {numero} es : {factorial}')
