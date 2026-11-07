import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv("backend/.env")
raw_url = os.getenv("DATABASE_URL_POOLER") or os.getenv("DATABASE_URL")
if raw_url.startswith("postgres://"):
    raw_url = raw_url.replace("postgres://", "postgresql+psycopg2://", 1)
elif raw_url.startswith("postgresql://") and not raw_url.startswith("postgresql+"):
    raw_url = raw_url.replace("postgresql://", "postgresql+psycopg2://", 1)

print("Connecting to:", raw_url.split("@")[1])
engine = create_engine(raw_url)
with engine.connect() as conn:
    cols = conn.execute(text("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'delitos_sexuales_atlantico'")).fetchall()
    print("Columns in DB table:")
    for c in cols:
        print(f"  {c[0]} ({c[1]})")
    cnt = conn.execute(text("SELECT COUNT(*) FROM delitos_sexuales_atlantico")).scalar()
    print("Total rows in DB table:", cnt)
