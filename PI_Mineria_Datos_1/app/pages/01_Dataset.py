import streamlit as st
import pandas as pd
import os

# ── CONFIGURACIÓN ──
st.set_page_config(
    page_title="Dataset - PI Minería de Datos I",
    page_icon="📊",
    layout="wide"
)

# ── CSS ──
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

# ── RUTAS ──
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
df_raw = pd.read_json(os.path.join(BASE, 'data', 'raw', 'streaming_users_dirty.csv'))
df_clean = pd.read_csv(os.path.join(BASE, 'data', 'processed', 'streaming_users_clean.csv'))

# ── TÍTULO ──
st.title("📁 Dataset")
st.markdown("Descripción general del dataset original y resumen de las transformaciones realizadas.")
st.divider()

# ── MÉTRICAS ──
st.subheader("📊 Resumen general")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Filas originales", f"{df_raw.shape[0]:,}")
col2.metric("Filas finales", f"{df_clean.shape[0]:,}")
col3.metric("Columnas", f"{df_clean.shape[1]}")
col4.metric("Retención", f"{df_clean.shape[0]/df_raw.shape[0]*100:.1f}%")

st.divider()

# ── DESCRIPCIÓN DE VARIABLES ──
st.subheader("📋 Variables del dataset")

st.markdown("""
<div class="info-card">
<p><b>user_id</b> — Identificador único del usuario (numérico entero)</p>
<p><b>
