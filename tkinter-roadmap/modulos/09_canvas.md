# 09 - Canvas

`Canvas` sirve para dibujar formas, texto e imagenes.

```python
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

canvas.create_line(10, 10, 200, 10)
canvas.create_rectangle(50, 50, 150, 120, fill="skyblue")
canvas.create_oval(180, 50, 260, 130, fill="tomato")
canvas.create_text(200, 200, text="Hola Canvas")
```

## Coordenadas

El punto `(0, 0)` esta arriba a la izquierda.

- `x` crece hacia la derecha.
- `y` crece hacia abajo.

## Mover objetos

```python
rect = canvas.create_rectangle(10, 10, 60, 60, fill="blue")
canvas.move(rect, 20, 0)
```

## Eventos en Canvas

```python
def click(evento):
    canvas.create_oval(evento.x - 5, evento.y - 5, evento.x + 5, evento.y + 5)

canvas.bind("<Button-1>", click)
```

## Usos

- Dibujos simples.
- Juegos pequenos.
- Diagramas.
- Visualizaciones.
- Herramientas interactivas.

