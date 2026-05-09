# Ejemplo 01: Manipulación de Datos con Pandas

import pandas as pd

# 1. Crear un DataFrame desde un diccionario
data = {
    'Producto': ['Laptop', 'Mouse', 'Monitor', 'Teclado'],
    'Precio': [1200, 25, 300, 80],
    'Stock': [5, 50, 10, 20]
}

df = pd.DataFrame(data)

# 2. Visualización básica
print("--- DataFrame Completo ---")
print(df)

# 3. Filtrado de datos (Productos con precio > 100)
caros = df[df['Precio'] > 100]
print("\n--- Productos Caros ---")
print(caros)

# 4. Operaciones matemáticas
promedio_precio = df['Precio'].mean()
print(f"\nPrecio promedio: ${promedio_precio}")

# 5. Agregar una columna (Valor total del inventario)
df['Valor_Inventario'] = df['Precio'] * df['Stock']
print("\n--- Inventario con Valor Total ---")
print(df)
