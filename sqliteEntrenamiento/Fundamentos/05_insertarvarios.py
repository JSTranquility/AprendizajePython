import sqlite3

productos = [
    ('Camiseta', 19.99),
    ('Pantalones', 39.99),
    ('Zapatos', 59.99),
    ('Gorra', 14.99),
    ('Chaqueta', 89.99)
]
conexion = sqlite3.connect('tienda.db')
cursor = conexion.cursor()

cursor.executemany('''
INSERT INTO productos (nombre, precio) VALUES (?, ?)
''', productos)

conexion.commit()
conexion.close()

print("Productos insertados correctamente.")