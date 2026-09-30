-- Objetivo: os 3 vendedores que mais faturam em cada estado

-- Primeiro bloco (CTE) monta o total de cada vendedor
WITH vendas AS (
  SELECT
    s.seller_id,                                     -- identificador do vendedor
    s.seller_state,                                  -- estado do vendedor
    COUNT(DISTINCT oi.order_id) AS pedidos,          -- pedidos em que ele vendeu
    SUM(oi.price) AS faturamento                     -- total vendido por ele
  FROM order_items oi                                -- começa pelos itens vendidos
  JOIN sellers s ON s.seller_id = oi.seller_id       -- liga o item ao vendedor
  JOIN orders o ON o.order_id = oi.order_id          -- liga o item ao pedido
  WHERE o.order_status <> 'canceled'                 -- ignora pedidos cancelados
  GROUP BY s.seller_id, s.seller_state               -- uma linha por vendedor
)
-- Consulta final mostra só quem ficou entre os 3 primeiros do estado
SELECT *
FROM (
  SELECT
    seller_state AS estado,                          -- estado do vendedor
    seller_id,
    pedidos,
    ROUND(faturamento::numeric, 2) AS faturamento,   -- faturamento com 2 casas decimais
    -- cria o ranking e recomeça a contagem a cada estado (PARTITION BY)
    -- dentro de cada estado, ordena do maior faturamento para o menor
    RANK() OVER (PARTITION BY seller_state ORDER BY faturamento DESC) AS posicao_no_estado
  FROM vendas
) ranking
WHERE posicao_no_estado <= 3                         -- filtra só as posições 1, 2 e 3
ORDER BY estado, posicao_no_estado;                  -- organiza por estado e depois pela posição