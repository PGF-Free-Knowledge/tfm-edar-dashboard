import pandas as pd

from utils import extract_block

file_path = r"C:\TFM_EDAR\data\raw\TFM_EDAR.xlsx"

# Leer hoja
df = pd.read_excel(
    file_path,
    sheet_name="Cerceda tabla",
    header=None
)

# Extraer bloque
cargas = extract_block(
    df,
    110,
    124,
    1,
    16
)

print(cargas.head())