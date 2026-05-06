import sqlite3

conexion = sqlite3.connect('tienda.db')
cursor = conexion.cursor()

# Ordenar por precio de menor a mayor
cursor.execute('SELECT id, nombre, precio FROM productos ORDER BY precio ASC')
productos_asc = cursor.fetchall()
print("Productos ordenados por precio (menor a mayor):")
for producto in productos_asc:
    print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]:.2f}")

# Ordenar por precio de mayor a menor
cursor.execute('SELECT id, nombre, precio FROM productos ORDER BY precio DESC')
productos_desc = cursor.fetchall()
print("\nProductos ordenados por precio (mayor a menor):")
for producto in productos_desc:
    print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]:.2f}")

#ordenar por nombre alfabéticamente
cursor.execute('SELECT id, nombre, precio FROM productos ORDER BY nombre ASC')
productos_nombre = cursor.fetchall()
print("\nProductos ordenados por nombre (A-Z):")
for producto in productos_nombre:
    print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]:.2f}")
conexion.close()