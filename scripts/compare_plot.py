import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -------------------------
# CERCCEDA
# -------------------------

file_path = r"C:\TFM_EDAR\data\raw\TFM_EDAR.xlsx"

df_c = pd.read_excel(
    file_path,
    sheet_name="Cerceda tabla",
    header=None
)

cerceda = df_c.iloc[110:124, 1:16]

cerceda.columns = cerceda.iloc[0]

cerceda = cerceda[1:].reset_index(drop=True)

# -------------------------
# VEDRA
# -------------------------

df_v = pd.read_excel(
    file_path,
    sheet_name="Vedra tabla",
    header=None
)

vedra = df_v.iloc[88:99, 1:13]

vedra.columns = vedra.iloc[0]

vedra = vedra[1:].reset_index(drop=True)

print("\nCOLUMNAS VEDRA:\n")
print(vedra.columns)

# -------------------------
# EXTRAER MEDIAS
# -------------------------

parametros = ["DBO5", "DQO", "SST"]

media_c = []
media_v = []

for p in parametros:

    valor_c = cerceda[
        cerceda["Parámetros"] == p
    ]["MEDIA"].values[0]

    valor_v = vedra[
        vedra["Parámetros"] == p
    ]["MEDIA"].values[0]

    media_c.append(valor_c)

    media_v.append(valor_v)

# -------------------------
# GRÁFICO
# -------------------------

x = np.arange(len(parametros))

width = 0.35

plt.figure(figsize=(10,6))

plt.bar(
    x - width/2,
    media_c,
    width,
    label="Cerceda"
)

plt.bar(
    x + width/2,
    media_v,
    width,
    label="Vedra"
)

plt.xticks(x, parametros)

plt.ylabel("kg/d")

plt.title("Comparación de cargas medias entrada")

plt.legend()

plt.grid(axis='y')

# Guardar gráfico
plt.savefig(
    r"C:\TFM_EDAR\outputs\figures\comparacion_cargas.png",
    dpi=300,
    bbox_inches='tight'
)

plt.show()