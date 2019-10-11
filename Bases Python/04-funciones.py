def informacion(name, lenguaje='python'):
    print(
        f'Soy {name} y trabajo con {lenguaje}. Esta es mi primera función con python.')


informacion('Cristian', 'React Js')
informacion('Ricardo')


def dataUsuario(email):
    return email


usuario = dataUsuario('cristianhz1109@gmail.com')
print(usuario)


def mensaje_bienvenida():
    print('Bienvenido')


mensaje_bienvenida()

nombre_visitante = 'Cristian'


def mensaje_bienvenida_visitante(nombre):
    print(f'Bienvenido {nombre}')


mensaje_bienvenida_visitante(nombre_visitante)
