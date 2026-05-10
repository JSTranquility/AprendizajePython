from flask import Flask, request, redirect
from flask import render_template as rt

app = Flask(__name__)

usuarios = [
    {'id': 1, 'nombre': 'Alice', 'email': 'alice@example.com'},
    {'id': 2, 'nombre': 'Bob', 'email': 'bob@example.com'},
    {'id': 3, 'nombre': 'Charlie', 'email': 'charlie@example.com'}
]

peliculas = [
    {'id': 1, 'titulo': 'Inception', 'director': 'Christopher Nolan'},
    {'id': 2, 'titulo': 'The Matrix', 'director': 'Lana Wachowski, Lilly Wachowski'},
    {'id': 3, 'titulo': 'Interstellar', 'director': 'Christopher Nolan'}
]

@app.route('/')
def home():
    return "¡Hola, Mundo!"

@app.route('/index')
def index():
    return rt('index.html')

@app.route('/usuarios')
def get_usuarios():
    return rt('usuarios.html', usuarios=usuarios)

@app.route('/usuarios/<int:id>')
def mostrar_usuario(id):
    usuario = next((u for u in usuarios if u['id'] == id), None)
    if usuario:
        return rt('usuario.html', usuario=usuario)
    else:
        return "Usuario no encontrado", 404
    
@app.route('/peliculas')
def get_peliculas():
    return rt('peliculas.html', peliculas=peliculas)

@app.route('/peliculas/agregar_pelicula', methods=['GET', 'POST'])
def agregar_pelicula():
    if request.method == 'POST':
        titulo = request.form['titulo']
        director = request.form['director']
        peliculas.append({'id': len(peliculas) + 1, 'titulo': titulo, 'director': director})
        return redirect('/peliculas')
    return rt('agregar_pelicula.html')

if __name__ == '__main__':
    app.run(debug=True)