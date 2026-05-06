# Curso Completo de Python

Este curso esta pensado para aprender Python desde cero hasta un nivel practico: escribir programas, resolver problemas, organizar proyectos, leer archivos, manejar errores, crear pruebas, usar APIs, trabajar con bases de datos y construir proyectos pequenos.

## Como usar este curso

1. Lee los modulos en orden dentro de `modulos/`.
2. Ejecuta todos los ejemplos en tu terminal.
3. Resuelve los ejercicios de `ejercicios/` sin mirar soluciones primero.
4. Construye los proyectos de `proyectos/`.
5. Cuando algo falle, lee el error completo. Python suele decir exactamente donde esta el problema.

## Comandos basicos

Ver version:

```powershell
python --version
```

Si Windows responde que no tiene acceso a `python.exe` o abre Microsoft Store, instala Python desde https://www.python.org/downloads/ y marca la opcion "Add python.exe to PATH". Tambien puedes desactivar los alias de Microsoft Store en:

```text
Configuracion -> Aplicaciones -> Configuracion avanzada de aplicaciones -> Alias de ejecucion de aplicaciones
```

Desactiva los alias de `python.exe` y `python3.exe`, cierra la terminal y abre una nueva.

Ejecutar un archivo:

```powershell
python ejercicios/01_fundamentos.py
```

Abrir consola interactiva:

```powershell
python
```

## Ruta recomendada

### Etapa 1: Fundamentos

- `modulos/01_introduccion.md`
- `modulos/02_variables_tipos.md`
- `modulos/03_control_flujo.md`
- `modulos/04_funciones.md`
- `ejercicios/01_fundamentos.py`

### Etapa 2: Estructuras y problemas

- `modulos/05_colecciones.md`
- `modulos/06_strings_archivos.md`
- `ejercicios/02_colecciones.py`

### Etapa 3: Programas reales

- `modulos/07_errores_modulos.md`
- `modulos/08_poo.md`
- `proyectos/01_calculadora_cli.py`
- `proyectos/02_gestor_tareas.py`

### Etapa 4: Calidad y datos

- `modulos/09_pruebas.md`
- `modulos/10_json_csv_sqlite.md`
- `proyectos/03_control_gastos.py`

### Etapa 5: Nivel siguiente

- `modulos/11_apis_entornos_paquetes.md`
- `modulos/12_siguiente_nivel.md`
- `modulos/13_mysql_python.md`
- `modulos/14_sqlite_python.md`

## Habitos importantes

- Escribe codigo todos los dias, aunque sean 20 minutos.
- No copies ejemplos sin ejecutarlos.
- Cambia los valores y rompe el programa a proposito para entenderlo.
- Usa nombres claros: `precio_total` es mejor que `x`.
- Divide problemas grandes en funciones pequenas.

## Objetivo final

Al terminar, debes poder crear programas de consola, automatizaciones simples, proyectos organizados, pruebas basicas, lectura/escritura de datos y estar preparado para aprender frameworks como Flask, FastAPI, Django, pandas o automatizacion web.
