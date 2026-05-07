# 01 - Idea general de Machine Learning

Machine Learning consiste en entrenar un programa para encontrar patrones en datos y hacer predicciones.

En este modulo haremos clasificacion:

> Dado el comportamiento de un jugador, predecir su nivel de engagement.

## Conceptos basicos

- Dataset: tabla de datos.
- Fila: un ejemplo individual.
- Columna: una variable.
- Feature: dato usado para predecir.
- Target: valor que queremos predecir.
- Modelo: algoritmo entrenado.
- Entrenamiento: proceso donde el modelo aprende patrones.
- Evaluacion: medir que tan bien predice.

## Flujo completo

```text
datos -> limpieza -> features/target -> train/test -> modelo -> evaluacion -> prediccion
```

## Clasificacion

Clasificacion significa predecir una categoria.

Ejemplos:

- Bajo, medio o alto engagement.
- Cliente compra o no compra.
- Email spam o no spam.
- Juego recomendado o no recomendado.

## Error comun

No debes evaluar el modelo con los mismos datos que usaste para entrenar. Por eso separamos:

- Datos de entrenamiento.
- Datos de prueba.

