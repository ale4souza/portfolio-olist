-- Objetivo: uma tabela por estado com entrega, atraso e nota, para o dashboard

-- Primeiro bloco reune os pedidos entregues com as datas necessarias
WITH pedidos AS (
  SELECT
    c.customer_state AS estado,                                  -- estado do cliente
    o.order_id,                                                  -- identificador do pedido
    o.order_purchase_timestamp::timestamp AS compra,             -- data da compra
    o.order_delivered_customer_date::timestamp AS entrega,       -- data da entrega
    o.order_estimated_delivery_date::timestamp AS estimada       -- data prometida ao cliente
  FROM orders o                                                  -- comeca pela tabela de pedidos
  JOIN customers c ON c.customer_id = o.customer_id              -- liga o pedido ao cliente
  WHERE o.order_status = 'delivered'                             -- so pedidos entregues
    AND o.order_delivered_customer_date IS NOT NULL              -- ignora pedidos sem data de entrega
),
-- Segundo bloco calcula a nota media de cada pedido
notas AS (
  SELECT order_id, AVG(review_score) AS nota                     -- media das notas do pedido
  FROM order_reviews
  GROUP BY order_id                                              -- uma linha por pedido
)
SELECT
  p.estado,                                                      -- estado do cliente
  COUNT(*) AS pedidos,                                           -- pedidos avaliados no estado
  -- tempo medio entre compra e entrega, em dias
  ROUND(AVG(EXTRACT(EPOCH FROM (p.entrega - p.compra)) / 86400)::numeric, 1) AS dias_medios,
  -- percentual de pedidos entregues depois da data prometida
  ROUND(100.0 * SUM(CASE WHEN p.entrega > p.estimada THEN 1 ELSE 0 END) / COUNT(*), 2) AS pct_atrasados,
  ROUND(AVG(n.nota)::numeric, 2) AS nota_media                   -- nota media do estado
FROM pedidos p
JOIN notas n ON n.order_id = p.order_id                          -- junta entrega e nota do mesmo pedido
GROUP BY p.estado                                                -- uma linha por estado
HAVING COUNT(*) >= 100                                           -- evita estados com poucos pedidos
ORDER BY pct_atrasados DESC;                                     -- dos mais atrasados para os menos