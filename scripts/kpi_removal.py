import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------------
# ARCHIVO
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

# BLOQUE RESUMEN
cerceda = df_c.iloc[54:63, 15:22]

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

vedra = df_v.iloc[105:114, 15:22]

vedra.columns = vedra.iloc[0]

vedra = vedra[1:].reset_index(drop=True)

print("\nCOLUMNAS CERCCEDA:\n")
print(cerceda.columns)

print("\nCOLUMNAS VEDRA:\n")
print(vedra.columns)

# -----------------------------------
# PARÁMETROS
# -----------------------------------

parametros = ["DBO5", "DQO", "SST", "NT", "PT"]

# -----------------------------------
# EXTRAER EFICIENCIAS
# -----------------------------------

eff_c = []
eff_v = []

for p in parametros:

    valor_c = cerceda[
        cerceda["Parámetros"] == p
    ]["% eliminación"].values[0]

    valor_v = vedra[
        vedra["Parámetros"] == p
    ]["% eliminación"].values[0]

    eff_c.append(valor_c * 100)

    eff_v.append(valor_v * 100)

# -----------------------------------
# GRÁFICO
# -----------------------------------

x = np.arange(len(parametros))

width = 0.35

plt.figure(figsize=(10,6))

plt.bar(
    x - width/2,
    eff_c,
    width,
    label="Cerceda"
)

plt.bar(
    x + width/2,
    eff_v,
    width,
    label="Vedra"
)

plt.xticks(x, parametros)

plt.ylabel("Eficiencia (%)")

plt.title("Comparación de eficiencia de eliminación")

plt.ylim(0, 110)

plt.grid(axis='y')

plt.legend()

# Guardar
plt.savefig(
    r"C:\TFM_EDAR\outputs\figures\eficiencias_comparacion.png",
    dpi=300,
    bbox_inches='tight'
)

plt.show()