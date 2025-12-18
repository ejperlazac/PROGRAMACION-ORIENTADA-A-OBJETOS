class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def mostrar_datos(self):
        return f"Cliente: {self.nombre}, Cédula: {self.cedula}"


class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def reservar(self):
        self.disponible = False

    def liberar(self):
        self.disponible = True


class Reserva:
    def __init__(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias

    def confirmar_reserva(self):
        if self.habitacion.disponible:
            self.habitacion.reservar()
            total = self.habitacion.precio * self.dias
            return (
                f"{self.cliente.mostrar_datos()}\n"
                f"Habitación {self.habitacion.numero} reservada por {self.dias} días.\n"
                f"Total a pagar: ${total}"
            )
        else:
            return "La habitación no está disponible."


# Ejecución del programa
cliente1 = Cliente("Evelyn Perlaza", "0102030405")
habitacion1 = Habitacion(101, "Matrimonial", 45)
reserva1 = Reserva(cliente1, habitacion1, 3)

print(reserva1.confirmar_reserva())
