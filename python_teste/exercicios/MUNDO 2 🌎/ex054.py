"""
====================================================================
DESAFIO - 054
Crie um programa que leia o ano de nascimento de 7 pessoas. No final
mostre quantas pessoas ainda não atingiram a maioridade e quantas já
são maiores.
(OBS.: considere a maior idade sendo 21 ANOS)
====================================================================
"""

#==================meu código==========================================
# maior = 0
# menor = 0
# for c in range(0,7):
#     ano = int(input('Qual ano você nasceu? '))
#     if ano <= 2003:

#
# print("Há {} pessoas maiores de idade\nHá {} pessoas maiores de idade".format(maior, menor))


"""
==============Resolução da vídeo aula=================================
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pess in range(1, 8):
    nasc = int(input('Em qual ano a {}° pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    print('Essa pessoa tem {} anos.'.format(idade))
    if idade >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print("Essa pessoa é menor de idade")
print("Essa pessoa é maior de idade")"""
