import math

print('Distancia entre el primer valor y el segundo.')
primer_valor = input('Digite el primer número:')
segundo_valor = input('Digite el segundo número:')
primer_valor = float(primer_valor)
segundo_valor = float(segundo_valor)

distancia = math.fabs(primer_valor-segundo_valor)
print(f'Hay {distancia} números de distancia.')
