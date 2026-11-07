# 📊 Fase 4: Visualización y Dashboard Directivo en Power BI

> **Estado:** EN PROCESO (Endpoint backend en Render en diseño; pendiente ensamble del archivo `.pbix`)  
> **Entregable:** Archivo `dashboard_delitos_sexuales_atlantico.pbix`  
> **Requisito universitario:** "Se deben diseñar dashboards e informes interactivos en Power BI orientados al análisis y conocimiento con KPIs, medidas DAX y capturas de pantalla del entorno y modelo".

---

## 📋 Lista de Tareas y Checklists

- [x] **4.1. Definición de Endpoints para Consumo en Power BI**
  - [x] Endpoint directo `/api/v1/delitos/powerbi/dataset` (JSON plano de los 16,664 registros).
  - [x] Endpoints agregados precalculados para KPIs ligeros.

- [ ] **4.2. Modelado Dimensional y Conexión en Power BI Desktop**
  - [ ] Conexión Web (`Json.Document(Web.Contents("..."))`) o conexión directa PostgreSQL Supabase.
  - [ ] Transformación de tipos en Power Query.
  - [ ] Creación de Tabla Calendario (`Dim_Calendario`) y relaciones.

- [ ] **4.3. Formulación de Medidas DAX Principales**
  - [ ] `Total Casos = COUNTROWS(Delitos)`
  - [ ] `Total Victimas = SUM(Delitos[cantidad])`
  - [ ] `% Casos Femenino = DIVIDE(CALCULATE([Total Casos], Delitos[genero] = "FEMENINO"), [Total Casos], 0)`
  - [ ] `% Casos Menores = DIVIDE(CALCULATE([Total Casos], Delitos[grupo_etario] = "MENORES"), [Total Casos], 0)`
  - [ ] `Variacion Anual = [Total Casos] - CALCULATE([Total Casos], SAMEPERIODLASTYEAR(Dim_Calendario[Date]))`

- [ ] **4.4. Diseño Visual de Reportes (Páginas del Informe)**
  - [ ] Página 1: Resumen Ejecutivo y KPIs Generales.
  - [ ] Página 2: Comportamiento Cronológico y Análisis de Serie Temporal.
  - [ ] Página 3: Desglose Demográfico y Vulnerabilidad Infantil / Adolescente.
  - [ ] Página 4: Mapa y Distribución Municipal en el Atlántico.

- [ ] **4.5. Evidencias para el Artículo**
  - [ ] Captura de pantalla de la vista del modelo relacional en Power BI.
  - [ ] Captura de pantalla del editor avanzado de Power Query y medidas DAX.
  - [ ] Capturas de los paneles del informe terminado.

