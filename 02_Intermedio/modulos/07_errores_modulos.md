# 07 - Errores, excepciones y modulos

## Excepciones

Una excepcion ocurre cuando algo falla durante la ejecucion.

```python
try:
    numero = int(input("Numero: "))
    print(10 / numero)
except ValueError:
    print("Debes escribir un numero valido")
except ZeroDivisionError:
    print("No se puede dividir entre cero")
```

## else y finally

```python
try:
    archivo = open("datos.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("Archivo no existe")
else:
    print(archivo.read())
    archivo.close()
finally:
    print("Proceso terminado")
```

## Levantar errores

```python
def dividir(a, b):
    if b == 0:
        raise ValueError("b no puede ser cero")
    return a / b
```

## Modulos

Un modulo es un archivo `.py` que puedes importar.

```python
import math

print(math.sqrt(16))
```

```python
from datetime import date

print(date.today())
```

## Crear tu propio modulo

Archivo `utilidades.py`:

```python
def doblar(numero):
    return numero * 2
```

Archivo `programa.py`:

```python
from utilidades import doblar

print(doblar(5))
```

