# 10 - JSON, CSV y SQLite

## JSON

JSON sirve para guardar datos estructurados.

```python
import json

datos = {"nombre": "Ana", "edad": 25}

with open("persona.json", "w", encoding="utf-8") as archivo:
    json.dump(datos, archivo, indent=2)
```

```python
with open("persona.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)
```

## CSV

CSV sirve para tablas simples.

```python
import csv

with open("productos.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["nombre", "precio"])
    escritor.writerow(["teclado", 45.99])
```

## SQLite

SQLite es una base de datos incluida con Python.

```python
import sqlite3

conexion = sqlite3.connect("app.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tareas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    completada INTEGER NOT NULL DEFAULT 0
)
""")

conexion.commit()
conexion.close()
```

## Cuando usar cada uno

- JSON: configuraciones, listas pequenas, intercambio con APIs.
- CSV: datos tabulares simples.
- SQLite: datos con consultas, relaciones o crecimiento.

