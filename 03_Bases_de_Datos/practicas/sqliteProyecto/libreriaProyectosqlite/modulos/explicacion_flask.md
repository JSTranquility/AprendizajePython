# Aprendiendo Flask: El Puente entre Python y tu Navegador

Flask es un "micro-framework" que actúa como el pegamento entre tu código de Python (lógica, bases de datos) y lo que el usuario ve en su navegador (HTML, CSS).

Aquí tienes el desglose de cómo funciona todo en tu proyecto actual.

---

## 1. El Concepto de "Ruta" (@app.route)

Imagina que tu aplicación es una casa con muchas puertas. Cada puerta tiene una dirección (URL).

En tu archivo `app.py`:
```python
@app.route('/libros')
def index():
    # ... lógica ...
    return render_template('index.html', libros=libros)
```
- `@app.route('/libros')`: Le dice a Flask: "Si alguien visita `tu-web.com/libros`, ejecuta esta función".
- `def index()`: Es la función que decide qué hacer cuando alguien entra por esa "puerta".

---

## 2. Renderizar Plantillas (HTML)

Flask no solo envía texto plano; envía archivos HTML completos usando `render_template`.

```python
return render_template('index.html', libros=libros)
```
- `'index.html'`: Es el archivo que está dentro de tu carpeta `/templates`.
- `libros=libros`: Aquí es donde ocurre la magia. Estás pasando una variable de Python (`libros`) al archivo HTML para que pueda ser usada allí.

---

## 3. Jinja2: Python dentro de HTML

HTML por sí solo es estático (no cambia). Pero Flask usa un motor llamado **Jinja2** que te permite escribir "lógica" dentro del HTML usando llaves `{}`.

### Mostrar variables: `{{ ... }}`
Si quieres mostrar el nombre de un libro en tu HTML:
```html
<h1>{{ libro[1] }}</h1> 
```
*(Esto imprimirá el contenido de la posición 1 de tu tupla de libro).*

### Bucles (Ciclos): `{% for ... %}`
Si tienes una lista de libros y quieres crear una fila por cada uno:
```html
<ul>
  {% for libro in libros %}
    <li>{{ libro[1] }} - Autor: {{ libro[2] }}</li>
  {% endfor %}
</ul>
```
Esto repetirá el código HTML tantas veces como libros haya en tu base de datos.

---

## 4. El Flujo de Datos (Paso a Paso)

Así es como se conecta todo en tu proyecto de Librería:

1.  **El Usuario** hace clic en un enlace o escribe una URL (ej: `/libros`).
2.  **Flask** recibe la petición y busca la ruta `@app.route('/libros')`.
3.  **Python** ejecuta la función:
    - Llama a `consultar_libros()` (en tu archivo `db.py`).
    - Recibe los datos de SQLite.
4.  **Flask** toma esos datos y los "inyecta" en el HTML usando `render_template`.
5.  **El Navegador** recibe el HTML ya procesado y muestra la lista de libros al usuario.

---

## 5. Estructura de Carpetas Obligatoria

Para que Flask funcione, siempre debes tener esta estructura (que ya tienes bien armada):

- `app.py` (Tu servidor principal).
- `db.py` (Tu lógica de base de datos).
- `templates/` (Carpeta **obligatoria** donde van tus archivos `.html`).
- `static/` (Carpeta donde irían tus imágenes, CSS y archivos JavaScript).

---

## Tips para aprender:
- **`debug=True`**: En tu `app.py` tienes `app.run(debug=True)`. Esto es vital porque si cometes un error en Python, Flask te mostrará el error exacto en el navegador para que sepas qué arreglar.
- **Variables dinámicas**: Cuando ves `<int:categoria_id>` en una ruta, significa que esa parte de la URL puede cambiar (ej: `/categoria/1`, `/categoria/2`) y Python recibirá ese número automáticamente.
