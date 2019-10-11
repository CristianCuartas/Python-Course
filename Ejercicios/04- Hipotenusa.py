import math
print('Calcular la hipotenusa de un triangulo rectángulo')
cateto_a = input('Cateto A:')
cateto_b = input('Cateto B:')
cateto_a = float(cateto_a)
cateto_b = float(cateto_b)

hipotenusa = ((cateto_a**2) + (cateto_b**2))
hipotenusa = float(hipotenusa)
hipotenusa = math.sqrt(hipotenusa)

print(f'El valor de la hipotenusa es de: {hipotenusa}')
