import os
import sys
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv(r"C:\portfolio-olist\.env")
url = os.getenv("DATABASE_URL")

try:
    import psycopg2  # noqa: F401
    if url.startswith("postgresql://"):
        url = url.replace("postgresql://", "postgresql+psycopg2://", 1)
except ImportError:
    if url.startswith("postgresql://"):
        url = url.replace("postgresql://", "postgresql+psycopg://", 1)

engine = create_engine(url)

arquivo = sys.argv[1]
with open(arquivo, encoding="utf-8") as f:
    consulta = f.read()

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", None)

with engine.connect() as conn:
    resultado = pd.read_sql(text(consulta), conn)

print(resultado)