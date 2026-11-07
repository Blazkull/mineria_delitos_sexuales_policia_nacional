import os
import sys
import logging
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("Enable_RLS")

load_dotenv("backend/.env")

raw_url = os.getenv("DATABASE_URL_POOLER") or os.getenv("DATABASE_URL")
if not raw_url:
    logger.error("No se encontró cadena de conexión en backend/.env")
    sys.exit(1)

if raw_url.startswith("postgres://"):
    raw_url = raw_url.replace("postgres://", "postgresql+psycopg2://", 1)
elif raw_url.startswith("postgresql://") and not raw_url.startswith("postgresql+"):
    raw_url = raw_url.replace("postgresql://", "postgresql+psycopg2://", 1)

def aplicar_rls():
    logger.info("=" * 70)
    logger.info("APLICANDO ROW LEVEL SECURITY (RLS) EN SUPABASE POSTGRESQL")
    logger.info("=" * 70)

    engine = create_engine(raw_url, pool_pre_ping=True)
    with engine.connect() as conn:
        logger.info("Habilitando Row Level Security en 'delitos_sexuales_atlantico'...")
        conn.execute(text("ALTER TABLE delitos_sexuales_atlantico ENABLE ROW LEVEL SECURITY;"))

        # Política 1: Lectura abierta para anon, authenticated y postgres
        logger.info("Configurando politica de lectura publica...")
        conn.execute(text("""
            DROP POLICY IF EXISTS "Permitir lectura publica de delitos sexuales" ON delitos_sexuales_atlantico;
            CREATE POLICY "Permitir lectura publica de delitos sexuales" 
            ON delitos_sexuales_atlantico 
            FOR SELECT 
            TO anon, authenticated, postgres
            USING (true);
        """))

        # Política 2: Escritura restringida a roles de servicio y administrador
        logger.info("Configurando politica de escritura restringida...")
        conn.execute(text("""
            DROP POLICY IF EXISTS "Restringir escritura a service_role y postgres" ON delitos_sexuales_atlantico;
            CREATE POLICY "Restringir escritura a service_role y postgres" 
            ON delitos_sexuales_atlantico 
            FOR ALL 
            TO service_role, postgres
            USING (true)
            WITH CHECK (true);
        """))

        conn.commit()
        logger.info("Políticas RLS aplicadas con éxito.")

        # Verificar relrowsecurity
        check_rls = conn.execute(text("SELECT relrowsecurity FROM pg_class WHERE relname = 'delitos_sexuales_atlantico'")).scalar()
        logger.info(f"Estado de RLS en 'delitos_sexuales_atlantico': {'HABILITADO' if check_rls else 'DESHABILITADO'}")

        # Listar políticas
        query_policies = text("SELECT policyname, permissive, roles, cmd FROM pg_policies WHERE tablename = 'delitos_sexuales_atlantico'")
        policies = conn.execute(query_policies).fetchall()
        logger.info(f"Total políticas activas: {len(policies)}")
        for p in policies:
            logger.info(f"  • {p[0]} -> Comando: {p[3]} | Roles: {p[2]}")

    logger.info("=" * 70)

if __name__ == "__main__":
    aplicar_rls()

