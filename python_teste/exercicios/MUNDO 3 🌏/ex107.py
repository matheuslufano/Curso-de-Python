"""
====================================================================
DESAFIO - 107
Crie um módulo chamado moeda.py que tenhas as funções incorporadas:
- aumentar();
- diminuir();
- dobro();
- metade().

Faça também um programa que importe esse módulo e use algumas dessas funções
====================================================================
"""
from arquivo import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {moeda.metade(p)}\n'
      f'O dobro de {p} é {moeda.dobro(p)}\n'
      f'Aumentando 10%, temos {moeda.acréscimo(p, 10)} (+{-(p-( moeda.acréscimo(p, 10)))})\n'
      f'Reduzindo 13%, temos {moeda.desconto(p, 13)} (-{p-(moeda.desconto(p, 13))})')

