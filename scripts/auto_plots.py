import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------------
# RUTA
# -----------------------------------

file_path = r"C:\TFM_EDAR\data\raw\TFM_EDAR.xlsx"

# -----------------------------------
# CERCCEDA
# -----------------------------------

df_c = pd.read_excel(
    file_path,
    sheet_name="Cerceda tabla",
    header=None
)

cerceda = df_c.iloc[110:124, 1:16]

cerceda.columns = cerceda.iloc[0]

cerceda = cerceda[1:].reset_index(drop=True)

# -----------------------------------
# VEDRA
# -----------------------------------

df_v = pd.read_excel(
    file_path,
    sheet_name="Vedra tabla",
    header=None
)

vedra = df_v.iloc[88:99, 1:13]

vedra.columns = vedra.iloc[0]

vedra = vedra[1:].reset_index(drop=True)

# -----------------------------------
# PARÁMETROS
# -----------------------------------

parametros = [
    "DBO5",
    "DQO",
    "SST",
    "NT",
    "PT"
]

# -----------------------------------
# CREAR GRÁFICOS
# -----------------------------------

for p in parametros:

    valor_c = cerceda[
        cerceda["Parámetros"] == p
    ]["MEDIA"].values[0]

    valor_v = vedra[
        vedra["Parámetros"] == p
    ]["MEDIA"].values[0]

    plt.figure(figsize=(6,5))

    plantas = ["Cerceda", "Vedra"]

    valores = [valor_c, valor_v]

    plt.bar(plantas, valores)

    plt.title(f"{p} - Comparación EDAR")

    plt.ylabel("kg/d")

    plt.grid(axis='y')

    # Guardar automáticamente
    plt.savefig(
        fr"C:\TFM_EDAR\outputs\figures\{p}_comparacion.png",
        dpi=300,
        bbox_inches='tight'
    )

    plt.close()

print("\nGráficos generados correctamente.")