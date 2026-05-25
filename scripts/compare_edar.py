import pandas as pd

# Ruta archivo
file_path = r"C:\TFM_EDAR\data\raw\TFM_EDAR.xlsx"

# Leer hoja Vedra
vedra = pd.read_excel(
    file_path,
    sheet_name="Vedra tabla",
    header=None
)

# Mostrar filas útiles
for i, row in vedra.iterrows():

    if row.notna().sum() > 3:
        print(f"\nFILA {i}")
        print(row.tolist())