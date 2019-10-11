import os

CARPETA = 'contactos/'  # Carpeta de Contactos
EXTENSIÓN = '.txt'  # Extención del archivo

# Contactos


class Contactos:
    def __init__(self, nombre, telefono, empresa):
        self.nombre = nombre
        self.telefono = telefono
        self.empresa = empresa


def app():
    # Revisa si la carpeta existe o no
    crear_directorio()

    # Muestra el menú
    mostrar_menu()

    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opción:')
        opcion = int(opcion)

# Acciones del menú
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opción no válida, intente nuevamente: ')

# FUNCIONES


def eliminar_contacto():
    print('Eliminar contacto')
    nombre = input('Nombre: ')
    try:
        os.remove(CARPETA + nombre + EXTENSIÓN)
        print('Contacto eliminado con éxito.')
    except IOError:
        print("El contacto que desea eliminar no éxite.")
        print(IOError)
    app()


def buscar_contacto():
    print('Buscar contacto')
    nombre = input('Nombre: ')
    try:
        with open(CARPETA + nombre + EXTENSIÓN, encoding='utf-8') as contacto:
            print('Información del contacto.')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe.')
        print(IOError)
    app()


def mostrar_contactos():
    print('Contactos: ')
    archivos = os.listdir(CARPETA)
    archivos_txt = [i for i in archivos if i.endswith(EXTENSIÓN)]
    for archivo in archivos_txt:
        with open(CARPETA + archivo, encoding='utf=8') as contacto:
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')


def editar_contacto():
    print('Editar contacto')
    nombre_anterior = input('Nombre:')
    existe = existe_contacto(nombre_anterior)
    if existe:
        with open(CARPETA + nombre_anterior + EXTENSIÓN, 'w', encoding='utf-8') as archivo:
            nombre_contacto = input('Editar Nombre:')
            telefono_contacto = input('Editar Teléfono:')
            empresa_contacto = input('Editar Empresa:')

            # Intanciar
            contacto = Contactos(
                nombre_contacto, telefono_contacto, empresa_contacto)

            # Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\n')
            archivo.write('Empresa: ' + contacto.empresa + '\n')
            archivo.close()
            # Renombrar el archivo
            os.rename(CARPETA + nombre_anterior + EXTENSIÓN,
                      CARPETA + nombre_contacto + EXTENSIÓN)
            print('El contaco se edito con éxito.')

    else:
        print('El contacto no existe, intentelo nuevamente')


def agregar_contacto():
    print('Nuevo contacto')
    nombre_contacto = input('Nombre:')

    # Revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_contacto)
    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSIÓN, 'w', encoding='utf-8') as archivo:

            telefono_contacto = input('Teléfono:')
            empresa_contacto = input('Empresa:')

            contacto = Contactos(
                nombre_contacto, telefono_contacto, empresa_contacto)
            archivo.write('Nombre: ' + contacto.nombre + '\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\n')
            archivo.write('Empresa: ' + contacto.empresa + '\n')

            archivo.close()
    else:
        print(f'El contacto "{nombre_contacto}" ya existe.')
    # Reiniciar la app
    app()


def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSIÓN)


def mostrar_menu():
    print('\r\n')
    print('----------------------------------------')
    print('----------------------------------------')
    print(' Seleccione del Menú lo qué desea hacer:')
    print('----------------------------------------')
    print('----------------------------------------')
    print('\r\n')
    print('1) Agregar contacto.')
    print('2) Editar contacto.')
    print('3) Ver contactos.')
    print('4) Buscar contactos.')
    print('5) Eliminar contacto.')


def crear_directorio():
    if not os.path.exists('contactos/'):
        os.makedirs('contactos/')


app()
