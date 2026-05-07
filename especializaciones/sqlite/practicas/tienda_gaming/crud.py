import sqlite3
from pathlib import Path


RUTA_DB = Path(__file__).resolve().parents[2] / "data" / "tiendagaming.db"

def obtener_conexion():
    conexion = sqlite3.connect(RUTA_DB)
    conexion.row_factory = sqlite3.Row
    return conexion

def crear_tabla_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()

def agregar_producto():
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    stock = int(input("Stock del producto: "))

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        'INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)',
        (nombre, precio, stock)
    )
    conexion.commit()
    conexion.close()

    print("Producto agregado correctamente.")

def listar_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute('SELECT id, nombre, precio, stock FROM productos')
    productos = cursor.fetchall()
    conexion.close()

    if not productos:
        print("No hay productos disponibles.")
    else:
        for producto in productos:
            print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}, Stock: {producto['stock']} unidades")

def buscar_producto():
    producto_id = int(input("Ingrese el ID del producto: "))

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        'SELECT id, nombre, precio, stock FROM productos WHERE id = ?',
        (producto_id,)
    )
    producto = cursor.fetchone()
    conexion.close()

    if producto:
        print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}, Stock: {producto['stock']}")
    else:
        print("Producto no encontrado.")

def actualizar_stock():
    id_producto = int(input("Ingrese el ID del producto a actualizar: "))
    nuevo_stock = int(input("Ingrese el nuevo stock: "))

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        'UPDATE productos SET stock = ? WHERE id = ?',
        (nuevo_stock, id_producto)
    )
    conexion.commit()
    conexion.close()

    print(f"Stock del producto con ID {id_producto} actualizado.")

def eliminar_producto():
    id_producto = int(input("Ingrese el ID del producto a eliminar: "))

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        'DELETE FROM productos WHERE id = ?',
        (id_producto,)
    )
    conexion.commit()
    conexion.close()

    print(f"Producto con ID {id_producto} eliminado.")

def mostrar_menu():
    print("\n--- Menú de la Tienda Gaming ---")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Buscar producto por ID")
    print("4. Actualizar stock de un producto")
    print("5. Eliminar producto")
    print("6. Salir")

def main():
    crear_tabla_productos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            listar_productos()
        elif opcion == '3':
            buscar_producto()
        elif opcion == '4':
            actualizar_stock()
        elif opcion == '5':
            eliminar_producto()
        elif opcion == '6':
            print("¡Gracias por usar la Tienda Gaming!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
