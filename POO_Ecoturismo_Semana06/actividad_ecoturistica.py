# Aplicación de Programación Orientada a Objetos en Python
# Tema: Actividades Ecoturísticas - Semana 06
# Autora: Evelin Perlaza

# -------------------------------
# CLASE BASE
# -------------------------------
class Actividad:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.__precio = precio  # Atributo privado (encapsulación)

    # Método getter
    def obtener_precio(self):
        return self.__precio

    # Método setter
    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio

    # Método a sobrescribir (polimorfismo)
    def descripcion(self):
        return "Actividad turística general"


# -------------------------------
# CLASE DERIVADA (HERENCIA)
# -------------------------------
class CaminataSelva(Actividad):
    def __init__(self, nombre, precio, duracion_horas):
        super().__init__(nombre, precio)
        self.duracion_horas = duracion_horas

    # Sobreescritura de método (polimorfismo)
    def descripcion(self):
        return f"Caminata por la selva con duración de {self.duracion_horas} horas"


# -------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------
if __name__ == "__main__":

    # Creación de objetos (instanciación)
    actividad_general = Actividad("Observación de fauna", 15)
    caminata = CaminataSelva("Ruta amazónica", 25, 4)

    # Uso de métodos
    print("Actividad:", actividad_general.nombre)
    print("Precio:", actividad_general.obtener_precio())
    print("Descripción:", actividad_general.descripcion())

    print("\nActividad:", caminata.nombre)
    print("Precio:", caminata.obtener_precio())
    print("Descripción:", caminata.descripcion())

    # Modificación de precio usando encapsulación
    caminata.cambiar_precio(30)
    print("\nNuevo precio de la caminata:", caminata.obtener_precio())
