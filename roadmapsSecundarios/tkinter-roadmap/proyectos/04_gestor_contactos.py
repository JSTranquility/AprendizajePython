import json
import tkinter as tk
from pathlib import Path
from tkinter import messagebox
from tkinter import ttk


RUTA_DATOS = Path(__file__).with_name("contactos.json")


def cargar_contactos():
    if not RUTA_DATOS.exists():
        return []
    with open(RUTA_DATOS, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_contactos(contactos):
    with open(RUTA_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(contactos, archivo, indent=2)


def crear_contacto(nombre, telefono, email):
    if not nombre.strip():
        raise ValueError("El nombre es obligatorio")
    if not telefono.strip():
        raise ValueError("El telefono es obligatorio")
    return {
        "nombre": nombre.strip(),
        "telefono": telefono.strip(),
        "email": email.strip(),
    }


class ContactosApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de contactos")
        self.geometry("760x420")
        self.contactos = cargar_contactos()
        self.nombre = tk.StringVar()
        self.telefono = tk.StringVar()
        self.email = tk.StringVar()
        self.crear_widgets()
        self.refrescar_tabla()

    def crear_widgets(self):
        contenedor = ttk.Frame(self, padding=12)
        contenedor.pack(fill="both", expand=True)

        formulario = ttk.LabelFrame(contenedor, text="Contacto", padding=12)
        formulario.pack(fill="x")

        ttk.Label(formulario, text="Nombre").grid(row=0, column=0, sticky="w")
        ttk.Entry(formulario, textvariable=self.nombre).grid(
            row=1, column=0, sticky="ew", padx=(0, 8)
        )

        ttk.Label(formulario, text="Telefono").grid(row=0, column=1, sticky="w")
        ttk.Entry(formulario, textvariable=self.telefono).grid(
            row=1, column=1, sticky="ew", padx=(0, 8)
        )

        ttk.Label(formulario, text="Email").grid(row=0, column=2, sticky="w")
        ttk.Entry(formulario, textvariable=self.email).grid(
            row=1, column=2, sticky="ew", padx=(0, 8)
        )

        ttk.Button(formulario, text="Agregar", command=self.agregar).grid(
            row=1, column=3, sticky="ew"
        )

        for columna in range(3):
            formulario.columnconfigure(columna, weight=1)

        self.tabla = ttk.Treeview(
            contenedor,
            columns=("nombre", "telefono", "email"),
            show="headings",
            selectmode="browse",
        )
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("telefono", text="Telefono")
        self.tabla.heading("email", text="Email")
        self.tabla.pack(fill="both", expand=True, pady=12)

        acciones = ttk.Frame(contenedor)
        acciones.pack(fill="x")
        ttk.Button(acciones, text="Eliminar", command=self.eliminar).pack(side="left")
        ttk.Button(acciones, text="Limpiar campos", command=self.limpiar).pack(
            side="left", padx=8
        )

    def refrescar_tabla(self):
        self.tabla.delete(*self.tabla.get_children())
        for indice, contacto in enumerate(self.contactos):
            self.tabla.insert(
                "",
                "end",
                iid=str(indice),
                values=(contacto["nombre"], contacto["telefono"], contacto["email"]),
            )

    def limpiar(self):
        self.nombre.set("")
        self.telefono.set("")
        self.email.set("")

    def agregar(self):
        try:
            contacto = crear_contacto(
                self.nombre.get(),
                self.telefono.get(),
                self.email.get(),
            )
        except ValueError as error:
            messagebox.showerror("Error", str(error))
            return

        self.contactos.append(contacto)
        guardar_contactos(self.contactos)
        self.limpiar()
        self.refrescar_tabla()

    def eliminar(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Seleccion requerida", "Selecciona un contacto.")
            return

        if not messagebox.askyesno("Confirmar", "Eliminar contacto?"):
            return

        indice = int(seleccion[0])
        self.contactos.pop(indice)
        guardar_contactos(self.contactos)
        self.refrescar_tabla()


if __name__ == "__main__":
    ContactosApp().mainloop()

