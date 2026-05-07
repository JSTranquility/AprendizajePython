# 🏗️ Módulo 05: Estructura Profesional y Conexión Final

¡Felicidades! Ya conoces las piezas del rompecabezas. Ahora vamos a ver cómo se organizan de forma profesional para que tu código no sea un caos cuando el proyecto crezca.

---

## 1. El Patrón de Carpetas (Resumen)
Un proyecto de Flask serio siempre se ve así:

*   📂 **`proyecto/`**
    *   📄 `app.py` (Solo arranca la aplicación)
    *   📄 `db.py` (Lógica de SQL)
    *   📄 `routes.py` (Opcional: puedes separar las rutas aquí)
    *   📂 **`static/`**
        *   📂 `css/`, `js/`, `img/`
    *   📂 **`templates/`**
        *   📄 `base.html` (La estructura)
        *   📄 `index.html`, `detalles.html`, etc.

---

## 2. Conectando SQLite con Flask (Repaso)
Para que todo funcione, tu función en Flask debe llamar a tu función en SQLite y pasar el resultado al template.

```python
# app.py
from db import consultar_libros

@app.route('/')
def lista():
    datos = consultar_libros() # Traemos de SQLite
    return render_template('index.html', libros=datos) # Enviamos al HTML
```

---

## 3. Manejo de Errores
Es vital manejar los errores para que el servidor no se caiga si algo sale mal.

```python
@app.errorhandler(404)
def pagina_no_encontrada(e):
    return render_template('404.html'), 404
```

---

## 🚀 Tu Proyecto Final de este Roadmap
Tu misión ahora es completar la aplicación de la **Librería** usando todo lo aprendido:
1.  Usa un `base.html` para el diseño.
2.  Crea una página para **ver** todos los libros.
3.  Crea un formulario para **agregar** libros nuevos.
4.  Añade un botón para **eliminar** libros.
5.  Usa `flash` para confirmar cada acción.

---

## 📚 Recursos adicionales
*   **Documentación oficial:** [flask.palletsprojects.com](https://flask.palletsprojects.com/)
*   **Flask-SQLAlchemy:** Para manejar la base de datos de forma más elegante en el futuro.
