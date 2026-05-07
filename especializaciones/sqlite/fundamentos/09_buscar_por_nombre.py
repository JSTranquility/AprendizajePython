import sqlite3

from ruta_db import RUTA_DB

texto = input("Ingrese el nombre del producto a buscar: ")

conexion = sqlite3.connect(RUTA_DB)
cursor = conexion.cursor()

cursor.execute('SELECT id, nombre, precio FROM productos WHERE nombre LIKE ?', ('%' + texto + '%',))

productos = cursor.fetchall()
conexion.close()

for producto in productos:
    print(producto)
