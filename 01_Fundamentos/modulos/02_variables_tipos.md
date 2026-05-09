# 02 - Variables y tipos de datos

Una variable guarda un valor.

```python
nombre = "Ana"
edad = 25
altura = 1.70
activo = True
```

## Tipos principales

- `str`: texto.
- `int`: numero entero.
- `float`: numero decimal.
- `bool`: verdadero o falso.
- `None`: ausencia de valor.

```python
producto = "Teclado"
precio = 45.99
cantidad = 2
disponible = True
descuento = None
```

## Operaciones numericas

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

## Convertir tipos

`input()` siempre devuelve texto.

```python
edad = int(input("Edad: "))
precio = float(input("Precio: "))
```

## f-strings

La forma recomendada de insertar valores en texto:

```python
nombre = "Luis"
edad = 30
print(f"{nombre} tiene {edad} anos")
```

## Regla practica

Si un valor representa texto, usa `str`. Si vas a hacer cuentas, conviertelo a `int` o `float`.

