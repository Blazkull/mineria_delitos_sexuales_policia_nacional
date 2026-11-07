import os
from typing import Tuple
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

# Cargar variables de entorno desde backend/.env o analytics/.env
for env_candidate in [
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "backend", ".env")),
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env")),
    ".env"
]:
    if os.path.exists(env_candidate):
        load_dotenv(env_candidate)

@st.cache_data(show_spinner=True)
def load_clean_data(file_path: str = None) -> pd.DataFrame:
    """
    Carga y cachea en memoria el dataset limpio de delitos sexuales del Atlántico.
    Prioridad:
    1. Base de datos PostgreSQL en Supabase (si las credenciales están disponibles en .env).
    2. Archivo CSV limpio local (docs/data_set/delitos_sexuales_atlantico_limpio.csv).

    Garantiza:
    - CERO columna sintética 'id'.
    - Tipado estricto de fechas y valores.
    - Metadato explícito sobre la fuente de datos cargada.
    """
    df = None
    fuente_cargada = "Desconocida"

    # 1. Intentar conectar a PostgreSQL en Supabase
    db_url = os.getenv("DATABASE_URL_POOLER") or os.getenv("DATABASE_URL")
    if db_url:
        try:
            from sqlalchemy import create_engine
            engine = create_engine(db_url, pool_pre_ping=True)
            df = pd.read_sql("SELECT * FROM delitos_sexuales_atlantico ORDER BY fecha_hecho ASC", engine)
            if df is not None and len(df) > 0:
                fuente_cargada = "PostgreSQL en Supabase Cloud (aws-0-us-east-2.pooler.supabase.com)"
        except Exception:
            # Fallback transparente a CSV si falla la conexión a la base de datos
            df = None

    # 2. Fallback a CSV local si la base de datos no está disponible o no tiene registros
    if df is None or len(df) == 0:
        if file_path is None:
            possible_paths = [
                os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "docs", "data_set", "delitos_sexuales_atlantico_limpio.csv")),
                os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs", "data_set", "delitos_sexuales_atlantico_limpio.csv")),
                "docs/data_set/delitos_sexuales_atlantico_limpio.csv"
            ]
            for p in possible_paths:
                if os.path.exists(p):
                    file_path = p
                    break

        if not file_path or not os.path.exists(file_path):
            raise FileNotFoundError(f"No se encontró el archivo limpio ni conexión a Supabase.")

        df = pd.read_csv(file_path)
        fuente_cargada = f"Archivo CSV Limpio ({os.path.basename(file_path)})"

    # 3. Regla No Negociable: Eliminar cualquier columna 'id' si existiese
    if "id" in df.columns:
        df = df.drop(columns=["id"])
    if "creado_en" in df.columns:
        df = df.drop(columns=["creado_en"])

    # Conversión estricta de fecha_hecho
    df["fecha_hecho"] = pd.to_datetime(df["fecha_hecho"])

    # Almacenar metadato de procedencia en atributos del dataframe
    df.attrs["fuente"] = fuente_cargada
    df.attrs["total_registros"] = len(df)

    return df
