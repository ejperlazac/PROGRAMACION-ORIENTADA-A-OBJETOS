import tkinter as tk

# Crear ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("400x450")

# Lista de tareas
tasks = []

# Función para añadir tarea
def add_task(event=None):
    task = entry.get()
    if task != "":
        tasks.append({"text": task, "completed": False})
        update_list()
        entry.delete(0, tk.END)

# Función para actualizar lista visual
def update_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        if task["completed"]:
            listbox.insert(tk.END, "✔ " + task["text"])
            listbox.itemconfig(tk.END, fg="green")
        else:
            listbox.insert(tk.END, "✗ " + task["text"])
            listbox.itemconfig(tk.END, fg="black")

# Marcar tarea como completada
def complete_task(event=None):
    try:
        index = listbox.curselection()[0]
        tasks[index]["completed"] = True
        update_list()
    except:
        pass

# Eliminar tarea
def delete_task(event=None):
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        update_list()
    except:
        pass

# Cerrar aplicación
def exit_app(event=None):
    root.destroy()

# ---------------- UI ----------------

# Entrada
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Botones
btn_add = tk.Button(root, text="Añadir Tarea", command=add_task)
btn_add.pack(pady=5)

btn_complete = tk.Button(root, text="Completar Tarea", command=complete_task)
btn_complete.pack(pady=5)

btn_delete = tk.Button(root, text="Eliminar Tarea", command=delete_task)
btn_delete.pack(pady=5)

# Lista de tareas
listbox = tk.Listbox(root, width=40, height=15)
listbox.pack(pady=10)

# ---------------- EVENTOS ----------------

# Enter → añadir tarea
root.bind("<Return>", add_task)

# C → completar tarea
root.bind("c", complete_task)

# Delete → eliminar tarea
root.bind("<Delete>", delete_task)

# Escape → cerrar app
root.bind("<Escape>", exit_app)

# Ejecutar
root.mainloop()