# ================================================
#                     EJEMPLO DE HERENCIA
# ================================================

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        return f"{self.nombre}, {self.edad} años"


class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def mostrar(self):
        return f"Estudiante: {self.nombre}, {self.edad} años - Carrera: {self.carrera}"


# Programa principal
est = Estudiante("María", 20, "Ingeniería")
print(est.mostrar())
