# 03 - Preprocesamiento

Los modelos de scikit-learn necesitan datos numericos. Si una columna tiene texto, hay que convertirla.

## Columnas numericas

Ejemplos:

- `Age`
- `PlayTimeHours`
- `SessionsPerWeek`
- `AvgSessionDurationMinutes`
- `PlayerLevel`
- `AchievementsUnlocked`

Estas columnas pueden escalarse con `StandardScaler`.

## Columnas categoricas

Ejemplos:

- `Gender`
- `Location`
- `GameGenre`
- `GameDifficulty`

Estas columnas se convierten con `OneHotEncoder`.

## Pipeline

Un pipeline une pasos:

```text
preprocesamiento -> modelo
```

Ventaja: evita repetir transformaciones manuales y reduce errores.

## ColumnTransformer

Permite aplicar transformaciones distintas por tipo de columna:

- Numericas: imputar y escalar.
- Categoricas: imputar y one-hot encoding.

