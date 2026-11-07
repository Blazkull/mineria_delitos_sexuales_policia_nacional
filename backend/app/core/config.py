import os
from typing import Optional
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

def get_normalized_db_url() -> str:
    url = os.getenv("DATABASE_URL_POOLER") or os.getenv("DATABASE_URL") or "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
    if url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql+psycopg2://", 1)
    elif url.startswith("postgresql://") and not url.startswith("postgresql+"):
        url = url.replace("postgresql://", "postgresql+psycopg2://", 1)
    return url

class Settings(BaseSettings):
    PROJECT_NAME: str = "Minería de Delitos Sexuales - Policía Nacional (Atlántico)"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    PORT: int = 8000
    ENVIRONMENT: str = "development"

    # Conexión a Base de Datos PostgreSQL / Supabase
    DATABASE_URL: str = get_normalized_db_url()
    DATABASE_URL_POOLER: Optional[str] = os.getenv("DATABASE_URL_POOLER", None)
    
    # Credenciales de Supabase opcionales
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", "")
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY", "")

    # Rutas de datos
    DATASET_RAW_PATH: str = os.getenv(
        "DATASET_RAW_PATH", 
        "docs/data_set/Reporte__Delitos_sexuales_Policía_Nacional_20261106.csv"
    )
    DATASET_CLEAN_PATH: str = os.getenv(
        "DATASET_CLEAN_PATH", 
        "docs/data_set/delitos_sexuales_atlantico_limpio.csv"
    )
    FECHA_DESCARGA_DATASET: str = "2026-11-06"
    DEPARTAMENTO_OBJETIVO: str = "ATLÁNTICO"

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(__file__), "..", "..", ".env"),
        env_file_encoding="utf-8",
        extra="ignore"
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
