print('Suma - Resta - Multiplicación y División')
numero_1 = input('Digite el primer número:')
numero_2 = input('Digite el segundo número:')

numero_1 = float(numero_1)
numero_2 = float(numero_2)

# numero_1 + numero_2
suma = (numero_1 + numero_2)
resta = (numero_1 - numero_2)
multiplicacion = (numero_1 * numero_2)
division = (numero_1/numero_2)
#numero_2 + numero_1
resta_2 = (numero_2 - numero_1)
division_2 = (numero_2/numero_1)

print(f'La suma de los valores es de: {suma}')
print(f'La resta del primer valor menos el segundo valor es de: {resta}')
print(f'La resta del segundo valor menos el primer valor es de: {resta_2}')
print(f'La multiplicación de los valores es de: {multiplicacion}')
print(f'La división del primer valor entre el segundo valor es de: {division}')
print(
    f'La división del segundo valor entre el primer valor es de: {division_2}')
