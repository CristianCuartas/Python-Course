from random import randrange
print('Adivine el número en 5 intentos.')
intentos = 0
random_num = randrange(100)
print(random_num)
print('Número aleatorio generado.')
num = int(input('Introduzca un número de 1 al 100: '))
while num != random_num:
    if random_num > num:
        print('El número es mayor')
        if intentos == 5:
            print('Ha completado el número de intentos, intente nuevamente')
            break
        num = int(input('Introduzca un número de 1 al 100: '))
        intentos += 1
    elif random_num < num:
        print('El número es menor')
        if intentos == 5:
            print('Ha completado el número de intentos, intente nuevamente')
            break
        num = int(input('Introduzca un número de 1 al 100: '))
        intentos += 1
if random_num == num:
    print(f'Adivinaste! El número es {random_num}')
