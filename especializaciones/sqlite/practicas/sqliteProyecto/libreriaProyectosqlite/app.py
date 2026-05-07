from flask import Flask, render_template
from db import consultar_libros

app = Flask(__name__)

@app.route('/')
def index():
    # Obtenemos los libros de la base de datos
    libros = consultar_libros()
    # Los enviamos al HTML
    return render_template('index.html', libros=libros)

if __name__ == "__main__":
    app.run(debug=True)