#DESAFIOS DA AULA #10 - Condições (Parte 1)

#================Desafio 030========================
"""
    DESAFIO-030
Crie um programa que leia um número inteiro e mostre na tela se ele
é PAR ou IMPAR.
"""

num = int(input('Digite um númeor: '))
if num % 2 == 0:
    print('O número {}, é PAR'.format(num))
else:
    print('O número {}, é IMPAR'.format(num))