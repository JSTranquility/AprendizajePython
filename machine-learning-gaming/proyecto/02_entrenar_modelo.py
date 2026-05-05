from pathlib import Path

import joblib
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

from src.datos import cargar_dataset
from src.datos import preparar_features_target
from src.datos import separar_columnas_por_tipo
from src.modelo import crear_pipeline


RUTA_MODELO = Path(__file__).resolve().parents[1] / "modelos" / "modelo_engagement.joblib"


def main():
    df, ruta_csv = cargar_dataset()
    print(f"Entrenando con: {ruta_csv}")

    X, y = preparar_features_target(df)
    columnas_numericas, columnas_categoricas = separar_columnas_por_tipo(X)

    print("\nColumnas numericas:")
    print(columnas_numericas)
    print("\nColumnas categoricas:")
    print(columnas_categoricas)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    pipeline = crear_pipeline(columnas_numericas, columnas_categoricas)
    pipeline.fit(X_train, y_train)

    predicciones = pipeline.predict(X_test)
    accuracy = pipeline.score(X_test, y_test)

    print(f"\nAccuracy: {accuracy:.4f}")
    print("\nClassification report:")
    print(classification_report(y_test, predicciones))
    print("Matriz de confusion:")
    print(confusion_matrix(y_test, predicciones))

    RUTA_MODELO.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(
        {
            "pipeline": pipeline,
            "columnas": X.columns.tolist(),
        },
        RUTA_MODELO,
    )
    print(f"\nModelo guardado en: {RUTA_MODELO}")


if __name__ == "__main__":
    main()

