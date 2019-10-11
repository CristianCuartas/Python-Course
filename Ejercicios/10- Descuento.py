print("Descuento en el total de la compra")
valor_compra = input('Valor de la compra:')
valor_compra = float(valor_compra)
descuento = ((valor_compra*15)/100)
descuento = float(descuento)
total = valor_compra - descuento
total = float(total)
print('Su compra aplica el 14% de descuento')
print(f'El total es de: {total} ')
