# 03 - Control de flujo

El control de flujo decide que partes del codigo se ejecutan.

## Condicionales

```python
edad = 18

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")
```

## elif

```python
nota = 85

if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
else:
    print("Reprobado")
```

## Operadores de comparacion

- `==` igual
- `!=` diferente
- `>` mayor
- `<` menor
- `>=` mayor o igual
- `<=` menor o igual

## Operadores logicos

```python
usuario = "admin"
clave = "1234"

if usuario == "admin" and clave == "1234":
    print("Acceso permitido")
```

## Bucles

### for

```python
for numero in range(1, 6):
    print(numero)
```

### while

```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1
```

## break y continue

```python
for numero in range(10):
    if numero == 5:
        break
    print(numero)
```

```python
for numero in range(5):
    if numero == 2:
        continue
    print(numero)
```

