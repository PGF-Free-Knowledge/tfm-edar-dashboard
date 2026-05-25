import pandas as pd

from scripts.utils import extract_block

# -----------------------------------
# RUTA GLOBAL
# -----------------------------------

FILE_PATH = r"C:\TFM_EDAR\data\raw\TFM_EDAR.xlsx"

# -----------------------------------
# CERCCEDA
# -----------------------------------

def load_cerceda():

    df = pd.read_excel(
        FILE_PATH,
        sheet_name="Cerceda tabla",
        header=None
    )

    cargas = extract_block(
        df,
        110,
        124,
        1,
        16
    )

    return cargas

# -----------------------------------
# VEDRA
# -----------------------------------

def load_vedra():

    df = pd.read_excel(
        FILE_PATH,
        sheet_name="Vedra tabla",
        header=None
    )

    cargas = extract_block(
        df,
        88,
        99,
        1,
        13
    )

    return cargas