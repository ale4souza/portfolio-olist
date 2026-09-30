-- Objetivo: faturamento, pedidos e ticket médio por estado do cliente
SELECT
  c.customer_state AS estado,                        -- estado onde o cliente mora
  COUNT(DISTINCT o.order_id) AS pedidos,             -- quantidade de pedidos, sem repetir o mesmo pedido
  ROUND(SUM(oi.price)::numeric, 2) AS faturamento,   -- soma dos preços dos itens, com 2 casas decimais
  ROUND((SUM(oi.price) / COUNT(DISTINCT o.order_id))::numeric, 2) AS ticket_medio  -- faturamento dividido pelos pedidos
FROM orders o                                        -- começa pela tabela de pedidos
JOIN customers c ON c.customer_id = o.customer_id    -- liga cada pedido ao seu cliente
JOIN order_items oi ON oi.order_id = o.order_id      -- liga cada pedido aos seus itens
WHERE o.order_status <> 'canceled'                   -- ignora pedidos cancelados
GROUP BY c.customer_state                            -- uma linha por estado
ORDER BY faturamento DESC;                           -- do maior faturamento para o menor