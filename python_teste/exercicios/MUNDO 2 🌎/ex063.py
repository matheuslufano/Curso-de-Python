"""
====================================================================
DESAFIO - 063
Escreva um programa que leia um número N inteiro qualquer e mostre
na tela os N primeiros elementos de uma Sequência de fibonacci.
Ex: 0 ->1->1->2->3->5->8.
====================================================================
"""

# O programa tem que ler um número N 'int'
# mostras os N 1° n° de uma Sequência de fibonacci primos1
print('=============Sequência de fibonacc===================')
n = int(input('Em qual termo a Sequência de fibonacci deve mostrar: '))
repete = 1
num1 = 0
num2 = 1
num3 = num2 + num1
print('{}, {}, '.format(num1, num2), end='')
while repete <= (n - 2):
    repete += 1
    print('{}, '.format(num3), end='')
    num1 = num2
    num2 = num3
    num3 = num1 + num2
    num4 = num2 - num3 + num3
print('(O {}° termo é ({})'.format(n, num4))