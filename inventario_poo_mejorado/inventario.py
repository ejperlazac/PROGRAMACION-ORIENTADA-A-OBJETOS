from producto import Producto


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    # ===============================
    # CARGAR INVENTARIO DESDE ARCHIVO
    # ===============================
    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        id_producto = int(datos[0])
                        nombre = datos[1]
                        cantidad = int(datos[2])
                        precio = float(datos[3])
                        producto = Producto(id_producto, nombre, cantidad, precio)
                        self.productos.append(producto)
            print("Inventario cargado correctamente.")
        except FileNotFoundError:
            print("Archivo no encontrado. Se creará uno nuevo.")
            open(self.archivo, "w").close()
        except PermissionError:
            print("Error: No tienes permisos para leer el archivo.")
        except Exception as e:
            print(f"Error inesperado al cargar el archivo: {e}")

    # ===============================
    # GUARDAR INVENTARIO EN ARCHIVO
    # ===============================
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                for p in self.productos:
                    f.write(
                        f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n"
                    )
            print("Inventario guardado correctamente en archivo.")
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar el archivo: {e}")

    # ===============================
    # MÉTODOS CRUD
    # ===============================
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: el ID ya existe.")
                return
        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("Producto eliminado.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad, precio):
        for p in self.productos:
            if p.get_id() == id_producto:
                p.set_cantidad(cantidad)
                p.set_precio(precio)
                self.guardar_en_archivo()
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for p in self.productos:
                print(p)