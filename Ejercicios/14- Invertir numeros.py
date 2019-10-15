print('Invertir números')
print('Presione el número 0 para salir.')

condicion = True


def num():
    numero = input('Introduzca un número de dos cifras:')
    numero = int(numero)
    if numero == 0:
        condicion = False
    elif len(str(numero)) > 2 or len(str(numero)) < 2:
        print('El número debe ser de dos cifras')
        condicion = False
        num()

    return numero


while condicion:
    x = num()
    if not x == 0:
        condicion = False
    else:
        x = str(x)
        print(f'El número invertido es: {x[1]}{x[0]}')
