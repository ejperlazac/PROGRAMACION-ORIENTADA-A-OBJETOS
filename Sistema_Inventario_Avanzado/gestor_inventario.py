import json
from producto import Producto


class Inventario:
    def __init__(self):
        self.productos = {}
        self.ids = set()
        self.archivo = "inventario.json"
        self.cargar_archivo()

    def añadir_producto(self, producto):
        if producto.get_id() in self.ids:
            print("El ID ya existe.")
            return

        self.productos[producto.get_id()] = producto
        self.ids.add(producto.get_id())
        self.guardar_archivo()
        print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.ids.remove(id_producto)
            self.guardar_archivo()
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad, precio):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            producto.set_cantidad(cantidad)
            producto.set_precio(precio)
            self.guardar_archivo()
            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        return [
            p for p in self.productos.values()
            if nombre.lower() in p.get_nombre().lower()
        ]

    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
        for producto in self.productos.values():
            print(producto)

    def guardar_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                json.dump(
                    [p.to_dict() for p in self.productos.values()],
                    f,
                    indent=4
                )
        except Exception as e:
            print("Error al guardar:", e)

    def cargar_archivo(self):
        try:
            with open(self.archivo, "r") as f:
                datos = json.load(f)
                for item in datos:
                    producto = Producto.from_dict(item)
                    self.productos[producto.get_id()] = producto
                    self.ids.add(producto.get_id())
        except FileNotFoundError:
            with open(self.archivo, "w") as f:
                json.dump([], f)
        except json.JSONDecodeError:
            self.productos = {}
            self.ids = set()