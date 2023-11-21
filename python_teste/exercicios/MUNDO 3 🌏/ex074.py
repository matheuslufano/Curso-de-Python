"""
Exercício Python 074:

Crie um programa que vai gerar cinco números aleatórios e colocar
em uma tupla. Depois disso, mostre a listagem de números gerados
e também indique o menor e o maior valor que estão na tupla.
"""
#- sortear
#- qual é o maior
#- qual é o menor
maior = 0
menor = 0
cont = 0
num = 0
from random import randint
sorte = (randint(0,10), randint(0,10), randint(0,10),
         randint(0,10), randint(0,10))
print(f'O pc sorteou o número: ', end= '')
for c in sorte:
    print(f' {c}', end='')
print(f'\nO maior valor foi {max(sorte)}\n'
      f'O menor valor foi {min(sorte)}')
