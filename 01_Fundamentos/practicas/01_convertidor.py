# Desafío 1: El Convertidor de Unidades

# Consigna:
# Crea un programa que convierta grados Celsius a Fahrenheit.
# La fórmula es: (Celsius * 9/5) + 32

# Pasos:
# 1. Pide al usuario que ingrese la temperatura en Celsius (usa input()).
# 2. Convierte el valor a float.
# 3. Realiza el cálculo.
# 4. Muestra el resultado con un mensaje amigable.

# --- ESCRIBE TU CÓDIGO ABAJO ---

print("Hola, bienvenido a la app!")

celsius = input("Por favor ingresa la temperatura en grados Celsius")

celsius = float(celsius)

fahrenheit = (celsius * 9/5) + 32

print(f"La temperatura en grados Fahrenheit es:{fahrenheit}")


