# 13 - MySQL con Python

MySQL es una base de datos. Sirve para guardar informacion en tablas y luego buscarla, cambiarla o borrarla.

Piensa en una tabla como una hoja de Excel:

- La base de datos es el archivo completo.
- La tabla es una hoja.
- Las columnas son los nombres de los datos.
- Las filas son los registros guardados.

Ejemplo de tabla `productos`:

| id | nombre | precio | stock |
| --- | --- | --- | --- |
| 1 | Teclado | 45.99 | 10 |
| 2 | Mouse | 25.50 | 15 |

## MySQL vs SQLite

SQLite guarda los datos en un archivo:

```text
Python -> app.db
```

MySQL trabaja como un servidor:

```text
Python -> servidor MySQL -> base de datos
```

SQLite es bueno para aprender rapido y crear proyectos pequenos. MySQL se usa mucho en aplicaciones web, sistemas de usuarios, inventarios, tiendas y proyectos donde varios programas pueden usar la misma base de datos.

## Que necesitas instalar

Necesitas dos cosas:

1. MySQL Server: el programa que guarda la base de datos.
2. Un conector de Python: el paquete que permite que Python hable con MySQL.

Instala el conector con:

```powershell
python -m pip install mysql-connector-python
```

Comprueba que Python lo puede importar:

```powershell
python
```

Dentro de Python:

```python
import mysql.connector

print("MySQL connector funciona")
```

Si no aparece error, el paquete esta instalado.

## Entrar a MySQL

Si tienes MySQL instalado, normalmente puedes entrar desde terminal con:

```powershell
mysql -u root -p
```

Significa:

- `mysql`: abrir el cliente de MySQL.
- `-u root`: usar el usuario `root`.
- `-p`: pedir contrasena.

Despues escribes tu contrasena de MySQL.

Si `mysql` no se reconoce como comando, puede que MySQL no este en el PATH. Tambien puedes usar MySQL Workbench si lo tienes instalado.

## Crear una base de datos

Dentro de MySQL, escribe:

```sql
CREATE DATABASE tienda_python;
```

Eso crea una base de datos llamada `tienda_python`.

Para usarla:

```sql
USE tienda_python;
```

Para ver bases de datos:

```sql
SHOW DATABASES;
```

Para ver en cual estas trabajando:

```sql
SELECT DATABASE();
```

## Crear una tabla

Ahora crea una tabla de productos:

```sql
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL
);
```

Desglose:

- `CREATE TABLE productos`: crea una tabla llamada `productos`.
- `id`: columna para identificar cada producto.
- `INT`: numero entero.
- `AUTO_INCREMENT`: MySQL pone 1, 2, 3, 4 automaticamente.
- `PRIMARY KEY`: columna unica que identifica cada fila.
- `nombre VARCHAR(100)`: texto de hasta 100 caracteres.
- `NOT NULL`: obligatorio, no puede quedar vacio.
- `precio DECIMAL(10, 2)`: numero con 2 decimales.
- `stock INT`: cantidad disponible.

Para ver las tablas:

```sql
SHOW TABLES;
```

Para ver la estructura de la tabla:

```sql
DESCRIBE productos;
```

## Insertar datos

`INSERT` sirve para guardar datos nuevos.

```sql
INSERT INTO productos (nombre, precio, stock)
VALUES ('Teclado', 45.99, 10);
```

Otro producto:

```sql
INSERT INTO productos (nombre, precio, stock)
VALUES ('Mouse', 25.50, 15);
```

No escribimos el `id` porque MySQL lo genera solo.

## Leer datos

`SELECT` sirve para consultar datos.

Ver todo:

```sql
SELECT * FROM productos;
```

Ver solo algunas columnas:

```sql
SELECT nombre, precio FROM productos;
```

Filtrar por precio:

```sql
SELECT * FROM productos
WHERE precio > 30;
```

Filtrar por id:

```sql
SELECT * FROM productos
WHERE id = 1;
```

Ordenar:

```sql
SELECT * FROM productos
ORDER BY precio DESC;
```

`DESC` significa de mayor a menor. Para menor a mayor usa `ASC`.

## Actualizar datos

`UPDATE` sirve para cambiar datos existentes.

```sql
UPDATE productos
SET precio = 39.99
WHERE id = 1;
```

Esto cambia el precio del producto con `id = 1`.

Cuidado: el `WHERE` es muy importante.

Este comando es peligroso:

```sql
UPDATE productos
SET precio = 39.99;
```

Sin `WHERE`, MySQL cambia todos los productos.

## Borrar datos

`DELETE` sirve para borrar filas.

```sql
DELETE FROM productos
WHERE id = 2;
```

Cuidado con esto:

```sql
DELETE FROM productos;
```

Sin `WHERE`, borra todos los productos.

## CRUD

CRUD son las 4 acciones principales de una aplicacion:

| Accion | SQL | Significado |
| --- | --- | --- |
| Create | INSERT | Crear datos |
| Read | SELECT | Leer datos |
| Update | UPDATE | Actualizar datos |
| Delete | DELETE | Borrar datos |

Si entiendes CRUD, ya entiendes la base de casi cualquier app con datos.

## Conectar Python con MySQL

Crea un archivo llamado `mysql_prueba.py` en la raiz del curso.

```python
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_password",
    database="tienda_python"
)

cursor = conexion.cursor()

cursor.execute("SELECT * FROM productos")

productos = cursor.fetchall()

for producto in productos:
    print(producto)

cursor.close()
conexion.close()
```

Cambia `tu_password` por tu contrasena real de MySQL.

Ejecuta:

```powershell
python mysql_prueba.py
```

Deberias ver algo parecido a:

```text
(1, 'Teclado', Decimal('45.99'), 10)
(2, 'Mouse', Decimal('25.50'), 15)
```

## Desglose del codigo Python

```python
import mysql.connector
```

Importa el paquete que permite conectarse a MySQL.

```python
conexion = mysql.connector.connect(...)
```

Abre la conexion.

```python
host="localhost"
```

MySQL esta en tu propia computadora.

```python
user="root"
```

Usuario de MySQL.

```python
password="tu_password"
```

Contrasena del usuario.

```python
database="tienda_python"
```

Base de datos que quieres usar.

```python
cursor = conexion.cursor()
```

El cursor es el objeto que envia instrucciones SQL a MySQL.

```python
cursor.execute("SELECT * FROM productos")
```

Ejecuta una consulta.

```python
productos = cursor.fetchall()
```

Trae todas las filas encontradas.

```python
for producto in productos:
    print(producto)
```

Recorre cada fila y la imprime.

```python
cursor.close()
conexion.close()
```

Cierra el cursor y la conexion.

## Insertar desde Python

Crea `mysql_insertar.py`:

```python
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_password",
    database="tienda_python"
)

cursor = conexion.cursor()

sql = "INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)"
valores = ("Monitor", 199.99, 5)

cursor.execute(sql, valores)
conexion.commit()

print("Producto guardado con id:", cursor.lastrowid)

cursor.close()
conexion.close()
```

Ejecuta:

```powershell
python mysql_insertar.py
```

Luego revisa en MySQL:

```sql
SELECT * FROM productos;
```

## Por que usamos `%s`

Esto es correcto:

```python
sql = "INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)"
valores = ("Monitor", 199.99, 5)
cursor.execute(sql, valores)
```

Esto evita errores y problemas de seguridad.

Esto no es recomendable:

```python
nombre = "Monitor"
sql = f"INSERT INTO productos (nombre) VALUES ('{nombre}')"
cursor.execute(sql)
```

Cuando un dato viene de un usuario, nunca lo pegues directamente dentro del SQL.

## Leer datos desde Python

Crea `mysql_listar.py`:

```python
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_password",
    database="tienda_python"
)

cursor = conexion.cursor()

cursor.execute("SELECT id, nombre, precio, stock FROM productos")

for id_producto, nombre, precio, stock in cursor.fetchall():
    print(f"{id_producto} - {nombre} - ${precio} - stock: {stock}")

cursor.close()
conexion.close()
```

## Buscar con filtros desde Python

Crea `mysql_buscar.py`:

```python
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_password",
    database="tienda_python"
)

cursor = conexion.cursor()

precio_minimo = 30

sql = "SELECT id, nombre, precio, stock FROM productos WHERE precio >= %s"
valores = (precio_minimo,)

cursor.execute(sql, valores)

for producto in cursor.fetchall():
    print(producto)

cursor.close()
conexion.close()
```

Nota importante:

```python
valores = (precio_minimo,)
```

La coma es necesaria porque Python necesita saber que eso es una tupla de un solo valor.

## Actualizar desde Python

Crea `mysql_actualizar.py`:

```python
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_password",
    database="tienda_python"
)

cursor = conexion.cursor()

sql = "UPDATE productos SET stock = %s WHERE id = %s"
valores = (20, 1)

cursor.execute(sql, valores)
conexion.commit()

print("Filas actualizadas:", cursor.rowcount)

cursor.close()
conexion.close()
```

`cursor.rowcount` dice cuantas filas fueron afectadas.

## Borrar desde Python

Crea `mysql_borrar.py`:

```python
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_password",
    database="tienda_python"
)

cursor = conexion.cursor()

sql = "DELETE FROM productos WHERE id = %s"
valores = (3,)

cursor.execute(sql, valores)
conexion.commit()

print("Filas borradas:", cursor.rowcount)

cursor.close()
conexion.close()
```

## Evitar repetir la conexion

Cuando empiezas, repetir el codigo esta bien para entender. Pero luego conviene crear una funcion.

Crea `db.py`:

```python
import mysql.connector


def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="tu_password",
        database="tienda_python"
    )
```

Ahora otro archivo puede importar esa funcion.

Crea `productos.py`:

```python
from db import obtener_conexion


def listar_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT id, nombre, precio, stock FROM productos")
    productos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return productos


for producto in listar_productos():
    print(producto)
```

Ejecuta:

```powershell
python productos.py
```

## Importar funciones entre archivos

Si tienes esto en `db.py`:

```python
def saludar():
    print("Hola desde db.py")
```

Puedes usarlo desde otro archivo asi:

```python
from db import saludar

saludar()
```

Eso se llama importar.

Con MySQL hacemos lo mismo:

```python
from db import obtener_conexion
```

Significa: "trae la funcion `obtener_conexion` desde el archivo `db.py`".

## Mini proyecto: inventario simple

Crea `inventario.py`:

```python
from db import obtener_conexion


def crear_producto(nombre, precio, stock):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = "INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)"
    valores = (nombre, precio, stock)

    cursor.execute(sql, valores)
    conexion.commit()

    nuevo_id = cursor.lastrowid

    cursor.close()
    conexion.close()

    return nuevo_id


def listar_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT id, nombre, precio, stock FROM productos ORDER BY id")
    productos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return productos


def actualizar_stock(id_producto, nuevo_stock):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = "UPDATE productos SET stock = %s WHERE id = %s"
    valores = (nuevo_stock, id_producto)

    cursor.execute(sql, valores)
    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    return filas


def borrar_producto(id_producto):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = "DELETE FROM productos WHERE id = %s"
    valores = (id_producto,)

    cursor.execute(sql, valores)
    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    return filas
```

Crea `main_inventario.py`:

```python
from inventario import (
    actualizar_stock,
    borrar_producto,
    crear_producto,
    listar_productos,
)


def mostrar_productos():
    productos = listar_productos()

    if not productos:
        print("No hay productos.")
        return

    for id_producto, nombre, precio, stock in productos:
        print(f"{id_producto}. {nombre} - ${precio} - stock: {stock}")


while True:
    print()
    print("1. Crear producto")
    print("2. Listar productos")
    print("3. Actualizar stock")
    print("4. Borrar producto")
    print("5. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))

        nuevo_id = crear_producto(nombre, precio, stock)
        print("Producto creado con id:", nuevo_id)

    elif opcion == "2":
        mostrar_productos()

    elif opcion == "3":
        id_producto = int(input("Id del producto: "))
        nuevo_stock = int(input("Nuevo stock: "))

        filas = actualizar_stock(id_producto, nuevo_stock)
        print("Filas actualizadas:", filas)

    elif opcion == "4":
        id_producto = int(input("Id del producto: "))

        filas = borrar_producto(id_producto)
        print("Filas borradas:", filas)

    elif opcion == "5":
        break

    else:
        print("Opcion invalida")
```

Ejecuta:

```powershell
python main_inventario.py
```

## Manejo basico de errores

A veces MySQL puede fallar porque:

- La contrasena esta mal.
- MySQL no esta encendido.
- La base de datos no existe.
- La tabla no existe.
- El SQL tiene un error.

Ejemplo con `try` y `except`:

```python
import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="tu_password",
        database="tienda_python"
    )

    print("Conexion exitosa")
    conexion.close()

except mysql.connector.Error as error:
    print("Error al conectar con MySQL:")
    print(error)
```

## Buenas practicas

- No escribas SQL con datos pegados usando f-strings.
- Usa `%s` y pasa los valores aparte.
- Cierra el cursor y la conexion.
- Usa `commit()` despues de `INSERT`, `UPDATE` y `DELETE`.
- Usa `WHERE` para actualizar o borrar datos especificos.
- No guardes contrasenas reales en GitHub.
- Para practicar localmente, usar `root` esta bien; para proyectos reales, crea un usuario con permisos limitados.

## Comandos SQL que debes practicar

```sql
CREATE DATABASE tienda_python;
USE tienda_python;
SHOW DATABASES;
SHOW TABLES;
DESCRIBE productos;
INSERT INTO productos (nombre, precio, stock) VALUES ('Cable USB', 8.99, 30);
SELECT * FROM productos;
SELECT * FROM productos WHERE precio > 10;
UPDATE productos SET stock = 50 WHERE id = 1;
DELETE FROM productos WHERE id = 1;
```

## Ejercicios

1. Crea una base de datos llamada `escuela_python`.
2. Crea una tabla `estudiantes` con `id`, `nombre`, `edad` y `nota`.
3. Inserta 3 estudiantes desde MySQL.
4. Consulta todos los estudiantes.
5. Consulta solo los estudiantes con nota mayor o igual a 70.
6. Cambia la nota de un estudiante usando `UPDATE`.
7. Borra un estudiante usando `DELETE`.
8. Haz un archivo Python que liste todos los estudiantes.
9. Haz un archivo Python que inserte un estudiante.
10. Haz un mini menu en Python para crear, listar, actualizar y borrar estudiantes.

## Reto recomendado

Crea un proyecto llamado `proyectos/04_inventario_mysql.py`.

Debe permitir:

- Agregar productos.
- Listar productos.
- Buscar productos por nombre.
- Actualizar precio.
- Actualizar stock.
- Borrar productos.

Empieza simple. Primero haz que conecte. Luego que liste. Luego agrega una funcion a la vez.

