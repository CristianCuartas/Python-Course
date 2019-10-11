def parcial_1():
    nota_parcial_1 = input('Nota parcial 1:')
    nota_parcial_1 = float(nota_parcial_1)
    if nota_parcial_1 > 5 or nota_parcial_1 < 1:
        print('La notas debe estar en un rango de 1 a 5')
        notas = False
        parcial_1()
    else:
        return nota_parcial_1


def parcial_2():
    nota_parcial_2 = input('Nota parcial 2:')
    nota_parcial_2 = float(nota_parcial_2)
    if nota_parcial_2 > 5 or nota_parcial_2 < 1:
        print('La notas debe estar en un rango de 1 a 5')
        notas = False
        parcial_2()
    else:
        return nota_parcial_2


def parcial_3():
    nota_parcial_3 = input('Nota parcial 3:')
    nota_parcial_3 = float(nota_parcial_3)
    if nota_parcial_3 > 5 or nota_parcial_3 < 1:
        print('La notas debe estar en un rango de 1 a 5')
        notas = False
        parcial_3()
    else:
        return nota_parcial_3


def examen_final():
    nota_examen_final = input('Nota examen final:')
    nota_examen_final = float(nota_examen_final)
    if nota_examen_final > 5 or nota_examen_final < 1:
        print('La notas debe estar en un rango de 1 a 5')
        notas = False
        examen_final()
    else:
        return nota_examen_final


def trabajo_final():
    nota_trabajo_final = input('Nota trabajo final:')
    nota_trabajo_final = float(nota_trabajo_final)
    if nota_trabajo_final > 5 or nota_trabajo_final < 1:
        print('La notas debe estar en un rango de 1 a 5')
        notas = False
        trabajo_final()

    return nota_trabajo_final
