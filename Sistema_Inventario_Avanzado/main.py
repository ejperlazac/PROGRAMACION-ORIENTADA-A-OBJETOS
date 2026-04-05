from gestor_inventario import Inventario
from producto import Producto


def menu():
    inventario = Inventario()

    while True:
        print("\n===== SISTEMA AVANZADO DE GESTIÓN DE INVENTARIO =====")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                id_producto = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)

            elif opcion == "2":
                id_producto = input("ID a eliminar: ")
                inventario.eliminar_producto(id_producto)

            elif opcion == "3":
                id_producto = input("ID a actualizar: ")
                cantidad = int(input("Nueva cantidad: "))
                precio = float(input("Nuevo precio: "))
                inventario.actualizar_producto(id_producto, cantidad, precio)

            elif opcion == "4":
                nombre = input("Nombre a buscar: ")
                resultados = inventario.buscar_por_nombre(nombre)
                if resultados:
                    for producto in resultados:
                        print(producto)
                else:
                    print("No se encontraron productos.")

            elif opcion == "5":
                inventario.mostrar_todos()

            elif opcion == "6":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida.")

        except ValueError:
            print("Ingrese valores numéricos válidos.")


if __name__ == "__main__":
    menu()