# Desafio GUI 1: Calculadora de Edad con Tkinter

# Consigna:
# Crea una ventana que permita calcular la edad aproximada de una persona.

# Requisitos:
# 1. Debe tener un campo para escribir el ano de nacimiento.
# 2. Debe tener un boton que haga el calculo.
# 3. Debe mostrar el resultado en una etiqueta.
# 4. Debe validar que el usuario escriba un numero correcto.

# --- ESCRIBE TU CODIGO ABAJO ---

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calcular_edad():
    try:
        ano_nacimiento = int(entry_ano.get())
        ano_actual = datetime.now().year
        edad = ano_actual - ano_nacimiento
        if edad < 0:
            messagebox.showerror("Error", "El año de nacimiento no puede ser mayor que el año actual.")
        else:
            label_resultado.config(text=f"Tu edad aproximada es: {edad} años")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido para el año de nacimiento.")


ventana = tk.Tk()
ventana.title("Calculadora de Edad")
ventana.geometry("300x150")


label_ano = tk.Label(ventana, text="Año de nacimiento:")
label_ano.pack(pady=5)
entry_ano = tk.Entry(ventana)
entry_ano.pack(pady=5)
boton_calcular = tk.Button(ventana, text="Calcular Edad", command=calcular_edad)
boton_calcular.pack(pady=5)
label_resultado = tk.Label(ventana, text="")
label_resultado.pack(pady=5)

ventana.mainloop()

