import FuncionesCalificaciones
print('Calificación de estudiante de 1.0 a 5.0')
notas = True
while notas:
    p1 = FuncionesCalificaciones.parcial_1()
    p2 = FuncionesCalificaciones.parcial_2()
    p3 = FuncionesCalificaciones.parcial_3()
    tf = FuncionesCalificaciones.trabajo_final()
    ef = FuncionesCalificaciones.examen_final()

    promedio_parciales = ((p1+p2+p3)/3)
    nota_examen_final = ef
    nota_trabajo_final = tf
    cien_porciento = 5
    cincuenta_cinco_porciento = (0.55*promedio_parciales)
    treinta_porciento = (0.30*nota_examen_final)
    quince_porciento = (0.15*nota_trabajo_final)
    notaFinal = (cincuenta_cinco_porciento +
                 treinta_porciento + quince_porciento)
    print(f'Nota definitiva: {notaFinal}')

    notas = False
