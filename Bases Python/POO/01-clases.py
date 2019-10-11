class Restaurant:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.__precio = precio
        # Default: public, _PROTECTED, __PRIVATE

    # def agregar_restaurant(self, nombre):
    #     self.nombre = nombre

    def mostar_informacion(self):
        print(
            f'Restaurant: {self.nombre}, Tipo de comida: {self.categoria}, Precio: {self.__precio}')

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio


restaurant = Restaurant('Pozzeto', 'Comida Italiana', 100.000)
# restaurant.agregar_restaurant('Pozzeto')
# restaurant.__precio = 120.000

restaurant.mostar_informacion()
restaurant.set_precio(70.000)
restaurant.get_precio()

restaurant2 = Restaurant('Wok', 'Comida de Mar', 200.000)
# restaurant2.agregar_restaurant('Wok')
# restaurant._precio = 220.000

restaurant2.mostar_informacion()
restaurant.set_precio(120.000)
restaurant2.get_precio()

# Mostrar información
# print(f'Nombre Restaurant: {restaurant.nombre}')
# print(f'Nombre Restaurant: {restaurant2.nombre}')
