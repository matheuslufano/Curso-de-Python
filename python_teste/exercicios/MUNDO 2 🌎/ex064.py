"""
====================================================================
DESAFIO - 064
Crie um programa que leia vários números inteiros pelo teclado. O
programa só vai parar quando o usuário digitar o valor 999, que é a
condição de parada. No final, mostra quantos números foram digitados
e qual foi a soma entre eles (Desconsiderando o flog).
====================================================================
"""

# ler various n° pelo teclado
# para no 999
# mostrar quantos números foam digitados
# e sua soma
num = 0
tentativas = 0
soma = 0
repete = 1
while num != 999:
    repete += 1
    num = int(input('Digite um número: '))
    soma += num
    tentativas += 1
print('Foram {} tentativas, a soma de todos os valores são {}'.format(tentativas, soma))

