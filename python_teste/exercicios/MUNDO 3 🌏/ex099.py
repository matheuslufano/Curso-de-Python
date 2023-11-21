"""
====================================================================================
Desafio - 099 😯
Faça um programa que tenha uma função chamada maior(), que receba vários
parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
====================================================================================
"""
from time import sleep
def maior(*num):
    print('-' * 33)
    print('Analisando os valores passados...')
    print(f'Forem informados "{len(num)}" Valores: ')
    if len(num) == 0:
        sleep(0.5)
        print(f'O maior número é 0.')
    else:
        for c in range(0, len(num)):
            print(num[c], end=' ')
            sleep(0.4)
            if c == 0:
                maior = num[c]
            else:
                if num[c] > maior:
                    maior = num[c]
        print(f'\nO maior número é: {maior}.')
maior(1,3,19,28,3,5,1,2,8)
maior(9,2,0,3)
maior(2,5,4,7,)
maior()