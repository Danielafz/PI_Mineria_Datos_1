import streamlit as st
import os

# ── CONFIGURACIÓN ──
st.set_page_config(
    page_title="Conclusiones - PI Minería de Datos I",
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
    .info-card {
        background: white;
        border-radius: 12px;
        padding: 20px 25px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.08);
        border-top: 4px solid #1E6FBA;
        margin-bottom: 15px;
    }
    .card-green { border-top: 4px solid #4CAF50; }
    .card-red { border-top: 4px solid #F44336; }
    .card-orange { border-top: 4px solid #FF9800; }
    </style>
""", unsafe_allow_html=True)

# ── TÍTULO ──
st.title("✅ Conclusiones")
st.markdown("Hallazgos principales, limitaciones del análisis y próximos pasos.")
st.divider()

# ── HALLAZGOS ──
st.subheader("🔍 Hallazgos principales")

st.markdown("""
<div class="info-card card-green">
    <h3>Sobre los planes de suscripción</h3>
    <p>✅ El plan Básico concentra la mayor parte de los usuarios (44.8%), seguido por Estándar (35.3%) y Premium (19.9%).</p>
    <p>✅ Los usuarios con plan Premium muestran el mayor tiempo de visualización mensual, tanto en media como en mediana.</p>
    <p>✅ Existe una relación clara entre el tipo de plan contratado y el nivel de consumo de contenido.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="info-card card-green">
    <h3>Sobre las edades y el consumo</h3>
    <p>✅ La distribución de edades es aproximadamente uniforme, sin concentración en un grupo etario particular.</p>
    <p>✅ No existe correlación lineal fuerte entre la edad y el tiempo de visualización mensual.</p>
    <p>✅ Al incorporar el plan como tercera variable, los usuarios Premium muestran mayor consumo independientemente de la edad.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="info-card card-green">
    <h3>Sobre géneros y países</h3>
    <p>✅ La preferencia de géneros es relativamente homogénea entre países, sin diferencias drásticas.</p>
    <p>✅ Se observan pequeñas variaciones culturales que podrían aprovecharse para personalizar recomendaciones por región.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="info-card card-green">
    <h3>Sobre el PCA</h3>
    <p>✅ Las tres variables numéricas muestran contribuciones diferenciadas en las componentes principales.</p>
    <p>✅ PC1 explica el 33.8% de la varianza, con contribuciones similares de las tres variables.</p>
    <p>✅ PC2 está dominada principalmente por la edad del usuario.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── LIMITACIONES ──
st.subheader("⚠️ Limitaciones")

st.markdown("""
<div class="info-card card-red">
    <p>🔴 El dataset contiene solo 3 variables numéricas continuas, lo que acota el alcance del PCA y del análisis multivariado.</p>
    <p>🔴 Las variables categóricas no fueron incorporadas al PCA por requerir codificación adicional.</p>
    <p>🔴 Los valores faltantes y errores de carga presentes en el dataset original pueden haber introducido sesgos, aun después de la limpieza.</p>
    <p>🔴 El alcance de las conclusiones se encuentra condicionado por la información disponible y por las decisiones documentadas durante el proceso.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── PRÓXIMOS PASOS ──
st.subheader("🚀 Próximos pasos")

st.markdown("""
<div class="info-card card-orange">
    <p>🔶 Incorporar la codificación de variables categóricas para enriquecer el análisis de PCA.</p>
    <p>🔶 Aplicar técnicas de clustering para identificar grupos de usuarios con comportamientos similares.</p>
    <p>🔶 Incorporar variables adicionales como frecuencia de login o historial de cambios de plan.</p>
    <p>🔶 Explorar modelos predictivos para estimar el plan de suscripción o el tiempo de visualización.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── ENLACES ──
st.subheader("🔗 Enlaces del proyecto")

st.markdown("""
<div class="info-card">
    <p>📁 <a href="https://github.com/Danielafz/PI_Mineria_Datos_1" target="_blank">Repositorio en GitHub</a></p>
    <p>📊 Aplicación desplegada en Streamlit Cloud</p>
</div>
""", unsafe_allow_html=True)
