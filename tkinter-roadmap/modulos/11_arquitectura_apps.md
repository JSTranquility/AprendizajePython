# 11 - Arquitectura de aplicaciones Tkinter

Una app grafica se vuelve dificil si toda la logica vive dentro de botones.

## Separacion recomendada

- UI: ventanas, widgets, eventos.
- Estado: datos actuales de la app.
- Persistencia: archivos o base de datos.
- Logica: funciones puras cuando sea posible.

## Estructura sugerida

```text
mi_app/
  app.py
  ui.py
  servicios.py
  almacenamiento.py
```

## Evita esto

```python
def boton_guardar():
    # validar UI
    # calcular
    # escribir archivo
    # actualizar tabla
    # mostrar mensaje
```

## Mejor

```python
def crear_contacto(nombre, telefono):
    if not nombre:
        raise ValueError("Nombre requerido")
    return {"nombre": nombre, "telefono": telefono}
```

La UI llama a esa funcion y decide como mostrar errores.

## Apps con clases

```python
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("App")
        self.crear_widgets()

    def crear_widgets(self):
        pass
```

## Regla profesional

Mantén las funciones de UI pequenas. Si una funcion de un boton pasa de 20-30 lineas, probablemente esta haciendo demasiado.

