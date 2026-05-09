from datos import USUARIOS


MENU_RESTAURANTE = {
    1: "Pizza",
    2: "Hamburguesa",
    3: "Ensalada",
    4: "Pasta",
}

pedidos_por_usuario = {}


def menu_restaurante(nombre_usuario):
    while True:
        print("\nBienvenido a nuestro restaurante.")
        print("Por favor, elige un plato del menu:")

        for opcion, plato in MENU_RESTAURANTE.items():
            print(f"{opcion}. {plato}")

        try:
            opcion = int(input("Opcion: "))
        except ValueError:
            print("Debes ingresar un numero.")
            continue

        if opcion not in MENU_RESTAURANTE:
            print("Opcion no valida.")
            continue

        plato = MENU_RESTAURANTE[opcion]
        pedidos_por_usuario.setdefault(nombre_usuario, []).append(plato)
        print(f"\n{nombre_usuario} eligio {plato}")

        respuesta = input("Deseas seleccionar otro plato? (si/no): ").strip().lower()
        if respuesta != "si":
            print("\nPedido guardado:")
            print(pedidos_por_usuario[nombre_usuario])
            break


def verificar_usuario():
    print("Bienvenido a nuestra app.")

    nombre_usuario = input("Ingresa tu nombre: ")

    for usuario in USUARIOS:
        if usuario["nombre"].lower() == nombre_usuario.lower():
            print("Usuario verificado.")
            menu(nombre_usuario)
            return

    print("Usuario no reconocido.")
    respuesta = input("Deseas registrarte? (si/no): ").strip().lower()

    if respuesta != "si":
        print("Registro cancelado.")
        return

    try:
        edad = int(input("Ingresa tu edad: "))
    except ValueError:
        print("Edad invalida. Debes escribir un numero.")
        return

    USUARIOS.append({"nombre": nombre_usuario, "edad": edad})
    print("Usuario registrado.")
    menu(nombre_usuario)


def menu(nombre_usuario):
    while True:
        print("\n--- MENU ---")
        print("1. Perfil")
        print("2. Configuracion")
        print("3. Menu restaurante")
        print("4. Ver pedido")
        print("5. Salir")

        try:
            opcion = int(input("Opcion: "))
        except ValueError:
            print("Debes ingresar un numero valido.")
            continue

        if opcion == 1:
            print(f"\nPerfil de {nombre_usuario}")
        elif opcion == 2:
            print("\nConfiguracion...")
        elif opcion == 3:
            menu_restaurante(nombre_usuario)
        elif opcion == 4:
            if nombre_usuario in pedidos_por_usuario:
                print(f"\nTu pedido es: {pedidos_por_usuario[nombre_usuario]}")
            else:
                print("\nNo has realizado ningun pedido.")
        elif opcion == 5:
            print("\nSaliendo...")
            break
        else:
            print("Opcion no valida.")
