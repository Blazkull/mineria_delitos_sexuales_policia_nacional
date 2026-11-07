# 📈 Fase 3: Análisis Exploratorio de Datos (EDA) en Streamlit

> **Estado:** COMPLETADO (Código y aplicativo interactivo listos)  
> **Archivo principal:** `analytics/app.py`  
> **Requisito universitario:** "El EDA debe realizarse con Python con Streamlit. Identificar valores faltantes, atípicos, distribuciones, correlaciones y estadísticas descriptivas con evidencias".

---

## 📋 Lista de Tareas y Checklists

- [x] **3.1. Infraestructura de Streamlit**
  - [x] Configuración de tema visual en `analytics/.streamlit/config.toml`.
  - [x] Dependencias de interfaz y visualización en `analytics/requirements.txt`.
  - [x] Carga optimizada con `@st.cache_data` en `analytics/utils/data_loader.py`.

- [x] **3.2. Módulos y Visualizaciones del EDA**
  - [x] Tarjetas de KPIs principales (Total casos: 16,664, Total víctimas, Municipio top, Delito predominante).
  - [x] Pestaña 1: Tendencia Temporal (Evolución anual 2010-2026, estacionalidad mensual y días de la semana).
  - [x] Pestaña 2: Análisis Demográfico (Distribución por género, grupos etarios y cruce bivariado).
  - [x] Pestaña 3: Distribución Geográfica (Barranquilla vs 22 municipios del Atlántico, tabla porcentual).
  - [x] Pestaña 4: Tipología Penal y Armas (Top 10 artículos penales y medios empleados).
  - [x] Pestaña 5: Matriz de Calor / Correlación (Intensidad entre municipios y grupos etarios).
  - [x] Pestaña 6: Explorador de Datos paginado y botón de descarga CSV.

- [ ] **3.3. Captura de Evidencias Gráficas**
  - [ ] Captura de pantalla de la ejecución en navegador (localhost:8501).
  - [ ] Capturas de los gráficos clave rotulados para el artículo científico en Word.

