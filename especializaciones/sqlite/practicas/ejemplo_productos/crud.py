from db import obtener_conexion

def crear_tabla_productos():
    conexion = obtener_conexion()
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

def agregar_producto(nombre, precio):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute('INSERT INTO productos (nombre, precio) VALUES (?, ?)', (nombre, precio))

    conexion.commit()
    conexion.close()

def obtener_producto_por_id(producto_id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute('SELECT id, nombre, precio FROM productos WHERE id = ?', (producto_id,))
    producto = cursor.fetchone()

    conexion.close()
    return producto

def buscar_productos_por_nombre(texto):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute('SELECT id, nombre, precio FROM productos WHERE nombre LIKE ?', ('%' + texto + '%',))
    productos = cursor.fetchall()

    conexion.close()
    return productos

def listar_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute('SELECT id, nombre, precio FROM productos')
    productos = cursor.fetchall()

    conexion.close()
    return productos
    

