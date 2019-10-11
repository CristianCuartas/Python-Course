print('Ejercio con porcentajes y cantidades.')
sueldo_base = 10000

venta = input('Valor de la venta 1:')
venta = float(venta)

if venta >= 0:
    porcentaje_ventas = ((venta*10)/100)
    porcentaje_ventas = float(porcentaje_ventas)
    ganancia_venta_1 = (porcentaje_ventas)

venta = input('Valor de la venta 2:')
venta = float(venta)
if venta >= 0:
    porcentaje_ventas = ((venta*10)/100)
    porcentaje_ventas = float(porcentaje_ventas)
    ganancia_venta_2 = (porcentaje_ventas)

venta = input('Valor de la venta 3:')
venta = float(venta)
if venta >= 0:
    porcentaje_ventas = ((venta*10)/100)
    porcentaje_ventas = float(porcentaje_ventas)
    ganancia_venta_3 = (porcentaje_ventas)

comisiones = ganancia_venta_1 + ganancia_venta_2 + ganancia_venta_3
total = sueldo_base + comisiones

print(f'El sueldo total es de: {total}')
