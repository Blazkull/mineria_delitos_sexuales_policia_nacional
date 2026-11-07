# 🏛️ Arquitectura del Sistema y Flujo de Información

> **Proyecto:** Minería de Delitos Sexuales en el Atlántico (2010–2026)  
> **Plataformas de Despliegue:** FastAPI en **Render**, PostgreSQL en **Supabase / Neon**, EDA en **Streamlit**, Visualización en **Power BI**.

---

## 1. Diagrama de Arquitectura Global

```mermaid
flowchart TB
    subgraph FUENTE["📥 Fuente de Datos Abiertos"]
        RAW_CSV["Portal datos.gov.co<br/>Policía Nacional<br/>405,193 registros (2010-2026)"]
    end

    subgraph ETL["⚙️ Pipeline ETL (Python + Pandas)"]
        SCRIPT_ETL["backend/scripts/clean_and_filter_atlantico.py<br/>- Filtro Atlántico (16,664 filas)<br/>- Cero registros perdidos<br/>- Imputación 'NO REPORTADO'<br/>- Normalización de texto y fechas"]
        CLEAN_CSV["delitos_sexuales_atlantico_limpio.csv<br/>(16,664 registros íntegros)"]
    end

    subgraph CLOUD_DB["🗄️ Capa de Almacenamiento (PostgreSQL en Supabase / Neon)"]
        PG_DB[("Tabla: delitos_sexuales_atlantico<br/>- Índices B-Tree analíticos<br/>- Vistas materializadas<br/>- Auditoría: 2026-11-06")]
    end

    subgraph BACKEND_RENDER["🚀 Backend en la Nube (FastAPI en Render)"]
        RENDER_API["FastAPI API REST<br/>https://tu-app.onrender.com<br/>- /api/v1/delitos<br/>- /api/v1/delitos/powerbi/dataset<br/>- /api/v1/delitos/metricas/*<br/>- CORS habilitado & Compresión GZip"]
    end

    subgraph CLIENTES["📊 Capa de Consumo y Visualización"]
        POWER_BI["Power BI Desktop (.pbix)<br/>- Conexión Web API Render o Directa PG<br/>- Modelo Dimensional en Estrella<br/>- Medidas DAX y Reportes Directivos"]
        STREAMLIT["Streamlit Dashboard (Python)<br/>- EDA Interactivo<br/>- Univariado, Bivariado, Multivariado<br/>- Exportación CSV y Gráficos Plotly"]
        WEB_FRONT["Frontend Web SPA (React/Vite)<br/>- Portal público complementario"]
    end

    subgraph PAPER["📝 Entregable Académico Final"]
        WORD_PAPER["Artículo Científico en Word<br/>- ≥4.000 palabras<br/>- ≥15 referencias recientes APA 7ª ed.<br/>- Evidencias gráficas de todas las herramientas"]
    end

    RAW_CSV --> SCRIPT_ETL
    SCRIPT_ETL --> CLEAN_CSV
    CLEAN_CSV --> PG_DB
    PG_DB <--> RENDER_API
    PG_DB -.-> POWER_BI
    RENDER_API --> POWER_BI
    RENDER_API --> WEB_FRONT
    CLEAN_CSV --> STREAMLIT
    PG_DB -.-> STREAMLIT
    STREAMLIT --> WORD_PAPER
    POWER_BI --> WORD_PAPER
    PG_DB --> WORD_PAPER
```

---

## 2. Diagrama de Secuencia: Consumo de Power BI hacia Render

```mermaid
sequenceDiagram
    autonumber
    actor Usuario as Investigador / Evaluador
    participant PBI as Power BI Desktop (.pbix)
    participant Render as FastAPI en Render
    participant Supabase as PostgreSQL Supabase / Neon

    Usuario->>PBI: Abre informe o presiona 'Actualizar'
    PBI->>Render: GET /api/v1/delitos/powerbi/dataset (Header: Accept=application/json)
    Note over Render: FastAPI recibe solicitud con compresión GZip
    Render->>Supabase: SELECT * FROM delitos_sexuales_atlantico ORDER BY fecha_hecho DESC
    Supabase-->>Render: 16,664 registros estructurados
    Render-->>PBI: JSON optimizado con datos y tipos pre-parseados
    Note over PBI: Power BI carga tabla en el modelo en memoria VertiPaq
    PBI->>PBI: Aplica cálculos DAX, segmentadores y KPIs
    PBI-->>Usuario: Muestra Dashboard interactivo actualizado
```

---

## 3. Modelo Entidad-Relación (ERD)

```mermaid
erDiagram
    DELITOS_SEXUALES_ATLANTICO {
        bigint id PK "Clave primaria autoincremental"
        varchar departamento "Constante 'ATLÁNTICO'"
        varchar municipio "Nombre normalizado del municipio (23)"
        varchar codigo_dane "Código DANE 8 dígitos"
        varchar armas_medios "Arma o medio empleado"
        date fecha_hecho "Fecha del hecho (YYYY-MM-DD)"
        smallint anio "Año (2010 a 2026)"
        smallint mes "Mes (1 a 12)"
        varchar nombre_mes "Nombre del mes (Enero a Diciembre)"
        smallint dia "Día del mes (1 a 31)"
        varchar dia_semana "Día de la semana (Lunes a Domingo)"
        smallint trimestre "Trimestre (1 a 4)"
        smallint semestre "Semestre (1 a 2)"
        varchar genero "FEMENINO, MASCULINO, NO REPORTADO"
        varchar grupo_etario "ADULTOS, MENORES, ADOLESCENTES, NO REPORTADO"
        integer cantidad "Total de víctimas registradas (>=1)"
        varchar codigo_articulo "Artículo penal extraído"
        text delito "Descripción completa del delito"
        date fecha_descarga_dataset "Fija: 2026-11-06"
        varchar origen_datos "Policía Nacional de Colombia"
        timestamptz creado_en "Fecha de inserción en BD"
    }
```

