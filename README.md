# Proyecto Integrador — Minería de Datos I

**Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial — ITSE**  
**Integrantes:** Daniela Fernandez — Julio Nahuel Gomez  
**Profesor:** Fernando Elias Mubarqui  
**Año:** 2026

---

## Descripción

Análisis completo de un dataset de usuarios de una plataforma de streaming, aplicando las etapas del proceso de minería de datos: inspección inicial, limpieza, análisis exploratorio, reducción de dimensionalidad y conclusiones.

---

## Estructura del proyecto

```text
PI_Mineria_Datos_1/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_inspeccion_inicial.ipynb
│   ├── 02_calidad_y_limpieza.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_pca.ipynb
│   └── 05_conclusiones.ipynb
├── app/
│   ├── Home.py
│   └── pages/
│       ├── 01_Dataset.py
│       ├── 02_EDA.py
│       ├── 03_PCA.py
│       └── 04_Conclusiones.py
├── reports/
├── logs/
├── requirements.txt
└── README.md
```
## Dataset

- **Archivo original:** `data/raw/streaming_users_dirty.csv`
- **Formato real:** JSON con extensión .csv
- **Dimensiones originales:** 8.160 filas × 8 columnas
- **Variables:** user_id, age, subscription_plan, monthly_watch_time_mins, country, favorite_genre, last_login_date, customer_support_tickets

---

## Pipeline de limpieza

| Paso | Transformación |
|------|----------------|
| 1 | Eliminación de 126 duplicados |
| 2 | Normalización de subscription_plan (15 variantes → 3 categorías) |
| 3 | Normalización de country (26 variantes → 7 países) |
| 4 | Normalización de favorite_genre |
| 5 | Imputación de favorite_genre con moda |
| 6 | Eliminación de nulos en last_login_date |
| 7 | Parseo de fechas con format='mixed' |
| 8 | Filtrado de edades imposibles (fuera de 0–100) |
| 9 | Eliminación de monthly_watch_time_mins imposibles |
| 10 | Imputación de monthly_watch_time_mins con mediana |
| 11 | Winsorización de outliers estadísticos (k=1.5) |
| 12 | Eliminación de valores centinela en customer_support_tickets (-1, 99, 150) |

---

## Análisis exploratorio

Se realizaron 5 visualizaciones:

- **Univariada 1:** Distribución de usuarios por plan de suscripción
- **Univariada 2:** Distribución de edades de los usuarios
- **Bivariada 1:** Tiempo de visualización por plan de suscripción
- **Bivariada 2:** Géneros favoritos por país
- **Multivariada:** Tiempo de visualización vs edad según plan

---

## PCA

Se aplicó Análisis de Componentes Principales sobre las 3 variables numéricas del dataset (age, monthly_watch_time_mins, customer_support_tickets), previa estandarización con StandardScaler.

---

## Aplicación Streamlit

🔗 [Ver aplicación](https://proyectointegradormineriadedatos1.streamlit.app/)

---

## Repositorio

🔗 [GitHub — PI_Mineria_Datos_1](https://github.com/Danielafz/PI_Mineria_Datos_1)

---

## Cómo ejecutar localmente

```bash
pip install -r requirements.txt
cd app
streamlit run Home.py
```
