# 06 - Variables de Tkinter

Tkinter tiene variables especiales que sincronizan datos con widgets.

## StringVar

```python
nombre = tk.StringVar()
entrada = tk.Entry(root, textvariable=nombre)
entrada.pack()

print(nombre.get())
nombre.set("Ana")
```

## IntVar, DoubleVar y BooleanVar

```python
edad = tk.IntVar(value=18)
precio = tk.DoubleVar(value=10.5)
activo = tk.BooleanVar(value=True)
```

## trace_add

Permite reaccionar cuando cambia una variable.

```python
def cambio(*args):
    print("Cambio:", nombre.get())

nombre.trace_add("write", cambio)
```

## Cuando usarlas

Usa variables de Tkinter cuando:

- Un widget debe reflejar un estado.
- Quieres leer o cambiar el valor desde varias funciones.
- Necesitas observar cambios.

Para logica interna compleja, puedes usar variables normales de Python.

