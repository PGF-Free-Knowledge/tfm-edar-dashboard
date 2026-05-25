import pandas as pd
import matplotlib.pyplot as plt

# Ruta Excel
file_path = r"C:\TFM_EDAR\data\raw\TFM_EDAR.xlsx"

# Leer hoja
df = pd.read_excel(
    file_path,
    sheet_name="Cerceda tabla",
    header=None
)

# Extraer bloque cargas entrada
cargas = df.iloc[110:124, 1:16]

# Encabezados
cargas.columns = cargas.iloc[0]

# Eliminar encabezado duplicado
cargas = cargas[1:].reset_index(drop=True)

# Extraer fila DBO5
dbo5 = cargas[cargas["Parámetros"] == "DBO5"]

# Meses
meses = dbo5.columns[2:-1]

# Valores
valores = dbo5.iloc[0, 2:-1].astype(float)

# Crear gráfico
plt.figure(figsize=(10,5))

plt.plot(meses, valores, marker='o')

plt.title("DBO5 Entrada - EDAR Cerceda")

plt.xlabel("Mes")

plt.ylabel("kg/d")

plt.grid(True)

# Guardar gráfico
plt.savefig(
    r"C:\TFM_EDAR\outputs\figures\dbo5_entrada_cerceda.png",
    dpi=300,
    bbox_inches='tight'
)

plt.show()