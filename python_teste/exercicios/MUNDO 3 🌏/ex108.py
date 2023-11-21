"""
====================================================================
DESAFIO - 108
Adapte o código do desafio 107, criando uma função adicional chamada
moeda() que consiga mostrar os valores como um valor monetário formatado.
====================================================================
"""
from arquivo import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}\n'
      f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}\n'
      f'Aumentando 10%, temos {moeda.moeda(moeda.acréscimo(p, 10))} (+{moeda.moeda(-(p-( moeda.acréscimo(p, 10))))})\n'
      f'Reduzindo 13%, temos {moeda.moeda(moeda.desconto(p, 13))} (-{moeda.moeda(p-(moeda.desconto(p, 13)))})')

