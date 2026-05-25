from data_loader import load_cerceda
from data_loader import load_vedra

# -----------------------------------
# CERCCEDA
# -----------------------------------

cerceda = load_cerceda()

print("\nCERCCEDA:\n")

print(cerceda.head())

# -----------------------------------
# VEDRA
# -----------------------------------

vedra = load_vedra()

print("\nVEDRA:\n")

print(vedra.head())