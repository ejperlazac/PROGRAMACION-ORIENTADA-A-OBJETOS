# Programa: Promedio semanal del clima (Programación Tradicional)
# Autor: Evelin Perlaza

def ingresar_temperaturas():
    temperaturas = []
    print("Ingrese la temperatura de los 7 días:")
    for dia in range(1, 8):
        temp = float(input(f"Temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

def main():
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"El promedio semanal es {promedio:.2f} °C")

if __name__ == "__main__":
    main()
