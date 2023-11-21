"""
====================================================================
DESAFIO - 093
Crie um programa que gerencie o aproveitamento de um jogador de
futebol. O programa vai ler o nome do jogador e quantas partidas ele
jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total
de gols feitos durante o campeonato.
====================================================================
"""
print('Time: SUPERBOYS🌈👨🏻👨🏻‍🦰🧔🏻🧔🏽‍♂️⚽🥅\n'
      '=====================================')
dicionario = dict()
dicionario['nome'] = str(input('Nome do jogador 🧔🏽‍♂️: '))
dicionario['partidas'] = int(input(f'Quantas partidas {dicionario["nome"]} jogou? '))
cont = []
print("     🟦🟩🟨🟧🟥⚽🏃🏻🏃🏿‍♂️🟥🟧🟨🟩🟦")
for a in range(1, (dicionario['partidas']+1)):
    cont.append(int(input(f'     - Quantos gols na {a}° partida: ⚽ ')))
dicionario['gols'] = cont[:]
dicionario['Total'] = sum(cont) #função de somar de uma lista. (com x += y)
print('-'*60, '\n',
      dicionario.keys())
print('-'*60)

for k, v in dicionario.items():
    print(f'O campo "{k}" tem o valor "{v}"')

#=========================================
# jogador = dict()
# partidas = list()
# jogador['nome'] = str(input('Nome do jogador: '))
# tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
# for c in range(0, tot):
#     partidas.append(int(input(f'    Quantos gols na {c+1}° partida ? ')))
# jogador['gols'] = partidas[:]
# jogador['total'] = sum(partidas)
# print('-=' *30)
# print(jogador)
# print('-=' *30)
# for k, v in jogador.items():
#     print(f'O campo {k} tem o  valor {v}')
# print('-='*30)
# print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
# for i, v in enumerate(jogador['gols']):
#     print(f'    => Na partida {i}, fez {v} gols.')
# print(f'Foi um total de {jogador["total"]} gols.')