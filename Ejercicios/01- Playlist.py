playlist = {}
playlist['canciones'] = []


def app():
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input('Nombre de la Playlist: \r\n')
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            agregar_playlist = False
            agregar_canciones()


def agregar_canciones():
    agregar_canciones = True

    while agregar_canciones:
        nombre_playlist = playlist['nombre']
        pregunta = f'\r\n Agrega canciones a tu playlist {nombre_playlist}: \r\n'
        pregunta += 'Escribe "X" para salir.\r\n'

        cancion = input(pregunta)
        if cancion == 'X':
            print('Finalizando...')
            agregar_canciones = False
            mostrar_resumen()
        else:
            playlist['canciones'].append(cancion)
            print(playlist)


def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    canciones_playlist = playlist['canciones']

    print(f'Playlist: {nombre_playlist} \r\n')
    print(f'Canciones: \r\n')
    for cancion in canciones_playlist:
        print(f'\r\n{cancion}')


app()
