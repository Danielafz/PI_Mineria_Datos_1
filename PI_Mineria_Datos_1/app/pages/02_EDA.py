import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(
    page_title="EDA - PI Mineria de Datos I",
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
df = pd.read_csv(os.path.join(BASE, 'data', 'processed', 'streaming_users_clean.csv'))

st.title("📈 Análisis Exploratorio de Datos (EDA)")
st.markdown("Visualizaciones univariadas, bivariadas y multivariadas con interpretaciones.")
st.divider()

# UNIVARIADO 1
st.subheader("📊 Visualización 1 — ¿Cómo se distribuyen los usuarios por plan de suscripción?")

fig, ax = plt.subplots(figsize=(8, 4))
conteo = df['subscription_plan'].value_counts()
colores = ['#4CAF50', '#FFC107', '#F44336']
bars = ax.bar(conteo.index, conteo.values, color=colores, edgecolor='white', width=0.5)
for bar, val in zip(bars, conteo.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 30,
            f'{val:,}\n({val/len(df)*100:.1f}%)',
            ha='center', va='bottom', fontsize=9)
ax.set_title('Distribución de usuarios por plan de suscripción')
ax.set_xlabel('Plan')
ax.set_ylabel('Cantidad de usuarios')
ax.set_ylim(0, conteo.max() * 1.2)
plt.tight_layout()
st.pyplot(fig)
plt.close()

st.markdown("""
<div class="info-card">
<p>El plan Básico concentra la mayor parte de los usuarios, seguido por Estándar y luego Premium.
La mayoría de los usuarios opta por el plan de menor costo. El plan Premium tiene la menor adopción,
lo que es esperable en servicios de streaming donde los planes más caros tienen menor cantidad de suscriptores.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# UNIVARIADO 2
st.subheader("📊 Visualización 2 — ¿Cómo es la distribución de edades de los usuarios?")

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].hist(df['age'], bins=20, color='steelblue', edgecolor='white')
axes[0].set_title('Distribución de edades')
axes[0].set_xlabel('Edad (años)')
axes[0].set_ylabel('Cantidad de usuarios')
axes[1].boxplot(df['age'], vert=True, patch_artist=True,
                boxprops=dict(facecolor='steelblue', color='navy'))
axes[1].set_title('Boxplot de edades')
axes[1].set_ylabel('Edad (años)')
plt.tight_layout()
st.pyplot(fig)
plt.close()

st.markdown("""
<div class="info-card">
<p>La distribución de edades es aproximadamente uniforme, lo que indica que la plataforma tiene usuarios
de todas las edades sin una concentración marcada en un grupo etario particular. La mediana y la media
están cercanas entre sí, confirmando una distribución bastante simétrica.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# BIVARIADO 1
st.subheader("📊 Visualización 3 — ¿Los usuarios con plan Premium ven más contenido?")

fig, ax = plt.subplots(figsize=(8, 4))
orden = ['Básico', 'Estándar', 'Premium']
colores = ['#4CAF50', '#FFC107', '#F44336']

for i, (plan, color) in enumerate(zip(orden, colores), start=1):
    data = df[df['subscription_plan'] == plan]['monthly_watch_time_mins'].dropna()
    ax.boxplot(data, positions=[i], patch_artist=True,
               boxprops=dict(facecolor=color, alpha=0.7),
               medianprops=dict(color='black'),
               whiskerprops=dict(color='gray'),
               capprops=dict(color='gray'),
               flierprops=dict(marker='o', markerfacecolor=color, markersize=3))
    media = data.mean()
    ax.scatter(i, media, color='black', zorder=5, s=60, label='Media' if i == 1 else '')

ax.set_xticks([1, 2, 3])
ax.set_xticklabels(orden)
ax.set_title('Tiempo mensual de visualización por plan')
ax.set_xlabel('Plan de suscripción')
ax.set_ylabel('Minutos por mes')
ax.legend()
plt.tight_layout()
st.pyplot(fig)
plt.close()

st.markdown("""
<div class="info-card">
<p>Los usuarios con plan Premium muestran un tiempo de visualización mensual mayor que los de planes
Básico y Estándar. Esto sugiere que existe una relación entre el tipo de plan contratado y el nivel
de consumo: los usuarios que más usan la plataforma tienden a optar por planes superiores.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# BIVARIADO 2
st.subheader("📊 Visualización 4 — ¿Cuál es el género favorito según el país?")

tabla = df.groupby(['country', 'favorite_genre']).size().unstack(fill_value=0)
tabla_pct = tabla.div(tabla.sum(axis=1), axis=0) * 100
fig, ax = plt.subplots(figsize=(12, 5))
tabla_pct.plot(kind='bar', ax=ax, colormap='tab10', width=0.8)
ax.set_title('Géneros favoritos por país (%)')
ax.set_xlabel('País')
ax.set_ylabel('Porcentaje de usuarios (%)')
ax.legend(title='Género', bbox_to_anchor=(1.01, 1), loc='upper left', fontsize=8)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
plt.tight_layout()
st.pyplot(fig)
plt.close()

st.markdown("""
<div class="info-card">
<p>La distribución de géneros favoritos es relativamente homogénea entre países, sin diferencias drásticas.
Sin embargo se observan algunas variaciones culturales. Esto indica que si bien el comportamiento general
es similar entre regiones, existen matices que podrían considerarse para personalizar recomendaciones por país.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# MULTIVARIADO
st.subheader("📊 Visualización 5 — ¿La edad y el tiempo de visualización varían según el plan?")

fig, ax = plt.subplots(figsize=(10, 5))
colores_plan = {'Básico': '#4CAF50', 'Estándar': '#FFC107', 'Premium': '#F44336'}
for plan, color in colores_plan.items():
    subset = df[df['subscription_plan'] == plan]
    ax.scatter(subset['age'], subset['monthly_watch_time_mins'],
               c=color, label=plan, alpha=0.4, s=20)
ax.set_title('Tiempo de visualización vs Edad según plan')
ax.set_xlabel('Edad (años)')
ax.set_ylabel('Minutos mensuales')
ax.legend(title='Plan')
plt.tight_layout()
st.pyplot(fig)
plt.close()

st.markdown("""
<div class="info-card">
<p>No existe una correlación lineal fuerte entre la edad y el tiempo de visualización. Los usuarios de
todas las edades presentan niveles de consumo similares. Sin embargo al separar por plan de suscripción,
los usuarios Premium tienden a concentrarse en niveles de consumo más altos independientemente de la edad.</p>
</div>
""", unsafe_allow_html=True)
