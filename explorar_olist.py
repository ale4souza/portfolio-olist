"""
Exploração inicial do dataset Olist Brazilian E-Commerce.
Objetivo: entender as tabelas, as chaves de junção e a qualidade dos dados
antes de escrever qualquer query de negócio.

Como usar:
1. Extraia o ZIP do Kaggle numa pasta (ex: ./olist_data/)
2. Ajuste a variável DATA_DIR abaixo se o nome da pasta for diferente
3. pip install pandas
4. python explorar_olist.py
"""

import pandas as pd
from pathlib import Path

DATA_DIR = Path("olist_data")

# Nome dos arquivos como vêm no ZIP do Kaggle
ARQUIVOS = {
    "customers": "olist_customers_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "payments": "olist_order_payments_dataset.csv",
    "reviews": "olist_order_reviews_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "geolocation": "olist_geolocation_dataset.csv",
    "category_translation": "product_category_name_translation.csv",
}


def carregar_tabelas():
    tabelas = {}
    for nome, arquivo in ARQUIVOS.items():
        caminho = DATA_DIR / arquivo
        if not caminho.exists():
            print(f"[AVISO] não encontrei {caminho} — pulei essa tabela.")
            continue
        tabelas[nome] = pd.read_csv(caminho)
    return tabelas


def resumo_tabela(nome, df):
    print(f"\n{'=' * 60}")
    print(f"TABELA: {nome}  ({df.shape[0]} linhas, {df.shape[1]} colunas)")
    print(f"{'=' * 60}")
    print("Colunas e tipos:")
    print(df.dtypes.to_string())

    nulos = df.isnull().sum()
    nulos = nulos[nulos > 0]
    if not nulos.empty:
        print("\nColunas com valores nulos:")
        for col, qtd in nulos.items():
            pct = 100 * qtd / len(df)
            print(f"  {col}: {qtd} ({pct:.1f}%)")
    else:
        print("\nSem valores nulos.")

    # Colunas que parecem ser chave de junção (terminam em _id)
    chaves = [c for c in df.columns if c.endswith("_id")]
    if chaves:
        print(f"\nProváveis chaves de junção: {chaves}")


def checar_relacionamentos(tabelas):
    print(f"\n{'=' * 60}")
    print("CHECAGEM DE RELACIONAMENTOS ENTRE TABELAS")
    print(f"{'=' * 60}")

    pares = [
        ("orders", "customer_id", "customers", "customer_id"),
        ("order_items", "order_id", "orders", "order_id"),
        ("order_items", "product_id", "products", "product_id"),
        ("order_items", "seller_id", "sellers", "seller_id"),
        ("payments", "order_id", "orders", "order_id"),
        ("reviews", "order_id", "orders", "order_id"),
    ]

    for tabela_a, coluna_a, tabela_b, coluna_b in pares:
        if tabela_a not in tabelas or tabela_b not in tabelas:
            continue
        ids_a = set(tabelas[tabela_a][coluna_a])
        ids_b = set(tabelas[tabela_b][coluna_b])
        sem_match = ids_a - ids_b
        pct = 100 * len(sem_match) / len(ids_a) if ids_a else 0
        print(
            f"{tabela_a}.{coluna_a} -> {tabela_b}.{coluna_b}: "
            f"{len(sem_match)} sem correspondência ({pct:.1f}%)"
        )


if __name__ == "__main__":
    tabelas = carregar_tabelas()

    if not tabelas:
        print("Nenhuma tabela carregada. Confira o caminho em DATA_DIR.")
    else:
        for nome, df in tabelas.items():
            resumo_tabela(nome, df)
        checar_relacionamentos(tabelas)

        print(f"\n{'=' * 60}")
        print("Próximo passo: com base nos nulos e relacionamentos acima,")
        print("decida a modelagem das tabelas no banco SQL (passo 3 do plano).")
        print(f"{'=' * 60}")
