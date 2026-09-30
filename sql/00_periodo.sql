-- Objetivo: descobrir o período coberto pela base de pedidos
SELECT
  -- data da compra mais antiga (convertida de texto para data e hora)
  MIN(order_purchase_timestamp::timestamp) AS primeira_compra,
  -- data da compra mais recente
  MAX(order_purchase_timestamp::timestamp) AS ultima_compra
FROM orders;  -- tabela de pedidos