while True:
    try:
        x = int(input('Introduce un número: '))
        break
    except ValueError:
        print(f'Debes introducir un número. Error: {ValueError}')
