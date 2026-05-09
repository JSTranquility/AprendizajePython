# 04 - Layout: pack, grid y place

Tkinter tiene tres sistemas principales para colocar widgets.

## pack

`pack` acomoda widgets en bloques.

```python
tk.Label(root, text="Arriba").pack(side="top", fill="x")
tk.Button(root, text="Salir").pack(side="bottom")
```

Opciones utiles:

- `side`
- `fill`
- `expand`
- `padx`
- `pady`

## grid

`grid` usa filas y columnas. Es el mas util para formularios.

```python
tk.Label(root, text="Nombre").grid(row=0, column=0, padx=8, pady=8)
tk.Entry(root).grid(row=0, column=1, padx=8, pady=8)
```

Configurar expansion:

```python
root.columnconfigure(1, weight=1)
```

## place

`place` usa coordenadas exactas.

```python
tk.Button(root, text="OK").place(x=50, y=80)
```

Usalo poco. Es menos flexible al cambiar el tamano de la ventana.

## Regla central

No uses `pack` y `grid` en el mismo contenedor padre.

Correcto:

```python
frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Nombre").grid(row=0, column=0)
tk.Entry(frame).grid(row=0, column=1)
```

