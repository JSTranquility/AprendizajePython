# 10 - ttk, Treeview y estilos

`ttk` ofrece widgets con apariencia mas moderna.

```python
from tkinter import ttk

ttk.Button(root, text="Guardar").pack()
ttk.Entry(root).pack()
```

## Combobox

```python
opcion = tk.StringVar()
combo = ttk.Combobox(root, textvariable=opcion, values=["A", "B", "C"])
combo.pack()
```

## Notebook

Pestanas.

```python
notebook = ttk.Notebook(root)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text="Inicio")
notebook.add(tab2, text="Datos")
notebook.pack(fill="both", expand=True)
```

## Treeview

Tabla o arbol.

```python
tabla = ttk.Treeview(root, columns=("nombre", "edad"), show="headings")
tabla.heading("nombre", text="Nombre")
tabla.heading("edad", text="Edad")
tabla.insert("", "end", values=("Ana", 25))
tabla.pack(fill="both", expand=True)
```

## Estilos

```python
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", padding=6)
```

No intentes convertir Tkinter en una app web moderna. Busca claridad, buen espaciado y consistencia.

