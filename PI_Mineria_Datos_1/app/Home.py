import streamlit as st

# ── CONFIGURACIÓN DE LA PÁGINA ──
st.set_page_config(
    page_title="Proyecto Integrador - Minería de Datos I",
    page_icon="📊",
    layout="wide"
)

# ── CSS ──
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
    * { font-family: 'Poppins', sans-serif !important; }
    .stApp {
        background-color: #F8F9FA;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='100'%3E%3Ctext y='30' font-size='20' opacity='0.08'%3E⛏️%3C/text%3E%3Ctext x='50' y='70' font-size='20' opacity='0.08'%3E📊%3C/text%3E%3Ctext y='90' font-size='20' opacity='0.08'%3E⛏️%3C/text%3E%3Ctext x='25' y='55' font-size='20' opacity='0.08'%3E📊%3C/text%3E%3C/svg%3E");
        background-repeat: repeat;
        background-size: 120px 120px;
    }
    h1 { color: #1E6FBA; padding-bottom: 10px; font-weight: 700; }
    h2 { color: #1A1A2E; border-left: 5px solid #1E6FBA; padding-left: 10px; font-weight: 600; }
    h3 { color: #1E6FBA; font-weight: 600; }
    [data-testid="stSidebar"] { background-color: #1A1A2E; }
    [data-testid="stSidebar"] * { color: white !important; font-family: 'Poppins', sans-serif !important; }
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
    .info-card p { margin: 8px 0; font-size: 0.95rem; }
    .info-card h3 { margin-bottom: 12px; }
    </style>
""", unsafe_allow_html=True)

# ── BANNER ──
st.image("https://raw.githubusercontent.com/Danielafz/PI_Mineria_Datos_I/main/app/assets/Gemini_Generated_Image_cnoe92cnoe92cnoe.png", use_container_width=True)
st.divider()

# ── TÍTULO ──
st.title("📊 Proyecto Integrador - Minería de Datos I")
st.subheader("Análisis de usuarios de una plataforma de streaming")
st.divider()

# ── INFORMACIÓN DEL PROYECTO ──
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>👥 Integrantes</h3>
        <p>👤 Daniela Fernandez</p>
        <p>👤 Julio Nahuel Gomez</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3>📋 Información</h3>
        <p>🎓 Tec. Sup. Ciencia de Datos e IA</p>
        <p>🏫 ITSE</p>
        <p>📖 Minería de Datos I</p>
        <p>👨‍🏫 Fernando Elias Mubarqui</p>
        <p>📅 2026</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ── CONTEXTO ──
st.markdown("""
<div class="info-card">
    <h3>🔍 Contexto del proyecto</h3>
    <p>Este proyecto analiza un dataset de usuarios de una plataforma de streaming
    que contiene información sobre planes de suscripción, consumo de contenido,
    preferencias de género, país de origen y actividad reciente.</p>
    <p>El objetivo es aplicar los contenidos de Minería de Datos I para construir
    un análisis reproducible con decisiones justificadas, trazabilidad del proceso
    y comunicación clara de los resultados.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── ENLACE AL REPOSITORIO ──
st.markdown("""
<div class="info-card">
    <h3>🔗 Repositorio</h3>
    <p>📁 <a href="https://github.com/Danielafz/PI_Mineria_Datos_I" target="_blank">
    Ver repositorio en GitHub</a></p>
</div>
""", unsafe_allow_html=True)