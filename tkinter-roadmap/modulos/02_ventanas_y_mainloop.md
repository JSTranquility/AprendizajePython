# 02 - Ventanas y mainloop

La ventana principal se crea con `tk.Tk()`.

```python
import tkinter as tk

root = tk.Tk()
root.title("Aplicacion")
root.geometry("400x300")
root.mainloop()
```

## mainloop

`mainloop()` mantiene la aplicacion abierta y escucha eventos como clicks, teclas y cambios de ventana.

Sin `mainloop`, la ventana aparece y se cierra inmediatamente.

## Propiedades comunes

```python
root.title("Titulo")
root.geometry("500x400")
root.minsize(300, 200)
root.maxsize(900, 700)
root.resizable(True, False)
root.configure(bg="white")
```

## Toplevel

`Toplevel` crea una ventana secundaria.

```python
def abrir_secundaria():
    ventana = tk.Toplevel(root)
    ventana.title("Secundaria")
    tk.Label(ventana, text="Otra ventana").pack(padx=20, pady=20)
```

## Cierre controlado

```python
def al_cerrar():
    print("Cerrando...")
    root.destroy()

root.protocol("WM_DELETE_WINDOW", al_cerrar)
```

