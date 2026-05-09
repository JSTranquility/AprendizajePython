import sqlite3

from ruta_db import RUTA_DB

productos = [
    ('Camiseta', 19.99),
    ('Pantalones', 39.99),
    ('Zapatos', 59.99),
    ('Gorra', 14.99),
    ('Chaqueta', 89.99)
]
conexion = sqlite3.connect(RUTA_DB)
cursor = conexion.cursor()

cursor.executemany('''
INSERT INTO productos (nombre, precio) VALUES (?, ?)
''', productos)

conexion.commit()
conexion.close()

print("Productos insertados correctamente.")
