# Cepeda Darrell
# NC = 0030

import pandas as pd

# ==========================================
#        Verificar versión de Pandas
# ==========================================
print("=== VERIFICACIÓN DE ENTORNO ===")
print("Versión de Pandas instalada:", pd.__version__)
print("=" * 40)

# ==========================================
#         Caso Práctico en Código
# ==========================================
# Datos personalizados del alumno:
# Número de lista: 10 | Género: Hombre | Número de control: 0030

NUM_LISTA = 10
GENERO = "Hombre"
NUM_CONTROL = "0030"

print(f"\n=== CASO PRÁCTICO ML - ALUMNO NO. {NUM_LISTA} ===")
print(f"Género: {GENERO} | No. Control: {NUM_CONTROL}\n")

# Construcción de un Dataset para Machine Learning
dataset = {
    'ID_Cliente': [f"CLI-{NUM_CONTROL}-{i:02d}" for i in range(1, 6)],
    'Edad': [18 + NUM_LISTA, 25, 30 + NUM_LISTA, 45, 20 + NUM_LISTA],
    'Monto_Compra_MXN': [1200.50, 3500.00, 890.00, 4200.00, 2100.50],
    'Frecuencia_Visitas': [2, 6, 1, 9, 4],
    'Categoria_Target': ['Bajo', 'Alto', 'Bajo', 'Alto', 'Medio']
}

df = pd.DataFrame(dataset)

print("--- Dataframe Creado ---")
print(df)

print("\n--- Estadísticas Descriptivas ---")
print(df.describe())