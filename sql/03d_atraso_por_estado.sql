-- Objetivo: ver o percentual de pedidos atrasados e a nota media por estado

-- Primeiro bloco marca cada pedido entregue como atrasado ou no prazo
WITH entregas AS (
  SELECT
    c.customer_state AS estado,                      -- estado do cliente
    o.order_id,                                      -- identificador do pedido
    -- vale 1 se a entrega passou da data estimada e 0 se chegou no prazo
    CASE WHEN o.order_delivered_customer_date::timestamp
              > o.order_estimated_delivery_date::timestamp
         THEN 1 ELSE 0 END AS atrasado
  FROM orders o                                      -- comeca pela tabela de pedidos
  JOIN customers c ON c.customer_id = o.customer_id  -- liga o pedido ao cliente
  WHERE o.order_status = 'delivered'                 -- so pedidos entregues
    AND o.order_delivered_customer_date IS NOT NULL  -- ignora pedidos sem data de entrega
),
-- Segundo bloco calcula a nota media de cada pedido
notas AS (
  SELECT order_id, AVG(review_score) AS nota         -- media das notas do pedido
  FROM order_reviews
  GROUP BY order_id                                  -- uma linha por pedido
)
SELECT
  e.estado,                                          -- estado do cliente
  COUNT(*) AS pedidos,                               -- pedidos avaliados no estado
  ROUND(100.0 * SUM(e.atrasado) / COUNT(*), 2) AS pct_atrasados,  -- percentual de pedidos atrasados
  ROUND(AVG(n.nota)::numeric, 2) AS nota_media       -- nota media do estado
FROM entregas e
JOIN notas n ON n.order_id = e.order_id              -- junta entrega e nota do mesmo pedido
GROUP BY e.estado                                    -- uma linha por estado
HAVING COUNT(*) >= 100                               -- evita estados com poucos pedidos
ORDER BY pct_atrasados DESC;                         -- dos mais atrasados para os menos