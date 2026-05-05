"""
Ejercicios de colecciones.

Ejecuta:
    python ejercicios/02_colecciones.py
"""


def obtener_pares(numeros):
    return [numero for numero in numeros if numero % 2 == 0]


def contar_palabras(texto):
    conteo = {}
    for palabra in texto.lower().split():
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo


def eliminar_duplicados(valores):
    resultado = []
    vistos = set()

    for valor in valores:
        if valor not in vistos:
            resultado.append(valor)
            vistos.add(valor)

    return resultado


def agrupar_por_categoria(productos):
    grupos = {}

    for producto in productos:
        categoria = producto["categoria"]
        grupos.setdefault(categoria, []).append(producto["nombre"])

    return grupos


def producto_mas_caro(productos):
    if not productos:
        return None
    return max(productos, key=lambda producto: producto["precio"])


def ejecutar_pruebas():
    assert obtener_pares([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert contar_palabras("Hola hola python") == {"hola": 2, "python": 1}
    assert eliminar_duplicados(["a", "b", "a", "c"]) == ["a", "b", "c"]

    productos = [
        {"nombre": "teclado", "categoria": "tech", "precio": 40},
        {"nombre": "mouse", "categoria": "tech", "precio": 20},
        {"nombre": "pan", "categoria": "comida", "precio": 2},
    ]

    assert agrupar_por_categoria(productos) == {
        "tech": ["teclado", "mouse"],
        "comida": ["pan"],
    }
    assert producto_mas_caro(productos)["nombre"] == "teclado"
    assert producto_mas_caro([]) is None
    print("Todos los ejercicios de colecciones pasaron.")


if __name__ == "__main__":
    ejecutar_pruebas()

