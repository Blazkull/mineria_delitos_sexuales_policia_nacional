# 🗄️ Fase 2: Base de Datos PostgreSQL (Supabase / Neon)

> **Estado:** COMPLETADO (100% - Conexión establecida con Supabase Pooler y los 16,664 registros cargados)  
> **Script DDL:** `docs/database/supabase_ddl.sql`  
> **Script de carga batch:** `backend/scripts/upload_to_supabase.py`  

---

## 📋 Lista de Tareas y Checklists

- [x] **2.1. Modelado de Datos Relacional**
  - [x] Selección de tipos SQL óptimos (`BIGSERIAL`, `VARCHAR`, `SMALLINT`, `INTEGER`, `DATE`, `TIMESTAMPTZ`).
  - [x] Definición de clave primaria y valores por defecto (`fecha_descarga_dataset = '2026-11-06'`).
  - [x] Creación de modelo ORM SQLAlchemy en `backend/app/models/delito.py`.

- [x] **2.2. Estrategia de Indexación Analítica**
  - [x] Índice compuesto `idx_delitos_anio_muni` sobre `(anio, municipio)`.
  - [x] Índices simples sobre `codigo_articulo`, `genero`, `grupo_etario`, `fecha_hecho`.
  - [x] Documentación de la justificación técnica de índices en `docs/database/DATABASE_SCHEMA.md`.

- [x] **2.3. Script de Carga Masiva y Automatización**
  - [x] Creación de `backend/scripts/upload_to_supabase.py` con inserción por lotes (`chunksize=2000`).
  - [x] Soporte para conexión directa y conmutación de esquemas.

- [x] **2.4. Despliegue en la Nube y Verificación de Registros**
  - [x] Configuración de cadena de conexión (`DATABASE_URL` y `DATABASE_URL_POOLER`) en `backend/.env`.
  - [x] Validación de conectividad con Supabase Connection Pooler (`aws-0-us-east-2.pooler.supabase.com:6543`).
  - [x] Ejecución de carga masiva: **16,664 registros limpios verificados en Supabase PostgreSQL**.

