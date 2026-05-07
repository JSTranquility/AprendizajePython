import sqlite3

from ruta_db import RUTA_DB

id_producto = int(input("Ingrese el ID del producto a borrar: "))

conexion = sqlite3.connect(RUTA_DB)
cursor = conexion.cursor()

cursor.execute('DELETE FROM productos WHERE id = ?', (id_producto,))
conexion.commit()
conexion.close()

print(f"Producto con ID {id_producto} ha sido borrado.")
