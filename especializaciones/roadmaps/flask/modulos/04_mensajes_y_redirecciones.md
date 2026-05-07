# 📢 Módulo 04: Mensajes Flash y Redirecciones

En una aplicación real, cuando el usuario hace algo (como guardar un libro), no queremos que se quede mirando una pantalla en blanco. Queremos **redirigirlo** de vuelta a la lista y darle un **mensaje de confirmación**.

---

## 1. Redirecciones (`redirect` y `url_for`)
En lugar de devolver un string o un HTML directamente, le pedimos al navegador que vaya a otra ruta.

```python
from flask import redirect, url_for

@app.route('/guardar', methods=['POST'])
def guardar():
    # ... lógica de guardar en DB ...
    return redirect(url_for('index')) # 'index' es el nombre de la función de la ruta principal
```
*   **`url_for('funcion')`**: Es mejor que escribir `/` a mano, porque si cambias la URL en el decorador, `url_for` la encontrará automáticamente.

---

## 2. Mensajes Relámpago (`flash`)
Flask tiene un sistema llamado `flash` para enviar mensajes temporales que solo duran una petición (aparecen, se leen y desaparecen).

### En Python:
```python
from flask import flash

app.secret_key = 'una_clave_secreta' # Necesario para usar flash

@app.route('/eliminar/<id>')
def eliminar(id):
    # ... lógica de eliminar ...
    flash("¡Libro eliminado con éxito!", "danger")
    return redirect(url_for('index'))
```

### En el HTML (`base.html`):
Para mostrar los mensajes, debemos poner este bloque en nuestra plantilla base (así aparecerán en cualquier página):

```html
{% with messages = get_flashed_messages(with_categories=true) %}
  {% if messages %}
    {% for category, message in messages %}
      <div class="alert alert-{{ category }}">
        {{ message }}
      </div>
    {% endfor %}
  {% endif %}
{% endwith %}
```

---

## 3. ¿Por qué usar Redirecciones?
*   **Evita duplicados:** Si el usuario refresca la página después de un POST, el navegador intentará enviar los datos otra vez. Al redirigir, el refresco solo recarga la página final limpia.
*   **Mejor UX:** El usuario siempre sabe dónde está y qué ha pasado.

---

## 💡 Próximo Desafío
Añade un `flash` a tu aplicación cuando el usuario entre a la página principal por primera vez. ¡Verás lo profesional que se siente!
