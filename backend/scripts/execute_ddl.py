import os
import sys
import logging
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("Execute_DDL")

load_dotenv("backend/.env")

raw_url = os.getenv("DATABASE_URL_POOLER") or os.getenv("DATABASE_URL")
if not raw_url:
    logger.error("No se encontró DATABASE_URL_POOLER ni DATABASE_URL en backend/.env")
    sys.exit(1)

if raw_url.startswith("postgres://"):
    raw_url = raw_url.replace("postgres://", "postgresql+psycopg2://", 1)
elif raw_url.startswith("postgresql://") and not raw_url.startswith("postgresql+"):
    raw_url = raw_url.replace("postgresql://", "postgresql+psycopg2://", 1)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DDL_FILE_PATH = os.path.join(BASE_DIR, "docs", "database", "supabase_ddl.sql")

def ejecutar_ddl():
    logger.info("=" * 70)
    logger.info("EJECUTANDO SCRIPT DDL EN POSTGRESQL (SUPABASE)")
    logger.info("=" * 70)
    logger.info(f"Conectando a: {raw_url.split('@')[1]}")

    if not os.path.exists(DDL_FILE_PATH):
        logger.error(f"No existe el archivo DDL en: {DDL_FILE_PATH}")
        sys.exit(1)

    with open(DDL_FILE_PATH, "r", encoding="utf-8") as f:
        ddl_sql = f.read()

    engine = create_engine(raw_url, pool_pre_ping=True)
    with engine.connect() as conn:
        logger.info("Ejecutando sentencias SQL...")
        # Separar sentencias por ';' limpiando comentarios vacíos
        sentencias = [s.strip() for s in ddl_sql.split(";") if s.strip()]
        for s in sentencias:
            # Ignorar comentarios de una sola línea
            if s.startswith("--") and "\n" not in s:
                continue
            try:
                conn.execute(text(s))
            except Exception as e:
                logger.warning(f"Aviso ejecutando sentencia: {e}")
        conn.commit()
        logger.info("Script DDL ejecutado con éxito.")

        # Verificar tablas y vistas
        tablas = conn.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")).fetchall()
        logger.info(f"Objetos en esquema public: {[t[0] for t in tablas]}")

        # Conteo de registros
        cnt = conn.execute(text("SELECT COUNT(*) FROM delitos_sexuales_atlantico")).scalar()
        logger.info(f"Total registros en 'delitos_sexuales_atlantico': {cnt}")

    logger.info("=" * 70)

if __name__ == "__main__":
    ejecutar_ddl()

