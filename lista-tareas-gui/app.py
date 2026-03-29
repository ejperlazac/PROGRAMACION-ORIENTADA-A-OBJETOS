import tkinter as tk

# Lista donde se almacenan las tareas
tareas = []

# -------------------------------
# FUNCIONES (MANEJADORES DE EVENTOS)
# -------------------------------

def agregar_tarea(event=None):
    """Agrega una nueva tarea a la lista"""
    tarea = entrada.get()

    if tarea != "":
        tareas.append({"texto": tarea, "completada": False})
        lista.insert(tk.END, tarea)
        entrada.delete(0, tk.END)


def marcar_completada():
    """Marca una tarea como completada"""
    try:
        indice = lista.curselection()[0]
        tareas[indice]["completada"] = True

        # Cambia visualmente la tarea
        lista.delete(indice)
        lista.insert(indice, f"✔ {tareas[indice]['texto']}")
        lista.itemconfig(indice, {'fg': 'gray'})

    except:
        pass


def eliminar_tarea():
    """Elimina una tarea seleccionada"""
    try:
        indice = lista.curselection()[0]
        lista.delete(indice)
        tareas.pop(indice)
    except:
        pass


def doble_click(event):
    """Evento opcional: doble clic para completar tarea"""
    marcar_completada()


# -------------------------------
# INTERFAZ GRÁFICA
# -------------------------------

ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x400")

# Campo de entrada
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=10)

# Evento: presionar ENTER
entrada.bind("<Return>", agregar_tarea)

# Lista de tareas
lista = tk.Listbox(ventana, width=40, height=10)
lista.pack(pady=10)

# Evento opcional: doble clic
lista.bind("<Double-Button-1>", doble_click)

# Botones
btn_agregar = tk.Button(ventana, text="Añadir Tarea", command=agregar_tarea)
btn_agregar.pack(pady=5)

btn_completar = tk.Button(ventana, text="Marcar como Completada", command=marcar_completada)
btn_completar.pack(pady=5)

btn_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# Ejecutar aplicación
ventana.mainloop()