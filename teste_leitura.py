import pandas as pd

orders = pd.read_csv(r"C:\portfolio-olist\olist_data\olist_orders_dataset.csv")
print(orders.shape)
print(orders.head())