#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
CARGA MASIVA A SUPABASE / NEON POSTGRESQL (SIN COLUMNA ID)
=============================================================================
Carga los 16,664 registros limpios de 'delitos_sexuales_atlantico_limpio.csv'
hacia la tabla 'delitos_sexuales_atlantico' en PostgreSQL (Supabase / Neon).
=============================================================================
"""

import os
import sys
import logging
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv("backend/.env")

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("Upload_Supabase")

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CLEAN_CSV_PATH = os.path.join(BASE_DIR, "docs", "data_set", "delitos_sexuales_atlantico_limpio.csv")

def obtener_database_url():
    url = os.getenv("DATABASE_URL_POOLER") or os.getenv("DATABASE_URL")
    if not url or "YOUR_PASSWORD" in url or "localhost" in url:
        return None
    if url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql+psycopg2://", 1)
    elif url.startswith("postgresql://") and not url.startswith("postgresql+"):
        url = url.replace("postgresql://", "postgresql+psycopg2://", 1)
    return url

DATABASE_URL = obtener_database_url()

def subir_datos():
    if not DATABASE_URL:
        logger.warning("DATABASE_URL no está configurada para producción en el archivo .env.")
        return

    if not os.path.exists(CLEAN_CSV_PATH):
        logger.error(f"No se encontró el archivo limpio en: {CLEAN_CSV_PATH}")
        sys.exit(1)

    logger.info(f"Leyendo dataset limpio: {CLEAN_CSV_PATH}")
    df = pd.read_csv(CLEAN_CSV_PATH)
    
    # Asegurar que la columna 'id' no esté presente en el DataFrame
    if "id" in df.columns:
        df = df.drop(columns=["id"])
        
    total_filas = len(df)
    logger.info(f"Total registros a cargar (sin columna id): {total_filas:,}")
    logger.info(f"Columnas a cargar: {list(df.columns)}")

    engine = create_engine(DATABASE_URL, pool_pre_ping=True)

    with engine.connect() as conn:
        logger.info("Verificando conexión a PostgreSQL...")
        res = conn.execute(text("SELECT version();")).scalar()
        logger.info(f"Conectado exitosamente: {res}")

        # Recrear tabla sin columna ID
        logger.info("Recreando tabla 'delitos_sexuales_atlantico' sin columna ID...")
        ddl_script = """
        DROP TABLE IF EXISTS delitos_sexuales_atlantico CASCADE;

        CREATE TABLE delitos_sexuales_atlantico (
            departamento VARCHAR(50) NOT NULL DEFAULT 'ATLÁNTICO',
            municipio VARCHAR(100) NOT NULL,
            codigo_dane VARCHAR(20) NOT NULL,
            armas_medios VARCHAR(100) NOT NULL DEFAULT 'NO REPORTADO',
            fecha_hecho DATE NOT NULL,
            anio SMALLINT NOT NULL,
            mes SMALLINT NOT NULL,
            nombre_mes VARCHAR(20) NOT NULL,
            dia SMALLINT NOT NULL,
            dia_semana VARCHAR(20) NOT NULL,
            trimestre SMALLINT NOT NULL,
            semestre SMALLINT NOT NULL,
            genero VARCHAR(30) NOT NULL DEFAULT 'NO REPORTADO',
            grupo_etario VARCHAR(30) NOT NULL DEFAULT 'NO REPORTADO',
            cantidad INTEGER NOT NULL DEFAULT 1,
            codigo_articulo VARCHAR(30) NOT NULL,
            delito TEXT NOT NULL,
            fecha_descarga_dataset DATE NOT NULL DEFAULT '2026-11-06',
            origen_datos VARCHAR(150) NOT NULL DEFAULT 'Policía Nacional de Colombia - Datos Abiertos',
            creado_en TIMESTAMPTZ NOT NULL DEFAULT NOW()
        );

        CREATE INDEX IF NOT EXISTS idx_delitos_anio ON delitos_sexuales_atlantico(anio);
        CREATE INDEX IF NOT EXISTS idx_delitos_municipio ON delitos_sexuales_atlantico(municipio);
        CREATE INDEX IF NOT EXISTS idx_delitos_articulo ON delitos_sexuales_atlantico(codigo_articulo);
        CREATE INDEX IF NOT EXISTS idx_delitos_genero ON delitos_sexuales_atlantico(genero);
        CREATE INDEX IF NOT EXISTS idx_delitos_grupo_etario ON delitos_sexuales_atlantico(grupo_etario);
        CREATE INDEX IF NOT EXISTS idx_delitos_fecha_hecho ON delitos_sexuales_atlantico(fecha_hecho);
        CREATE INDEX IF NOT EXISTS idx_delitos_anio_muni ON delitos_sexuales_atlantico(anio, municipio);
        CREATE INDEX IF NOT EXISTS idx_delitos_demografico ON delitos_sexuales_atlantico(genero, grupo_etario);

        CREATE OR REPLACE VIEW vista_resumen_anual_municipio AS
        SELECT 
            anio,
            municipio,
            codigo_articulo,
            COUNT(*) AS total_casos,
            SUM(cantidad) AS total_victimas
        FROM delitos_sexuales_atlantico
        GROUP BY anio, municipio, codigo_articulo;

        CREATE OR REPLACE VIEW vista_perfil_demografico_anual AS
        SELECT 
            anio,
            genero,
            grupo_etario,
            COUNT(*) AS total_casos,
            SUM(cantidad) AS total_victimas
        FROM delitos_sexuales_atlantico
        GROUP BY anio, genero, grupo_etario;
        """
        conn.execute(text(ddl_script))
        conn.commit()
        logger.info("Estructura sin ID verificada y creada.")

        logger.info("Iniciando inserción masiva por lotes...")
        df.to_sql(
            "delitos_sexuales_atlantico",
            con=engine,
            if_exists="append",
            index=False,
            chunksize=2000,
            method="multi"
        )
        logger.info("Carga masiva finalizada con éxito.")

        finales = conn.execute(text("SELECT COUNT(*) FROM delitos_sexuales_atlantico;")).scalar()
        logger.info(f"Total registros verificados en base de datos: {finales:,}")

if __name__ == "__main__":
    subir_datos()
