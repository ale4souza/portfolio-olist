# Objetivo: calcular a correlação entre atraso, tempo de entrega e nota por estado

import pandas as pd  # biblioteca de análise de dados

# lê o CSV com uma linha por estado
df = pd.read_csv(r"C:\portfolio-olist\dashboard_data\estado_entrega_nota.csv")

# correlação entre o percentual de pedidos atrasados e a nota média
print("Atraso x nota:", round(df["pct_atrasados"].corr(df["nota_media"]), 2))

# correlação entre os dias médios de entrega e a nota média
print("Dias de entrega x nota:", round(df["dias_medios"].corr(df["nota_media"]), 2))