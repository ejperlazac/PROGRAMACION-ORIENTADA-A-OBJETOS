from inventario import Inventario


def menu():
    inventario = Inventario()

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            inventario.agregar_producto(nombre, precio, cantidad)
            print("Producto agregado correctamente.")

        elif opcion == "2":
            inventario.mostrar_productos()

        elif opcion == "3":
            nombre = input("Ingrese el nombre a buscar: ")
            producto = inventario.buscar_producto(nombre)
            if producto:
                print(producto.mostrar_info())
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
