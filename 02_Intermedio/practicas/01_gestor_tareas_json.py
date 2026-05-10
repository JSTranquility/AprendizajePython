# Desafio Intermedio 1: Gestor de Tareas con POO y JSON

# Consigna:
# Crea una pequena aplicacion en consola para registrar tareas.

# Requisitos:
# 1. Usa una clase Tarea para representar cada tarea.
# 2. Usa una clase GestorTareas para agregar, listar y completar tareas.
# 3. Guarda las tareas en un archivo JSON para no perder la informacion.
# 4. Maneja errores comunes con try/except.
# 5. Muestra un menu para que el usuario practique varias opciones.

# --- ESCRIBE TU CODIGO ABAJO ---

import json 

class Tarea:
    def __init__(self, titulo, descripcion, estado="pendiente"):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

    def __dict__(self):
        return {
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "estado": self.estado
        }

class GestorTareas:
    def __init__(self, archivo_json):
        self.archivo_json = archivo_json
        self.tareas = []
        self.cargar_tareas()

    def cargar_tareas(self):
        try:
            with open(self.archivo_json, 'r') as f:
                datos = json.load(f)
                self.tareas = [Tarea(**t) for t in datos]
        except FileNotFoundError:
            self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        self.guardar_tareas()

    def guardar_tareas(self):
        with open(self.archivo_json, 'w') as f:
            json.dump([t.__dict__() for t in self.tareas], f, indent=4)
    
    def listar_tareas(self):
        if not self.tareas:
            print("No hay tareas pendientes.")
            return
        for i, tarea in enumerate(self.tareas):
            print(f"{i+1}. {tarea.titulo} - {tarea.estado}")
    
    def completar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].estado = "completada"
            self.guardar_tareas()
            print("Tarea completada.")
        else:
            print("Indice de tarea invalido.")
    
    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas.pop(indice)
            self.guardar_tareas()
            print("Tarea eliminada.")
        else:
            print("Indice de tarea invalido.")

    
    def menu(self):
        while True:
            print("\n--- Gestor de Tareas ---")
            print("1. Agregar tarea")
            print("2. Listar tareas")
            print("3. Completar tarea")
            print("4. Eliminar tarea")
            print("5. Salir")
            opcion = input("Seleccione una opcion: ")
            if opcion == "1":
                titulo = input("Ingrese el titulo de la tarea: ")
                descripcion = input("Ingrese la descripcion de la tarea: ")
                self.agregar_tarea(Tarea(titulo, descripcion))
            elif opcion == "2":
                self.listar_tareas()
            elif opcion == "3":
                indice = int(input("Ingrese el indice de la tarea a completar: ")) - 1
                self.completar_tarea(indice)
            elif opcion == "4":
                indice = int(input("Ingrese el indice de la tarea a eliminar: ")) - 1
                self.eliminar_tarea(indice)
            elif opcion == "5":
                break
            else:
                print("Opcion invalida.")
    
    def run(self):
        self.menu()

if __name__ == "__main__":
    gestor = GestorTareas("tareas.json")
    gestor.run()