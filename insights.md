97 em cada 100 clientes compraram uma única vez. Para um marketplace, isso indica que o negócio depende quase todo de aquisição de clientes novos, e pouco de retenção.
Ressalva: a base cobre só cerca de 2 anos (2016 a 2018), então parte dos clientes pode não ter tido tempo de voltar. No portfólio, mencione esse limite, porque mostra maturidade analítica.
Recomendação de negócio (exemplo): investir em ações de pós-compra, como cupom para a segunda compra e e-mail de reengajamento, e depois testar se elas aumentam a taxa.
Fato: pedidos atrasados (7,99% do total) têm nota média de 2,57, contra 4,29 dos pedidos no prazo.
Cuidado: isso mostra associação, não prova que o atraso causa a nota baixa. É uma hipótese forte, mas a análise não isola outros fatores.

primeira_compra 2016-09-04 21:15:19    
ultima_compra 2018-10-17 17:30:18

Fatos (saem direto das tabelas)

SP lidera com folga: 41.128 pedidos e R$ 5,17 milhões em faturamento, seguido por RJ (R$ 1,81 mi) e MG (R$ 1,57 mi).
Concentração: somando as linhas da tabela, SP tem cerca de 38% do faturamento e 42% dos pedidos. SP, RJ e MG juntos passam de 63% do faturamento.
Ticket médio: SP tem o menor entre os grandes (R$ 125,59). Os maiores tickets estão em estados pequenos, como PB (R$ 216,34), AP (R$ 198,15), AC (R$ 197,32) e AL (R$ 195,41).
Vendedores: vários estados têm só 1 ou 2 vendedores na lista (AC, AM, MA, PA e PI com 1; RO e SE com 2). Como o ranking mostra até 3, isso significa que o estado tem poucos vendedores.
Concentração entre vendedores: na Bahia, o maior vendedor faturou R$ 222.776, mais de 12 vezes o segundo colocado (R$ 17.522). O maior da BA fica perto do maior de SP (R$ 229.237), mesmo com a Bahia tendo bem menos pedidos.
Pedidos não são faturamento: em SP, o vendedor com mais pedidos (1.804) faturou menos que outro com 1.131, o que sugere produtos de preço diferente.

Interpretação

O negócio é muito concentrado geograficamente, tanto nas compras quanto nas vendas, e o eixo SP, RJ e MG domina.
Os tickets altos em estados pequenos devem ser lidos com cuidado: com poucos pedidos (AP tem 68), uma compra grande muda bastante a média.

Hipóteses (precisam de teste)

Clientes de estados distantes compram menos vezes e juntam mais itens numa compra, o que elevaria o ticket.
Estados com poucos vendedores dependem de entregas vindas de longe, o que pode pesar no prazo e na nota. Isso conversa com a pergunta 2, em que o atraso derrubou a nota de 4,29 para 2,57.
Um detalhe técnico: o faturamento aqui é a soma de price, ou seja, não inclui frete. Então o ticket alto não se explica por frete.

## Período e qualidade dos dados
- Fato: base de set/2016 a out/2018; volume consistente de jan/2017 a ago/2018.
- Fato: 97% dos pedidos entregues; 8 pedidos "delivered" sem data de entrega.
- Fato: 77,1% das notas são 4 ou 5; nota 1 (11,5%) supera a 2 e a 3.
- Fato: entrega média de 12,1 dias, mediana de 10, máximo de 209.
- Hipótese: pico de nov/2017 ligado a Black Friday (não verificado).
- Decisão: excluir meses incompletos nos gráficos e usar mediana para entrega.

## Entrega e nota por estado (pergunta 3)
- Fato: SP entrega em 8,7 dias em média; Norte e Nordeste levam de 19 a 26 dias.
- Fato: AM tem a entrega mais lenta (26,4 dias) e nota 4,24, igual à de SP.
- Fato: RJ e RS têm o mesmo prazo (cerca de 15 dias), mas nota 3,97 contra 4,19.
- Hipótese: a nota depende mais do atraso frente ao prazo prometido do que dos dias de entrega (teste na 03d).

## Pergunta 3: entrega, atraso e nota por estado
- Fato: correlação entre estados de -0,56 (dias de entrega x nota) e -0,87 (% atrasados x nota).
- Fato: AM tem a entrega mais lenta (26,4 dias) e só 4,17% de atrasos, nota 4,24.
- Fato: RJ e RS têm prazo parecido (cerca de 15 dias), mas atraso de 13,29% vs 7,10%, e nota 3,97 vs 4,19.
- Interpretação: a nota depende mais de cumprir o prazo prometido do que do tempo de entrega.
- Limite: correlação entre 24 estados, sem controlar outros fatores; testar no nível do pedido.
- Hipótese de ação: ajustar o prazo prometido nas regiões com mais atraso.