import matplotlib.pyplot as plt

# -----------------------------------
# FIGURA
# -----------------------------------

fig, ax = plt.subplots(figsize=(12,4))

# Quitar ejes
ax.axis('off')

# -----------------------------------
# BLOQUES
# -----------------------------------

blocks = [
    ("Entrada", 0.1),
    ("Pretratamiento", 0.3),
    ("Biológico", 0.5),
    ("Decantador", 0.7),
    ("Salida", 0.9)
]

# Dibujar bloques
for label, x in blocks:

    ax.text(
        x,
        0.5,
        label,
        ha='center',
        va='center',
        fontsize=12,
        bbox=dict(
            boxstyle="round,pad=0.5",
            edgecolor="black",
            facecolor="lightblue"
        )
    )

# -----------------------------------
# FLECHAS
# -----------------------------------

for i in range(len(blocks)-1):

    x1 = blocks[i][1]
    x2 = blocks[i+1][1]

    ax.annotate(
        "",
        xy=(x2-0.07, 0.5),
        xytext=(x1+0.07, 0.5),
        arrowprops=dict(arrowstyle="->", lw=2)
    )

# -----------------------------------
# TÍTULO
# -----------------------------------

plt.title(
    "Diagrama simplificado proceso EDAR",
    fontsize=14
)

# -----------------------------------
# GUARDAR
# -----------------------------------

plt.savefig(
    r"C:\TFM_EDAR\outputs\figures\edar_diagram.png",
    dpi=300,
    bbox_inches='tight'
)

plt.show()