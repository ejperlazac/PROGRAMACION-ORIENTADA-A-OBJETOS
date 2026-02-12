from producto import Producto


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):
        producto = Producto(nombre, precio, cantidad)
        self.productos.append(producto)

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto.mostrar_info())

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None
