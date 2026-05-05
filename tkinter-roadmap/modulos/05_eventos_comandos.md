# 05 - Eventos y comandos

Tkinter responde a acciones del usuario.

## command

Muchos widgets reciben una funcion con `command`.

```python
def guardar():
    print("Guardando")

tk.Button(root, text="Guardar", command=guardar).pack()
```

Importante: pasa la funcion sin parentesis.

```python
command=guardar
```

No:

```python
command=guardar()
```

## bind

`bind` conecta eventos mas especificos.

```python
def al_presionar_enter(evento):
    print("Enter")

root.bind("<Return>", al_presionar_enter)
```

## Eventos comunes

- `<Button-1>` click izquierdo.
- `<Double-Button-1>` doble click.
- `<Return>` tecla Enter.
- `<Escape>` tecla Escape.
- `<Key>` cualquier tecla.
- `<Configure>` cambio de tamano.

## lambda

Sirve para pasar argumentos simples.

```python
tk.Button(root, text="A", command=lambda: elegir("A")).pack()
```

No abuses de `lambda`; si la logica crece, crea una funcion normal.

