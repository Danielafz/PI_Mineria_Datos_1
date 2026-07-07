import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# ── CONFIGURACIÓN ──
st.set_page_config(
    page_title="PCA - PI Minería de Datos I",
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
    </style>
""", unsafe_allow_html=True)

# ── RUTAS ──
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
df = pd.read_csv(os.path.join(BASE, 'data', 'processed', 'streaming_users_clean.csv'))

# ── PCA ──
variables_pca = ['age', 'monthly_watch_time_mins', 'customer_support_tickets']
X = df[variables_pca].copy()
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
pca = PCA()
pca.fit(X_scaled)
varianza_explicada = pca.explained_variance_ratio_
varianza_acumulada = np.cumsum(varianza_explicada)
loadings = pd.DataFrame(
    pca.components_.T,
    index=variables_pca,
    columns=[f'PC{i}' for i in range(1, len(varianza_explicada)+1)]
)

# ── TÍTULO ──
st.title("🔬 Análisis de Componentes Principales (PCA)")
st.markdown("Reducción de dimensionalidad sobre las variables numéricas del dataset.")
st.divider()

# ── VARIABLES Y ESCALAMIENTO ──
st.subheader("📋 Variables utilizadas y escalamiento")

st.markdown("""
<div class="info-card">
<p><b>Variables seleccionadas:</b> age, monthly_watch_time_mins, customer_support_tickets</p>
<p><b>Escalamiento:</b> StandardScaler (estandarización z-score — media=0, desvío=1)</p>
<p><b>Justificación:</b> PCA es sensible a la escala. Sin escalar, monthly_watch_time_mins
(hasta 1500 minutos) dominaría sobre customer_support_tickets (0 a 5), distorsionando los resultados.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── VARIANZA EXPLICADA ──
st.subheader("📊 Visualización 1 — Varianza explicada por componente (Scree Plot)")

fig, ax = plt.subplots(figsize=(8, 4))
componentes = [f'PC{i}' for i in range(1, len(varianza_explicada)+1)]
ax.bar(componentes, varianza_explicada * 100, color='steelblue', edgecolor='white', alpha=0.8, label='Varianza por componente')
ax.plot(componentes, varianza_acumulada * 100, color='red', marker='o', linewidth=2, label='Varianza acumulada')
ax.axhline(y=80, color='gray', linestyle='--', linewidth=1, label='Umbral 80%')
for i, (var, acu) in enumerate(zip(varianza_explicada, varianza_acumulada)):
    ax.text(i, var*100 + 1, f'{var*100:.1f}%', ha='center', fontsize=10)
    ax.text(i, acu*100 + 2, f'{acu*100:.1f}%', ha='center', fontsize=9, color='red')
ax.set_title('Varianza explicada por componente principal (Scree Plot)')
ax.set_xlabel('Componente principal')
ax.set_ylabel('Varianza explicada (%)')
ax.set_ylim(0, 115)
ax.legend()
plt.tight_layout()
st.pyplot(fig)

st.markdown("""
<div class="info-card">
<p>El Scree Plot muestra cómo se distribuye la varianza entre las tres componentes principales.
La primera componente (PC1) explica la mayor proporción de la varianza total del dataset.
La línea roja muestra la varianza acumulada, indicando cuántas componentes son necesarias
para representar adecuadamente la información original.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── LOADINGS ──
st.subheader("📊 Visualización 2 — Contribución de variables (Loadings)")

import seaborn as sns
fig, ax = plt.subplots(figsize=(8, 4))
sns.heatmap(loadings, annot=True, fmt='.3f', cmap='RdBu_r',
            center=0, ax=ax, linewidths=0.5, annot_kws={'size': 11})
ax.set_title('Loadings: contribución de cada variable a cada componente')
ax.set_xlabel('Componente principal')
ax.set_ylabel('Variable original')
plt.tight_layout()
st.pyplot(fig)

st.markdown("""
<div class="info-card">
<p>El mapa de calor muestra el peso de cada variable en cada componente principal.
Los colores azules indican contribuciones positivas y los rojos negativas.
Las variables con valores absolutos más altos son las que más definen cada componente.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── RESUMEN ──
st.subheader("📋 Resumen del PCA")

col1, col2, col3 = st.columns(3)
col1.metric("Variables utilizadas", "3")
col2.metric("Escalamiento", "StandardScaler")
col3.metric("Varianza PC1", f"{varianza_explicada[0]*100:.1f}%")

st.markdown("""
<div class="info-card">
<p><b>Limitación:</b> Al trabajar con solo 3 variables numéricas, la reducción de dimensionalidad
tiene un alcance acotado. Una mejora futura podría incorporar variables adicionales como
la codificación del plan de suscripción o el país para enriquecer el análisis.</p>
</div>
""", unsafe_allow_html=True)
