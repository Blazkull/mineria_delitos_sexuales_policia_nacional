import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv("backend/.env")

env_vars = ["DATABASE_URL", "DATABASE_URL_POOLER", "DIRECT_URL", "POOLER_URL", "DATABASE_POOLER_URL", "SUPABASE_DB_URL"]

found_any = False
for var_name in env_vars:
    val = os.getenv(var_name)
    if val and "YOUR_PASSWORD" not in val and "localhost" not in val:
        found_any = True
        masked = val
        if "@" in val:
            host_part = val.split("@")[1]
            masked = f"postgresql://***:***@{host_part}"
        print(f"Probando {var_name}: {masked}")
        
        try:
            # Si la url no tiene driver, asegurar postgresql+psycopg2
            url = val
            if url.startswith("postgres://"):
                url = url.replace("postgres://", "postgresql+psycopg2://", 1)
            elif url.startswith("postgresql://") and not url.startswith("postgresql+"):
                url = url.replace("postgresql://", "postgresql+psycopg2://", 1)
                
            engine = create_engine(
                url,
                pool_pre_ping=True,
                connect_args={"connect_timeout": 10}
            )
            with engine.connect() as conn:
                res = conn.execute(text("SELECT version();")).scalar()
                print(f"  [SUCCESS] {var_name} conectó correctamente!")
                print(f"  Servidor: {res.split(',')[0] if res else 'PostgreSQL'}")
                
                # Tablas existentes
                query_tables = text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
                tables = [r[0] for r in conn.execute(query_tables).fetchall()]
                print(f"  Tablas en esquema public: {tables}")
                
                if "delitos_sexuales_atlantico" in tables:
                    cnt = conn.execute(text("SELECT COUNT(*) FROM delitos_sexuales_atlantico")).scalar()
                    print(f"  Total registros en 'delitos_sexuales_atlantico': {cnt}")
                else:
                    print("  La tabla 'delitos_sexuales_atlantico' aun no existe.")
        except Exception as e:
            print(f"  [FAILED] {var_name} error: {e}")

if not found_any:
    print("No se encontraron variables de base de datos válidas en backend/.env.")
