"""
Programa: Cálculo del área de un rectángulo
Descripción: Este programa solicita el ancho y el alto de un rectángulo,
calcula su área y determina si es grande o pequeño.
Autora: Evelin Perlaza
"""

ancho_rectangulo = float(input("Ingrese el ancho del rectángulo: "))
alto_rectangulo = float(input("Ingrese el alto del rectángulo: "))

area_rectangulo = ancho_rectangulo * alto_rectangulo
es_rectangulo_grande = area_rectangulo >= 50

print("El área del rectángulo es:", area_rectangulo)

if es_rectangulo_grande:
    print("El rectángulo es considerado grande.")
else:
    print("El rectángulo es considerado pequeño.")


