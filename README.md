# 🛡️ Minería de Datos y Analítica Predictiva: Delitos Sexuales en el Departamento del Atlántico (2010–2026)

> **Asignatura:** Minería de Datos | **Entrega Final:** 23 de Noviembre de 2026  
> **Fuente Oficial de Datos:** Policía Nacional de Colombia — Portal Nacional de Datos Abiertos (`datos.gov.co`)  
> **Fecha de Descarga Oficial:** **2026-11-06**  
> **Población de Estudio:** Departamento del Atlántico (23 municipios, 16,664 hechos registrados)  

---

## 📌 1. Visión General del Proyecto

Este repositorio contiene la solución completa de ingeniería y minería de datos aplicada al análisis histórico, criminológico y predictivo de los delitos contra la libertad, integridad y formación sexuales registrados en el **Departamento del Atlántico (Colombia)** entre los años **2010 y 2026**.

El sistema cubre de extremo a extremo el ciclo de vida analítico:
1. **Pipeline ETL y Limpieza Rigurosa:** Filtrado de 405,193 registros nacionales a **16,664 registros íntegros del Atlántico**, aplicando la política no negociable de **Cero Eliminación de Registros**, imputación explícita de nulos (`NO REPORTADO`), corrección de *Mojibake* y enriquecimiento de 7 dimensiones temporales.
2. **Capa de Almacenamiento Estructurado:** Base de datos relacional PostgreSQL desplegada en la nube (**Supabase**) con claves primarias, tipos optimizados (`SMALLINT`, `DATE`), 8 índices B-Tree y vistas analíticas pre-agregadas.
3. **Backend API REST (FastAPI):** Servicio desplegable en **Render** con soporte completo de filtros multidimensionales en **Swagger UI** (rango de fechas, años, municipios, artículos penales, grupos etarios, géneros, búsqueda textual) y endpoints optimizados para **Power BI**.
4. **Análisis Exploratorio de Datos (EDA) en Streamlit:** Dashboard interactivo en Python con 6 pestañas de análisis estadístico, gráficos interactivos Plotly y exportador de datos.
5. **Dashboard Directivo en Power BI (`.pbix`):** Tablero modelado en estrella con métricas DAX avanzadas y diseño visual ejecutivo consumiendo los datos desde Render o PostgreSQL Supabase.
6. **Documentación Exhaustiva y Control de Tareas:** Tablero maestro `MASTER_STATUS.md` (idéntico a estándares industriales), catálogo de endpoints, justificación metodológica y especificación completa de Power BI.

---

## 🗺️ 2. Mapa de Arquitectura y Componentes del Repositorio

```
mineria_delitos_sexuales_policia_nacional/
├── backend/                              # API REST FastAPI + Pipeline ETL y Conectores DB
│   ├── .venv/                            # Entorno virtual Python 3.11 aislado
│   ├── app/                              # Aplicación FastAPI
│   │   ├── main.py                       # Configuración de FastAPI, CORS y rutas
│   │   ├── core/                         # config.py (Pydantic Settings) y database.py (Session Pooler)
│   │   ├── models/delito.py              # Modelo ORM SQLAlchemy para PostgreSQL
│   │   ├── schemas/delito.py             # Esquemas Pydantic v2 para serialización y validación
│   │   ├── services/delito_service.py    # Lógica analítica, filtros avanzados y fallback resiliente
│   │   └── api/v1/endpoints/delitos.py   # Endpoints documentados para Swagger y Power BI
│   ├── scripts/
│   │   ├── clean_and_filter_atlantico.py # Script ETL de limpieza y extracción (16,664 filas)
│   │   └── upload_to_supabase.py         # Script de carga batch masiva a PostgreSQL Supabase
│   ├── requirements.txt                  # Dependencias estrictas del backend
│   ├── .env.example & .env               # Variables de entorno
│   ├── AGENTS.md                         # Contexto técnico de agentes en Backend
│   └── README.md                         # Guía de ejecución del backend
├── analytics/                            # Dashboard EDA con Python + Streamlit
│   ├── app.py                            # Aplicación interactiva de Streamlit (6 módulos analíticos)
│   ├── utils/data_loader.py              # Carga y caché de datos con @st.cache_data
│   ├── .streamlit/config.toml            # Tema visual institucional
│   ├── requirements.txt                  # Dependencias de visualización
│   ├── .env.example                      # Variables de entorno de analítica
│   ├── AGENTS.md                         # Contexto técnico de agentes en Analytics
│   └── README.md                         # Guía de ejecución de Streamlit
├── frontend/                             # Portal Web de visualización complementario
│   ├── AGENTS.md                         # Contexto de Frontend
│   └── README.md                         # Documentación del Frontend
├── docs/                                 # Documentación maestra y entregables
│   ├── tasks/
│   │   ├── MASTER_STATUS.md              # Tablero maestro de control y progreso (Git Flow)
│   │   └── fases/                        # Fases de trabajo detalladas (01 a 05)
│   ├── documentacion/                    # Documentación técnica profunda del sistema
│   │   ├── 01_DECISIONES_METODOLOGICAS_FILTRADO.md # Justificación de cero pérdidas e imputación
│   │   ├── 02_DIAGRAMA_Y_MODELO_BASE_DATOS.md      # Esquema relacional, tipos e índices
│   │   ├── 03_CATALOGO_ENDPOINTS_API.md            # Documentación completa de endpoints REST
│   │   ├── 04_FLUJO_ARQUITECTURA_Y_PROCESOS.md     # Ciclo de vida y flujos del sistema
│   │   └── 05_ESTANDARIZACION_Y_BUENAS_PRACTICAS.md# Estándares de calidad y rendimiento
│   ├── architecture/
│   │   └── ARCHITECTURE.md               # Diagramas de flujo y secuencia en Mermaid
│   ├── database/
│   │   ├── supabase_ddl.sql              # Script SQL DDL listo para Supabase / Neon
│   │   └── DATABASE_SCHEMA.md            # Diccionario de datos de la base de datos
│   ├── powerbi/
│   │   ├── ESPECIFICACION_POWERBI.md     # Especificación visual, visuales, páginas y DAX
│   │   └── POWERBI_GUIDE.md              # Código M para Power Query y conexión Web
│   ├── paper/
│   │   └── PLAN_ARTICULO.md              # Esquema para el artículo de 4.000 palabras (APA 7)
│   ├── data_set/                         # Datasets crudos y limpios
│   │   ├── Reporte__Delitos_sexuales_Policía_Nacional_20261106.csv # Original (405,193 filas)
│   │   └── delitos_sexuales_atlantico_limpio.csv                  # Limpio (16,664 filas)
│   ├── AGENTS.md                         # Contexto de documentación
│   └── README.md                         # Índice general de documentación
├── render.yaml                           # Infraestructura como código (IaC) para Render
├── AGENTS.md                             # Contexto maestro del sistema para agentes de IA
└── README.md                             # Este archivo
```

---

## 💻 3. Tecnologías y Librerías Utilizadas

| Componente | Tecnología | Versión | Rol / Propósito |
|---|---|---|---|
| **Lenguaje Base** | Python | `3.11.0` | Motor de procesamiento ETL, API y visualización |
| **Pipeline ETL** | Pandas | `3.1.1` | Limpieza, imputación, normalización tipográfica y agregación |
| **Computación Numérica** | NumPy | `2.4.6` | Operaciones vectorizadas y condiciones |
| **Backend Framework** | FastAPI | `0.110+` | API REST asíncrona de alto rendimiento con Swagger UI |
| **Servidor ASGI** | Uvicorn | `0.28+` | Servidor de producción para FastAPI |
| **Validación de Datos** | Pydantic | `2.14+` | Esquemas de datos tipados y serialización JSON |
| **ORM y BD** | SQLAlchemy | `2.1+` | Mapeo objeto-relacional y consultas SQL estructuradas |
| **Driver PostgreSQL** | Psycopg2-binary | `2.9.13` | Conexión binaria optimizada con PostgreSQL |
| **Cliente Cloud DB** | Supabase-py | `2.34+` | SDK para operaciones con la base de datos de Supabase |
| **Dashboard EDA** | Streamlit | `1.35+` | Interfaz interactiva para el Análisis Exploratorio de Datos |
| **Gráficos Interactivos** | Plotly Express | `5.20+` | Visualizaciones multivariadas, líneas y mapas de calor |
| **Entorno Virtual** | Python venv | `3.11` | Aislamiento estricto de dependencias en `backend/.venv` |
| **Base de Datos Cloud**| PostgreSQL (Supabase) | `15+` | Persistencia gestionada con Transaction Pooler |
| **Plataforma Hosting** | Render | Cloud PaaS | Despliegue continuo del backend mediante `render.yaml` |
| **Herramienta BI** | Power BI Desktop | Última versión | Modelado dimensional en estrella y reportes directivos |

---

## 📊 4. Hallazgos Analíticos del Departamento del Atlántico (16,664 Hechos)

Del procesamiento de los **16,664 registros íntegros** correspondientes a los **23 municipios** del Atlántico en el periodo **2010 a 2026**, se destacan las siguientes conclusiones cuantitativas:

```mermaid
pie title Distribución de Delitos por Género de la Víctima (Atlántico)
    "Femenino (85.1%)" : 14184
    "Masculino (14.1%)" : 2355
    "No Reportado (0.8%)" : 125
```

- **Víctimas de Género Femenino:** Concentran el **85.12%** de los casos (14,184 hechos), evidenciando una marcada desproporción de género.
- **Vulnerabilidad Infantil y Juvenil:** El **32.93%** de las víctimas corresponden a menores de edad (**3,026 menores de 14 años** y **2,461 adolescentes** de 14 a 17 años).
- **Concentración Territorial:**
  - **Barranquilla (Distrito Capital):** 8,778 casos (**52.68%**).
  - **Soledad:** 3,613 casos (**21.68%**).
  - **Área Metropolitana (Barranquilla + Soledad + Malambo + Galapa + Puerto Colombia):** Concentra más del **79%** de los hechos del departamento.
- **Tipificación Penal Predominante:**
  - **Artículo 209 del Código Penal:** *Actos sexuales con menor de 14 años* es la conducta punible con mayor número de reportes.

---

## 🚀 5. Guía de Ejecución Rápida

### ⚡ Arranque Unificado con Un Solo Comando (Recomendado)
Puede iniciar todos los servicios del proyecto (**Backend FastAPI en `:8000`**, **Dashboard Streamlit en `:8501`** y **Frontend Portal en `:3000`**) ejecutando un único comando o haciendo doble clic:

- **En PowerShell:** `.\run_dev.ps1`
- **En CMD o con Doble Clic:** `run_dev.bat`

---

### Arranque Paso a Paso (Modo Desarrollo Manual)

#### Paso 1: Clonar y Activar el Entorno Virtual de Backend
```powershell
# En Windows PowerShell
cd e:\IA-UNIVERSIDAD\mineria_delitos_sexuales_policia_nacional
.\backend\.venv\Scripts\Activate.ps1
```

### Paso 2: Ejecutar el Pipeline ETL de Limpieza
```powershell
.\backend\.venv\Scripts\python.exe backend/scripts/clean_and_filter_atlantico.py
```
*Generará `docs/data_set/delitos_sexuales_atlantico_limpio.csv` con 16,664 registros limpios y 0 nulos.*

### Paso 3: Cargar los Datos a Supabase PostgreSQL
1. Cree su proyecto en [Supabase](https://supabase.com).
2. Abra el **SQL Editor** en Supabase y ejecute el script `docs/database/supabase_ddl.sql`.
3. Configure su cadena de conexión en `backend/.env`:
   ```env
   DATABASE_URL=postgresql+psycopg2://postgres.TU_PROYECTO:[PASSWORD]@aws-0-us-east-1.pooler.supabase.com:5432/postgres
   ```
4. Ejecute la carga masiva:
   ```powershell
   .\backend\.venv\Scripts\python.exe backend/scripts/upload_to_supabase.py
   ```

### Paso 4: Iniciar el Backend FastAPI (Local o Render)
```powershell
cd backend
..\backend\.venv\Scripts\uvicorn.exe app.main:app --reload --port 8000
```
- **Documentación Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Endpoint para Power BI:** [http://localhost:8000/api/v1/delitos/powerbi/dataset](http://localhost:8000/api/v1/delitos/powerbi/dataset)

### Paso 5: Iniciar el Dashboard EDA en Streamlit
```powershell
cd analytics
..\backend\.venv\Scripts\streamlit.exe run app.py --server.port 8501
```
- **Aplicación Web:** [http://localhost:8501](http://localhost:8501)

### Paso 6: Conectar Power BI Desktop
1. En Power BI Desktop: **Obtener datos ➡️ Web**.
2. URL: `https://api-delitos-sexuales-atlantico.onrender.com/api/v1/delitos/powerbi/dataset` (o `http://localhost:8000/api/v1/delitos/powerbi/dataset`).
3. Pegue el código M disponible en [docs/powerbi/POWERBI_GUIDE.md](docs/powerbi/POWERBI_GUIDE.md).

---

## 📑 6. Índice de Documentación Detallada

- 📘 **Guía Maestra para Nuevos Desarrolladores:** [docs/GUIA_COMPLETA_DEL_PROYECTO.md](docs/GUIA_COMPLETA_DEL_PROYECTO.md)
- 📋 **Control de Tareas y Fases:** [docs/tasks/MASTER_STATUS.md](docs/tasks/MASTER_STATUS.md)
- 📊 **Especificación Completa de Power BI:** [docs/powerbi/ESPECIFICACION_POWERBI.md](docs/powerbi/ESPECIFICACION_POWERBI.md)
- 🔬 **Decisiones Metodológicas de Filtrado:** [docs/documentacion/01_DECISIONES_METODOLOGICAS_FILTRADO.md](docs/documentacion/01_DECISIONES_METODOLOGICAS_FILTRADO.md)
- 🗄️ **Modelo y Diagrama de Base de Datos:** [docs/documentacion/02_DIAGRAMA_Y_MODELO_BASE_DATOS.md](docs/documentacion/02_DIAGRAMA_Y_MODELO_BASE_DATOS.md)
- 📡 **Catálogo Completo de Endpoints REST:** [docs/documentacion/03_CATALOGO_ENDPOINTS_API.md](docs/documentacion/03_CATALOGO_ENDPOINTS_API.md)
- 🔄 **Flujo de Arquitectura y Procesos:** [docs/documentacion/04_FLUJO_ARQUITECTURA_Y_PROCESOS.md](docs/documentacion/04_FLUJO_ARQUITECTURA_Y_PROCESOS.md)
- 🛡️ **Estandarización y Buenas Prácticas:** [docs/documentacion/05_ESTANDARIZACION_Y_BUENAS_PRACTICAS.md](docs/documentacion/05_ESTANDARIZACION_Y_BUENAS_PRACTICAS.md)
