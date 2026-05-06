import sqlite3

id_producto = int(input("Ingrese el ID del producto a actualizar: "))
nueva_cantidad = int(input("Ingrese la cantidad de precio: "))

conexion = sqlite3.connect('tienda.db')
cursor = conexion.cursor()

cursor.execute('UPDATE productos SET precio = ? WHERE id = ?', (nueva_cantidad, id_producto))

conexion.commit()
conexion.close()

print(f"Stock del producto con ID {id_producto} actualizado a {nueva_cantidad}.")