import tkinter as tk
from pathlib import Path
from tkinter import filedialog
from tkinter import messagebox


class BlocNotas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bloc de notas")
        self.geometry("800x520")
        self.ruta_actual = None
        self.crear_menu()
        self.crear_editor()

    def crear_menu(self):
        menu = tk.Menu(self)
        self.config(menu=menu)

        archivo = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="Archivo", menu=archivo)
        archivo.add_command(label="Nuevo", command=self.nuevo)
        archivo.add_command(label="Abrir", command=self.abrir)
        archivo.add_command(label="Guardar", command=self.guardar)
        archivo.add_command(label="Guardar como", command=self.guardar_como)
        archivo.add_separator()
        archivo.add_command(label="Salir", command=self.destroy)

    def crear_editor(self):
        self.editor = tk.Text(self, wrap="word", undo=True)
        self.editor.pack(fill="both", expand=True)

    def nuevo(self):
        self.editor.delete("1.0", "end")
        self.ruta_actual = None
        self.title("Bloc de notas")

    def abrir(self):
        ruta = filedialog.askopenfilename(
            filetypes=[("Texto", "*.txt"), ("Todos", "*.*")]
        )
        if not ruta:
            return

        contenido = Path(ruta).read_text(encoding="utf-8")
        self.editor.delete("1.0", "end")
        self.editor.insert("1.0", contenido)
        self.ruta_actual = Path(ruta)
        self.title(f"Bloc de notas - {self.ruta_actual.name}")

    def guardar(self):
        if self.ruta_actual is None:
            self.guardar_como()
            return

        contenido = self.editor.get("1.0", "end-1c")
        self.ruta_actual.write_text(contenido, encoding="utf-8")
        messagebox.showinfo("Guardado", "Archivo guardado.")

    def guardar_como(self):
        ruta = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Texto", "*.txt"), ("Todos", "*.*")],
        )
        if not ruta:
            return

        self.ruta_actual = Path(ruta)
        self.guardar()
        self.title(f"Bloc de notas - {self.ruta_actual.name}")


if __name__ == "__main__":
    BlocNotas().mainloop()

