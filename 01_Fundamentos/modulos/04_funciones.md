# 04 - Funciones

Una funcion agrupa instrucciones reutilizables.

```python
def saludar(nombre):
    return f"Hola, {nombre}"

mensaje = saludar("Ana")
print(mensaje)
```

## Por que usar funciones

- Evitan repetir codigo.
- Hacen el programa mas facil de probar.
- Separan responsabilidades.
- Ayudan a leer el programa.

## Parametros y retorno

```python
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
```

## Valores por defecto

```python
def crear_usuario(nombre, activo=True):
    return {"nombre": nombre, "activo": activo}
```

## Scope

Las variables creadas dentro de una funcion viven dentro de esa funcion.

```python
def calcular():
    total = 10
    return total
```

## Buena practica

Una funcion debe hacer una cosa concreta. Si una funcion crece demasiado, probablemente necesita dividirse.

