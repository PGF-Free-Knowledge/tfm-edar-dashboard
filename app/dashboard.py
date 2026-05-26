import streamlit as st
import plotly.graph_objects as go

# -----------------------------------
# FUNCIÓN SEMÁFORO
# -----------------------------------

def estado_eficiencia(valor):

    if valor >= 90:
        return "🟢 Excelente"

    elif valor >= 70:
        return "🟡 Aceptable"

    else:
        return "🔴 Crítico"

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


# -----------------------------------
# KPIs DINÁMICOS
# -----------------------------------

if planta == "Cerceda":

    col1.metric(
        "Caudal Medio",
        f"{caudal_c:.1f} m3/d"
    )

    col2.metric(
        "DBO5 Medio",
        f"{dbo_c:.1f} kg/d"
    )

    col3.metric(
        "DQO Medio",
        f"{dqo_c:.1f} kg/d"
    )

    col4.metric(
        "SST Medio",
        f"{sst_c:.1f} kg/d"
    )

else:

    col1.metric(
        "Caudal Medio",
        f"{caudal_v:.1f} m3/d"
    )

    col2.metric(
        "DBO5 Medio",
        f"{dbo_v:.1f} kg/d"
    )

    col3.metric(
        "DQO Medio",
        f"{dqo_v:.1f} kg/d"
    )

    col4.metric(
        "SST Medio",
        f"{sst_v:.1f} kg/d"
    )
    
# -----------------------------------
# EFICIENCIAS DINÁMICAS
# -----------------------------------

if planta == "Cerceda":

    eff_dbo = 92.48
    eff_dqo = 95.27
    eff_sst = 96.35
    eff_nt = 87.19
    eff_pt = 76.75

else:

    eff_dbo = 87.10
    eff_dqo = 89.40
    eff_sst = 82.50
    eff_nt = 74.20
    eff_pt = 68.10

# -----------------------------------
# KPIs EFICIENCIA
# -----------------------------------

st.subheader("Eficiencia de remoción")

e1, e2, e3, e4, e5 = st.columns(5)

e1.metric(
    "DBO5",
    f"{eff_dbo:.1f}%",
    estado_eficiencia(eff_dbo)
)

e2.metric(
    "DQO",
    f"{eff_dqo:.1f}%",
    estado_eficiencia(eff_dqo)
)

e3.metric(
    "SST",
    f"{eff_sst:.1f}%",
    estado_eficiencia(eff_sst)
)

e4.metric(
    "NT",
    f"{eff_nt:.1f}%",
    estado_eficiencia(eff_nt)
)

e5.metric(
    "PT",
    f"{eff_pt:.1f}%",
    estado_eficiencia(eff_pt)
)

st.markdown("---")

# -----------------------------------
# GAUGES INDUSTRIALES
# -----------------------------------

st.subheader("Indicadores operacionales")

g1, g2, g3 = st.columns(3)

# -----------------------------------
# FUNCIÓN GAUGE
# -----------------------------------

def crear_gauge(valor, titulo):

    fig = go.Figure(
        go.Indicator(
            mode = "gauge+number",
            value = valor,

            title = {'text': titulo},

            gauge = {
                'axis': {'range': [0,100]},

                'steps': [

                    {'range': [0,70], 'color': "lightcoral"},
                    {'range': [70,90], 'color': "khaki"},
                    {'range': [90,100], 'color': "lightgreen"}

                ],

                'bar': {'color': "darkblue"}
            }
        )
    )

    fig.update_layout(
        height=300,
        margin=dict(l=20,r=20,t=50,b=20)
    )

    return fig

# -----------------------------------
# MOSTRAR GAUGES
# -----------------------------------

with g1:

    st.plotly_chart(
        crear_gauge(eff_dbo, "DBO5"),
        use_container_width=True
    )

with g2:

    st.plotly_chart(
        crear_gauge(eff_dqo, "DQO"),
        use_container_width=True
    )

with g3:

    st.plotly_chart(
        crear_gauge(eff_sst, "SST"),
        use_container_width=True
    )

st.markdown("---")


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

# -----------------------------------
# DIAGRAMA EDAR
# -----------------------------------

st.markdown("---")

st.subheader("Diagrama simplificado proceso EDAR")

st.image(
    "outputs/figures/edar_diagram.png",
    width='stretch'
)