# If
balance = 2400

if balance >= 2400:
    print('Luz verde')
else:
    if balance < 2400:
        print('Luz roja')

# If en en estring
mensaje = 'Tenga un buen viaje'

if not mensaje == 'Saldo insuficiente':
    print(mensaje)

# If en booleano
saldo_insuficiente = True

if saldo_insuficiente:
    print('Saldo insufienciente')
else:
    print('Tenga un buen viaje')

# If anidado
saldo_insuficiente = True
prestamo_saldo = True

if saldo_insuficiente:
    if prestamo_saldo:
        print('Tenga un buen viaje')
elif saldo_insuficiente:
    print('Saldo insufienciente')
else:
    print('Tenga un buen viaje')

# If en arreglos
lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript', 'Ruby', 'PHP']

if 'React' in lenguajes:
    print('Framework de JavaScript')
else:
    print('Agregar frameworks al arreglo.')

# For
for lenguaje in lenguajes:
    if lenguaje == 'Python':
        print('Excelente Python')
    else:
        print(lenguaje)
