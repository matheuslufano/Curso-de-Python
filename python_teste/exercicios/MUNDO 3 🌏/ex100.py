"""
Desafio - 100
Faça um programa que tenha uma:
 - lista chamada números
 - duas funções chamadas:
    Sorteio()
    SomaPar
A primeira função vai sortear 5 números e vai colocá-los
dentro da lista.
A segunda função vai mostrar a soma entre todos os valores
PARES sorteados pela função anterior.
"""
# from random import randint
# from time import sleep
# def sorte():
#     números = []
#     print('Sorteando "05" valores: ')
#     # 1°) Sorteio(5 valores)
#     for a in range(0, 5):
#         números.append(randint(0, 10))
#         print(números[a], end=' ')
#         sleep(0.5)
#     print("PRONTO!")
#     # 2º) SomaPar
#     par = []
#     for b in números:
#         if b % 2 == 0:
#             par.append(b)
#     sleep(1)
#     print('A soma dos pares:')
#     sleep(1)
#     print(f'{par} é igual a {sum(par)}')
# sorte()
#=====================Curso em vídeo============================
from random import randint
from time import sleep

def sorteia(lista):
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end =' ', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores de {lista}, temos {soma}')

número = list()
sorteia(número)
somaPar(número)
