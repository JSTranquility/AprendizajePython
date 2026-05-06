# 12 - Empaquetado y siguiente nivel

## Ejecutar una app

```powershell
python proyectos/01_calculadora_gui.py
```

## Crear ejecutable

Puedes usar PyInstaller.

```powershell
python -m pip install pyinstaller
pyinstaller --onefile --windowed proyectos/01_calculadora_gui.py
```

El ejecutable queda normalmente en `dist/`.

## Cosas a cuidar

- Rutas de archivos.
- Iconos e imagenes.
- Archivos JSON o SQLite junto al ejecutable.
- Errores silenciosos en modo `--windowed`.

## Siguiente nivel

Despues de Tkinter puedes aprender:

- `customtkinter` para una apariencia mas moderna.
- PySide6 o PyQt para aplicaciones mas complejas.
- Kivy para interfaces tactiles.
- Flask/FastAPI si prefieres interfaces web.

## Proyecto final recomendado

Crea una aplicacion de escritorio con:

- Menu superior.
- Dos o mas pantallas.
- Formulario con validacion.
- Tabla `Treeview`.
- Guardado en JSON o SQLite.
- Dialogos de error y confirmacion.
- Pruebas para la logica principal.

