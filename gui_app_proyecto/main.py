import tkinter as tk
from tkinter import messagebox


class AppGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("Gestor de Datos - GUI")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.crear_componentes()

    def crear_componentes(self):

        # Título
        titulo = tk.Label(
            self.root,
            text="Aplicación GUI Básica",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=10)

        # Frame entrada
        frame_entrada = tk.Frame(self.root)
        frame_entrada.pack(pady=10)

        etiqueta = tk.Label(frame_entrada, text="Ingrese un dato:")
        etiqueta.grid(row=0, column=0, padx=5)

        self.entrada = tk.Entry(frame_entrada, width=30)
        self.entrada.grid(row=0, column=1, padx=5)

        boton_agregar = tk.Button(
            frame_entrada,
            text="Agregar",
            command=self.agregar_dato
        )
        boton_agregar.grid(row=0, column=2, padx=5)

        # Lista de datos
        self.lista = tk.Listbox(self.root, width=50, height=12)
        self.lista.pack(pady=10)

        # Frame botones
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        boton_eliminar = tk.Button(
            frame_botones,
            text="Eliminar seleccionado",
            command=self.eliminar_dato
        )
        boton_eliminar.grid(row=0, column=0, padx=10)

        boton_limpiar = tk.Button(
            frame_botones,
            text="Limpiar lista",
            command=self.limpiar_lista
        )
        boton_limpiar.grid(row=0, column=1, padx=10)

    def agregar_dato(self):

        dato = self.entrada.get()

        if dato == "":
            messagebox.showwarning("Advertencia", "Ingrese un dato primero")
            return

        self.lista.insert(tk.END, dato)
        self.entrada.delete(0, tk.END)

    def eliminar_dato(self):

        try:
            indice = self.lista.curselection()[0]
            self.lista.delete(indice)
        except:
            messagebox.showwarning("Advertencia", "Seleccione un elemento")

    def limpiar_lista(self):

        self.lista.delete(0, tk.END)


if __name__ == "__main__":

    root = tk.Tk()
    app = AppGUI(root)
    root.mainloop()