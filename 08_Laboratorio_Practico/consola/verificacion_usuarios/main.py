from usuarios import GestorUsuarios


def main():
    gestor = GestorUsuarios()

    while True:
        print("\n1. Registrar")
        print("2. Buscar")
        print("3. Listar")
        print("4. Salir")

        try:
            opcion = int(input("Opcion: "))

            if opcion == 1:
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                gestor.registrar(nombre, edad)
            elif opcion == 2:
                nombre = input("Nombre a buscar: ")
                usuario = gestor.buscar(nombre)

                if usuario:
                    print(
                        f"Usuario encontrado: {usuario['nombre']} - "
                        f"{usuario['edad']} anos"
                    )
                else:
                    print("No encontrado")
            elif opcion == 3:
                gestor.listar()
            elif opcion == 4:
                break
            else:
                print("Opcion invalida")

        except ValueError:
            print("Entrada invalida")


if __name__ == "__main__":
    main()
