import sqlite3

conexion = sqlite3.connect('tienda.db')
cursor = conexion.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS productos ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL
)
''')

conexion.commit()
conexion.close()
