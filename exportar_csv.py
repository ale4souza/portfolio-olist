# Objetivo: rodar as consultas SQL e salvar cada resultado em um arquivo CSV

import os                                   # trabalha com pastas e caminhos
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

pasta_saida = r"C:\portfolio-olist\dashboard_data"  # pasta onde os CSVs serão salvos
os.makedirs(pasta_saida, exist_ok=True)             # cria a pasta se ela ainda não existir

# nome do arquivo SQL (dentro da pasta sql) e nome do CSV que será gerado
consultas = {
    "01_recompra.sql": "recompra.csv",
    "02_atraso_vs_nota.sql": "atraso_vs_nota.csv",
    "03a_faturamento_por_estado.sql": "faturamento_por_estado.csv",
    "04_pedidos_por_mes.sql": "pedidos_por_mes.csv",
    "05_dashboard_estado.sql": "estado_entrega_nota.csv",
}

for arquivo_sql, arquivo_csv in consultas.items():                 # repete para cada consulta
    caminho_sql = os.path.join(r"C:\portfolio-olist\sql", arquivo_sql)  # caminho do arquivo SQL
    with open(caminho_sql, encoding="utf-8") as f:                 # abre o arquivo SQL
        consulta = f.read()                                        # lê o texto da consulta
    with engine.connect() as conn:                                 # abre a conexão com o banco
        tabela = pd.read_sql(text(consulta), conn)                 # executa e guarda o resultado
    destino = os.path.join(pasta_saida, arquivo_csv)               # caminho do CSV de saída
    tabela.to_csv(destino, index=False, encoding="utf-8")          # salva o CSV sem a coluna de índice
    print(f"{arquivo_csv}: {len(tabela)} linhas salvas")           # mostra o resumo no terminal

print("Concluído!")