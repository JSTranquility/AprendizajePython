from pathlib import Path

import joblib
import pandas as pd


RUTA_MODELO = Path(__file__).resolve().parents[1] / "modelos" / "modelo_engagement.joblib"


def crear_jugador_ejemplo(columnas):
    valores_base = {
        "Age": 22,
        "Gender": "Male",
        "Location": "USA",
        "GameGenre": "Action",
        "PlayTimeHours": 12.5,
        "InGamePurchases": 1,
        "GameDifficulty": "Medium",
        "SessionsPerWeek": 5,
        "AvgSessionDurationMinutes": 90,
        "PlayerLevel": 20,
        "AchievementsUnlocked": 35,
    }

    jugador = {}
    for columna in columnas:
        jugador[columna] = valores_base.get(columna, 0)

    return pd.DataFrame([jugador], columns=columnas)


def main():
    if not RUTA_MODELO.exists():
        raise FileNotFoundError(
            "Primero entrena el modelo con: python proyecto/02_entrenar_modelo.py"
        )

    artefacto = joblib.load(RUTA_MODELO)
    pipeline = artefacto["pipeline"]
    columnas = artefacto["columnas"]

    jugador = crear_jugador_ejemplo(columnas)
    prediccion = pipeline.predict(jugador)[0]

    print("Jugador usado para predecir:")
    print(jugador)
    print(f"\nPrediccion de engagement: {prediccion}")

    if hasattr(pipeline.named_steps["modelo"], "predict_proba"):
        probabilidades = pipeline.predict_proba(jugador)[0]
        clases = pipeline.named_steps["modelo"].classes_
        print("\nProbabilidades:")
        for clase, probabilidad in zip(clases, probabilidades):
            print(f"- {clase}: {probabilidad:.4f}")


if __name__ == "__main__":
    main()

