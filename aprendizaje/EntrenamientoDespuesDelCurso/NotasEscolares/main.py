from funciones import (
    CalcularPromedio,
    CalcularNotaFinal,
    CalcularNota,
    CalcularPromedioGeneral,
    listar_estudiantes,
    buscar_estudiante,
    agregar_estudiante
)

from estudiantes import estudiantes


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
            opcion = int(input("Elige una opción: "))

            if opcion == 1:
                listar_estudiantes(estudiantes)

            elif opcion == 2:
                nombre = input("Ingresa el nombre del estudiante: ")
                resultados = buscar_estudiante(estudiantes, nombre)

                if resultados:
                    print("\nEstudiantes encontrados:")
                    for estudiante in resultados:
                        print(f"{estudiante['nombre']} - Nota: {estudiante['nota']} - Calificación: {CalcularNota(estudiante['nota'])}")
                else:
                    print("No se encontró ese estudiante.")

            elif opcion == 3:
                promedio_general = CalcularPromedioGeneral(estudiantes)
                print(f"\nEl promedio general es: {promedio_general:.2f}")

            elif opcion == 4:
                notas_input = input("Ingresa notas separadas por comas: ")

                try:
                    notas = [float(nota.strip()) for nota in notas_input.split(",")]
                    promedio = CalcularPromedio(notas)
                    print(f"El promedio es: {promedio:.2f}")
                    print(f"Calificación: {CalcularNota(promedio)}")

                except ValueError:
                    print("Debes ingresar solo números separados por comas.")

            elif opcion == 5:
                notas_input = input("Ingresa notas separadas por comas: ")
                ponderaciones_input = input("Ingresa ponderaciones separadas por comas. Ejemplo: 0.3,0.4,0.3: ")

                try:
                    notas = [float(nota.strip()) for nota in notas_input.split(",")]
                    ponderaciones = [float(p.strip()) for p in ponderaciones_input.split(",")]

                    if len(notas) != len(ponderaciones):
                        print("La cantidad de notas y ponderaciones debe ser igual.")
                    else:
                        nota_final = CalcularNotaFinal(notas, ponderaciones)
                        print(f"Nota final: {nota_final:.2f}")
                        print(f"Calificación: {CalcularNota(nota_final)}")

                except ValueError:
                    print("Debes ingresar solo números separados por comas.")

            elif opcion == 6:
                nombre = input("Nombre del estudiante: ")

                try:
                    nota = float(input("Nota del estudiante: "))
                    agregar_estudiante(estudiantes, nombre, nota)

                except ValueError:
                    print("La nota debe ser un número.")

            elif opcion == 7:
                print("Saliendo del sistema...")
                break

            else:
                print("Opción no válida.")

        except ValueError:
            print("Debes ingresar un número válido.")


if __name__ == "__main__":
    main()