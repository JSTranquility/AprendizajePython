from src.datos import TARGET_COLUMN
from src.datos import cargar_dataset


def main():
    df, ruta_csv = cargar_dataset()

    print(f"CSV encontrado: {ruta_csv}")
    print(f"Filas: {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")
    print("\nColumnas:")
    for columna in df.columns:
        print(f"- {columna}: {df[columna].dtype}")

    print("\nPrimeras filas:")
    print(df.head())

    if TARGET_COLUMN in df.columns:
        print(f"\nDistribucion de {TARGET_COLUMN}:")
        print(df[TARGET_COLUMN].value_counts())
    else:
        print(f"\nNo se encontro la columna objetivo {TARGET_COLUMN!r}.")


if __name__ == "__main__":
    main()

