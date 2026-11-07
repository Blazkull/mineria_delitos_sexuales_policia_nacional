#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
ETL PIPELINE: Limpieza, Filtrado y Normalización de Delitos Sexuales (Atlántico)
=============================================================================
Asignatura: Minería de Datos
Fuente de Datos: Policía Nacional de Colombia - Datos Abiertos (datos.gov.co)
Fecha de Descarga: 2026-11-06
Objetivo:
    1. Cargar el dataset crudo nacional (405,193 registros).
    2. Filtrar exclusivamente los registros del Departamento del ATLÁNTICO.
    3. Garantizar CERO pérdida de registros (preservar los 16,664 registros íntegros).
    4. Imputar y estandarizar valores nulos o vacíos ('NO REPORTADO').
    5. Normalizar texto, corregir codificación Mojibake y estandarizar nombres de municipios.
    6. Parsear fechas y extraer columnas temporales analíticas (año, mes, día, día semana, trimestre).
    7. Agregar columnas de auditoría ('fecha_descarga_dataset', 'origen_datos').
    8. Exportar dataset limpio a 'docs/data_set/delitos_sexuales_atlantico_limpio.csv'.
=============================================================================
"""

import os
import sys
import re
import logging
from datetime import datetime
import pandas as pd
import numpy as np

# Configuración de Logging profesional
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("ETL_Delitos_Atlantico")

# Rutas de Archivos relativas a la raíz del repositorio
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RAW_CSV_PATH = os.path.join(BASE_DIR, "docs", "data_set", "Reporte__Delitos_sexuales_Policía_Nacional_20261106.csv")
CLEAN_CSV_PATH = os.path.join(BASE_DIR, "docs", "data_set", "delitos_sexuales_atlantico_limpio.csv")

FECHA_DESCARGA_FIJA = "2026-11-06"
ORIGEN_DATOS_FIJO = "Policía Nacional de Colombia - Datos Abiertos"

# Mapeo de meses en español
MESES_ESP = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}

# Mapeo de días de la semana en español
DIAS_ESP = {
    0: "Lunes", 1: "Martes", 2: "Miércoles", 3: "Jueves",
    4: "Viernes", 5: "Sábado", 6: "Domingo"
}

def reparar_mojibake(texto: str) -> str:
    """Corrige artefactos de doble codificación o caracteres corruptos en texto."""
    if not isinstance(texto, str):
        return texto
    reemplazos = {
        "ARTÃ CULO": "ARTÍCULO",
        "ARTÃ\x8dCULO": "ARTÍCULO",
        "AGRAVACIÃ“N": "AGRAVACIÓN",
        "AÃ‘OS": "AÑOS",
        "MonterÃ\xada": "Montería",
        "MonterÃ­a": "Montería",
        "CÃ“RDOBA": "CÓRDOBA",
        "Ã\x81": "Á", "Ã‰": "É", "Ã\x8d": "Í", "Ã“": "Ó", "Ãš": "Ú",
        "Ã¡": "á", "Ã©": "é", "Ã­": "í", "Ã³": "ó", "Ãº": "ú",
        "Ã±": "ñ", "Ã‘": "Ñ",
    }
    res = texto
    for k, v in reemplazos.items():
        res = res.replace(k, v)
    return res.strip()

def extraer_articulo(delito_str: str) -> str:
    """Extrae el número o referencia del artículo penal (ej. 'ARTÍCULO 209')."""
    if not isinstance(delito_str, str):
        return "OTRO"
    match = re.search(r"(ART[ÍI]CULO\s+\d+[\s\w\.]*)", delito_str, re.IGNORECASE)
    if match:
        part = match.group(1).split(".")[0].strip().upper()
        return part
    return "OTRO"

def normalizar_municipio(mun_str: str) -> str:
    """Remueve sufijos administrativos como ' (CT)' y limpia espacios."""
    if not isinstance(mun_str, str):
        return "DESCONOCIDO"
    mun_limpio = re.sub(r"\s*\([Cc][Tt]\)", "", mun_str).strip()
    return mun_limpio

def ejecutar_etl():
    logger.info("=" * 70)
    logger.info("INICIANDO PIPELINE DE MINERÍA DE DATOS - POLICÍA NACIONAL")
    logger.info("=" * 70)
    logger.info(f"Ruta de dataset crudo: {RAW_CSV_PATH}")

    if not os.path.exists(RAW_CSV_PATH):
        logger.error(f"El archivo fuente no existe: {RAW_CSV_PATH}")
        sys.exit(1)

    # 1. Carga con detección y manejo de codificación
    logger.info("Cargando dataset crudo nacional...")
    encodings_to_try = ["utf-8", "latin-1", "cp1252"]
    df_raw = None
    for enc in encodings_to_try:
        try:
            df_raw = pd.read_csv(RAW_CSV_PATH, encoding=enc, low_memory=False)
            logger.info(f"Dataset cargado exitosamente con codificación: {enc}")
            break
        except Exception as e:
            logger.warning(f"Fallo carga con {enc}: {e}")

    if df_raw is None:
        logger.error("No fue posible leer el archivo con las codificaciones especificadas.")
        sys.exit(1)

    total_nacional = len(df_raw)
    logger.info(f"Total registros a nivel nacional: {total_nacional:,}")

    # Normalizar nombres de columnas a mayúsculas limpias
    df_raw.columns = [c.strip().upper() for c in df_raw.columns]
    logger.info(f"Columnas detectadas: {list(df_raw.columns)}")

    # 2. Filtrado estricto por Departamento del Atlántico
    logger.info("Filtrando registros del departamento del Atlántico...")
    # Asegurar coincidencia robusta (con o sin tilde)
    mask_atlantico = df_raw["DEPARTAMENTO"].astype(str).str.upper().str.contains("ATL", na=False)
    df_atl = df_raw[mask_atlantico].copy()
    total_atlantico = len(df_atl)

    logger.info(f"Registros encontrados para el Atlántico: {total_atlantico:,}")
    if total_atlantico != 16664:
        logger.warning(f"Observación: Se esperaban 16,664 registros y se obtuvieron {total_atlantico:,}")

    # 3. Limpieza y Reparación Tipográfica
    logger.info("Normalizando cadenas de texto y reparando codificación...")
    for col in ["DEPARTAMENTO", "MUNICIPIO", "ARMAS MEDIOS", "GENERO", "GRUPO ETARIO", "delito".upper()]:
        if col in df_atl.columns:
            df_atl[col] = df_atl[col].astype(str).apply(reparar_mojibake)

    # 4. Tratamiento e Imputación de Nulos (NO DROP POLICY)
    logger.info("Aplicando regla no negociable: Cero eliminación de registros. Imputando nulos...")
    
    # Estandarizar Municipio
    df_atl["municipio_estandar"] = df_atl["MUNICIPIO"].apply(normalizar_municipio)

    # Género: Imputar vacíos o nulos
    df_atl["GENERO"] = df_atl["GENERO"].replace(["", "nan", "NAN", "NULL", "None"], np.nan)
    df_atl["GENERO"] = df_atl["GENERO"].fillna("NO REPORTADO").str.strip().str.upper()
    df_atl["GENERO"] = df_atl["GENERO"].replace({"NO REPORTA": "NO REPORTADO"})

    # Grupo Etario: Imputar vacíos o nulos
    df_atl["GRUPO ETARIO"] = df_atl["GRUPO ETARIO"].replace(["", "nan", "NAN", "NULL", "None"], np.nan)
    df_atl["GRUPO ETARIO"] = df_atl["GRUPO ETARIO"].fillna("NO REPORTADO").str.strip().str.upper()

    # Armas / Medios
    df_atl["ARMAS MEDIOS"] = df_atl["ARMAS MEDIOS"].replace(["", "nan", "NAN", "NULL", "None"], np.nan)
    df_atl["ARMAS MEDIOS"] = df_atl["ARMAS MEDIOS"].fillna("NO REPORTADO").str.strip().str.upper()

    # Cantidad: asegurar entero positivo
    df_atl["CANTIDAD"] = pd.to_numeric(df_atl["CANTIDAD"], errors="coerce").fillna(1).astype(int)

    # Delito y Extracción de Artículo Penal
    df_atl["DELITO_NOMBRE"] = df_atl["delito".upper()].str.strip().str.upper()
    df_atl["codigo_articulo"] = df_atl["DELITO_NOMBRE"].apply(extraer_articulo)

    # 5. Parseo de Fechas y Enriquecimiento Temporal
    logger.info("Parseando fechas y extrayendo variables temporales...")
    # FECHA HECHO formato 'DD/MM/YYYY'
    df_atl["fecha_dt"] = pd.to_datetime(df_atl["FECHA HECHO"], format="%d/%m/%Y", errors="coerce")
    
    # Derivación de componentes
    df_atl["anio"] = df_atl["fecha_dt"].dt.year.astype("Int64")
    df_atl["mes"] = df_atl["fecha_dt"].dt.month.astype("Int64")
    df_atl["nombre_mes"] = df_atl["mes"].map(MESES_ESP).fillna("Desconocido")
    df_atl["dia"] = df_atl["fecha_dt"].dt.day.astype("Int64")
    df_atl["dia_semana"] = df_atl["fecha_dt"].dt.day_name(locale=None) if hasattr(df_atl["fecha_dt"].dt, "day_name") else df_atl["fecha_dt"].dt.dayofweek.map(DIAS_ESP)
    # Estandarizar día de la semana con mapeo numérico robusto
    try:
        dia_num = df_atl["fecha_dt"].dt.day_of_week
    except AttributeError:
        dia_num = df_atl["fecha_dt"].dt.dayofweek
    df_atl["dia_semana"] = dia_num.map(DIAS_ESP).fillna("Desconocido")
    df_atl["trimestre"] = df_atl["fecha_dt"].dt.quarter.astype("Int64")
    df_atl["semestre"] = np.where(df_atl["mes"] <= 6, 1, 2)
    df_atl["fecha_formato_iso"] = df_atl["fecha_dt"].dt.strftime("%Y-%m-%d")

    # 6. Adición de Metadatos de Auditoría
    df_atl["fecha_descarga_dataset"] = FECHA_DESCARGA_FIJA
    df_atl["origen_datos"] = ORIGEN_DATOS_FIJO
    df_atl["departamento_estandar"] = "ATLÁNTICO"

    # 7. Construcción de DataFrame Final Estructurado
    df_clean = pd.DataFrame({
        "departamento": df_atl["departamento_estandar"],
        "municipio": df_atl["municipio_estandar"],
        "codigo_dane": df_atl["CODIGO DANE"].astype(str).str.strip().str.zfill(8),
        "armas_medios": df_atl["ARMAS MEDIOS"],
        "fecha_hecho": df_atl["fecha_formato_iso"],
        "anio": df_atl["anio"],
        "mes": df_atl["mes"],
        "nombre_mes": df_atl["nombre_mes"],
        "dia": df_atl["dia"],
        "dia_semana": df_atl["dia_semana"],
        "trimestre": df_atl["trimestre"],
        "semestre": df_atl["semestre"],
        "genero": df_atl["GENERO"],
        "grupo_etario": df_atl["GRUPO ETARIO"],
        "cantidad": df_atl["CANTIDAD"],
        "codigo_articulo": df_atl["codigo_articulo"],
        "delito": df_atl["DELITO_NOMBRE"],
        "fecha_descarga_dataset": df_atl["fecha_descarga_dataset"],
        "origen_datos": df_atl["origen_datos"]
    })

    # 8. Verificaciones de Calidad y Cero Pérdidas
    filas_finales = len(df_clean)
    logger.info("-" * 70)
    logger.info("INFORME DE CONTROL DE CALIDAD:")
    logger.info(f"Total registros originales Atlántico: {total_atlantico}")
    logger.info(f"Total registros procesados limpios:    {filas_finales}")
    assert filas_finales == total_atlantico, "ERROR CRÍTICO: La cantidad de registros no coincide."

    nulos_finales = df_clean.isnull().sum()
    logger.info(f"Conteo de valores nulos finales:\n{nulos_finales[nulos_finales > 0] if (nulos_finales > 0).any() else 'CERO NULOS EN TODAS LAS COLUMNAS'}")

    logger.info("-" * 70)
    logger.info("ESTADÍSTICAS BÁSICAS DEL PERIODO:")
    logger.info(f"Rango de Años: {df_clean['anio'].min()} a {df_clean['anio'].max()}")
    logger.info(f"Total Municipios Únicos: {df_clean['municipio'].nunique()}")
    logger.info(f"Top 5 Municipios con más registros:\n{df_clean['municipio'].value_counts().head(5)}")
    logger.info(f"Distribución por Género:\n{df_clean['genero'].value_counts()}")
    logger.info(f"Distribución por Grupo Etario:\n{df_clean['grupo_etario'].value_counts()}")

    # 9. Exportación a CSV
    logger.info("-" * 70)
    logger.info(f"Exportando archivo limpio a: {CLEAN_CSV_PATH}")
    df_clean.to_csv(CLEAN_CSV_PATH, index=False, encoding="utf-8")
    logger.info(f"Exportación completada exitosamente. Tamaño del archivo: {os.path.getsize(CLEAN_CSV_PATH):,} bytes.")
    logger.info("=" * 70)

if __name__ == "__main__":
    ejecutar_etl()
