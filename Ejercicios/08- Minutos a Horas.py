print('Conversor de minutos a el tiempo en horas y minutos.')

minutos = input('Minutos:')
minutos = float(minutos)

hora_decimales = (minutos/60)

hora_entero = (minutos//60)
hora_entero = int(hora_entero)

minutos_hora = ((hora_decimales - hora_entero)*60)
minutos_hora = int(minutos_hora)

if hora_entero == 1:
    print(f'{hora_entero} hora y {minutos_hora} minutos.')
else:
    print(f'{hora_entero} horas y {minutos_hora} minutos.')
