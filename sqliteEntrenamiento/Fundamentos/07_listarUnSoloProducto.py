import sqlite3

conexion = sqlite3.connect('tienda.db')
cursor = conexion.cursor()

cursor.execute('SELECT id, nombre, precio FROM productos where id = ?', (1,))
producto = cursor.fetchone()

conexion.close()

print(producto)