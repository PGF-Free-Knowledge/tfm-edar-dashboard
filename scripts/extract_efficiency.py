import pandas as pd

# -----------------------------------
# ARCHIVO
# -----------------------------------

file_path = r"C:\TFM_EDAR\data\raw\TFM_EDAR.xlsx"

# -----------------------------------
# LEER HOJA
# -----------------------------------

df = pd.read_excel(
    file_path,
    sheet_name="Cerceda tabla",
    header=None
)

# -----------------------------------
# EXTRAER TABLA EFICIENCIA
# -----------------------------------

# Según exploración:
# fila 141 contiene encabezados

tabla = df.iloc[141:150].copy()

# usar fila 141 como columnas
tabla.columns = tabla.iloc[0]

# eliminar fila encabezado
tabla = tabla[1:]

# reset índice
tabla.reset_index(drop=True, inplace=True)

# -----------------------------------
# MOSTRAR
# -----------------------------------

print("\n")
print("TABLA EFICIENCIA CERCCEDA:\n")

print(
    tabla[
        [
            "Parámetros",
            "Media IN",
            "Media OUT",
            "% eliminación"
        ]
    ]
)