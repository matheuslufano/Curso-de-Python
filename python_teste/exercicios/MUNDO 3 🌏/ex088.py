"""
====================================================================
DESAFIO - 088
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear
e vai sortear 6 números entre 1 a 60 para cada jogo, cadastrando
tudo em uma lista composta.
====================================================================
"""
# print('-'*30)
# print(f'     JOGO DA MEGA SENA')
# print('-'*30)
# lista = []
# sorte = int(input("Quantos jogos você quer que eu sorteie? "))
# print(f'SORTEANDO {sorte} JOGOS')
# for c in range(sorte):
#     from random import randint
#     for l in range(0,6):
#         num = randint(0,60)
#         lista.append(num)
#     print(f'Jogo {c+1}: {lista}')
#     lista.clear()
# print('BORA SORTE')

#======CÓDIGO CURSO=========
from random import randint
from time import sleep
lista = list()
jogos = list()
print(f'{"="*30}\n'
      f'{" "*5} JOGA NA MEGA SENA {" "*5}\n'
      f'{"="*30}')
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS ', '-='*3)
for i, l in enumerate(jogos): #i é o indice da variable l.
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 3, '< BOA SORTE ☺️ >', '-='*3)