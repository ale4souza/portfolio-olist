-- Objetivo: pedidos por mes, so no periodo em que a base esta completa
SELECT
  -- primeiro dia do mes, para o Looker reconhecer como data
  DATE_TRUNC('month', order_purchase_timestamp::timestamp)::date AS mes,
  COUNT(*) AS pedidos                                -- quantidade de pedidos no mes
FROM orders                                          -- tabela de pedidos
WHERE order_status <> 'canceled'                     -- ignora pedidos cancelados
  AND order_purchase_timestamp::timestamp >= '2017-01-01'  -- inicio do periodo completo
  AND order_purchase_timestamp::timestamp <  '2018-09-01'  -- fim do periodo completo
GROUP BY 1                                           -- agrupa pela primeira coluna (o mes)
ORDER BY 1;                                          -- ordena do mes mais antigo ao mais recente