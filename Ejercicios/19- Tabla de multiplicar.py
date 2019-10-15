print('Tabla de multiplicar.')
numero = int(input('Introduzca un número:'))
for var in range(0, 10+1):
    multiplicacion = (var*numero)
    print(f'{numero} X {var} = {multiplicacion}')
