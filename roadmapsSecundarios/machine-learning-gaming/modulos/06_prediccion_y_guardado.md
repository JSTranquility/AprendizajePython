# 06 - Prediccion y guardado

Despues de entrenar, guardamos el modelo para reutilizarlo.

## Guardar

```python
import joblib

joblib.dump(modelo, "modelos/modelo_engagement.joblib")
```

## Cargar

```python
modelo = joblib.load("modelos/modelo_engagement.joblib")
```

## Predecir

El nuevo dato debe tener las mismas columnas usadas para entrenar.

```python
prediccion = modelo.predict(nuevo_jugador)
```

## Regla importante

No entrenes el modelo cada vez que quieras predecir. Entrenas una vez, guardas el modelo y luego lo cargas para hacer predicciones.

