print('Determinar si un número es multiplo del otro')


def EsMultiplo():
    a = int(input('Introduzca un número: '))
    b = int(input('Introduzca un número: '))
    if a % b == 0 or b % a == 0:
        print('Lo números son multiplos entre sí')
    else:
        print('Los números no son multiplos')


EsMultiplo()
