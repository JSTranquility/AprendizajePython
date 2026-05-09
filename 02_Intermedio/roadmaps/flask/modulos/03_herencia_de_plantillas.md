# 🏛️ Módulo 03: Herencia de Plantillas (Base Layout)

¿Te imaginas tener que copiar y pegar el menú de navegación en cada archivo HTML de tu sitio? Si tienes 100 páginas y quieres cambiar un enlace, ¡sería una pesadilla! 

Flask usa la **Herencia de Plantillas** para evitar esto.

---

## 1. El archivo `base.html`
Creamos un archivo "maestro" que contiene la estructura común (HTML, HEAD, BODY, Nav, Footer). En los lugares donde el contenido va a cambiar, usamos etiquetas `{% block %}`.

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Mi Librería{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="/">Inicio</a> | <a href="/nuevo">Agregar</a>
    </nav>

    <main>
        {% block content %}
        <!-- Aquí se inyectará el contenido de otras páginas -->
        {% endblock %}
    </main>

    <footer>© 2026 Mi Proyecto Python</footer>
</body>
</html>
```

---

## 2. Extendiendo la base
Ahora, cuando creamos una página nueva (como `index.html`), no escribimos todo el código de nuevo. Simplemente "extendemos" la base:

```html
<!-- templates/index.html -->
{% extends "base.html" %}

{% block title %}Inicio - Librería{% endblock %}

{% block content %}
    <h1>Listado de Libros</h1>
    <table>
        <!-- Tu tabla de libros aquí -->
    </table>
{% endblock %}
```

---

## 3. ¿Por qué es importante?
1.  **Código Limpio:** Tus archivos de contenido son cortos y fáciles de leer.
2.  **Mantenimiento:** Si quieres cambiar el color del menú, solo lo cambias en `base.html` y se actualiza en TODO el sitio.
3.  **Organización:** Te permite separar la estructura visual del contenido real.

---

## 💡 Próximo Desafío
Intenta crear un archivo `base.html` y haz que tu `index.html` actual lo use. Verás cómo tu código se vuelve mucho más profesional de inmediato.
