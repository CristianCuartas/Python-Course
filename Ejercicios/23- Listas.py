import random

print('Lista de 10 números con su potencia al cuadrado y al cubo')


def listaAleatoria():
    lista = [0] * 10
    cuadrado = [0]*10
    cubo = [0]*10
    for i in range(0, 10):
        lista[i] = random.randint(0, 100)
        cuadrado[i] = (lista[i]**2)
        cubo[i] = (lista[i]**3)
    print(lista)
    print(f'Valores al cuadrado: {cuadrado}')
    print(f'Valores al cubo: {cubo}')


listaAleatoria()
