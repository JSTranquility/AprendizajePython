import sqlite3

from ruta_db import RUTA_DB

print("Primera base de datos con SQLite")

conexion = sqlite3.connect(RUTA_DB)
conexion.close()
