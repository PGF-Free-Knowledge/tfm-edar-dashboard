import pandas as pd

file_path = r"C:\TFM_EDAR\data\raw\TFM_EDAR.xlsx"

excel_file = pd.ExcelFile(file_path)

print("\nHojas disponibles:\n")

for sheet in excel_file.sheet_names:
    print("-", sheet)

print("\nArchivo leído correctamente")