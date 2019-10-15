class Persona():
    def __init__(self, nombre, edad, id):
        self.__nombre = nombre
        self.__edad = edad
        self.__id = id

    #Getters and Setter

    def get_mostrar_info(self):
        print(f'Nombre: {self.__nombre}')
        print(f'Edad: {self.__edad}')
        print(f'ID: {self.__id}')

    def esMayorDeEdad(self):
        if self.__edad < 18:
            print("Es menor de edad.")
        else:
            print("Es mayor de edad")


persona_1 = Persona("Cristian", 19, 1007647968)

persona_1.get_mostrar_info()
persona_1.esMayorDeEdad()
