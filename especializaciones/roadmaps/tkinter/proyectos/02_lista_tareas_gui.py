import json
import tkinter as tk
from pathlib import Path
from tkinter import messagebox
from tkinter import ttk


RUTA_DATOS = Path(__file__).with_name("tareas_gui.json")


def cargar_tareas():
    if not RUTA_DATOS.exists():
        return []
    with open(RUTA_DATOS, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_tareas(tareas):
    with open(RUTA_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, indent=2)


class TareasApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de tareas")
        self.geometry("520x360")
        self.tareas = cargar_tareas()
        self.titulo = tk.StringVar()
        self.crear_widgets()
        self.refrescar()

    def crear_widgets(self):
        contenedor = ttk.Frame(self, padding=12)
        contenedor.pack(fill="both", expand=True)

        formulario = ttk.Frame(contenedor)
        formulario.pack(fill="x")

        ttk.Entry(formulario, textvariable=self.titulo).pack(
            side="left", fill="x", expand=True
        )
        ttk.Button(formulario, text="Agregar", command=self.agregar).pack(
            side="left", padx=(8, 0)
        )

        self.lista = tk.Listbox(contenedor, height=10)
        self.lista.pack(fill="both", expand=True, pady=10)

        acciones = ttk.Frame(contenedor)
        acciones.pack(fill="x")

        ttk.Button(acciones, text="Completar", command=self.completar).pack(
            side="left"
        )
        ttk.Button(acciones, text="Eliminar", command=self.eliminar).pack(
            side="left", padx=8
        )

        self.bind("<Return>", lambda evento: self.agregar())
        self.bind("<Delete>", lambda evento: self.eliminar())

    def refrescar(self):
        self.lista.delete(0, "end")
        for tarea in self.tareas:
            estado = "[x]" if tarea["completada"] else "[ ]"
            self.lista.insert("end", f"{estado} {tarea['titulo']}")

    def indice_seleccionado(self):
        seleccion = self.lista.curselection()
        if not seleccion:
            messagebox.showwarning("Seleccion requerida", "Selecciona una tarea.")
            return None
        return seleccion[0]

    def agregar(self):
        titulo = self.titulo.get().strip()
        if not titulo:
            messagebox.showwarning("Titulo requerido", "Escribe una tarea.")
            return
        self.tareas.append({"titulo": titulo, "completada": False})
        self.titulo.set("")
        guardar_tareas(self.tareas)
        self.refrescar()

    def completar(self):
        indice = self.indice_seleccionado()
        if indice is None:
            return
        self.tareas[indice]["completada"] = not self.tareas[indice]["completada"]
        guardar_tareas(self.tareas)
        self.refrescar()

    def eliminar(self):
        indice = self.indice_seleccionado()
        if indice is None:
            return
        if not messagebox.askyesno("Confirmar", "Eliminar esta tarea?"):
            return
        self.tareas.pop(indice)
        guardar_tareas(self.tareas)
        self.refrescar()


if __name__ == "__main__":
    TareasApp().mainloop()

