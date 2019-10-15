class Alumno():
    def __init__(self, nombre=""):
        self.nombre = nombre
        self.__secreto = "contraseña"


alumno_1 = Alumno("Cristian")
print(alumno_1.nombre)


class Circulo():
    def __init__(self, radio):
        self.radio = radio

    @property
    def radio(self):
        print("Estoy dando el radio")
        return self.__radio

    @radio.setter
    def radio(self, radio):
        if radio >= 0:
            self.__radio = radio
        else:
            print("Radio debe ser positivo")
            self.__radio = 0


radio_circulo = Circulo(12)
