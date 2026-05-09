# Ejemplo 01: CRUD Básico con SQLite3

import sqlite3

# 1. Conexión (si no existe, se crea el archivo)
conexion = sqlite3.connect("mi_base_datos.db")
cursor = conexion.cursor()

# 2. Crear Tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        email TEXT UNIQUE
    )
""")

# 3. Insertar datos
try:
    cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", ("Pepe", "pepe@python.com"))
    conexion.commit()
    print("Usuario insertado correctamente.")
except sqlite3.IntegrityError:
    print("El usuario ya existe.")

# 4. Consultar datos
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

print("\n--- Lista de Usuarios ---")
for u in usuarios:
    print(f"ID: {u[0]} | Nombre: {u[1]} | Email: {u[2]}")

# 5. Cerrar conexión
conexion.close()
