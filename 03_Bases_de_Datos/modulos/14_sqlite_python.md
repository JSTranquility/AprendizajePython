# 14 - SQLite: la base de datos que ya trae Python

SQLite es una base de datos pequena, rapida y muy practica que ya viene incluida con Python.

No tienes que instalar MySQL.
No tienes que crear usuarios.
No tienes que levantar un servidor.
No tienes que configurar casi nada.

Solo importas `sqlite3`, creas un archivo `.db`, y ya puedes guardar datos reales.

## 1. Idea simple

Imagina una libreta de Excel guardada en un archivo.

Ese archivo puede tener varias hojas.
Cada hoja tiene columnas.
Cada fila guarda un registro.

En SQLite:

- El archivo se llama base de datos.
- Las hojas se llaman tablas.
- Las columnas se llaman campos.
- Las filas se llaman registros.

Ejemplo:

Base de datos:

```text
tienda.db
```

Tabla:

```text
productos
```

Columnas:

```text
id, nombre, precio, stock
```

Filas:

```text
1, "Mouse", 15.99, 10
2, "Teclado", 35.50, 5
3, "Monitor", 180.00, 2
```

## 2. Por que SQLite te conviene al empezar

SQLite es ideal para practicar porque viene con Python.

```python
import sqlite3
```

Si eso funciona, ya tienes SQLite disponible.

Usalo para:

- Programas pequenos.
- Proyectos de consola.
- Apps de escritorio con Tkinter.
- Practicar SQL.
- Guardar inventarios, contactos, tareas, notas, gastos, estudiantes.
- Aprender bases de datos antes de pasar a MySQL, PostgreSQL o servidores reales.

No lo uses como primera opcion para:

- Una aplicacion web con miles de usuarios escribiendo al mismo tiempo.
- Sistemas grandes con mucha concurrencia.
- Proyectos donde necesitas usuarios, permisos y administracion avanzada.

Para aprender, SQLite es excelente.

## 3. Probar si SQLite funciona

Crea un archivo llamado `probar_sqlite.py`:

```python
import sqlite3

print("SQLite funciona")
print(sqlite3.sqlite_version)
```

Ejecuta:

```powershell
python probar_sqlite.py
```

Si ves una version, todo esta listo.

## 4. Crear tu primera base de datos

Crea un archivo llamado `crear_db.py`:

```python
import sqlite3

conexion = sqlite3.connect("tienda.db")
conexion.close()

print("Base de datos creada")
```

Ejecuta:

```powershell
python crear_db.py
```

Despues de ejecutar, debe aparecer un archivo:

```text
tienda.db
```

Ese archivo es tu base de datos.

## 5. Que es una conexion

Esta linea abre la base de datos:

```python
conexion = sqlite3.connect("tienda.db")
```

Si `tienda.db` existe, Python la abre.
Si no existe, Python la crea.

Esta linea cierra la base de datos:

```python
conexion.close()
```

Piensalo asi:

- `connect()` abre la puerta.
- `close()` cierra la puerta.

## 6. Que es un cursor

El cursor es el objeto que manda instrucciones a la base de datos.

```python
cursor = conexion.cursor()
```

Piensalo como el lapiz que escribe o lee dentro de la base de datos.

La conexion abre el archivo.
El cursor ejecuta comandos SQL.

## 7. Crear una tabla

Una base de datos vacia no sirve de mucho.
Necesitamos crear una tabla.

Crea `crear_tabla.py`:

```python
import sqlite3

conexion = sqlite3.connect("tienda.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    stock INTEGER NOT NULL
)
""")

conexion.commit()
conexion.close()

print("Tabla productos creada")
```

Ejecuta:

```powershell
python crear_tabla.py
```

## 8. Desglose de la tabla

Esta parte crea la tabla:

```sql
CREATE TABLE IF NOT EXISTS productos
```

Significa:

"Crea una tabla llamada `productos`, pero si ya existe, no explotes con error."

Esta columna:

```sql
id INTEGER PRIMARY KEY AUTOINCREMENT
```

Significa:

- `id`: numero unico para cada producto.
- `INTEGER`: numero entero.
- `PRIMARY KEY`: identificador principal.
- `AUTOINCREMENT`: SQLite lo aumenta solo.

Esta columna:

```sql
nombre TEXT NOT NULL
```

Significa:

- `nombre`: nombre del producto.
- `TEXT`: texto.
- `NOT NULL`: obligatorio.

Esta columna:

```sql
precio REAL NOT NULL
```

Significa:

- `precio`: precio del producto.
- `REAL`: numero con decimales.
- `NOT NULL`: obligatorio.

Esta columna:

```sql
stock INTEGER NOT NULL
```

Significa:

- `stock`: cantidad disponible.
- `INTEGER`: numero entero.
- `NOT NULL`: obligatorio.

## 9. Que es commit

Cuando haces cambios en la base de datos, debes guardarlos.

```python
conexion.commit()
```

Si haces un `INSERT`, `UPDATE` o `DELETE` y no llamas `commit()`, los cambios pueden perderse.

Piensalo como guardar un archivo de Word:

- Escribes algo.
- Presionas guardar.

En SQLite:

- Ejecutas cambios.
- Llamas `commit()`.

## 10. Insertar datos

Crea `insertar_producto.py`:

```python
import sqlite3

conexion = sqlite3.connect("tienda.db")
cursor = conexion.cursor()

cursor.execute("""
INSERT INTO productos (nombre, precio, stock)
VALUES (?, ?, ?)
""", ("Mouse", 15.99, 10))

conexion.commit()
conexion.close()

print("Producto insertado")
```

Ejecuta:

```powershell
python insertar_producto.py
```

## 11. Por que se usan signos de pregunta

Esta parte:

```sql
VALUES (?, ?, ?)
```

Significa:

"Aqui van valores, pero los voy a pasar aparte."

Y esta parte:

```python
("Mouse", 15.99, 10)
```

Son los valores.

No hagas esto:

```python
nombre = "Mouse"
cursor.execute(f"INSERT INTO productos (nombre) VALUES ('{nombre}')")
```

Es una mala practica porque puede abrir problemas de seguridad y errores raros si el texto tiene comillas.

Haz esto:

```python
cursor.execute("INSERT INTO productos (nombre) VALUES (?)", (nombre,))
```

Nota importante:

```python
(nombre,)
```

Esa coma es necesaria cuando pasas una tupla de un solo valor.

## 12. Insertar varios productos

Crea `insertar_varios.py`:

```python
import sqlite3

productos = [
    ("Teclado", 35.50, 5),
    ("Monitor", 180.00, 2),
    ("Cable HDMI", 8.75, 20),
]

conexion = sqlite3.connect("tienda.db")
cursor = conexion.cursor()

cursor.executemany("""
INSERT INTO productos (nombre, precio, stock)
VALUES (?, ?, ?)
""", productos)

conexion.commit()
conexion.close()

print("Productos insertados")
```

`executemany()` sirve para insertar muchos datos de una vez.

## 13. Leer todos los datos

Crea `listar_productos.py`:

```python
import sqlite3

conexion = sqlite3.connect("tienda.db")
cursor = conexion.cursor()

cursor.execute("SELECT id, nombre, precio, stock FROM productos")
productos = cursor.fetchall()

conexion.close()

for producto in productos:
    print(producto)
```

Ejecuta:

```powershell
python listar_productos.py
```

Puedes ver algo parecido a:

```text
(1, 'Mouse', 15.99, 10)
(2, 'Teclado', 35.5, 5)
(3, 'Monitor', 180.0, 2)
```

Cada fila viene como una tupla.

## 14. Leer una fila

`fetchall()` trae todas las filas.

```python
productos = cursor.fetchall()
```

`fetchone()` trae una sola fila.

```python
producto = cursor.fetchone()
```

Ejemplo `buscar_uno.py`:

```python
import sqlite3

conexion = sqlite3.connect("tienda.db")
cursor = conexion.cursor()

cursor.execute("SELECT id, nombre, precio, stock FROM productos WHERE id = ?", (1,))
producto = cursor.fetchone()

conexion.close()

print(producto)
```

## 15. Mostrar datos mas bonito

Crea `listar_bonito.py`:

```python
import sqlite3

conexion = sqlite3.connect("tienda.db")
cursor = conexion.cursor()

cursor.execute("SELECT id, nombre, precio, stock FROM productos")
productos = cursor.fetchall()

conexion.close()

for producto in productos:
    id_producto = producto[0]
    nombre = producto[1]
    precio = producto[2]
    stock = producto[3]

    print(f"{id_producto}. {nombre} - ${precio} - Stock: {stock}")
```

## 16. Usar sqlite3.Row para leer por nombre

Leer por posicion funciona, pero esto:

```python
producto[1]
```

No dice claramente que es.

SQLite permite leer columnas por nombre.

Crea `listar_por_nombre.py`:

```python
import sqlite3

conexion = sqlite3.connect("tienda.db")
conexion.row_factory = sqlite3.Row
cursor = conexion.cursor()

cursor.execute("SELECT id, nombre, precio, stock FROM productos")
productos = cursor.fetchall()

conexion.close()

for producto in productos:
    print(f"{producto['id']}. {producto['nombre']} - ${producto['precio']} - Stock: {producto['stock']}")
```

Esta linea es la clave:

```python
conexion.row_factory = sqlite3.Row
```

Con eso puedes usar:

```python
producto["nombre"]
```

En vez de:

```python
producto[1]
```

## 17. Buscar con WHERE

`WHERE` sirve para filtrar.

Ejemplo:

```sql
SELECT * FROM productos WHERE stock > 5;
```

En Python:

```python
import sqlite3

conexion = sqlite3.connect("tienda.db")
cursor = conexion.cursor()

cursor.execute("SELECT id, nombre, precio, stock FROM productos WHERE stock > ?", (5,))
productos = cursor.fetchall()

conexion.close()

for producto in productos:
    print(producto)
```

## 18. Buscar por texto

Crea `buscar_por_nombre.py`:

```python
import sqlite3

texto = input("Buscar producto: ")

conexion = sqlite3.connect("tienda.db")
cursor = conexion.cursor()

cursor.execute("""
SELECT id, nombre, precio, stock
FROM productos
WHERE nombre LIKE ?
""", (f"%{texto}%",))

productos = cursor.fetchall()
conexion.close()

for producto in productos:
    print(producto)
```

`LIKE` busca texto parecido.

Si escribes:

```text
mo
```

Puede encontrar:

```text
Mouse
Monitor
```

Porque usamos:

```python
f"%{texto}%"
```

El simbolo `%` significa:

"Puede haber cualquier cosa antes o despues."

## 19. Ordenar resultados

Ordenar por precio:

```python
cursor.execute("SELECT id, nombre, precio, stock FROM productos ORDER BY precio")
```

Ordenar por precio de mayor a menor:

```python
cursor.execute("SELECT id, nombre, precio, stock FROM productos ORDER BY precio DESC")
```

Ordenar por nombre:

```python
cursor.execute("SELECT id, nombre, precio, stock FROM productos ORDER BY nombre")
```

## 20. Actualizar datos

Actualizar significa modificar algo que ya existe.

Crea `actualizar_stock.py`:

```python
import sqlite3

id_producto = int(input("ID del producto: "))
nuevo_stock = int(input("Nuevo stock: "))

conexion = sqlite3.connect("tienda.db")
cursor = conexion.cursor()

cursor.execute("""
UPDATE productos
SET stock = ?
WHERE id = ?
""", (nuevo_stock, id_producto))

conexion.commit()
conexion.close()

print("Stock actualizado")
```

Importante:

```sql
WHERE id = ?
```

Sin `WHERE`, actualizas todos los productos.

## 21. Borrar datos

Borrar un producto:

```python
import sqlite3

id_producto = int(input("ID del producto a borrar: "))

conexion = sqlite3.connect("tienda.db")
cursor = conexion.cursor()

cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))

conexion.commit()
conexion.close()

print("Producto borrado")
```

Importante:

```sql
WHERE id = ?
```

Sin `WHERE`, borras todos los productos.

## 22. CRUD

CRUD significa las 4 operaciones basicas de casi cualquier sistema:

| Letra | Significado | SQL |
| --- | --- | --- |
| C | Create, crear | INSERT |
| R | Read, leer | SELECT |
| U | Update, actualizar | UPDATE |
| D | Delete, borrar | DELETE |

Si entiendes CRUD, ya entiendes la base de muchas aplicaciones.

## 23. Crear un archivo db.py reutilizable

Cuando un programa crece, no quieres repetir esto en todos lados:

```python
conexion = sqlite3.connect("tienda.db")
```

Puedes crear un archivo para manejar la conexion.

Crea `db.py`:

```python
import sqlite3


def obtener_conexion():
    conexion = sqlite3.connect("tienda.db")
    conexion.row_factory = sqlite3.Row
    return conexion
```

Ahora otro archivo puede importar esa funcion.

## 24. Importar la conexion desde Python

Crea `productos_repo.py`:

```python
from db import obtener_conexion


def crear_tabla_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        stock INTEGER NOT NULL
    )
    """)

    conexion.commit()
    conexion.close()


def agregar_producto(nombre, precio, stock):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
    INSERT INTO productos (nombre, precio, stock)
    VALUES (?, ?, ?)
    """, (nombre, precio, stock))

    conexion.commit()
    conexion.close()


def listar_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT id, nombre, precio, stock FROM productos")
    productos = cursor.fetchall()

    conexion.close()
    return productos
```

Ahora crea `main_productos.py`:

```python
from productos_repo import crear_tabla_productos, agregar_producto, listar_productos


crear_tabla_productos()

agregar_producto("Mouse", 15.99, 10)
agregar_producto("Teclado", 35.50, 5)

productos = listar_productos()

for producto in productos:
    print(f"{producto['id']}. {producto['nombre']} - ${producto['precio']} - Stock: {producto['stock']}")
```

Ejecuta:

```powershell
python main_productos.py
```

## 25. Usar with para cerrar automaticamente

Puedes escribir:

```python
conexion = sqlite3.connect("tienda.db")
```

Y luego cerrar:

```python
conexion.close()
```

Pero tambien puedes usar `with`:

```python
import sqlite3

with sqlite3.connect("tienda.db") as conexion:
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

for producto in productos:
    print(producto)
```

Cuando el bloque termina, Python maneja mejor el cierre y el guardado de cambios.

Para empezar, usar `close()` esta bien porque se entiende facil.
Luego puedes practicar `with`.

## 26. Manejo de errores

Cuando trabajas con bases de datos, algo puede fallar.

Ejemplo:

- La tabla no existe.
- Escribiste mal una columna.
- Mandaste un tipo de dato incorrecto.
- El archivo `.db` no se puede abrir.

Ejemplo:

```python
import sqlite3

try:
    conexion = sqlite3.connect("tienda.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM tabla_que_no_existe")
    datos = cursor.fetchall()

    conexion.close()
    print(datos)

except sqlite3.Error as error:
    print("Error de SQLite:")
    print(error)
```

## 27. Mini proyecto: inventario con SQLite

Crea `inventario_sqlite.py`:

```python
import sqlite3


def obtener_conexion():
    conexion = sqlite3.connect("inventario.db")
    conexion.row_factory = sqlite3.Row
    return conexion


def crear_tabla():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        stock INTEGER NOT NULL
    )
    """)

    conexion.commit()
    conexion.close()


def agregar_producto():
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
    INSERT INTO productos (nombre, precio, stock)
    VALUES (?, ?, ?)
    """, (nombre, precio, stock))

    conexion.commit()
    conexion.close()

    print("Producto agregado")


def listar_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT id, nombre, precio, stock FROM productos ORDER BY id")
    productos = cursor.fetchall()

    conexion.close()

    if not productos:
        print("No hay productos")
        return

    for producto in productos:
        print(f"{producto['id']}. {producto['nombre']} - ${producto['precio']} - Stock: {producto['stock']}")


def buscar_producto():
    texto = input("Buscar: ")

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT id, nombre, precio, stock
    FROM productos
    WHERE nombre LIKE ?
    """, (f"%{texto}%",))

    productos = cursor.fetchall()
    conexion.close()

    for producto in productos:
        print(f"{producto['id']}. {producto['nombre']} - ${producto['precio']} - Stock: {producto['stock']}")


def actualizar_stock():
    id_producto = int(input("ID del producto: "))
    nuevo_stock = int(input("Nuevo stock: "))

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
    UPDATE productos
    SET stock = ?
    WHERE id = ?
    """, (nuevo_stock, id_producto))

    conexion.commit()
    conexion.close()

    print("Stock actualizado")


def borrar_producto():
    id_producto = int(input("ID del producto: "))

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))

    conexion.commit()
    conexion.close()

    print("Producto borrado")


def mostrar_menu():
    print()
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Actualizar stock")
    print("5. Borrar producto")
    print("6. Salir")


def main():
    crear_tabla()

    while True:
        mostrar_menu()
        opcion = input("Opcion: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            actualizar_stock()
        elif opcion == "5":
            borrar_producto()
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opcion invalida")


main()
```

Ejecuta:

```powershell
python inventario_sqlite.py
```

Este mini proyecto ya guarda datos de verdad.
Si cierras el programa y lo vuelves a abrir, los productos siguen ahi porque estan guardados en `inventario.db`.

## 28. Ver la base de datos con una herramienta visual

Puedes usar SQLite sin herramienta visual, solo con Python.

Pero si quieres ver las tablas como si fuera Excel, puedes instalar:

```text
DB Browser for SQLite
```

Con esa herramienta puedes abrir:

```text
tienda.db
inventario.db
```

Y mirar tablas, columnas y datos.

No es obligatorio, pero ayuda mucho al principio.

## 29. Tipos de datos comunes en SQLite

| Tipo | Para que sirve | Ejemplo |
| --- | --- | --- |
| INTEGER | Numeros enteros | 10 |
| REAL | Numeros con decimales | 15.99 |
| TEXT | Texto | "Mouse" |
| BLOB | Datos binarios | imagenes, archivos |
| NULL | Sin valor | NULL |

SQLite es flexible con los tipos, pero aun asi conviene usarlos bien.

## 30. Relaciones entre tablas

Una base de datos puede tener varias tablas.

Ejemplo:

```text
clientes
pedidos
```

Un cliente puede tener muchos pedidos.

Tabla `clientes`:

```text
id, nombre, telefono
```

Tabla `pedidos`:

```text
id, cliente_id, total
```

`cliente_id` guarda el `id` del cliente.

Ejemplo:

```sql
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    telefono TEXT
);

CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    total REAL NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);
```

Esto significa:

"Cada pedido pertenece a un cliente."

No necesitas dominar relaciones el primer dia, pero debes saber que existen.

## 31. Ejercicio guiado: estudiantes

Crea una base de datos llamada:

```text
escuela.db
```

Crea una tabla:

```text
estudiantes
```

Columnas:

```text
id, nombre, edad, nota
```

SQL sugerido:

```sql
CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL,
    nota REAL NOT NULL
);
```

Practica:

1. Insertar 5 estudiantes.
2. Listar todos.
3. Buscar estudiantes con nota mayor o igual a 70.
4. Buscar estudiantes menores de 18 anos.
5. Actualizar la nota de un estudiante.
6. Borrar un estudiante.

## 32. Reto final

Crea un proyecto:

```text
proyectos/04_inventario_sqlite.py
```

Debe tener un menu con:

1. Agregar producto.
2. Listar productos.
3. Buscar producto por nombre.
4. Actualizar precio.
5. Actualizar stock.
6. Borrar producto.
7. Mostrar productos con stock bajo.
8. Salir.

Reglas:

- Usa SQLite.
- Usa `sqlite3`.
- Usa `?` para pasar valores.
- Usa funciones.
- Crea la tabla automaticamente si no existe.
- No pierdas los datos al cerrar el programa.

## 33. Resumen

SQLite es la base de datos mas facil para empezar con Python.

Lo mas importante:

- `import sqlite3` importa la base de datos incluida.
- `sqlite3.connect("archivo.db")` abre o crea la base de datos.
- `cursor.execute()` ejecuta SQL.
- `commit()` guarda cambios.
- `close()` cierra la conexion.
- `INSERT` crea datos.
- `SELECT` lee datos.
- `UPDATE` modifica datos.
- `DELETE` borra datos.
- `?` protege tus consultas y evita errores.

Si entiendes este modulo, ya tienes una base fuerte para trabajar con datos reales en Python.
