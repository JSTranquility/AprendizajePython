# 05 - Colecciones

Las colecciones guardan varios valores.

## Listas

```python
frutas = ["manzana", "pera", "uva"]
frutas.append("mango")
print(frutas[0])
```

Metodos utiles:

- `append`
- `remove`
- `pop`
- `sort`
- `reverse`

## Tuplas

Son parecidas a listas, pero no se modifican.

```python
punto = (10, 20)
```

## Diccionarios

Guardan pares clave-valor.

```python
persona = {
    "nombre": "Ana",
    "edad": 25,
}

print(persona["nombre"])
persona["ciudad"] = "Santo Domingo"
```

## Sets

Guardan valores unicos.

```python
numeros = {1, 2, 2, 3}
print(numeros)
```

## Comprensiones

```python
cuadrados = [n * n for n in range(1, 6)]
pares = [n for n in range(10) if n % 2 == 0]
```

## Elegir estructura

- Usa lista cuando importa el orden y puede haber repetidos.
- Usa diccionario cuando necesitas buscar por clave.
- Usa set cuando necesitas valores unicos.
- Usa tupla cuando el dato no debe cambiar.

