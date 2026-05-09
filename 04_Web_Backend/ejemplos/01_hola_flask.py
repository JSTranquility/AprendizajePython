# Ejemplo 01: Servidor Básico con Flask

from flask import Flask

# Creamos la instancia de la aplicación
app = Flask(__name__)

# Definimos una ruta básica
@app.route("/")
def home():
    return "<h1>¡Hola desde Flask!</h1><p>Este es tu primer servidor web.</p>"

# Ruta con parámetros
@app.route("/usuario/<nombre>")
def saludar(nombre):
    return f"Hola, {nombre}. Bienvenido al curso de Backend."

if __name__ == "__main__":
    # Ejecutamos el servidor en modo debug
    app.run(debug=True)
