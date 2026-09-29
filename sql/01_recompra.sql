WITH pedidos_por_cliente AS (
  SELECT
    c.customer_unique_id,
    COUNT(DISTINCT o.order_id) AS qtd_pedidos
  FROM orders o
  JOIN customers c ON c.customer_id = o.customer_id
  WHERE o.order_status <> 'canceled'
  GROUP BY c.customer_unique_id
)
SELECT
  COUNT(*) AS total_clientes,
  COUNT(*) FILTER (WHERE qtd_pedidos > 1) AS clientes_recorrentes,
  ROUND(100.0 * COUNT(*) FILTER (WHERE qtd_pedidos > 1) / COUNT(*), 2) AS pct_recompra
FROM pedidos_por_cliente;