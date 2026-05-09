# 05 - Evaluacion

Evaluar significa medir que tan bien predice el modelo con datos que no vio durante entrenamiento.

## Accuracy

Porcentaje de predicciones correctas.

```python
accuracy = modelo.score(X_test, y_test)
```

## Classification report

Muestra precision, recall y f1-score por clase.

```python
from sklearn.metrics import classification_report

print(classification_report(y_test, predicciones))
```

## Matriz de confusion

Muestra donde se equivoca el modelo.

```python
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, predicciones))
```

## Interpretacion

Si el modelo acierta mucho en una clase pero falla en otra, puede haber:

- Datos desbalanceados.
- Features insuficientes.
- Categorias dificiles de separar.
- Ruido en los datos.

