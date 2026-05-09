from flask import Flask, render_template
from db import consultar_libros, obtener_categorias, consultar_libros_por_categoria

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/libros')
def index():
    libros = consultar_libros()
    return render_template('index.html', libros=libros)

@app.route('/categorias')
def categorias_lista():
    categorias = obtener_categorias()
    return render_template('categoria.html', categorias=categorias, libros=None)

@app.route('/categoria/<int:categoria_id>')
def ver_categoria(categoria_id):
    libros = consultar_libros_por_categoria(categoria_id)
    categorias = obtener_categorias()
    return render_template('categoria.html', categorias=categorias, libros=libros, categoria_seleccionada=categoria_id)

if __name__ == "__main__":
    app.run(debug=True)