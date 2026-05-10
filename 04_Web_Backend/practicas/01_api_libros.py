# Desafio Web 1: Mi Mini API de Libros

# Consigna:
# Crea una aplicacion Flask que gestione una lista de libros.

# Requisitos:
# 1. Crea una lista de diccionarios llamada 'libros' con al menos 3 libros (id, titulo, autor).
# 2. Crea una ruta '/libros' que devuelva la lista completa.
# 3. Crea una ruta '/libros/<int:libro_id>' que devuelva solo el libro solicitado.
# 4. Si el libro no existe, devuelve un mensaje de "Libro no encontrado".

# --- ESCRIBE TU CODIGO ABAJO ---

from flask import Flask, request, redirect

app = Flask(__name__)

libros = [
    {'id': 1, 'titulo': 'Cien Años de Soledad', 'autor': 'Gabriel García Márquez'},
    {'id': 2, 'titulo': 'Don Quijote de la Mancha', 'autor': 'Miguel de Cervantes'},
    {'id': 3, 'titulo': 'La Sombra del Viento', 'autor': 'Carlos Ruiz Zafón'}
]

@app.route('/libros')
def obtener_libros():
    return libros

@app.route('/libros/<int:libro_id>')
def obtener_libro(libro_id):
    libro = next((l for l in libros if l['id'] == libro_id), None)
    if libro:
        return libro
    else:
        return {'error': 'Libro no encontrado'}, 404
    
if __name__ == '__main__':
    app.run(debug=True)