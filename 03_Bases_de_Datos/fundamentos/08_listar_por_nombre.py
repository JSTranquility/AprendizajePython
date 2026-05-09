import sqlite3

from ruta_db import RUTA_DB

conexion = sqlite3.connect(RUTA_DB)
conexion.row_factory = sqlite3.Row
cursor = conexion.cursor()

cursor.execute('SELECT id, nombre, precio FROM productos')
productos = cursor.fetchall()

conexion.close()

for producto in productos:
    print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}")
