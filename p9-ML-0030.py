# Cepeda Darrell
# NC = 0030

import pandas as pd

# Paso 12: Verificación de versión de Pandas
print("Versión de Pandas instalada:", pd.__version__)
print("=" * 50)

# Paso 13: Caso Práctico en Código con tus datos (datos10)
datos10 = {
    'distancia_km': [4.1, 2.6, 5.9, 1.7, 3.4],
    'trafico_nivel': [2, 1, 3, 2, 1],
    'edad_repartidor': [35, 27, 43, 31, 24],
    'tiempo_entrega_min': [34, 19, 55, 15, 23]
}

# Creación del DataFrame
df = pd.DataFrame(datos10)

print("--- DATAFRAME DE TIEMPOS DE ENTREGA ---")
print(df)
print("\n" + "=" * 50)

# Identificación de Componentes de Machine Learning
print("--- CONCEPTOS FUNDAMENTALES APLICADOS ---")

# 1. Variables de entrada / Características / Features (X)
X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']]
print("\nCaracterísticas (X - Predictoras):")
print(X)

# 2. Variable de salida / Etiqueta / Target (y)
y = df['tiempo_entrega_min']
print("\nEtiqueta u Objetivo (y - Lo que queremos predecir):")
print(y)

# 3. Observaciones / Instancias (Filas/Registros)
print(f"\nNúmero total de observaciones (filas): {len(df)}")
print(f"Dimensiones del dataset (Filas, Columnas): {df.shape}")

print("Programa ejecutado por Cepeda Darrell NC = 0030")