class Restaurant:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def mostar_informacion(self):
        print(
            f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}')

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio


class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, penhouse):
        super().__init__(nombre, categoria, precio)
        self.penhouse = penhouse

    def get_penhouse(self):
        return self.penhouse

    def mostar_informacion(self):
        print(
            f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}, Penhouse: {self.penhouse}')


hotel = Hotel('Pythotel', '5 estellas', 10000000, 'Si')
hotel.mostar_informacion()
penhouse = hotel.get_penhouse()
print(penhouse)
