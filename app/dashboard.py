import streamlit as st
import plotly.graph_objects as go

from scripts.data_loader import load_cerceda
from scripts.data_loader import load_vedra

# -----------------------------------
# CONFIG
# -----------------------------------

st.set_page_config(
    page_title="TFM EDAR Dashboard",
    layout="wide"
)

# -----------------------------------
# TÍTULO
# -----------------------------------

st.title("TFM - Comparación EDAR")

st.markdown("---")


# -----------------------------------
# CARGAR DATOS
# -----------------------------------

cerceda = load_cerceda()

vedra = load_vedra()

# -----------------------------------
# KPIs
# -----------------------------------

st.subheader("Indicadores principales")

# Extraer medias
caudal_c = cerceda[
    cerceda["Parámetros"] == "Caudal"
]["MEDIA"].values[0]

caudal_v = vedra[
    vedra["Parámetros"] == "Caudal"
]["MEDIA"].values[0]

dbo_c = cerceda[
    cerceda["Parámetros"] == "DBO5"
]["MEDIA"].values[0]

dbo_v = vedra[
    vedra["Parámetros"] == "DBO5"
]["MEDIA"].values[0]

dqo_c = cerceda[
    cerceda["Parámetros"] == "DQO"
]["MEDIA"].values[0]

dqo_v = vedra[
    vedra["Parámetros"] == "DQO"
]["MEDIA"].values[0]

sst_c = cerceda[
    cerceda["Parámetros"] == "SST"
]["MEDIA"].values[0]

sst_v = vedra[
    vedra["Parámetros"] == "SST"
]["MEDIA"].values[0]

# Columnas KPI
col1, col2, col3, col4 = st.columns(4)

# KPI 1
col1.metric(
    "Caudal Medio",
    f"{caudal_c:.1f} m3/d",
    f"Vedra: {caudal_v:.1f}"
)

# KPI 2
col2.metric(
    "DBO5 Medio",
    f"{dbo_c:.1f} kg/d",
    f"Vedra: {dbo_v:.1f}"
)

# KPI 3
col3.metric(
    "DQO Medio",
    f"{dqo_c:.1f} kg/d",
    f"Vedra: {dqo_v:.1f}"
)

# KPI 4
col4.metric(
    "SST Medio",
    f"{sst_c:.1f} kg/d",
    f"Vedra: {sst_v:.1f}"
)

st.markdown("---")
# -----------------------------------
# SELECTOR
# -----------------------------------

# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.title("Configuración")

planta = st.sidebar.selectbox(
    "Seleccionar EDAR",
    ["Cerceda", "Vedra"]
)

parametro = st.sidebar.selectbox(
    "Seleccionar Parámetro",
    ["DBO5", "DQO", "SST", "NT", "PT"]
)

# -----------------------------------
# MOSTRAR TABLAS
# -----------------------------------

if planta == "Cerceda":

    st.subheader("EDAR Cerceda")

    st.dataframe(
    cerceda,
    hide_index=True,
    width='stretch'
)

else:

    st.subheader("EDAR Vedra")

    st.dataframe(
    vedra,
    hide_index=True,
    width='stretch'
)

# -----------------------------------
# GRÁFICO INTERACTIVO
# -----------------------------------

st.markdown("---")

st.subheader(f"Evolución mensual - {parametro}")

# -----------------------------------
# FILTRAR PARÁMETRO
# -----------------------------------

fila_c = cerceda[
    cerceda["Parámetros"] == parametro
]

fila_v = vedra[
    vedra["Parámetros"] == parametro
]

# -----------------------------------
# COLUMNAS MESES
# -----------------------------------

# Meses Cerceda
meses_c = [
    col for col in cerceda.columns
    if "24" in str(col)
]

# Meses Vedra
meses_v = [
    col for col in vedra.columns
    if "24" in str(col)
]

# Meses comunes
meses = [
    mes for mes in meses_c
    if mes in meses_v
]

# -----------------------------------
# VALORES
# -----------------------------------

valores_c = fila_c[meses].values.flatten()

valores_v = fila_v[meses].values.flatten()

# -----------------------------------
# CREAR FIGURA
# -----------------------------------

fig = go.Figure()

# CERCCEDA
fig.add_trace(
    go.Scatter(
        x=meses,
        y=valores_c,
        mode='lines+markers',
        name='Cerceda'
    )
)

# VEDRA
fig.add_trace(
    go.Scatter(
        x=meses,
        y=valores_v,
        mode='lines+markers',
        name='Vedra'
    )
)

# Layout
fig.update_layout(
    title=f"{parametro} - Comparación EDAR",
    xaxis_title="Mes",
    yaxis_title="kg/d",
    template="plotly_white"
)

# Mostrar
st.plotly_chart(
    fig,
    width='stretch'
)