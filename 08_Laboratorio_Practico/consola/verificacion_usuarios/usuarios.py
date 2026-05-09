USUARIOS_INICIALES = [
    {"nombre": "Juan", "edad": 25},
    {"nombre": "Maria", "edad": 30},
    {"nombre": "Pedro", "edad": 22},
]


class GestorUsuarios:
    def __init__(self):
        self.usuarios = list(USUARIOS_INICIALES)

    def registrar(self, nombre, edad):
        if self.buscar(nombre):
            print("El usuario ya existe.")
            return

        self.usuarios.append({"nombre": nombre, "edad": edad})
        print("Usuario registrado.")

    def buscar(self, nombre):
        for usuario in self.usuarios:
            if usuario["nombre"].lower() == nombre.lower():
                return usuario
        return None

    def listar(self):
        if not self.usuarios:
            print("No hay usuarios.")
            return

        for usuario in self.usuarios:
            print(f"{usuario['nombre']} - {usuario['edad']} anos")
