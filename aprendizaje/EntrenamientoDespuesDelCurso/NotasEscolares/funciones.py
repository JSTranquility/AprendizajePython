def CalcularPromedio(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

def CalcularNotaFinal(notas, ponderaciones):
    if len(notas) != len(ponderaciones):
        raise ValueError("La cantidad de notas y ponderaciones debe ser la misma.")
    
    nota_final = 0
    for nota, ponderacion in zip(notas, ponderaciones):
        nota_final += nota * ponderacion
    
    return nota_final

def CalcularNota(nota_final):
    if nota_final >= 90:
        return 'A'
    elif nota_final >= 80:
        return 'B'
    elif nota_final >= 70:
        return 'C'
    elif nota_final >= 60:
        return 'D'
    else:
        return 'F'
    
def CalcularPromedioGeneral(estudiantes):
    notas = [estudiante["nota"] for estudiante in estudiantes]
    return CalcularPromedio(notas)

def listar_estudiantes(estudiantes):
    print("\n--- LISTA DE ESTUDIANTES ---")

    for estudiante in estudiantes:
        print(f"{estudiante['nombre']} - Nota: {estudiante['nota']} - Calificación: {CalcularNota(estudiante['nota'])}")


def buscar_estudiante(estudiantes, nombre):
    encontrados = []

    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():
            encontrados.append(estudiante)

    return encontrados


def agregar_estudiante(estudiantes, nombre, nota):
    nuevo_estudiante = {
        "nombre": nombre,
        "nota": nota
    }

    estudiantes.append(nuevo_estudiante)
    print("Estudiante agregado correctamente.")