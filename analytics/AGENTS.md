# AGENTS.md — Contexto de IA para el Módulo Analytics (Streamlit EDA)

> Este archivo proporciona contexto específico para cualquier IA o agente que trabaje en el directorio `analytics/`.
> El contexto global del sistema está en el archivo raíz: `../AGENTS.md`.

---

## 📌 Identidad de este Microservicio

| Campo | Valor |
|---|---|
| **Nombre** | Analytics — Exploratory Data Analysis (EDA) & Visualización Interactiva |
| **Framework** | Streamlit ≥ 1.35.0 (Python 3.11+) |
| **Puerto por Defecto** | 8501 |
| **Librerías Gráficas** | Plotly Express, Altair, Seaborn, Matplotlib |
| **Objetivo Académico** | Demostrar el análisis exploratorio de datos exigido en la guía (análisis univariado, bivariado, multivariado, correlaciones, series temporales y mapas) |

---

## 🏗️ Arquitectura Interna de `analytics/`

```
analytics/
├── app.py                 → Aplicación principal Streamlit (Sidebar, KPIs globales, Router de módulos)
├── pages/
│   ├── 01_resumen_general.py → Visión ejecutiva, KPIs globales y tabla interactiva
│   ├── 02_analisis_temporal.py→ Tendencia 2010-2026, estacionalidad mensual y días de la semana
│   ├── 03_analisis_demografico.py → Distribución por género, grupos etarios y cruces
│   ├── 04_analisis_geografico.py  → Concentración por municipio (Barranquilla, Soledad, etc.)
│   └── 05_tipologia_delitos.py    → Artículos del código penal, armas y medios empleados
├── utils/
│   ├── data_loader.py     → Carga optimizada con @st.cache_data desde CSV limpio o Supabase
│   └── plots.py           → Funciones reutilizables con paletas consistentes
├── .streamlit/
│   └── config.toml        → Configuración de tema visual (colores institucionales)
├── requirements.txt       → Dependencias de visualización
├── .env.example           → Variables de conexión
├── AGENTS.md              → Este archivo
└── README.md              → Manual de ejecución
```

---

## 🚨 Reglas Críticas para la IA en `analytics/`

1. **Uso de Caché Obligatorio:** Todas las funciones de lectura o cálculo intensivo deben estar decoradas con `@st.cache_data`.
2. **Visualizaciones Interactivas con Plotly:** Priorizar gráficos interactivos de Plotly (`st.plotly_chart(..., use_container_width=True)`).
3. **Cero Eliminación de Registros:** Toda métrica o porcentaje se calcula sobre la base íntegra de **16,664 registros**.
4. **Exportabilidad:** Incluir botones de descarga (`st.download_button`) para exportar tablas filtradas a CSV o Excel.
5. **Capturas de Pantalla Legibles:** Diseñar las vistas con tipografía y contrastes aptos para extraer capturas de pantalla de alta resolución para el artículo científico en Word.

