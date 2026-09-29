WITH entregas AS (
  SELECT
    o.order_id,
    CASE
      WHEN o.order_delivered_customer_date::timestamp
         > o.order_estimated_delivery_date::timestamp
      THEN 'Atrasado'
      ELSE 'No prazo'
    END AS situacao
  FROM orders o
  WHERE o.order_status = 'delivered'
    AND o.order_delivered_customer_date IS NOT NULL
),
notas AS (
  SELECT order_id, AVG(review_score) AS nota
  FROM order_reviews
  GROUP BY order_id
)
SELECT
  e.situacao,
  COUNT(*) AS pedidos,
  ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS pct_pedidos,
  ROUND(AVG(n.nota), 2) AS nota_media
FROM entregas e
JOIN notas n ON n.order_id = e.order_id
GROUP BY e.situacao;