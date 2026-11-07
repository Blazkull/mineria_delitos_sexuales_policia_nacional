-- =============================================================================
-- SCRIPT DDL: BASE DE DATOS DELITOS SEXUALES - POLICÍA NACIONAL (ATLÁNTICO)
-- Plataforma: PostgreSQL 17 (Supabase / Neon)
-- Asignatura: Minería de Datos
-- Fecha de Descarga del Dataset: 2026-11-06
-- Cantidad de Registros Esperados: 16,664 registros íntegros
-- NOTA: Tabla limpia con columnas del dataset procesado (SIN COLUMNA ID)
-- SEGURIDAD: ROW LEVEL SECURITY (RLS) HABILITADO
-- =============================================================================

-- 1. Eliminación preventiva para regeneración limpia
DROP TABLE IF EXISTS delitos_sexuales_atlantico CASCADE;

-- 2. Creación de la Tabla Principal (Sin columna ID)
CREATE TABLE IF NOT EXISTS delitos_sexuales_atlantico (
    -- Ubicación Geográfica
    departamento VARCHAR(50) NOT NULL DEFAULT 'ATLÁNTICO',
    municipio VARCHAR(100) NOT NULL,
    codigo_dane VARCHAR(20) NOT NULL,
    
    -- Hecho y Medios
    armas_medios VARCHAR(100) NOT NULL DEFAULT 'NO REPORTADO',
    fecha_hecho DATE NOT NULL,
    
    -- Dimensiones Temporales Precalculadas para Analítica y Power BI
    anio SMALLINT NOT NULL,
    mes SMALLINT NOT NULL,
    nombre_mes VARCHAR(20) NOT NULL,
    dia SMALLINT NOT NULL,
    dia_semana VARCHAR(20) NOT NULL,
    trimestre SMALLINT NOT NULL,
    semestre SMALLINT NOT NULL,
    
    -- Dimensiones Demográficas
    genero VARCHAR(30) NOT NULL DEFAULT 'NO REPORTADO',
    grupo_etario VARCHAR(30) NOT NULL DEFAULT 'NO REPORTADO',
    cantidad INTEGER NOT NULL DEFAULT 1,
    
    -- Tipificación Penal
    codigo_articulo VARCHAR(30) NOT NULL,
    delito TEXT NOT NULL,
    
    -- Auditoría de Extracción (Requisito Universitario)
    fecha_descarga_dataset DATE NOT NULL DEFAULT '2026-11-06',
    origen_datos VARCHAR(150) NOT NULL DEFAULT 'Policía Nacional de Colombia - Datos Abiertos',
    creado_en TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- 3. Índices B-Tree para Aceleración de Consultas Analíticas y Power BI
CREATE INDEX IF NOT EXISTS idx_delitos_anio ON delitos_sexuales_atlantico(anio);
CREATE INDEX IF NOT EXISTS idx_delitos_municipio ON delitos_sexuales_atlantico(municipio);
CREATE INDEX IF NOT EXISTS idx_delitos_articulo ON delitos_sexuales_atlantico(codigo_articulo);
CREATE INDEX IF NOT EXISTS idx_delitos_genero ON delitos_sexuales_atlantico(genero);
CREATE INDEX IF NOT EXISTS idx_delitos_grupo_etario ON delitos_sexuales_atlantico(grupo_etario);
CREATE INDEX IF NOT EXISTS idx_delitos_fecha_hecho ON delitos_sexuales_atlantico(fecha_hecho);
CREATE INDEX IF NOT EXISTS idx_delitos_anio_muni ON delitos_sexuales_atlantico(anio, municipio);
CREATE INDEX IF NOT EXISTS idx_delitos_demografico ON delitos_sexuales_atlantico(genero, grupo_etario);

-- 4. Vistas Analíticas Pre-Agregadas para Power BI / Metabase / Direct Query

-- Vista 1: Resumen Anual por Municipio y Tipología
CREATE OR REPLACE VIEW vista_resumen_anual_municipio AS
SELECT 
    anio,
    municipio,
    codigo_articulo,
    COUNT(*) AS total_casos,
    SUM(cantidad) AS total_victimas
FROM delitos_sexuales_atlantico
GROUP BY anio, municipio, codigo_articulo;

-- Vista 2: Perfil Demográfico por Año
CREATE OR REPLACE VIEW vista_perfil_demografico_anual AS
SELECT 
    anio,
    genero,
    grupo_etario,
    COUNT(*) AS total_casos,
    SUM(cantidad) AS total_victimas
FROM delitos_sexuales_atlantico
GROUP BY anio, genero, grupo_etario;

-- 5. Configuración de Seguridad de Filas (Row Level Security - RLS)
ALTER TABLE delitos_sexuales_atlantico ENABLE ROW LEVEL SECURITY;

-- Política A: Permitir lectura pública para anon, authenticated y postgres
DROP POLICY IF EXISTS "Permitir lectura publica de delitos sexuales" ON delitos_sexuales_atlantico;
CREATE POLICY "Permitir lectura publica de delitos sexuales" 
ON delitos_sexuales_atlantico 
FOR SELECT 
TO anon, authenticated, postgres
USING (true);

-- Política B: Restringir operaciones de escritura (INSERT, UPDATE, DELETE) solo a service_role y postgres
DROP POLICY IF EXISTS "Restringir escritura a service_role y postgres" ON delitos_sexuales_atlantico;
CREATE POLICY "Restringir escritura a service_role y postgres" 
ON delitos_sexuales_atlantico 
FOR ALL 
TO service_role, postgres
USING (true)
WITH CHECK (true);
