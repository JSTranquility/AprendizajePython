import sqlite3

texto = input("Ingrese el nombre del producto a buscar: ")

conexion = sqlite3.connect('tienda.db')
cursor = conexion.cursor()

cursor.execute('SELECT id, nombre, precio FROM productos WHERE nombre LIKE ?', ('%' + texto + '%',))

productos = cursor.fetchall()
conexion.close()

for producto in productos:
    print(producto)