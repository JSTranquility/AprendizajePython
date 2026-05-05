from datos import usuarios

menu_restaurante_dict = {
    1: "Pizza",
    2: "Hamburguesa",
    3: "Ensalada",
    4: "Pasta"
}

eleccion_usuario = {}


def menu_restaurante(nombre_usuario):
    while True:
        print("\nBienvenido a nuestro restaurante!")
        print("Por favor, elige un plato del menú:")

        for key, value in menu_restaurante_dict.items():
            print(f"{key}. {value}")

        try:
            opcion = int(input("Opción: "))

            if opcion in menu_restaurante_dict:
                plato = menu_restaurante_dict[opcion]

                if nombre_usuario not in eleccion_usuario:
                    eleccion_usuario[nombre_usuario] = []

                eleccion_usuario[nombre_usuario].append(plato)

                print(f"\n{nombre_usuario} eligió {plato}")

                respuesta = input("¿Deseas seleccionar otro plato? (si/no): ")

                if respuesta.lower() == "si":
                    continue
                else:
                    print("\nPedido guardado:")
                    print(eleccion_usuario)
                    break

            else:
                print("Opción no válida.")

        except ValueError:
            print("Debes ingresar un número.")


def verificar_usuario():
    print("Bienvenido a nuestra App!")

    nombre_usuario = input("Ingresa tu nombre: ")

    for usuario in usuarios:
        if usuario["nombre"].lower() == nombre_usuario.lower():
            print("Usuario verificado.")
            menu(nombre_usuario)
            return

    print("Usuario no reconocido.")

    respuesta = input("¿Deseas registrarte? (si/no): ")

    if respuesta.lower() == "si":
        try:
            edad = int(input("Ingresa tu edad: "))

            nuevo_usuario = {
                "nombre": nombre_usuario,
                "edad": edad
            }

            usuarios.append(nuevo_usuario)

            print("Usuario registrado.")
            menu(nombre_usuario)

        except ValueError:
            print("Edad inválida. Debes escribir un número.")
    else:
        print("Registro cancelado.")


def menu(nombre_usuario):
    while True:
        print("\n--- MENÚ ---")
        print("1. Perfil")
        print("2. Configuración")
        print("3. Menú Restaurante")
        print("4. Ver Pedido")
        print("5. Salir")

        try:
            opcion = int(input("Opción: "))

            if opcion == 1:
                print(f"\nPerfil de {nombre_usuario}")

            elif opcion == 2:
                print("\nConfiguración...")

            elif opcion == 3:
                menu_restaurante(nombre_usuario)

            elif opcion == 4:
                if nombre_usuario in eleccion_usuario:
                    print(f"\nTu pedido es: {eleccion_usuario[nombre_usuario]}")
                else:
                    print("\nNo has realizado ningún pedido.")

            elif opcion == 5:
                print("\nSaliendo...")
                break

            else:
                print("Opción no válida.")

        except ValueError:
            print("Debes ingresar un número válido.")