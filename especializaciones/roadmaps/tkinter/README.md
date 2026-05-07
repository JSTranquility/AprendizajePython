# Roadmap Completo de Tkinter

Tkinter es la biblioteca incluida con Python para crear interfaces graficas de escritorio. Este roadmap te lleva desde una ventana vacia hasta aplicaciones organizadas con multiples pantallas, formularios, tablas, menus, archivos, estilos y proyectos reales.

## Requisitos

Antes de empezar debes saber:

- Variables, condicionales, bucles y funciones.
- Listas y diccionarios.
- Manejo basico de archivos.
- Clases basicas en Python.

Para verificar Tkinter:

```powershell
python -m tkinter
```

Si abre una ventana de prueba, Tkinter funciona.

## Orden recomendado

1. `modulos/01_que_es_tkinter.md`
2. `modulos/02_ventanas_y_mainloop.md`
3. `modulos/03_widgets_basicos.md`
4. `modulos/04_layout_pack_grid_place.md`
5. `modulos/05_eventos_comandos.md`
6. `modulos/06_variables_tkinter.md`
7. `modulos/07_frames_multiples_pantallas.md`
8. `modulos/08_dialogos_menus_archivos.md`
9. `modulos/09_canvas.md`
10. `modulos/10_ttk_treeview_estilos.md`
11. `modulos/11_arquitectura_apps.md`
12. `modulos/12_empaquetado_y_siguiente_nivel.md`

## Como estudiar

1. Lee un modulo.
2. Ejecuta el ejemplo del modulo.
3. Modifica colores, textos, tamanos y comportamiento.
4. Resuelve el ejercicio correspondiente.
5. Construye un proyecto.

## Proyectos incluidos

- `proyectos/01_calculadora_gui.py`
- `proyectos/02_lista_tareas_gui.py`
- `proyectos/03_bloc_notas.py`
- `proyectos/04_gestor_contactos.py`

## Conceptos que debes dominar

- `Tk`, `Toplevel` y `mainloop`.
- Widgets: `Label`, `Button`, `Entry`, `Text`, `Listbox`, `Checkbutton`, `Radiobutton`, `Scale`.
- Layouts: `pack`, `grid`, `place`.
- Eventos con `command` y `bind`.
- Variables: `StringVar`, `IntVar`, `BooleanVar`, `DoubleVar`.
- Contenedores con `Frame` y `LabelFrame`.
- Dialogos: mensajes, confirmar, abrir/guardar archivos.
- Menus superiores y contextuales.
- Dibujo con `Canvas`.
- Widgets modernos con `ttk`.
- Tablas con `Treeview`.
- Separar interfaz, estado y logica.

## Regla importante

No mezcles `pack` y `grid` dentro del mismo contenedor. Puedes usar `pack` en una ventana y `grid` dentro de un `Frame`, pero no ambos directamente en el mismo padre.

