import pandas as pd

# -----------------------------------
# ARCHIVO EXCEL
# -----------------------------------

file_path = r"C:\TFM_EDAR\data\raw\TFM_EDAR.xlsx"

# -----------------------------------
# CARGAR EXCEL
# -----------------------------------

excel = pd.ExcelFile(file_path)

# -----------------------------------
# RECORRER HOJAS
# -----------------------------------

for sheet in excel.sheet_names:

    print("\n")
    print("=" * 60)
    print(f"HOJA: {sheet}")
    print("=" * 60)

    # Leer hoja completa
    df = pd.read_excel(
        file_path,
        sheet_name=sheet,
        header=None
    )

    # Mostrar filas relevantes
    for i, row in df.iterrows():

        texto = " ".join(
            [str(x) for x in row.values]
        ).lower()

        keywords = [
            "entrada",
            "salida",
            "efluente",
            "vertido",
            "tratada",
            "rendimiento",
            "eliminación",
            "remoción"
        ]

        if any(k in texto for k in keywords):

            print(f"\nFILA {i}")
            print(row.tolist())