import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Dataset - PI Mineria de Datos I",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
    * { font-family: 'Poppins', sans-serif !important; }
    .stApp { background-color: #F8F9FA; }
    h1 { color: #1E6FBA; font-weight: 700; }
    h2 { color: #1A1A2E; border-left: 5px solid #1E6FBA; padding-left: 10px; font-weight: 600; }
    h3 { color: #1E6FBA; font-weight: 600; }
    [data-testid="stSidebar"] { background-color: #1A1A2E; }
    [data-testid="stSidebar"] * { color: white !important; }
    [data-testid="metric-container"] {
        background-color: white;
        border: 1px solid #1E6FBA;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    }
    .info-card {
        background: white;
        border-radius: 12px;
        padding: 20px 25px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.08);
        border-top: 4px solid #1E6FBA;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
df_raw = pd.read_json(os.path.join(BASE, 'data', 'raw', 'streaming_users_dirty.csv'))
df_clean = pd.read_csv(os.path.join(BASE, 'data', 'processed', 'streaming_users_clean.csv'))

st.title("📁 Dataset")
st.markdown("Descripcion general del dataset original y resumen de las transformaciones realizadas.")
st.divider()

st.subheader("📊 Resumen general")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Filas originales", f"{df_raw.shape[0]:,}")
col2.metric("Filas finales", f"{df_clean.shape[0]:,}")
col3.metric("Columnas", f"{df_clean.shape[1]}")
col4.metric("Retencion", f"{df_clean.shape[0]/df_raw.shape[0]*100:.1f}%")

st.divider()

st.subheader("📋 Variables del dataset")

st.markdown("""
<div class="info-card">
<p><b>user_id</b> - Identificador unico del usuario (numerico entero)</p>
<p><b>age</b> - Edad del usuario en anos (numerico entero)</p>
<p><b>subscription_plan</b> - Plan de suscripcion: Basico, Estandar o Premium (categorica)</p>
<p><b>monthly_watch_time_mins</b> - Tiempo de visualizacion mensual en minutos (numerico continuo)</p>
<p><b>country</b> - Pais de origen del usuario (categorica)</p>
<p><b>favorite_genre</b> - Genero de contenido favorito (categorica)</p>
<p><b>last_login_date</b> - Fecha del ultimo ingreso a la plataforma (fecha)</p>
<p><b>customer_support_tickets</b> - Cantidad de tickets de soporte generados (numerico discreto)</p>
</div>
""", unsafe_allow_html=True)

st.divider()

st.subheader("🔍 Calidad del dataset original")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>Problemas detectados</h3>
        <p>🔴 126 registros duplicados</p>
        <p>🔴 753 valores faltantes en total</p>
        <p>🔴 15 variantes en subscription_plan</p>
        <p>🔴 26 variantes en country</p>
        <p>🔴 Valores imposibles en age, monthly_watch_time_mins y customer_support_tickets</p>
        <p>🔴 last_login_date en formato texto con formatos mixtos</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3>Transformaciones aplicadas</h3>
        <p>✅ Eliminacion de duplicados</p>
        <p>✅ Normalizacion de variables categoricas</p>
        <p>✅ Imputacion de nulos con moda y mediana</p>
        <p>✅ Eliminacion de valores imposibles</p>
        <p>✅ Conversion de fechas con format='mixed'</p>
        <p>✅ Winsorizacion de outliers estadisticos</p>
        <p>✅ Eliminacion de valores centinela (99, 150, -1)</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.subheader("👀 Vista previa del dataset limpio")
st.dataframe(df_clean.head(10), use_container_width=True)
