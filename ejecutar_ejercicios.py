"""
Ejecuta los ejercicios automaticos del curso.

Uso:
    python ejecutar_ejercicios.py
"""

import subprocess
import sys
from pathlib import Path


EJERCICIOS = [
    Path("ejercicios/01_fundamentos.py"),
    Path("ejercicios/02_colecciones.py"),
    Path("ejercicios/03_funciones_poo.py"),
]


def main():
    errores = 0

    for ejercicio in EJERCICIOS:
        print(f"\nEjecutando {ejercicio}...")
        resultado = subprocess.run(
            [sys.executable, str(ejercicio)],
            check=False,
            text=True,
            capture_output=True,
        )

        if resultado.stdout:
            print(resultado.stdout.strip())

        if resultado.stderr:
            print(resultado.stderr.strip())

        if resultado.returncode != 0:
            errores += 1

    if errores:
        print(f"\n{errores} archivo(s) fallaron.")
        sys.exit(1)

    print("\nTodos los ejercicios pasaron.")


if __name__ == "__main__":
    main()

