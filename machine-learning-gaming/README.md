# Modulo Fijo de Machine Learning

Este modulo ensena Machine Learning con una sola meta fija:

> Predecir el nivel de engagement de jugadores online usando el dataset `rabieelkharoua/predict-online-gaming-behavior-dataset`.

El objetivo no es aprender mil modelos a la vez. El objetivo es dominar el flujo completo de un proyecto real:

1. Descargar datos.
2. Explorar columnas.
3. Limpiar datos.
4. Separar variables de entrada y objetivo.
5. Entrenar un modelo.
6. Evaluar resultados.
7. Guardar el modelo.
8. Usar el modelo para predecir.

## Dataset

Usaremos KaggleHub:

```python
import kagglehub

path = kagglehub.dataset_download("rabieelkharoua/predict-online-gaming-behavior-dataset")
print("Path to dataset files:", path)
```

## Instalacion

Desde esta carpeta:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Si `python` no funciona en Windows, revisa el README principal del curso para corregir los alias de Microsoft Store.

## Orden de estudio

1. `modulos/01_idea_general.md`
2. `modulos/02_dataset_y_objetivo.md`
3. `modulos/03_preprocesamiento.md`
4. `modulos/04_entrenamiento.md`
5. `modulos/05_evaluacion.md`
6. `modulos/06_prediccion_y_guardado.md`

## Comandos del proyecto

Descargar y ver datos:

```powershell
python proyecto/01_descargar_y_explorar.py
```

Entrenar modelo:

```powershell
python proyecto/02_entrenar_modelo.py
```

Predecir con un jugador de ejemplo:

```powershell
python proyecto/03_predecir.py
```

## Que vas a aprender

- Que son features y target.
- Diferencia entre clasificacion y regresion.
- `train_test_split`.
- Pipelines de scikit-learn.
- Codificacion de variables categoricas.
- Escalado de variables numericas.
- Random Forest como modelo base.
- Accuracy, classification report y matriz de confusion.
- Guardar modelos con `joblib`.

