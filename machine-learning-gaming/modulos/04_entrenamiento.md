# 04 - Entrenamiento

El entrenamiento usa datos historicos para ajustar un modelo.

## Separacion train/test

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)
```

## Modelo elegido

Usaremos `RandomForestClassifier`.

Ventajas:

- Funciona bien como primer modelo.
- Maneja relaciones no lineales.
- Requiere poca configuracion inicial.
- Es robusto para muchos datasets tabulares.

## No busques perfeccion al inicio

Primero crea una base funcional. Luego mejoras:

- Mas limpieza.
- Mas features.
- Ajuste de hiperparametros.
- Comparacion con otros modelos.

