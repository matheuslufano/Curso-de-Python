"""
====================================================================
DESAFIO - 095
Aprimore o desafio "ex093" para que ele funcione com various jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de
cada jogador.
====================================================================
"""
#=====1º parte============================================
lista = []
dicionario = {}
gols = []
partidas = []
while True:
    gols.clear()
    dicionario.clear()
    dicionario['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas "{dicionario["nome"]}" jogou? '))
    for i in range(1, 1 + tot):
        gols.append(int(input(f' - Quantos gols na 0{i}° partida: ')))
    dicionario['gol'] = gols[:]
    dicionario['total'] = sum(gols)
    lista.append(dicionario.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        print('-' * 40)
        if resp in 'SN':
            break
        print('Erro! escolha "S" (SIM) OU "N" (NÃO).')
    if resp == 'N':
        break
#======= 2° parte da atividade========================================
print('|================== PLACAR DOS JOGADORES ====================|\n'
      '|COD|       Nome       |       Gols       |      Total       |\n'
      '|———|——————————————————|——————————————————|——————————————————|')
for k, v in enumerate(lista):
    print(f'| {k+1:^2}|', end='')
    for d in v.values():
        print(f'{str(d):^18}|', end='')
    print()
print(' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
#===========3° parte da atividade========================================
resp = ' '
while True:
    dados = int(input('  De quel jogador/jogadora quer \n'
                      '  ver os dados: (999 "fecha") '))-1
    if dados == 999:
        break
    if dados >= len(lista):
        print(f"ERRO, não existe jogador com código {dados+1}!")
    print(f'    ◸---LEVANTAMENTO DE {lista[dados]["nome"].upper()} --◹')
    for p in range(0,len(lista[dados]['gol'])):
        print(f'    |  Na 0{p+1}° partida fez {lista[dados]["gol"][p]} gol!   |')
    print('    ◺-----------------------------◿')


#==============curso em vídeo==========================
# time = list()
# jogador = dict()
# partidas = list()
#
# while True:
#     print('-' * 40)
#     jogador.clear()#aclear(apaga)
#     jogador['nome'] = str(input('Nome do jogador: '))
#     tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
#     partidas.clear()
#     for c in range(0, tot):
#         partidas.append(int(input(f'    Quantos gols na {c+1}° partida ? ')))
#     jogador['gols'] = partidas[:]
#     jogador['total'] = sum(partidas)
#     time.append(jogador.copy())
#     while True:
#         resp = str(input('Quer continuar? [S/N] ')).upper()[0]
#         if resp in 'SN':
#             break
#         print('ERRO! Responda apenas S ou N.')
#     if resp == 'N':
#         break
# print('-'*40)
# for k, v in enumerate(time):
#     print(f'{k:>4}', end='')
#     for d in v.values():
#         print(f'{str(d):<15}', end='')
#     print()
# print('-'*40)
# print('-='*30)
# print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
# for i, v in enumerate(jogador['gols']):
#     print(f'    => Na partida {i}, fez {v} gols.')
# print(f'Foi um total de {jogador["total"]} gols.')