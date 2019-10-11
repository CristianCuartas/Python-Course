
print('Calcular el perímetro y párea de un rectángulo.')
altura_rectangulo = input('Altura del rectángulo: ')
base_rectangulo = input('Base del rectángulo: ')

altura_rectangulo = float(altura_rectangulo)
base_rectangulo = float(base_rectangulo)

perimetro_rectangulo = ((altura_rectangulo*2) + (base_rectangulo*2))
area_rectangulo = ((altura_rectangulo * base_rectangulo))

print(f'=> El perímetro del rectangulo es de: {perimetro_rectangulo}')
print(f'=> El área del rectangulo es de: {area_rectangulo}')
