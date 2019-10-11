musica = {
    'artista': 'Al2',
    'cancion': 'Amándote',
    'lanzamiento': 2019,
    'reproducciones': 9.5
}

# Acceder al objeto
print(musica['artista'])

# Mexclar con un string
cancion = musica['cancion']
print(f'Estoy escuchando {cancion}')

# Agregar valores
musica['plataforma'] = 'Spotify'

# Reemplazar valores
musica['reproducciones'] = 10.9

# Eliminar valores
del musica['lanzamiento']

print(musica)
