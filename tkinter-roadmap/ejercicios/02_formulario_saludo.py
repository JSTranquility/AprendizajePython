import tkinter as tk
from tkinter import messagebox


def main():
    root = tk.Tk()
    root.title("Formulario")
    root.geometry("360x180")

    nombre = tk.StringVar()

    def saludar():
        valor = nombre.get().strip()
        if not valor:
            messagebox.showwarning("Falta nombre", "Escribe tu nombre.")
            return
        messagebox.showinfo("Saludo", f"Hola, {valor}")

    contenedor = tk.Frame(root, padx=16, pady=16)
    contenedor.pack(fill="both", expand=True)

    tk.Label(contenedor, text="Nombre").grid(row=0, column=0, sticky="w")
    tk.Entry(contenedor, textvariable=nombre).grid(row=1, column=0, sticky="ew", pady=8)
    tk.Button(contenedor, text="Saludar", command=saludar).grid(row=2, column=0)

    contenedor.columnconfigure(0, weight=1)
    root.bind("<Return>", lambda evento: saludar())
    root.mainloop()


if __name__ == "__main__":
    main()

