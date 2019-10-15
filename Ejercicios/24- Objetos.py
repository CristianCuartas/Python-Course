print('Objeto qué almacena el número y su potencia cuadrada')

objeto = {}
condicion = True
while condicion:
    numero = int(input('Introduzca un número: '))
    cuadrado = (numero**2)
    if numero != 0:
        objeto[numero] = cuadrado
    elif numero == 0:
        condicion = False
print(objeto)
