# 📊 Analytics — Análisis Exploratorio de Datos (EDA) en Streamlit

Módulo analítico interactivo desarrollado en **Python con Streamlit** para el Análisis Exploratorio de Datos (EDA) del conjunto de delitos sexuales en el Departamento del Atlántico (2010 - 2026).

---

## 🚀 Requisitos y Configuración

### 1. Entorno de Ejecución
Se recomienda utilizar el entorno virtual creado o instalar las librerías necesarias:
```powershell
pip install -r analytics/requirements.txt
```

### 2. Variables de Configuración (Opcional)
Puede crear un archivo `.env` basado en `.env.example`:
```powershell
cp analytics/.env.example analytics/.env
```

---

## 🖥️ Ejecución de la Aplicación Streamlit

Para iniciar el servidor interactivo de Streamlit:
```powershell
streamlit run analytics/app.py --server.port 8501
```

Acceda a su navegador web en:
👉 **[http://localhost:8501](http://localhost:8501)**

---

## 📑 Módulos Analíticos Incluidos

1. **KPIs Generales:** Total de casos (16,664), total de víctimas, municipio de mayor criticidad y artículo penal más frecuente.
2. **Tendencia Temporal:** Serie cronológica anual 2010-2026, estacionalidad mensual y distribución por día de la semana.
3. **Análisis Demográfico:** Distribución porcentual por género, desglose por grupos etarios y cruce bivariado género vs edad.
4. **Distribución Geográfica:** Concentración municipal (Barranquilla, Soledad, Malambo, Sabanalarga y demás municipios).
5. **Tipología Jurídica y Armas:** Top 10 artículos penales más vulnerados y tipos de armas/medios empleados.
6. **Matriz de Intensidad (Heatmap):** Frecuencia cruzada entre principales municipios y grupos etarios.
7. **Explorador y Descarga:** Tabla interactiva paginada con botón para descargar datos filtrados en CSV.

---

## 📸 Evidencias para el Artículo Científico

Las vistas generadas por esta aplicación están diseñadas para ser capturadas directamente e integradas en el documento de Word del artículo científico como evidencias obligatorias (rotuladas bajo formato APA: *Figura X. Análisis de tendencia temporal en Streamlit. Elaboración propia*).

