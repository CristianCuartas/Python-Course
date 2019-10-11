import math
print('Distancia entre puntos en un plano.')
x1 = input('Posición en X:')
x1 = float(x1)
y1 = input('Posición en Y:')
y1 = float(y1)
print('Punto 1 marcado en el plano.')
x2 = input('Posición en X:')
x2 = float(x2)
y2 = input('Posición en Y:')
y2 = float(y2)
print('Punto 2 marcado en el plano')

distancia_x = math.fabs(x1-x2)
distancia_y = math.fabs(y1-y2)

print(f'Entre el punto 1 y el punto 2  la distancia en x es de {distancia_x}')
print(f'Entre el punto 1 y el punto 2 la distancia en y es de {distancia_y}')
