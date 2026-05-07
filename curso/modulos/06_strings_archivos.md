# 06 - Strings y archivos

## Strings

```python
texto = "python es practico"

print(texto.upper())
print(texto.lower())
print(texto.title())
print(texto.replace("practico", "poderoso"))
print(texto.split())
```

## Slicing

```python
palabra = "Python"
print(palabra[0])
print(palabra[-1])
print(palabra[0:3])
```

## Leer archivos

```python
with open("datos.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
```

## Escribir archivos

```python
with open("salida.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola\n")
```

## Agregar al final

```python
with open("salida.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Otra linea\n")
```

## Regla importante

Usa `with open(...)` porque cierra el archivo automaticamente aunque ocurra un error.

