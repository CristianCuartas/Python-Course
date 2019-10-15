class Restaurant:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.__precio = precio

    def mostar_informacion(self):
        print(
            f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}')

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio


class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio):
        super().__init__(nombre, categoria, precio)


hotel = Hotel('Pythotel', '5 estellas', 10000000)
hotel.mostar_informacion()
