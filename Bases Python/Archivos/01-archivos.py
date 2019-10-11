def app():
    archivo = open('archivo.txt', 'w')  # w es escritura

    # Generar numeros en archivo
    for i in range(0, 10):
        archivo.write('Esta es la linea' + str(i) + "\n")

    # Cerrar el archivo
    archivo.close()


app()
