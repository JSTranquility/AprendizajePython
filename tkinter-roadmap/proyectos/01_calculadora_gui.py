import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def calcular(a, b, operacion):
    if operacion == "+":
        return a + b
    if operacion == "-":
        return a - b
    if operacion == "*":
        return a * b
    if operacion == "/":
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b
    raise ValueError("Operacion invalida")


class CalculadoraApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Tkinter")
        self.geometry("360x260")
        self.resizable(False, False)

        self.numero_a = tk.StringVar()
        self.numero_b = tk.StringVar()
        self.operacion = tk.StringVar(value="+")
        self.resultado = tk.StringVar(value="Resultado: -")

        self.crear_widgets()

    def crear_widgets(self):
        contenedor = ttk.Frame(self, padding=16)
        contenedor.pack(fill="both", expand=True)

        ttk.Label(contenedor, text="Numero A").grid(row=0, column=0, sticky="w")
        ttk.Entry(contenedor, textvariable=self.numero_a).grid(
            row=1, column=0, sticky="ew", pady=(0, 10)
        )

        ttk.Label(contenedor, text="Numero B").grid(row=2, column=0, sticky="w")
        ttk.Entry(contenedor, textvariable=self.numero_b).grid(
            row=3, column=0, sticky="ew", pady=(0, 10)
        )

        operaciones = ttk.Frame(contenedor)
        operaciones.grid(row=4, column=0, sticky="ew", pady=(0, 10))

        for indice, simbolo in enumerate(["+", "-", "*", "/"]):
            ttk.Radiobutton(
                operaciones,
                text=simbolo,
                value=simbolo,
                variable=self.operacion,
            ).grid(row=0, column=indice, padx=4)

        ttk.Button(contenedor, text="Calcular", command=self.al_calcular).grid(
            row=5, column=0, sticky="ew"
        )
        ttk.Label(contenedor, textvariable=self.resultado, font=("Segoe UI", 12)).grid(
            row=6, column=0, pady=14
        )

        contenedor.columnconfigure(0, weight=1)
        self.bind("<Return>", lambda evento: self.al_calcular())

    def al_calcular(self):
        try:
            a = float(self.numero_a.get())
            b = float(self.numero_b.get())
            valor = calcular(a, b, self.operacion.get())
        except ValueError as error:
            messagebox.showerror("Error", str(error))
            return

        self.resultado.set(f"Resultado: {valor:g}")


if __name__ == "__main__":
    CalculadoraApp().mainloop()

