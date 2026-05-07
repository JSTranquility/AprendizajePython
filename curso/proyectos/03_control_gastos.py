"""
Control de gastos con SQLite.

Ejecuta:
    python curso/proyectos/03_control_gastos.py
"""

import sqlite3
from pathlib import Path


RUTA_DB = Path(__file__).with_name("gastos.db")


def conectar():
    return sqlite3.connect(RUTA_DB)


def crear_tabla():
    with conectar() as conexion:
        conexion.execute("""
            CREATE TABLE IF NOT EXISTS gastos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descripcion TEXT NOT NULL,
                categoria TEXT NOT NULL,
                monto REAL NOT NULL
            )
        """)


def agregar_gasto(descripcion, categoria, monto):
    with conectar() as conexion:
        conexion.execute(
            "INSERT INTO gastos (descripcion, categoria, monto) VALUES (?, ?, ?)",
            (descripcion, categoria, monto),
        )


def listar_gastos():
    with conectar() as conexion:
        cursor = conexion.execute(
            "SELECT id, descripcion, categoria, monto FROM gastos ORDER BY id DESC"
        )
        return cursor.fetchall()


def total_por_categoria():
    with conectar() as conexion:
        cursor = conexion.execute("""
            SELECT categoria, SUM(monto)
            FROM gastos
            GROUP BY categoria
            ORDER BY SUM(monto) DESC
        """)
        return cursor.fetchall()


def pedir_monto():
    while True:
        try:
            monto = float(input("Monto: "))
        except ValueError:
            print("Escribe un monto valido.")
            continue

        if monto <= 0:
            print("El monto debe ser positivo.")
            continue

        return monto


def opcion_agregar():
    descripcion = input("Descripcion: ").strip()
    categoria = input("Categoria: ").strip()

    if not descripcion or not categoria:
        print("Descripcion y categoria son obligatorias.")
        return

    monto = pedir_monto()
    agregar_gasto(descripcion, categoria, monto)
    print("Gasto guardado.")


def opcion_listar():
    gastos = listar_gastos()

    if not gastos:
        print("No hay gastos.")
        return

    for gasto_id, descripcion, categoria, monto in gastos:
        print(f"{gasto_id}. {descripcion} | {categoria} | {monto:.2f}")


def opcion_resumen():
    resumen = total_por_categoria()

    if not resumen:
        print("No hay gastos.")
        return

    for categoria, total in resumen:
        print(f"{categoria}: {total:.2f}")


def mostrar_menu():
    print("\nControl de gastos")
    print("1. Agregar gasto")
    print("2. Listar gastos")
    print("3. Total por categoria")
    print("4. Salir")


def main():
    crear_tabla()

    while True:
        mostrar_menu()
        opcion = input("Opcion: ").strip()

        if opcion == "1":
            opcion_agregar()
        elif opcion == "2":
            opcion_listar()
        elif opcion == "3":
            opcion_resumen()
        elif opcion == "4":
            break
        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    main()
