import sqlite3

def crear_basedatos():
    conexion = sqlite3.connect('productos.db')
    conexion.close()
    return print("Base de datos creada Exitosamente")