# 🌶️ Guía Rápida de Flask: De Python a la Web

Flask es un **micro-framework** de Python. Se le llama "micro" porque es ligero y te da solo lo básico para empezar, pero es increíblemente potente para conectar bases de datos con interfaces visuales (HTML).

---

## 1. El Concepto de "Ruta" (Routes)
En Flask, cada página de tu sitio web es una **función**. Usamos "decoradores" (`@app.route`) para decirle a Python qué URL debe disparar qué función.

```python
@app.route('/')
def inicio():
    return "¡Hola Mundo!"

@app.route('/contacto')
def contacto():
    return "Página de contacto"
```

---

## 2. El Motor de Plantillas: Jinja2
Flask usa **Jinja2** para permitir que el HTML sea "inteligente". Esto nos permite pasar variables desde Python al HTML.

### En Python (`app.py`):
```python
@app.route('/')
def index():
    usuario = "Henssell"
    return render_template('index.html', nombre=usuario)
```

### En HTML (`templates/index.html`):
```html
<h1>Bienvenido, {{ nombre }}</h1>
```
*   **`{{ variable }}`**: Imprime el valor de una variable.
*   **`{% for ... %}`**: Ejecuta un bucle (como hicimos con los libros).

---

## 3. Estructura de Proyecto Estándar
Flask es muy estricto con dónde pones los archivos:

*   📂 **`mi_proyecto/`**
    *   📄 `app.py` (Tu servidor)
    *   📄 `db.py` (Tu lógica de base de datos)
    *   📂 **`templates/`** (Aquí van TODOS los archivos `.html`)
    *   📂 **`static/`** (Aquí van imágenes, CSS y JavaScript)

---

## 4. El Ciclo de Vida de una Petición
Para tu proyecto de librería, el flujo es:

1.  **Navegador:** *"Hola app.py, dame la página principal (`/`)"*.
2.  **Flask (`app.py`):** *"Vale, espera... voy a llamar a `db.py` para ver qué libros hay"*.
3.  **Base de Datos:** Devuelve una lista de libros.
4.  **Flask:** *"Tengo los libros. Ahora los voy a 'dibujar' en el `index.html`"*.
5.  **Navegador:** Recibe el HTML ya construido y lo muestra.

---

## 5. Comandos Útiles
Si `pip` falla, recuerda usar siempre el prefijo `python -m`:

*   **Instalar:** `python -m pip install flask`
*   **Ejecutar:** `python app.py` o `python -m flask run`
*   **Modo Debug:** `app.run(debug=True)` (esto hace que el servidor se reinicie solo cuando guardas cambios).

---

## 💡 Próximos pasos recomendados
1.  **Formularios:** Aprender a enviar datos desde el HTML a Python (para agregar libros).
2.  **Redirects:** Redirigir al usuario a otra página después de una acción.
3.  **SQLAlchemy:** Una forma más "moderna" de manejar bases de datos en Flask sin escribir SQL puro (opcional).
