nombre = input('Cuál es tu nombre: \r\n')
print(f'Hola {nombre}')

# Leer datos numericos
edad = input('Cual es tu edad?\r\n')
edad = int(edad)

if edad >= 18:
    print('El Jamming te espera.\r\n')
else:
    print('Aún no puedes ir al Jamming\r\n')

# Ejercicio

nota = 0
print('Responde con "si" o "no" a las siguientes preguntas.\r\n')
pregunta_1 = input('¿Existe el billete de 100.000 en tu país?\r\n')
pregunta_2 = input('¿Damian Marly es un artista de música urbana?\r\n')
pregunta_3 = input('¿Pink Floyd es una chimba?\r\n')

if pregunta_1 == 'si':
    nota += 1
if pregunta_2 == 'no':
    nota += 1
if pregunta_3 == 'si':
    nota += 1
else:
    nota

print(f'Su calificación es de {nota}/3.')
