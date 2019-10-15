class Moto():
    # init  => constructor, inicializador
    def __init__(self, marca):
        self.marca = marca
        print("Objeto creado")
    # Metodos

    def propietario(self):
        print('Moto de {}'.format(self.marca))


moto_1 = Moto('Cristian Hernandez')
moto_1.propietario()
