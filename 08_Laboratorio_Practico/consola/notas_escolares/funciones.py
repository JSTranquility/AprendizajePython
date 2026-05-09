def calcular_promedio(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)


def calcular_nota_final(notas, ponderaciones):
    if len(notas) != len(ponderaciones):
        raise ValueError("La cantidad de notas y ponderaciones debe ser la misma.")

    nota_final = 0
    for nota, ponderacion in zip(notas, ponderaciones):
        nota_final += nota * ponderacion

    return nota_final


def calcular_calificacion(nota_final):
    if nota_final >= 90:
        return "A"
    if nota_final >= 80:
        return "B"
    if nota_final >= 70:
        return "C"
    if nota_final >= 60:
        return "D"
    return "F"


def calcular_promedio_general(estudiantes):
    notas = [estudiante["nota"] for estudiante in estudiantes]
    return calcular_promedio(notas)


def listar_estudiantes(estudiantes):
    print("\n--- LISTA DE ESTUDIANTES ---")

    for estudiante in estudiantes:
        print(
            f"{estudiante['nombre']} - Nota: {estudiante['nota']} - "
            f"Calificacion: {calcular_calificacion(estudiante['nota'])}"
        )


def buscar_estudiante(estudiantes, nombre):
    encontrados = []

    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():
            encontrados.append(estudiante)

    return encontrados


def agregar_estudiante(estudiantes, nombre, nota):
    estudiantes.append({"nombre": nombre, "nota": nota})
    print("Estudiante agregado correctamente.")
