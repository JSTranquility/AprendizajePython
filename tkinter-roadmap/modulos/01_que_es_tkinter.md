# 01 - Que es Tkinter

Tkinter es el wrapper oficial de Python para Tk, una biblioteca de interfaces graficas. Viene incluida con Python en la mayoria de instalaciones.

## Para que sirve

Tkinter sirve para crear:

- Formularios.
- Calculadoras.
- Gestores de tareas.
- Herramientas internas.
- Editores simples.
- Visualizadores de datos.
- Prototipos de aplicaciones de escritorio.

## Ventajas

- Viene incluido con Python.
- No requiere navegador.
- Es suficiente para muchas herramientas de escritorio.
- Tiene widgets clasicos y widgets `ttk` con mejor apariencia.

## Limitaciones

- No es ideal para interfaces muy modernas o animaciones complejas.
- El diseno visual requiere paciencia.
- Para apps grandes necesitas organizar bien el codigo.

## Primer ejemplo

```python
import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera app")
ventana.geometry("300x150")

etiqueta = tk.Label(ventana, text="Hola, Tkinter")
etiqueta.pack(pady=20)

ventana.mainloop()
```

## Vocabulario

- Ventana: contenedor principal.
- Widget: elemento visual.
- Layout: forma de colocar widgets.
- Evento: accion del usuario.
- Callback: funcion que se ejecuta ante un evento.

