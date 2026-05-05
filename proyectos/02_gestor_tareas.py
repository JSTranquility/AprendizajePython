"""
Gestor de tareas con archivo JSON.

Ejecuta:
    python proyectos/02_gestor_tareas.py
"""

import json
from pathlib import Path


RUTA_DATOS = Path(__file__).with_name("tareas.json")


def cargar_tareas():
    if not RUTA_DATOS.exists():
        return []

    with open(RUTA_DATOS, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_tareas(tareas):
    with open(RUTA_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, indent=2)


def listar_tareas(tareas):
    if not tareas:
        print("No hay tareas.")
        return

    for indice, tarea in enumerate(tareas, start=1):
        estado = "x" if tarea["completada"] else " "
        print(f"{indice}. [{estado}] {tarea['titulo']}")


def agregar_tarea(tareas):
    titulo = input("Titulo: ").strip()
    if not titulo:
        print("El titulo no puede estar vacio.")
        return

    tareas.append({"titulo": titulo, "completada": False})
    guardar_tareas(tareas)
    print("Tarea agregada.")


def completar_tarea(tareas):
    listar_tareas(tareas)
    if not tareas:
        return

    try:
        indice = int(input("Numero de tarea: ")) - 1
        tareas[indice]["completada"] = True
    except (ValueError, IndexError):
        print("Numero invalido.")
        return

    guardar_tareas(tareas)
    print("Tarea completada.")


def eliminar_tarea(tareas):
    listar_tareas(tareas)
    if not tareas:
        return

    try:
        indice = int(input("Numero de tarea: ")) - 1
        tareas.pop(indice)
    except (ValueError, IndexError):
        print("Numero invalido.")
        return

    guardar_tareas(tareas)
    print("Tarea eliminada.")


def mostrar_menu():
    print("\nGestor de tareas")
    print("1. Listar")
    print("2. Agregar")
    print("3. Completar")
    print("4. Eliminar")
    print("5. Salir")


def main():
    tareas = cargar_tareas()

    while True:
        mostrar_menu()
        opcion = input("Opcion: ").strip()

        if opcion == "1":
            listar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            break
        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    main()

