"""
====================================================================
DESAFIO - 109
Modifique as funções criadas no desafio 107 para que ela
aceite um parâmetro a mais, informando se o valor retornado por elas
vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
====================================================================
"""
from arquivo import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}\n'
      f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}\n'
      f'Aumentando 10%, temos {moeda.moeda(moeda.acréscimo(p, 10))} (+{moeda.moeda(-(p-( moeda.acréscimo(p, 10))))})\n'
      f'Reduzindo 13%, temos {moeda.moeda(moeda.desconto(p, 13))} (-{moeda.moeda(p-(moeda.desconto(p, 13)))})')



