# ================================================
#                 EJEMPLO DE ABSTRACCIÓN
# ================================================

class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def descripcion(self):
        return f"Vehículo: {self.marca} {self.modelo}, Año {self.anio}"


# Programa principal
vehiculo1 = Vehiculo("Toyota", "Corolla", 2020)
print(vehiculo1.descripcion())


