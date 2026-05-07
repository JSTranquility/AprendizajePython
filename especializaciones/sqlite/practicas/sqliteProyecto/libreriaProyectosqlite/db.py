
import sqlite3

def obtener_conexion():
    conexion = sqlite3.connect('libreria.db')
    conexion.row_factory = sqlite3.Row
    return conexion
def crear_base_datos():

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL UNIQUE,
            contraseña TEXT NOT NULL,
            rol TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categorias (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   categoria TEXT NOT NULL
                   )
             ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            precio REAL NOT NULL,
            categoria_id INTEGER,
            FOREIGN KEY (categoria_id) REFERENCES categorias(id)       
         )         
    ''')

    conexion.commit()
    conexion.close()

crear_base_datos()

def registrar_usuarios():

    nombre = input("Agregue el nombre de usuario: ")
    correo = input("Agregue su correo: ")
    password = input("Agregue su contraseña: ")

    if nombre == "" or correo == "" or password == "":
        print("Todos los campos son obligatorios")
        return iniciar_sesion()

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        'SELECT * FROM usuarios WHERE nombre = ?',
        (nombre,)
    )

    usuario_existente = cursor.fetchone()

    if usuario_existente:
        print("Ese nombre de usuario ya existe.")
    else:
        cursor.execute(
            'INSERT INTO usuarios (nombre, correo, contraseña) VALUES (?, ?, ?)',
            (nombre, correo, password)
        )

        conexion.commit()

        print("Usuario registrado correctamente.")

    conexion.close()

def ver_usuarios():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    

    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()

    for usuario in usuarios:
        print(dict(usuario))


    conexion.close()


def insertar_usuarios():
    usuarios = [
        ("Henssell", "rezoart1@gmail.com", "admin", "admin"),
        ("Ana", "ana45belp@gmail.com", "user", "user"),
        ("Juan", "juanalberto@gmail.com", "juancito123", "user")
    ]

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.executemany("""
        INSERT INTO usuarios (nombre, correo, contraseña, rol)
        VALUES (?, ?, ?, ?)
    """, usuarios)

    conexion.commit()
    conexion.close()

    print("Usuarios insertados!")
def ver_usuarios_alfabeticamente():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute('SELECT * FROM usuarios ORDER BY nombre ASC')
    usuarios = cursor.fetchall()

    for usuario in usuarios:
        print(dict(usuario))

    conexion.close()

def ver_categorias():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    

    cursor.execute('SELECT * FROM categorias')
    categorias = cursor.fetchall()

    for categoria in categorias:
        print(dict(categoria))


    conexion.close()

def insertar_categorias():
    categorias = {
        ("Terror",),
        ("Ciencia Ficción",),
        ("Novela",),
        ("Misterio",)
    }

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.executemany(""" 
    INSERT OR IGNORE INTO categorias (categoria)
                       VALUES (?)
""", categorias)
    
    conexion.commit()
    conexion.close()
    print(
        "Categorias insertadas!"
    )


def ver_libros():
    libros = consultar_libros()
    for libro in libros:
        print(dict(libro))

def consultar_libros():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute('''
        SELECT libros.titulo,
               libros.autor,
               libros.precio,
               categorias.categoria
        FROM libros
        JOIN categorias ON libros.categoria_id = categorias.id
    ''')
    libros = cursor.fetchall()
    conexion.close()
    return libros

def insertar_libros():
        libros = {
            ("Dracula", "Bram Stoker", 15.99, 1),
            ("Fundacion", "Isaac Asimov", 12.99, 2),
            ("Los Miserables", "Victor Hugo", 10.99, 3),
            ("El Principito", "Antoine de Saint-Exupery", 5.99, 4)
        }

        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.executemany(""" 
        INSERT INTO libros (titulo, autor, precio, categoria_id)
                           VALUES (?, ?, ?, ?)
        """, libros)
        
        conexion.commit()
        conexion.close()
        print(
            "Libros insertados!"
        )    

def eliminar_usuario(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id = ?', (id,))
    conexion.commit()
    conexion.close()
    print(
        "Usuario eliminado!"
    )


def actualizar_usuarios():
    id = input("ID del usuario a actualizar: ")
    nombre = input("Nuevo nombre: ")
    correo = input("Nuevo correo: ")
    password = input("Nueva contraseña: ")
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute('UPDATE usuarios SET nombre = ?, correo = ?, contraseña = ? WHERE id = ?', (nombre, correo, password, id))
    conexion.commit()
    conexion.close()
    print("Usuario actualizado!")

def eliminar_libro(id):
    id = input("ID del libro a eliminar: ")
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM libros WHERE id = ?', (id,))
    conexion.commit()
    conexion.close()
    print("Libro eliminado!")

def actualizar_libros():
    id = input("ID del libro a actualizar: ")
    titulo = input("Nuevo título: ")
    autor = input("Nuevo autor: ")
    precio = input("Nuevo precio: ")
    categoria_id = input("Nueva categoría ID: ")
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute('UPDATE libros SET titulo = ?, autor = ?, precio = ?, categoria_id = ? WHERE id = ?', (titulo, autor, precio, categoria_id, id))
    conexion.commit()
    conexion.close()
    print("Libro actualizado!")



def iniciar_sesion():
    correo = input("Correo: ")
    contraseña = input("Contraseña: ")

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        'SELECT * FROM usuarios WHERE correo = ? AND contraseña = ?',
        (correo, contraseña)
    )

    usuario = cursor.fetchone()
    conexion.close()

    if usuario:
        print(f"Bienvenido {usuario['nombre']}")

        if usuario["rol"] == "admin":
            menu_admin()
        else:
            menu_usuario()

    else:
        print("Usuario no encontrado")
        return iniciar_sesion()

def menu_admin():
    while True:
        print("\n---Menú---")
        print("1. Agregar Usuario")
        print("2. Ver Usuarios")
        print("3. Eliminar Usuario")
        print("4. Actualizar Usuario")
        print("5. Agregar Libro")
        print("6. Ver Libros")
        print("7. Eliminar Libro")
        print("8. Actualizar Libro")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_usuarios()
        elif opcion == "2":
            ver_usuarios()
        elif opcion == "3":
            eliminar_usuario()
        elif opcion == "4":
            actualizar_usuarios()
        elif opcion == "5":
            insertar_libros()
        elif opcion == "6":
            ver_libros()
        elif opcion == "7":
            eliminar_libro()
        elif opcion == "8":
            actualizar_libros()
        elif opcion == "0":
            break
        else:
            print("Opción no válida")


def menu_usuario():
    while True:
        print("\n---Menú---")
        print("1. Ver Libros")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            ver_libros()
        elif opcion == "0":
            break
        else:
            print("Opción no válida")
     

















