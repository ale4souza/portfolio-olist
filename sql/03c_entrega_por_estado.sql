-- Objetivo: comparar tempo medio de entrega e nota media por estado do cliente

-- Primeiro bloco calcula os dias de entrega de cada pedido entregue
WITH entregas AS (
  SELECT
    c.customer_state AS estado,                      -- estado do cliente
    o.order_id,                                      -- identificador do pedido
    -- diferenca entre entrega e compra, convertida de segundos para dias
    EXTRACT(EPOCH FROM (o.order_delivered_customer_date::timestamp
                      - o.order_purchase_timestamp::timestamp)) / 86400 AS dias_entrega
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
  ROUND(AVG(e.dias_entrega)::numeric, 1) AS dias_medios,  -- tempo medio de entrega em dias
  ROUND(AVG(n.nota)::numeric, 2) AS nota_media       -- nota media do estado
FROM entregas e
JOIN notas n ON n.order_id = e.order_id              -- junta entrega e nota do mesmo pedido
GROUP BY e.estado                                    -- uma linha por estado
HAVING COUNT(*) >= 100                               -- evita estados com poucos pedidos
ORDER BY dias_medios DESC;                           -- do mais lento para o mais rapido