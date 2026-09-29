import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
url = os.getenv("DATABASE_URL")

# Ajusta o prefixo conforme o driver instalado
try:
    import psycopg2  # noqa: F401
    if url.startswith("postgresql://"):
        url = url.replace("postgresql://", "postgresql+psycopg2://", 1)
except ImportError:
    if url.startswith("postgresql://"):
        url = url.replace("postgresql://", "postgresql+psycopg://", 1)

engine = create_engine(url)

pasta = r"C:\portfolio-olist\olist_data"

# Vamos deixar a geolocalização por último (é a maior, ~1 milhão de linhas)
arquivos = {
    "customers": "olist_customers_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "order_payments": "olist_order_payments_dataset.csv",
    "order_reviews": "olist_order_reviews_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "category_translation": "product_category_name_translation.csv",
}

for tabela, arquivo in arquivos.items():
    df = pd.read_csv(os.path.join(pasta, arquivo))
    df.to_sql(tabela, engine, if_exists="replace", index=False,
              chunksize=5000, method="multi")
    print(f"{tabela}: {len(df)} linhas carregadas")

print("Concluído!")