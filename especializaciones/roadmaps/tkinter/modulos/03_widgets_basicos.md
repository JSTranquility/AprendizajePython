# 03 - Widgets basicos

Un widget es un componente de la interfaz.

## Label

```python
label = tk.Label(root, text="Nombre")
label.pack()
```

## Button

```python
def saludar():
    print("Hola")

boton = tk.Button(root, text="Saludar", command=saludar)
boton.pack()
```

## Entry

```python
entrada = tk.Entry(root)
entrada.pack()

texto = entrada.get()
```

## Text

`Text` sirve para texto largo.

```python
editor = tk.Text(root, width=40, height=10)
editor.pack()

contenido = editor.get("1.0", "end")
```

## Listbox

```python
lista = tk.Listbox(root)
lista.insert("end", "Python")
lista.insert("end", "Tkinter")
lista.pack()
```

## Checkbutton

```python
activo = tk.BooleanVar()
check = tk.Checkbutton(root, text="Activo", variable=activo)
check.pack()
```

## Radiobutton

```python
opcion = tk.StringVar(value="a")
tk.Radiobutton(root, text="A", value="a", variable=opcion).pack()
tk.Radiobutton(root, text="B", value="b", variable=opcion).pack()
```

