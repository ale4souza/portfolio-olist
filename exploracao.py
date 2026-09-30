# Objetivo: explorar os dados do Olist com Python (pandas)

import os                                   # acessa variáveis do sistema
import pandas as pd                         # biblioteca de análise de dados
from dotenv import load_dotenv              # lê o arquivo .env
from sqlalchemy import create_engine, text  # conexão com o banco

load_dotenv(r"C:\portfolio-olist\.env")     # carrega a senha do banco guardada no .env
url = os.getenv("DATABASE_URL")             # pega a connection string

# ajusta o início da string conforme o driver do Postgres instalado
try:
    import psycopg2  # noqa: F401           # testa se o driver psycopg2 existe
    if url.startswith("postgresql://"):
        url = url.replace("postgresql://", "postgresql+psycopg2://", 1)
except ImportError:                          # se não existir, usa o psycopg novo
    if url.startswith("postgresql://"):
        url = url.replace("postgresql://", "postgresql+psycopg://", 1)

engine = create_engine(url)                  # cria a conexão com o Supabase


def ler(consulta):
    # função auxiliar: executa um SQL e devolve uma tabela do pandas
    with engine.connect() as conn:
        return pd.read_sql(text(consulta), conn)


orders = ler("SELECT * FROM orders")                 # tabela de pedidos
reviews = ler("SELECT * FROM order_reviews")         # tabela de avaliações

# ---------- 1. Tamanho e valores vazios ----------
print("Pedidos (linhas, colunas):", orders.shape)    # quantidade de linhas e colunas
print("\nValores vazios por coluna em orders:")
print(orders.isna().sum().to_string())               # conta os vazios de cada coluna

# ---------- 2. Status dos pedidos ----------
print("\nPedidos por status:")
print(orders["order_status"].value_counts().to_string())  # quantos pedidos em cada status

# ---------- 3. Pedidos por mês ----------
# as datas foram carregadas como texto, então convertemos para data
orders["data_compra"] = pd.to_datetime(orders["order_purchase_timestamp"])
por_mes = orders.groupby(orders["data_compra"].dt.to_period("M")).size()  # conta pedidos por mês
print("\nPedidos por mês:")
print(por_mes.to_string())

# ---------- 4. Distribuição das notas ----------
notas = reviews["review_score"].value_counts(normalize=True).sort_index() * 100  # percentual de cada nota
print("\nDistribuição das notas (%):")
print(notas.round(1).to_string())

# ---------- 5. Tempo de entrega em dias ----------
entregues = orders[orders["order_status"] == "delivered"].copy()         # só pedidos entregues
entregues["entrega"] = pd.to_datetime(entregues["order_delivered_customer_date"])  # data de entrega
entregues["dias"] = (entregues["entrega"] - entregues["data_compra"]).dt.days      # dias entre compra e entrega
print("\nTempo de entrega em dias (resumo):")
print(entregues["dias"].describe().round(1).to_string())  # média, mediana, mínimo, máximo etc.