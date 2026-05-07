import sqlite3

from ruta_db import RUTA_DB

print("SQLite Funciona!")
print (sqlite3.sqlite_version)

conexion = sqlite3.connect(RUTA_DB)
cursor = conexion.cursor()

cursor.execute('''
INSERT INTO productos (nombre, precio) VALUES
('Camiseta', 19.99),
('Pantalones', 39.99),
('Zapatos', 59.99)
''')


conexion.commit()
conexion.close()



