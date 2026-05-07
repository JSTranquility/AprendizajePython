# 📩 Módulo 02: Formularios y Métodos HTTP

Para que una aplicación web sea interactiva, no solo debe **mostrar** datos, sino también **recibirlos**. Aquí es donde entran los formularios y los métodos HTTP.

---

## 1. GET vs POST: Los dos caminos
Cuando el navegador habla con Flask, usa principalmente dos métodos:

*   **GET (Obtener):** Se usa para pedir una página o buscar algo. Los datos se ven en la URL (ej: `google.com/search?q=flask`).
*   **POST (Enviar):** Se usa para enviar datos sensibles o crear cosas (como un nuevo usuario o un libro). Los datos van "ocultos" dentro del paquete de la petición.

---

## 2. Configurando una ruta para recibir datos
Por defecto, las rutas de Flask solo aceptan `GET`. Si quieres recibir un formulario, debes decírselo:

```python
from flask import request # Importante para leer los datos

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_libro():
    if request.method == 'POST':
        # Aquí leemos lo que el usuario escribió en el HTML
        titulo = request.form['titulo']
        autor = request.form['autor']
        # Aquí llamaríamos a la función de db.py para insertar
        return f"Has agregado el libro: {titulo}"
    
    # Si es GET, simplemente mostramos el formulario
    return render_template('agregar.html')
```

---

## 3. El Formulario en HTML
Para que Flask reciba los datos, el HTML debe tener tres cosas clave:
1.  `method="POST"`
2.  `action="/tu_ruta"`
3.  Cada input debe tener un atributo `name` (así es como Flask lo identifica).

```html
<form action="/agregar" method="POST">
    <input type="text" name="titulo" placeholder="Título del libro">
    <input type="text" name="autor" placeholder="Autor">
    <button type="submit">Guardar Libro</button>
</form>
```

---

## 4. La Función `request`
Dentro de Flask, el objeto `request` es tu mejor amigo:
*   `request.form['nombre']`: Para obtener datos de un formulario POST.
*   `request.args.get('buscar')`: Para obtener datos de una búsqueda GET (URL).

---

## 💡 Ejercicio sugerido
Intenta crear una nueva ruta `/nuevo_libro` en tu `app.py` que muestre un formulario y, al darle a enviar, imprima el nombre del libro en la pantalla. ¡Es el primer paso para conectarlo con tu base de datos!
