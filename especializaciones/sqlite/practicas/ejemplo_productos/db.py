import sqlite3
from pathlib import Path


RUTA_DB = Path(__file__).resolve().parents[2] / "data" / "tienda.db"

def obtener_conexion():
    conexion = sqlite3.connect(RUTA_DB)
    conexion.row_factory = sqlite3.Row
    return conexion
