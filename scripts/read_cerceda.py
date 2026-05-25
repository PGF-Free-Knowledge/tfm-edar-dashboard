import pandas as pd

file_path = r"C:\TFM_EDAR\data\raw\TFM_EDAR.xlsx"

df = pd.read_excel(
    file_path,
    sheet_name="Cerceda tabla",
    header=None
)

# Mostrar filas NO vacías
for i, row in df.iterrows():
    
    if row.notna().sum() > 3:
        print(f"\nFILA {i}")
        print(row.tolist())