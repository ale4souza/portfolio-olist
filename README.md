# Olist: Recompra, Entrega e Satisfação

Análise de dados de um marketplace brasileiro (dataset público da Olist) com **SQL, Python e um dashboard**, para responder três perguntas de negócio sobre retenção de clientes, atrasos na entrega e satisfação.

**Dashboard interativo:** https://datastudio.google.com/s/gspMrgtIsMU

![Dashboard do projeto](docs/dashboard.png)

## Perguntas de negócio

1. **Recompra:** que parcela dos clientes compra mais de uma vez?
2. **Atraso e satisfação:** pedidos entregues com atraso recebem notas piores?
3. **Estados:** como entrega, atraso e nota variam entre os estados?

## Principais achados

- **Recompra baixa:** apenas **3,06%** dos clientes compraram mais de uma vez (2.924 de 95.560 clientes únicos).
- **Atraso derruba a nota:** **7,99%** dos pedidos entregues e avaliados chegaram depois da data prometida (7.661 de 95.824). Esses pedidos tiveram nota média **2,57**, contra **4,29** dos pedidos no prazo.
- **Entre os estados, o atraso pesa mais que o tempo de entrega:** a correlação entre o percentual de pedidos atrasados e a nota média foi de **−0,87**, enquanto a correlação entre dias de entrega e nota foi de **−0,56** (24 estados com 100 pedidos ou mais).
- **Amazonas é a exceção que ajuda a explicar:** a entrega é a mais lenta (26,4 dias, contra 8,7 em SP), mas só 4,17% dos pedidos atrasam e a nota é 4,24. O prazo prometido é longo e é cumprido.
- **Rio de Janeiro e Rio Grande do Sul têm prazo médio parecido** (cerca de 15 dias), mas o RJ atrasa 13,29% dos pedidos contra 7,10% do RS, e a nota acompanha: 3,97 contra 4,19.
- **Vendas concentradas:** SP lidera em faturamento (R$ 5,17 milhões em 41.128 pedidos). Na Bahia, o maior vendedor faturou R$ 222,8 mil, mais de 12 vezes o segundo colocado (R$ 17,5 mil).

## Limitações

- **Correlação não prova causa.** A análise por estado aponta uma direção forte, mas não isola outros fatores (tipo de produto, vendedor, preço). Um teste no nível do pedido seria o passo seguinte.
- **A recompra pode estar subestimada:** a base cobre cerca de dois anos, e clientes recentes tiveram pouco tempo para voltar a comprar.
- **Estados pequenos oscilam mais:** AM (144 pedidos avaliados) e RO (242) têm médias menos estáveis. Estados com menos de 100 pedidos avaliados ficaram fora da análise de entrega.
- **Período:** a base vai de set/2016 a out/2018, mas o volume é consistente apenas de jan/2017 a ago/2018, que foi o recorte usado no gráfico mensal.
- **Qualidade dos dados:** 8 pedidos com status `delivered` não têm data de entrega e ficaram fora das análises de prazo.
- **Pedidos cancelados** foram excluídos das análises de recompra, faturamento e volume mensal.

## Ferramentas

- **Python** (pandas, SQLAlchemy, python-dotenv) para carga, exploração e exportação dos dados
- **SQL** (PostgreSQL no Supabase) com CTEs, joins, agregações e window functions
- **Google Planilhas** como fonte do dashboard
- **Looker Studio** para o dashboard
- **Git e GitHub** para versionamento

## Estrutura do repositório

```
portfolio-olist/
├── sql/                        consultas SQL comentadas
│   ├── 00_periodo.sql          período coberto pela base
│   ├── 01_recompra.sql         taxa de recompra
│   ├── 02_atraso_vs_nota.sql   atraso x nota de avaliação
│   ├── 03a_faturamento_por_estado.sql
│   ├── 03b_top_vendedores_por_estado.sql
│   ├── 03c_entrega_por_estado.sql
│   ├── 03d_atraso_por_estado.sql
│   ├── 04_pedidos_por_mes.sql
│   └── 05_dashboard_estado.sql
├── dashboard_data/             CSVs agregados usados no dashboard
├── carregar_dados.py           carrega os CSVs do Kaggle no Postgres
├── rodar_sql.py                executa um arquivo .sql e mostra o resultado
├── exploracao.py               exploração: vazios, status, volume mensal, notas, entrega
├── exportar_csv.py             exporta os resultados das consultas para CSV
├── correlacao.py               correlação entre atraso, tempo de entrega e nota
├── insights.md                 anotações: fatos, interpretações e hipóteses
└── README.md
```

## Como reproduzir

1. Baixe o dataset **Brazilian E-Commerce Public Dataset by Olist** no Kaggle e extraia os CSVs na pasta `olist_data/` (ela não é versionada).
2. Crie um projeto gratuito no Supabase e guarde a connection string (Session pooler) num arquivo `.env` na raiz:
   ```
   DATABASE_URL=postgresql://usuario:senha@host:5432/postgres
   ```
3. Instale as dependências:
   ```
   pip install pandas sqlalchemy psycopg2-binary python-dotenv
   ```
4. Carregue os dados no banco:
   ```
   python carregar_dados.py
   ```
5. Rode uma consulta ou exporte todas:
   ```
   python rodar_sql.py sql\01_recompra.sql
   python exportar_csv.py
   ```
6. Explore e confirme as correlações:
   ```
   python exploracao.py
   python correlacao.py
   ```

Os caminhos nos scripts usam `C:\portfolio-olist`. Ajuste-os se o projeto estiver em outra pasta.

## Fonte dos dados

[Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) (Kaggle).

## Autora

**Alessandra Souza**
[LinkedIn](https://www.linkedin.com/in/alessandra-souza) · [GitHub](https://github.com/ale4souza)