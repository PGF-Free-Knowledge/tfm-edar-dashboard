import pandas as pd

file_path = r"C:\TFM_EDAR\data\raw\TFM_EDAR.xlsx"

# Leer hoja completa
df = pd.read_excel(
    file_path,
    sheet_name="Cerceda tabla",
    header=None
)

# Extraer bloque de cargas entrada
cargas = df.iloc[110:124, 1:16]

# Usar primera fila como encabezado
cargas.columns = cargas.iloc[0]

# Eliminar fila encabezado
cargas = cargas[1:]

# Reset índice
cargas = cargas.reset_index(drop=True)

print("\nCARGAS ENTRADA CERCCEDA:\n")

print(cargas)