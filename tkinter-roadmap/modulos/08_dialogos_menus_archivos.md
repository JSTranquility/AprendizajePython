# 08 - Dialogos, menus y archivos

Tkinter incluye dialogos comunes.

## Mensajes

```python
from tkinter import messagebox

messagebox.showinfo("Titulo", "Operacion completada")
messagebox.showwarning("Aviso", "Falta un campo")
messagebox.showerror("Error", "No se pudo guardar")
```

## Confirmar

```python
if messagebox.askyesno("Confirmar", "Deseas salir?"):
    root.destroy()
```

## Abrir archivo

```python
from tkinter import filedialog

ruta = filedialog.askopenfilename(
    filetypes=[("Texto", "*.txt"), ("Todos", "*.*")]
)
```

## Guardar archivo

```python
ruta = filedialog.asksaveasfilename(
    defaultextension=".txt",
    filetypes=[("Texto", "*.txt")]
)
```

## Menu superior

```python
menu = tk.Menu(root)
root.config(menu=menu)

archivo = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Archivo", menu=archivo)
archivo.add_command(label="Abrir", command=abrir)
archivo.add_separator()
archivo.add_command(label="Salir", command=root.destroy)
```

