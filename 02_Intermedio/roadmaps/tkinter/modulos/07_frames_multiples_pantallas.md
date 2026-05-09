# 07 - Frames y multiples pantallas

`Frame` permite agrupar widgets.

```python
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)
```

## Por que usar Frames

- Separan secciones.
- Permiten combinar layouts.
- Hacen el codigo mas ordenado.
- Facilitan cambiar pantallas.

## App con pantallas

```python
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pantallas")
        self.geometry("400x300")
        self.pantalla_actual = None
        self.mostrar_inicio()

    def limpiar(self):
        if self.pantalla_actual is not None:
            self.pantalla_actual.destroy()

    def mostrar_inicio(self):
        self.limpiar()
        frame = tk.Frame(self)
        frame.pack(fill="both", expand=True)
        tk.Label(frame, text="Inicio").pack()
        self.pantalla_actual = frame
```

## Patron recomendado

Para apps medianas:

- Una clase principal `App`.
- Un `Frame` por pantalla.
- Metodos para cambiar pantallas.
- Logica de datos separada de la UI.

