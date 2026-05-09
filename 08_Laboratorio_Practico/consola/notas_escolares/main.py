from estudiantes import estudiantes
from funciones import agregar_estudiante
from funciones import buscar_estudiante
from funciones import calcular_calificacion
from funciones import calcular_nota_final
from funciones import calcular_promedio
from funciones import calcular_promedio_general
from funciones import listar_estudiantes


def main():
    while True:
        print("\n===== SISTEMA DE NOTAS ESCOLARES =====")
        print("1. Listar estudiantes")
        print("2. Buscar estudiante")
        print("3. Ver promedio general")
        print("4. Calcular promedio manual")
        print("5. Calcular nota final con ponderaciones")
        print("6. Agregar estudiante")
        print("7. Salir")

        try:
            opcion = int(input("Elige una opcion: "))
        except ValueError:
            print("Debes ingresar un numero valido.")
            continue

        if opcion == 1:
            listar_estudiantes(estudiantes)
        elif opcion == 2:
            nombre = input("Ingresa el nombre del estudiante: ")
            resultados = buscar_estudiante(estudiantes, nombre)

            if resultados:
                print("\nEstudiantes encontrados:")
                for estudiante in resultados:
                    print(
                        f"{estudiante['nombre']} - Nota: {estudiante['nota']} - "
                        f"Calificacion: {calcular_calificacion(estudiante['nota'])}"
                    )
            else:
                print("No se encontro ese estudiante.")
        elif opcion == 3:
            promedio_general = calcular_promedio_general(estudiantes)
            print(f"\nEl promedio general es: {promedio_general:.2f}")
        elif opcion == 4:
            notas_input = input("Ingresa notas separadas por comas: ")

            try:
                notas = [float(nota.strip()) for nota in notas_input.split(",")]
            except ValueError:
                print("Debes ingresar solo numeros separados por comas.")
                continue

            promedio = calcular_promedio(notas)
            print(f"El promedio es: {promedio:.2f}")
            print(f"Calificacion: {calcular_calificacion(promedio)}")
        elif opcion == 5:
            notas_input = input("Ingresa notas separadas por comas: ")
            ponderaciones_input = input(
                "Ingresa ponderaciones separadas por comas. Ejemplo: 0.3,0.4,0.3: "
            )

            try:
                notas = [float(nota.strip()) for nota in notas_input.split(",")]
                ponderaciones = [
                    float(ponderacion.strip())
                    for ponderacion in ponderaciones_input.split(",")
                ]
            except ValueError:
                print("Debes ingresar solo numeros separados por comas.")
                continue

            if len(notas) != len(ponderaciones):
                print("La cantidad de notas y ponderaciones debe ser igual.")
                continue

            nota_final = calcular_nota_final(notas, ponderaciones)
            print(f"Nota final: {nota_final:.2f}")
            print(f"Calificacion: {calcular_calificacion(nota_final)}")
        elif opcion == 6:
            nombre = input("Nombre del estudiante: ")

            try:
                nota = float(input("Nota del estudiante: "))
            except ValueError:
                print("La nota debe ser un numero.")
                continue

            agregar_estudiante(estudiantes, nombre, nota)
        elif opcion == 7:
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
