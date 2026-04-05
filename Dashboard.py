import os
import subprocess
import json

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

# Clase GestorTareas
# Permite gestionar tareas académicas de Programación Orientada a Objetos
# Incluye funcionalidades para agregar, listar y completar tareas
# Las tareas se almacenan de forma persistente en un archivo JSON
class GestorTareas:
    def __init__(self, archivo_tareas):
        self.archivo_tareas = archivo_tareas
        self.tareas = []
        self.cargar_tareas()

    def cargar_tareas(self):
        if os.path.exists(self.archivo_tareas):
            with open(self.archivo_tareas, 'r', encoding='utf-8') as archivo:
                self.tareas = json.load(archivo)
        else:
            self.tareas = []

    def guardar_tareas(self):
        with open(self.archivo_tareas, 'w', encoding='utf-8') as archivo:
            json.dump(self.tareas, archivo, indent=4, ensure_ascii=False)

    def agregar_tarea(self, descripcion):
        tarea = {
            "descripcion": descripcion,
            "estado": "Pendiente"
        }
        self.tareas.append(tarea)
        self.guardar_tareas()
        print("Tarea agregada correctamente.")

    def listar_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas.")
        else:
            for i, tarea in enumerate(self.tareas, start=1):
                print(f"{i}. {tarea['descripcion']} - {tarea['estado']}")

    def completar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice]["estado"] = "Completada"
            self.guardar_tareas()
            print("Tarea marcada como completada.")
        else:
            print("Índice inválido.")

# Función principal del Dashboard
# Muestra el menú principal y permite:
# - Navegar por unidades del curso
# - Gestionar tareas académicas (agregar, listar, completar)
def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

# Se inicializa el gestor de tareas utilizando un archivo JSON
# ubicado en la misma carpeta del Dashboard
    gestor = GestorTareas(os.path.join(ruta_base, "tareas.json"))
    
    unidades = {
        '1': 'Unidad 1',
        '2': 'Unidad 2'
    }

    while True:
        print("\nMenu Principal - Dashboard")
        for key in unidades:
            print(f"{key} - {unidades[key]}")

    # Opciones adicionales del menú para la gestión de tareas académicas
        print("8 - Agregar tarea POO")
        print("9 - Listar tareas POO")
        print("10 - Completar tarea POO")
        print("0 - Salir")

        eleccion_unidad = input("Elige una unidad o '0' para salir: ")

        if eleccion_unidad == '0':
            print("Saliendo del programa.")
            break

        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))

        elif eleccion_unidad == '8':
            desc = input("Describe la tarea: ")
            gestor.agregar_tarea(desc)

        elif eleccion_unidad == '9':
            gestor.listar_tareas()

        elif eleccion_unidad == '10':
            gestor.listar_tareas()
            num = int(input("Número de tarea a completar: ")) - 1
            gestor.completar_tarea(num)

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_sub_menu(ruta_unidad):
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print("\nSubmenú - Selecciona una subcarpeta")
        # Imprime las subcarpetas
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")
        if eleccion_carpeta == '0':
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta]))
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_scripts(ruta_sub_carpeta):
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print("\nScripts - Selecciona un script para ver y ejecutar")
        # Imprime los scripts
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")

        eleccion_script = input("Elige un script, '0' para regresar o '9' para ir al menú principal: ")
        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return  # Regresar al menú principal
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print("No se ejecutó el script.")
                        else:
                            print("Opción no válida. Regresando al menú de scripts.")
                        input("\nPresiona Enter para volver al menú de scripts.")
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()

