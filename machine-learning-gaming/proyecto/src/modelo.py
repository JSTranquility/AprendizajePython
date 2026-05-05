from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler


def crear_pipeline(columnas_numericas, columnas_categoricas):
    preprocesamiento_numerico = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )

    preprocesamiento_categorico = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocesamiento = ColumnTransformer(
        transformers=[
            ("num", preprocesamiento_numerico, columnas_numericas),
            ("cat", preprocesamiento_categorico, columnas_categoricas),
        ]
    )

    modelo = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        class_weight="balanced",
    )

    return Pipeline(
        steps=[
            ("preprocesamiento", preprocesamiento),
            ("modelo", modelo),
        ]
    )

