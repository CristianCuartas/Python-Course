print('Identificar si el caracter introducido es una vocal')
print('Introduzca un espacio para salir.')
caracter = input('Introduzca un caracter:')
vocales = ['a', 'e', 'i', 'o', 'u']
while caracter != ' ':
    if caracter in vocales:
        print('VOCAL')
        caracter = input('Introduzca un caracter:')
    else:
        print('NO VOCAL')
        caracter = input('Introduzca un caracter:')
