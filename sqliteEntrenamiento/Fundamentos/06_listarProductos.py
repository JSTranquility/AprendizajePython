import sqlite3

conexion = sqlite3.connect('tienda.db')
cursor = conexion.cursor()

cursor.execute('SELECT id, nombre, precio FROM productos')
productos = cursor.fetchall()


print("Productos en la tienda:")
for producto in productos:
    print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]:.2f}")


conexion.close()