import sqlite3 

print("Primera base de datos con SQLite")

conexion = sqlite3.connect('tienda.db')
conexion.close()