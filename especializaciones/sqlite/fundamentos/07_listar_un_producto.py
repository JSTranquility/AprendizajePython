import sqlite3

from ruta_db import RUTA_DB

conexion = sqlite3.connect(RUTA_DB)
cursor = conexion.cursor()

cursor.execute('SELECT id, nombre, precio FROM productos where id = ?', (1,))
producto = cursor.fetchone()

conexion.close()

print(producto)
