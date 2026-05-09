"""
Ejercicios de fundamentos.

Ejecuta:
    python ejercicios/01_fundamentos.py

Completa las funciones donde veas TODO. Luego ejecuta el archivo.
"""


def convertir_a_entero(texto):
    # TODO: convierte texto a entero y retorna el resultado.
    return int(texto)


def calcular_total(precio, cantidad):
    # TODO: retorna precio * cantidad.
    return precio * cantidad


def es_mayor_de_edad(edad):
    # TODO: retorna True si edad es 18 o mas.
    return edad >= 18


def clasificar_nota(nota):
    # TODO:
    # 90 o mas -> "A"
    # 80 o mas -> "B"
    # 70 o mas -> "C"
    # menos de 70 -> "F"
    if nota >= 90:
        return "A"
    if nota >= 80:
        return "B"
    if nota >= 70:
        return "C"
    return "F"


def sumar_hasta(limite):
    # TODO: suma los numeros desde 1 hasta limite inclusive.
    total = 0
    for numero in range(1, limite + 1):
        total += numero
    return total


def ejecutar_pruebas():
    assert convertir_a_entero("10") == 10
    assert calcular_total(5, 3) == 15
    assert es_mayor_de_edad(18) is True
    assert es_mayor_de_edad(17) is False
    assert clasificar_nota(95) == "A"
    assert clasificar_nota(82) == "B"
    assert clasificar_nota(75) == "C"
    assert clasificar_nota(60) == "F"
    assert sumar_hasta(5) == 15
    print("Todos los ejercicios de fundamentos pasaron.")


if __name__ == "__main__":
    ejecutar_pruebas()

