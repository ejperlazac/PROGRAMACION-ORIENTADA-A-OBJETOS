# Programa: Gestión de Servicios Turísticos – Constructores y Destructores
# Asignatura: Programación Orientada a Objetos | Semana 07
# Autora: Evelin Perlaza


class ServicioTuristico:
    def __init__(self, nombre_servicio, destino, precio):
        self.nombre_servicio = nombre_servicio
        self.destino = destino
        self.precio = precio
        print(f"Servicio turístico creado: {self.nombre_servicio}")

    def mostrar_informacion(self):
        print("Información del servicio turístico:")
        print(f"Servicio: {self.nombre_servicio}")
        print(f"Destino: {self.destino}")
        print(f"Precio: ${self.precio}")

    def __del__(self):
        print(f"Servicio turístico eliminado: {self.nombre_servicio}")


class RegistroTuristico:
    def __init__(self, archivo):
        self.archivo = open(archivo, "w", encoding="utf-8")
        print("Archivo de registro turístico abierto.")

    def registrar_servicio(self, servicio):
        self.archivo.write("Registro de Servicio Turístico\n")
        self.archivo.write(f"Servicio: {servicio.nombre_servicio}\n")
        self.archivo.write(f"Destino: {servicio.destino}\n")
        self.archivo.write(f"Precio: ${servicio.precio}\n")
        self.archivo.write("-----------------------------\n")

    def __del__(self):
        if not self.archivo.closed:
            self.archivo.close()
            print("Archivo de registro turístico cerrado.")


if __name__ == "__main__":
    servicio1 = ServicioTuristico(
        "Tour Cultural",
        "Centro Histórico de Quito",
        35.00
    )

    servicio1.mostrar_informacion()

    registro = RegistroTuristico("registro_turismo.txt")
    registro.registrar_servicio(servicio1)

    del servicio1
    del registro
