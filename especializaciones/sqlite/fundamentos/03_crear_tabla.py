import sqlite3

from ruta_db import RUTA_DB

conexion = sqlite3.connect(RUTA_DB)
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
