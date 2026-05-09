"""
Calculadora de consola.

Ejecuta:
    python proyectos/01_calculadora_cli.py
"""


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Escribe un numero valido.")


def mostrar_menu():
    print("\nCalculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


def main():
    operaciones = {
        "1": sumar,
        "2": restar,
        "3": multiplicar,
        "4": dividir,
    }

    while True:
        mostrar_menu()
        opcion = input("Opcion: ").strip()

        if opcion == "5":
            print("Hasta luego.")
            break

        operacion = operaciones.get(opcion)
        if operacion is None:
            print("Opcion invalida.")
            continue

        a = pedir_numero("Primer numero: ")
        b = pedir_numero("Segundo numero: ")

        try:
            resultado = operacion(a, b)
        except ValueError as error:
            print(error)
        else:
            print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()

