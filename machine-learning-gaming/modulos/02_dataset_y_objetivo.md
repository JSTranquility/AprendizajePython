# 02 - Dataset y objetivo fijo

Dataset:

```text
rabieelkharoua/predict-online-gaming-behavior-dataset
```

Objetivo del proyecto:

```text
Predecir EngagementLevel
```

Si el dataset cambia de nombre de columna, los scripts imprimen las columnas disponibles para que puedas ajustar el objetivo.

## Posibles columnas del dataset

Este dataset normalmente contiene informacion como:

- Edad.
- Genero.
- Ubicacion.
- Genero de juego.
- Tiempo de juego.
- Compras dentro del juego.
- Dificultad.
- Sesiones por semana.
- Duracion promedio de sesion.
- Nivel del jugador.
- Logros desbloqueados.
- Nivel de engagement.

## Features y target

Target:

```python
y = df["EngagementLevel"]
```

Features:

```python
X = df.drop(columns=["EngagementLevel"])
```

Si existe una columna identificadora como `PlayerID`, no debe usarse para entrenar porque identifica una fila, no explica comportamiento.

