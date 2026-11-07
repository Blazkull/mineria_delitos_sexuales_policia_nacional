# 📘 Guía Maestra del Proyecto: Arquitectura, Flujo de Datos y Operación

> **Documento para Desarrolladores e Investigadores**  
> **Proyecto:** Minería de Datos y Analítica Predictiva de Delitos Sexuales en el Atlántico (2010–2026)  
> **Fuente Oficial:** Policía Nacional de Colombia — Portal de Datos Abiertos (`datos.gov.co`)  
> **Fecha Oficial de Descarga:** **2026-11-06** (Fija e inmutable para auditoría)  
> **Base de Datos:** PostgreSQL 17 en **Supabase** (Tabla: `delitos_sexuales_atlantico`, 16,664 registros)  

---

## 🎯 1. ¿De qué se trata este Proyecto?

Este proyecto implementa una solución de minería de datos, analítica predictiva y visualización directiva sobre el registro histórico oficial de delitos contra la libertad, integridad y formación sexuales en el **Departamento del Atlántico**, abarcando sus **23 municipios** durante un horizonte temporal de 17 años (**2010 a 2026**).

### 💡 Contexto del Negocio y del Problema:
1. **Universo Nacional:** El dataset crudo original nacional contiene **405,193 registros** de toda Colombia.
2. **Jurisdicción de Estudio:** Se filtró exclusivamente para el **Departamento del Atlántico**, obteniendo exactamente **16,664 registros íntegros**.
3. **Regla No Negociable de Calidad:** **Cero pérdida de registros**. Ningún hecho denunciado en el Atlántico fue descartado por presentar datos incompletos. Se aplicó una técnica de **imputación explícita categórica** (`NO REPORTADO`), preservando el 100% de la representatividad estadística (0 nulos finales).
4. **Objetivos Técnicos:**
   - Proveer una base de datos relacional en la nube (**Supabase PostgreSQL**) indexada para consultas de alto rendimiento.
   - Exponer una **API REST (FastAPI)** desplegada en **Render** con soporte completo de filtros multidimensionales en **Swagger UI**.
   - Conectar un **Dashboard interactivo en Power BI Desktop** mediante endpoints web y conexión directa.
   - Desarrollar un **Dashboard exploratorio (EDA) en Streamlit (Python)** para el análisis estadístico y generación de evidencias.
   - Servir como base empírica para la redacción de un **Artículo Científico** universitario bajo normas APA 7ª edición.

---

## 🔄 2. Diagrama de Flujo del Dato y Arquitectura del Sistema

```mermaid
flowchart TD
    subgraph S1["1. INGESTIÓN Y FUENTE PRIMARIA"]
        RAW_CSV["Portal datos.gov.co<br/>Policía Nacional<br/>Reporte Delitos Sexuales<br/>(405,193 registros nacionales)"]
    end

    subgraph S2["2. PIPELINE ETL DE LIMPIEZA (Python + Pandas)"]
        ETL["backend/scripts/clean_and_filter_atlantico.py<br/>- Filtro Atlántico (16,664 registros)<br/>- Cero filas eliminadas<br/>- Imputación nulos ('NO REPORTADO')<br/>- Normalización ortográfica y Mojibake<br/>- Derivación de 7 columnas temporales<br/>- Auditoría: fecha_descarga (2026-11-06)"]
        CLEAN_CSV["docs/data_set/delitos_sexuales_atlantico_limpio.csv<br/>(16,664 filas, 3.86 MB)"]
    end

    subgraph S3["3. ALMACENAMIENTO NUBE (Supabase PostgreSQL)"]
        SUPABASE[("PostgreSQL 17 en Supabase<br/>Host: aws-0-us-east-2.pooler.supabase.com<br/>Tabla: delitos_sexuales_atlantico<br/>8 Índices B-Tree + Vistas analíticas<br/>(16,664 registros cargados)")]
    end

    subgraph S4["4. SERVICIOS BACKEND (FastAPI en Render)"]
        FASTAPI["API REST FastAPI<br/>Render: https://api-delitos-sexuales-atlantico.onrender.com<br/>Local: http://localhost:8000<br/>- Swagger UI interactivo (/docs)<br/>- Endpoint Power BI (/delitos/powerbi/dataset)<br/>- Filtros avanzados (/delitos?...)<br/>- Fallback de alta disponibilidad a CSV"]
    end

    subgraph S5["5. CAPA DE VISUALIZACIÓN Y REPORTES"]
        POWER_BI["Power BI Desktop (.pbix)<br/>- Modelo en estrella (Fact_Delitos + Dimensiones)<br/>- 5 Páginas de reportes directivos<br/>- Catálogo de medidas DAX"]
        STREAMLIT["Streamlit Dashboard (Python)<br/>- EDA Interactivo (http://localhost:8501)<br/>- 6 Módulos analíticos con Plotly"]
    end

    subgraph S6["6. ENTREGABLE CIENTÍFICO"]
        PAPER["Artículo Científico Word<br/>- ≥4.000 palabras<br/>- ≥15 referencias APA 7ª ed.<br/>- Evidencias gráficas de todas las herramientas"]
    end

    RAW_CSV --> ETL
    ETL --> CLEAN_CSV
    CLEAN_CSV --> SUPABASE
    SUPABASE <--> FASTAPI
    FASTAPI --> POWER_BI
    SUPABASE -.->|Conexión Directa| POWER_BI
    CLEAN_CSV --> STREAMLIT
    STREAMLIT --> PAPER
    POWER_BI --> PAPER
    SUPABASE --> PAPER
```

---

## 📂 3. Mapa de Componentes y Carpetas

```
mineria_delitos_sexuales_policia_nacional/
├── backend/                              # Microservicio Backend y Pipeline ETL
│   ├── .venv/                            # Entorno virtual Python 3.11 aislado
│   ├── app/                              # Código fuente de FastAPI
│   │   ├── main.py                       # App FastAPI, CORS universal y Swagger metadata
│   │   ├── core/
│   │   │   ├── config.py                 # Lectura de variables .env con Pydantic Settings
│   │   │   └── database.py               # Motor SQLAlchemy y generador de sesiones get_db
│   │   ├── models/delito.py              # Modelo ORM de la tabla delitos_sexuales_atlantico
│   │   ├── schemas/delito.py             # Esquemas Pydantic v2 (validación y ejemplos)
│   │   ├── services/delito_service.py    # Consultas SQL, agregaciones y fallback a CSV
│   │   └── api/v1/endpoints/delitos.py   # 9 Endpoints REST documentados para Swagger
│   ├── scripts/
│   │   ├── clean_and_filter_atlantico.py # Script ETL de limpieza y normalización
│   │   ├── upload_to_supabase.py         # Script de carga batch masiva hacia PostgreSQL
│   │   ├── test_db_connection.py         # Script para probar conexiones de Supabase
│   │   └── test_api_endpoints.py         # Script de tests automatizados de la API
│   ├── requirements.txt                  # Dependencias de Python (FastAPI, SQLAlchemy, Pandas)
│   ├── .env                              # Archivo con credenciales reales (ignorado por Git)
│   ├── .env.example                      # Plantilla de variables de entorno
│   ├── AGENTS.md                         # Protocolo de trabajo para agentes IA en backend
│   └── README.md                         # Guía técnica del backend
├── analytics/                            # Dashboard EDA con Streamlit
│   ├── app.py                            # Aplicación interactiva Streamlit (6 módulos)
│   ├── utils/data_loader.py              # Carga y caché en memoria con @st.cache_data
│   ├── .streamlit/config.toml            # Configuración de tema visual institucional
│   ├── requirements.txt                  # Dependencias de visualización (Streamlit, Plotly)
│   ├── .env.example                      # Variables de entorno para analítica
│   ├── AGENTS.md                         # Protocolo para agentes en Analytics
│   └── README.md                         # Instrucciones de arranque de Streamlit
├── frontend/                             # Portal Web de visualización complementario
│   ├── AGENTS.md                         # Contexto de frontend
│   └── README.md                         # Documentación de frontend
├── docs/                                 # Documentación técnica exhaustiva
│   ├── GUIA_COMPLETA_DEL_PROYECTO.md     # ESTE DOCUMENTO (Manual integral para desarrolladores)
│   ├── tasks/
│   │   ├── MASTER_STATUS.md              # Tablero central de control de tareas y Git Flow
│   │   └── fases/                        # Desglose de tareas por fases (01 a 05)
│   ├── documentacion/                    # Guías técnicas profundas
│   │   ├── 01_DECISIONES_METODOLOGICAS_FILTRADO.md # Justificación de cero pérdidas
│   │   ├── 02_DIAGRAMA_Y_MODELO_BASE_DATOS.md      # Esquema relacional, tipos e índices
│   │   ├── 03_CATALOGO_ENDPOINTS_API.md            # Catálogo completo de endpoints REST
│   │   ├── 04_FLUJO_ARQUITECTURA_Y_PROCESOS.md     # Flujos de datos y arquitectura
│   │   └── 05_ESTANDARIZACION_Y_BUENAS_PRACTICAS.md# Buenas prácticas de ingeniería
│   ├── architecture/ARCHITECTURE.md      # Diagramas en Mermaid (flujo, secuencia, ERD)
│   ├── database/
│   │   ├── supabase_ddl.sql              # Script DDL SQL ejecutable en Supabase
│   │   └── DATABASE_SCHEMA.md            # Diccionario físico de datos
│   ├── powerbi/
│   │   ├── ESPECIFICACION_POWERBI.md     # Especificación de 5 páginas de reporte y DAX
│   │   └── POWERBI_GUIDE.md              # Código M para Power Query y conexión Web
│   ├── paper/PLAN_ARTICULO.md            # Esquema para el artículo de 4.000 palabras (APA 7)
│   ├── data_set/                         # Datasets original y procesado
│   │   ├── Reporte__Delitos_sexuales_Policía_Nacional_20261106.csv # Original (405,193 filas)
│   │   └── delitos_sexuales_atlantico_limpio.csv                  # Limpio (16,664 filas)
│   ├── AGENTS.md                         # Contexto de documentación
│   └── README.md                         # Índice general de documentación
├── render.yaml                           # Manifiesto de Infraestructura como Código (IaC) para Render
├── AGENTS.md                             # Contexto maestro del repositorio para agentes IA
└── README.md                             # Documentación principal en la raíz
```

---

## 🗄️ 4. Base de Datos en Supabase (PostgreSQL 17)

### 4.1. Información de Conexión en `backend/.env`
Supabase proporciona dos modos de conexión:
- **Connection Pooler (IPv4 - Recomendado para Local, Render y Power BI):**
  ```env
  DATABASE_URL=postgresql+psycopg2://postgres.cqmofowalebzthxjhfes:[PASSWORD]@aws-0-us-east-2.pooler.supabase.com:6543/postgres
  DATABASE_URL_POOLER=postgresql+psycopg2://postgres.cqmofowalebzthxjhfes:[PASSWORD]@aws-0-us-east-2.pooler.supabase.com:6543/postgres
  ```
  > **Nota de red:** Supabase requiere el uso del Connection Pooler (puerto `6543` o `5432`) para redes IPv4 estándar residenciales y para plataformas como Render, evitando errores de resolución DNS.
- **Conexión Directa (IPv6):**
  ```env
  DIRECT_URL=postgresql+psycopg2://postgres:[PASSWORD]@db.cqmofowalebzthxjhfes.supabase.co:5432/postgres
  ```

### 4.2. Estructura de la Tabla `delitos_sexuales_atlantico`
La tabla cuenta con **20 columnas** oficiales y de auditoría (sin columna sintética `id`):
- `departamento` (`VARCHAR(50)`): `'ATLÁNTICO'`.
- `municipio` (`VARCHAR(100)`): Nombre limpio del municipio (Barranquilla, Soledad, etc.).
- `codigo_dane` (`VARCHAR(20)`): Código oficial DANE (8 dígitos, ej. `08001000`).
- `armas_medios` (`VARCHAR(100)`): Medio o arma utilizada.
- `fecha_hecho` (`DATE`): Fecha del suceso (`YYYY-MM-DD`).
- `anio` (`SMALLINT`): Año cronológico (2010 a 2026).
- `mes` (`SMALLINT`), `nombre_mes` (`VARCHAR(20)`), `dia` (`SMALLINT`), `dia_semana` (`VARCHAR(20)`).
- `trimestre` (`SMALLINT`), `semestre` (`SMALLINT`).
- `genero` (`VARCHAR(30)`): `FEMENINO`, `MASCULINO`, `NO REPORTADO`.
- `grupo_etario` (`VARCHAR(30)`): `ADULTOS`, `MENORES`, `ADOLESCENTES`, `NO REPORTADO`.
- `cantidad` (`INTEGER`): Número de víctimas reportadas ($\ge 1$).
- `codigo_articulo` (`VARCHAR(30)`): Código penal extraído (ej. `ARTÍCULO 209`).
- `delito` (`TEXT`): Descripción jurídica íntegra.
- `fecha_descarga_dataset` (`DATE`): Constante de auditoría `'2026-11-06'`.
- `origen_datos` (`VARCHAR(150)`): Procedencia institucional.
- `creado_en` (`TIMESTAMPTZ`): Timestamp de inserción en la base de datos.

### 4.3. Índices Creados para Optimización Analítica
1. `idx_delitos_anio_muni` sobre `(anio, municipio)`.
2. `idx_delitos_demografico` sobre `(genero, grupo_etario)`.
3. `idx_delitos_fecha_hecho` sobre `(fecha_hecho)`.
4. `idx_delitos_articulo` sobre `(codigo_articulo)`.
5. `idx_delitos_anio`, `idx_delitos_municipio`, `idx_delitos_genero`, `idx_delitos_grupo_etario`.

---

## 🚀 5. Backend en FastAPI y Swagger UI

El backend está desarrollado con **FastAPI**, **SQLAlchemy** y **Pydantic v2**, e implementa un **mecanismo de alta disponibilidad**: si la base de datos remota llegase a experimentar latencia o desconexión, el backend recurre de forma transparente al archivo CSV limpio en memoria (`docs/data_set/delitos_sexuales_atlantico_limpio.csv`), evitando que las solicitudes de Power BI o los evaluadores reciban errores HTTP 500.

### 5.1. Los 9 Endpoints de la API:
1. `GET /health` ➡️ Health check para Render y monitor de uptime.
2. `GET /api/v1/delitos` ➡️ Listado paginado con soporte de 20 filtros multidimensionales (fechas, años, municipio, género, edad, ley, búsqueda libre).
3. `GET /api/v1/delitos/filtros/opciones` ➡️ Catálogo dinámico para poblar selects de interfaces con los 23 municipios, años y artículos penales.
4. `GET /api/v1/delitos/powerbi/dataset` ➡️ Entrega completa de los 16,664 registros en formato plano JSON para Power BI Desktop.
5. `GET /api/v1/delitos/metricas/anual` ➡️ Serie de tiempo cronológica anual (2010 a 2026).
6. `GET /api/v1/delitos/metricas/municipios?top=10` ➡️ Ranking municipal con total de casos y porcentaje de participación.
7. `GET /api/v1/delitos/metricas/genero` ➡️ Proporción porcentual por género de la víctima.
8. `GET /api/v1/delitos/metricas/grupo-etario` ➡️ Desglose por grupos de edad (adultos, adolescentes, menores de 14 años).
9. `GET /api/v1/delitos/metricas/articulos?top=10` ➡️ Frecuencia de los artículos penales más vulnerados.

### 5.2. Despliegue en Render Cloud (`render.yaml`)
El archivo `render.yaml` en la raíz permite desplegar el backend en Render con un solo clic:
- Tipo: `Web Service` (Python 3.11).
- Directorio Raíz: `backend`.
- Comando de Construcción: `pip install -r requirements.txt`.
- Comando de Inicio: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`.
- Variable de Entorno: `DATABASE_URL` (se sincroniza con la cadena del pooler de Supabase).

---

## 📊 6. Visualizaciones: Streamlit y Power BI

### 6.1. Dashboard EDA en Streamlit (`analytics/app.py`)
Diseñado para la exploración interactiva y para capturar las evidencias académicas:
- **Pestaña 1 (Tendencia Temporal):** Gráfico de líneas anual (2010–2026), estacionalidad por meses y días de la semana con mayor incidencia.
- **Pestaña 2 (Análisis Demográfico):** Distribución por género (85.1% femenino), grupos etarios y gráfico bivariado cruzado.
- **Pestaña 3 (Distribución Geográfica):** Top de concentración municipal (Barranquilla 52.7%, Soledad 21.7%).
- **Pestaña 4 (Tipología Penal y Armas):** Artículos penales más frecuentes (Art. 209 encabeza denuncias) y medios empleados.
- **Pestaña 5 (Matriz de Intensidad / Heatmap):** Mapa de calor cruzando los municipios principales contra grupos etarios.
- **Pestaña 6 (Explorador de Datos):** Tabla paginada con botón para descargar los datos filtrados en CSV.

### 6.2. Dashboard Directivo en Power BI Desktop (`.pbix`)
La especificación detallada está en `docs/powerbi/ESPECIFICACION_POWERBI.md`:
- **5 Páginas de Tablero:** Resumen Ejecutivo, Series de Tiempo, Desglose Demográfico, Distribución Territorial en Mapa y Tipología Penal.
- **Medidas DAX Listas:** `Total Casos`, `Total Victimas`, `Casos Año Anterior`, `Variacion % Interanual`, `% Victimas Femeninas`, `% Infancia y Adolescencia`, `% Concentracion Metropolitana`.
- **Conexión en Power Query:** Código M documentado en `docs/powerbi/POWERBI_GUIDE.md` apuntando al endpoint de Render o local.

---

## ⚡ 7. Guía de Arranque Rápido para el Nuevo Desarrollador (5 Minutos)

### Paso 1: Clonar y Ubicarse en el Directorio
```powershell
cd e:\IA-UNIVERSIDAD\mineria_delitos_sexuales_policia_nacional
```

### Paso 2: Activar el Entorno Virtual de Python
```powershell
# En Windows PowerShell
.\backend\.venv\Scripts\Activate.ps1
```

### Paso 3: Probar la Conexión a la Base de Datos en Supabase
```powershell
.\backend\.venv\Scripts\python.exe backend/scripts/test_db_connection.py
```
*Debe retornar `[SUCCESS] DATABASE_URL conectó correctamente! Total registros: 16664`.*

### Paso 4: Iniciar el Backend FastAPI
```powershell
cd backend
..\backend\.venv\Scripts\uvicorn.exe app.main:app --reload --port 8000
```
- Abra en su navegador: **[http://localhost:8000/docs](http://localhost:8000/docs)** para ver Swagger UI interactivo.

### Paso 5: Iniciar el Dashboard EDA en Streamlit
En una nueva pestaña de PowerShell:
```powershell
cd e:\IA-UNIVERSIDAD\mineria_delitos_sexuales_policia_nacional\analytics
..\backend\.venv\Scripts\streamlit.exe run app.py --server.port 8501
```
- Abra en su navegador: **[http://localhost:8501](http://localhost:8501)**.

### Paso 6: Ejecutar las Pruebas Automatizadas de los Endpoints
```powershell
.\backend\.venv\Scripts\python.exe backend/scripts/test_api_endpoints.py
```
*Valida que los 9 endpoints respondan código HTTP 200 con tipos de datos correctos.*

---

## ❓ 8. Preguntas Frecuentes y Solución de Problemas (FAQ)

### ¿Qué hago si cambio de base de datos o quiero recargar los datos?
Simplemente actualice la variable `DATABASE_URL` en `backend/.env` y ejecute:
```powershell
.\backend\.venv\Scripts\python.exe backend/scripts/upload_to_supabase.py
```
El script creará automáticamente las tablas, índices e insertará los 16,664 registros limpios en lotes de 2,000 filas.

### ¿Por qué se usa el puerto 6543 en Supabase en lugar del 5432?
El puerto `6543` corresponde al **Supabase Connection Pooler** (PgBouncer en modo transacción). Es el puerto oficial para redes IPv4 estándar (la mayoría de conexiones residenciales en Colombia y los servidores de Render). Si se utiliza la conexión directa en `db.xxxx.supabase.co:5432`, puede fallar por falta de soporte IPv6 local.

### ¿Dónde encuentro la lista de tareas y qué falta por hacer?
Revise el archivo maestro [docs/tasks/MASTER_STATUS.md](file:///e:/IA-UNIVERSIDAD/mineria_delitos_sexuales_policia_nacional/docs/tasks/MASTER_STATUS.md), el cual se mantiene sincronizado como fuente única de la verdad del proyecto.

