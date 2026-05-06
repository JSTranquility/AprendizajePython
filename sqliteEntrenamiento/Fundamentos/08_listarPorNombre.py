import sqlite3

conexion = sqlite3.connect('tienda.db')
conexion.row_factory = sqlite3.Row
cursor = conexion.cursor()

cursor.execute('SELECT id, nombre, precio FROM productos')
productos = cursor.fetchall()

conexion.close()

for producto in productos:
    print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}")