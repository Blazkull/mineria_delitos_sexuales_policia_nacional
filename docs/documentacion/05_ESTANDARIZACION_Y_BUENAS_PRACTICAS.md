# 🛡️ Guía de Estandarización, Buenas Prácticas y Calidad de Software

> **Alineado con:** Principios Senior Fullstack, Database Architect y Reglas Maestras del Repositorio  

---

## 1. Buenas Prácticas en Procesamiento de Datos (Python & Pandas)

1. **Aislamiento de Dependencias:** Todo script o servicio del backend opera estrictamente dentro del entorno virtual `.venv` (`backend/.venv`), asegurando reproducibilidad independientemente de la máquina del evaluador.
2. **Inmutabilidad de la Fuente Primaria:** El archivo crudo original descargado de la Policía Nacional jamás se sobrescribe ni se altera (`ReadOnly`).
3. **Control de Calidad Automatizado:** Todo pipeline ETL incluye aserciones matemáticas:
   - Verificación de igualdad de filas: `len(df_clean) == len(df_raw_filtrado)`.
   - Control de valores nulos finales: `df_clean.isnull().sum() == 0`.
4. **Tipado de Datos Estricto:** Evitar columnas de tipo `object` genérico; usar enteros explícitos para fechas (`Int64`), cadenas limpias (`str`) y fechas ISO-8601 (`YYYY-MM-DD`).

---

## 2. Buenas Prácticas en Base de Datos (PostgreSQL en Supabase)

1. **Eficiencia en Tipos de Datos:**
   - Uso de `SMALLINT` para años y meses (2 bytes vs 4 bytes de un Integer regular).
   - Uso de `DATE` nativo en lugar de cadenas de texto para fechas del hecho.
   - Uso de `BIGSERIAL` para garantizar escalabilidad ilimitada en la clave primaria.
2. **Compatibilidad con PgBouncer:**
   - En SQLAlchemy se especifica `connect_args={"statement_cache_size": 0}` para operar en modo Transaction Pooling de Supabase / Neon sin errores de prepared statements.
3. **Indexación Estratégica:** No sobre-indexar; crear únicamente índices en columnas que formen parte de cláusulas `WHERE`, `GROUP BY` o `ORDER BY` en los dashboards.

---

## 3. Buenas Prácticas en Backend API (FastAPI)

1. **Pydantic v2:** Uso exclusivo de sintaxis moderna de Pydantic v2 (`model_config = ConfigDict(from_attributes=True)`).
2. **Alta Disponibilidad y Resiliencia:** El backend cuenta con un mecanismo de fallback: si la base de datos remota entra en suspensión o experimenta latencia, el servicio sirve inmediatamente las peticiones desde el CSV limpio en memoria, garantizando que Power BI o Swagger nunca reciban un error HTTP 500.
3. **CORS Habilitado:** Cabeceras abiertas para permitir consultas desde Power BI Web, Streamlit y cualquier cliente JavaScript.

---

## 4. Buenas Prácticas en Power BI Desktop

1. **Separación de Medidas:** Crear una tabla dedicada `_Medidas` exclusivamente para almacenar fórmulas DAX con formato numérico explícito.
2. **Esquema en Estrella (Star Schema):** Relacionar la tabla de hechos con tablas dimensionales (`Dim_Calendario`, `Dim_Municipio`) con cardinalidad 1 a Varios (1:*), evitando relaciones bidireccionales innecesarias que degraden el rendimiento.
3. **Compresión VertiPaq:** Cargar únicamente las columnas necesarias para el análisis.

