import pandas as pd

# -----------------------------------
# RENOMBRAR MESES
# -----------------------------------

def rename_month_columns(df):

    month_map = {
        "1.24": "Ene-24",
        "2.24": "Feb-24",
        "3.24": "Mar-24",
        "4.24": "Abr-24",
        "5.24": "May-24",
        "6.24": "Jun-24",
        "7.24": "Jul-24",
        "8.24": "Ago-24",
        "9.24": "Sep-24",
        "10.24": "Oct-24",
        "11.24": "Nov-24",
        "12.24": "Dic-24"
    }

    # Convertir columnas a string
    df.columns = [str(col) for col in df.columns]

    # Renombrar columnas
    df = df.rename(columns=month_map)

    return df

# -----------------------------------
# EXTRAER BLOQUES
# -----------------------------------

def extract_block(
    df,
    row_start,
    row_end,
    col_start,
    col_end
):

    # Extraer bloque
    block = df.iloc[
        row_start:row_end,
        col_start:col_end
    ]

    # Encabezados
    block.columns = block.iloc[0]

    # Limpiar
    block = block[1:].reset_index(drop=True)

    # Renombrar meses
    block = rename_month_columns(block)

    return block