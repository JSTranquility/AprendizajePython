from pathlib import Path

import kagglehub
import pandas as pd


DATASET_ID = "rabieelkharoua/predict-online-gaming-behavior-dataset"
TARGET_COLUMN = "EngagementLevel"
ID_COLUMNS = ["PlayerID"]


def descargar_dataset():
    return Path(kagglehub.dataset_download(DATASET_ID))


def encontrar_csv(carpeta):
    archivos = list(Path(carpeta).rglob("*.csv"))
    if not archivos:
        raise FileNotFoundError(f"No se encontro ningun CSV en {carpeta}")
    return archivos[0]


def cargar_dataset():
    carpeta = descargar_dataset()
    ruta_csv = encontrar_csv(carpeta)
    df = pd.read_csv(ruta_csv)
    return df, ruta_csv


def preparar_features_target(df):
    if TARGET_COLUMN not in df.columns:
        columnas = ", ".join(df.columns)
        raise ValueError(
            f"No existe la columna objetivo {TARGET_COLUMN!r}. "
            f"Columnas disponibles: {columnas}"
        )

    columnas_a_eliminar = [TARGET_COLUMN]
    columnas_a_eliminar.extend(col for col in ID_COLUMNS if col in df.columns)

    X = df.drop(columns=columnas_a_eliminar)
    y = df[TARGET_COLUMN]
    return X, y


def separar_columnas_por_tipo(X):
    columnas_numericas = X.select_dtypes(include=["number"]).columns.tolist()
    columnas_categoricas = X.select_dtypes(exclude=["number"]).columns.tolist()
    return columnas_numericas, columnas_categoricas

