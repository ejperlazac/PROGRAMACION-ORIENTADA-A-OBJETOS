# Programa: Promedio semanal del clima (Programación Orientada a Objetos)
# Autor: Evelin Perlaza

class ClimaSemana:

    def __init__(self):
        self.__temperaturas = []

    def ingresar_temperaturas(self):
        print("Ingrese la temperatura de los 7 días:")
        for dia in range(1, 8):
            temp = float(input(f"Temperatura del día {dia}: "))
            self.__temperaturas.append(temp)

    def calcular_promedio(self):
        if len(self.__temperaturas) == 0:
            return 0
        return sum(self.__temperaturas) / len(self.__temperaturas)

    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"El promedio semanal es {promedio:.2f} °C")

if __name__ == "__main__":
    clima = ClimaSemana()
    clima.ingresar_temperaturas()
    clima.mostrar_promedio()
