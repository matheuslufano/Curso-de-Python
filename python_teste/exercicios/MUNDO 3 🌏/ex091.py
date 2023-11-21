"""====================================================================
DESAFIO - 091
Crie um programa onde 4 jogadores joguem um dado e tenham resultados
aleatórios. Guarde esses resultados em um dicionário em ordem, sabendo
que o vencedor tirou o maior número de dado.
===================================================================="""
# from random import randint
# jogador = dict()
# partida = list()
#
# print('Valores Sorteados: ')
# for c in range(1, 5):
#     dado = randint(1, 6)
#     print(f'     O jogador {c} tirou 🎲 = {dado}')
#
#     jogador = f'jogador {c}'
#     jogador[f'jogador{c}'] = dado
#     partida.append(jogador)
#
# print(f'partidas: valor dos dados {partida}\n'
#       f'jogador: {jogador}')

# ==============código curso====================
from random import randint
from time import sleep
from operator import itemgetter
jogador = {'jogador 1': randint(1, 6),
           'jogador 2': randint(1, 6),
           'jogador 3': randint(1, 6),
           'jogador 4': randint(1, 6)}
ranking = list()
print('Valores dos dados:')
for k, v in jogador.items():
    print(f'    {k} tirou 🎲 = {v}')
    sleep(1)
print('== Ranking dos jogadores ==')
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')