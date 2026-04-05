import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import re

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("650x400")
        self.root.resizable(False, False)

        # ===== FRAME PRINCIPAL =====
        main_frame = tk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # ===== FRAME LISTA =====
        frame_lista = tk.Frame(main_frame)
        frame_lista.pack(fill=tk.BOTH, expand=True)

        columns = ("Fecha", "Hora", "Descripción")
        self.tree = ttk.Treeview(frame_lista, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        self.tree.pack(side="left", fill=tk.BOTH, expand=True)

        # SCROLLBAR
        scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # ===== FRAME ENTRADA =====
        frame_entrada = tk.Frame(main_frame)
        frame_entrada.pack(fill=tk.X, pady=10)

        tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0)
        self.fecha_entry = DateEntry(frame_entrada, date_pattern='yyyy-mm-dd')
        self.fecha_entry.grid(row=0, column=1, padx=5)

        tk.Label(frame_entrada, text="Hora:").grid(row=0, column=2)
        self.hora_entry = tk.Entry(frame_entrada)
        self.hora_entry.grid(row=0, column=3, padx=5)

        tk.Label(frame_entrada, text="Descripción:").grid(row=0, column=4)
        self.desc_entry = tk.Entry(frame_entrada)
        self.desc_entry.grid(row=0, column=5, padx=5)

        # ===== FRAME BOTONES =====
        frame_botones = tk.Frame(main_frame)
        frame_botones.pack(fill=tk.X)

        tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones, text="Eliminar Evento", command=self.eliminar_evento).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones, text="Salir", command=root.quit).pack(side=tk.RIGHT, padx=5)

    # ===== VALIDAR HORA =====
    def validar_hora(self, hora):
        return re.match(r"^([01]\d|2[0-3]):([0-5]\d)$", hora)

    # ===== AGREGAR EVENTO =====
    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.desc_entry.get()

        if not (fecha and hora and descripcion):
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        if not self.validar_hora(hora):
            messagebox.showwarning("Error", "Formato de hora inválido (HH:MM)")
            return

        self.tree.insert("", tk.END, values=(fecha, hora, descripcion))
        self.limpiar_campos()

        messagebox.showinfo("Éxito", "Evento agregado correctamente")

    # ===== ELIMINAR EVENTO =====
    def eliminar_evento(self):
        selected_item = self.tree.selection()

        if selected_item:
            confirm = messagebox.askyesno("Confirmar", "¿Desea eliminar el evento?")
            if confirm:
                self.tree.delete(selected_item)
                self.tree.selection_remove(selected_item)
        else:
            messagebox.showwarning("Error", "Seleccione un evento")

    # ===== LIMPIAR CAMPOS =====
    def limpiar_campos(self):
        self.hora_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)


# ===== EJECUCIÓN =====
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
