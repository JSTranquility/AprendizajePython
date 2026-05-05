usuarios = [
    {"nombre": "Juan", "edad": 25},
    {"nombre": "Maria", "edad": 30},
    {"nombre": "Pedro", "edad": 22},
    {"nombre": "Ana", "edad": 28},
    {"nombre": "Luis", "edad": 35}
]

class GestorUsuarios:
    def __init__(self):
        self.usuarios = usuarios  

    def registrar(self, nombre, edad):
        if self.buscar(nombre):
            print("El usuario ya existe.")
            return

        nuevo = {"nombre": nombre, "edad": edad}
        self.usuarios.append(nuevo)
        print("Usuario registrado.")

    def buscar(self, nombre):
        for usuario in self.usuarios:
            if usuario["nombre"] == nombre:
                return usuario
        return None

    def listar(self):
        if not self.usuarios:
            print("No hay usuarios.")
            return

        for u in self.usuarios:
            print(f"{u['nombre']} - {u['edad']} años")