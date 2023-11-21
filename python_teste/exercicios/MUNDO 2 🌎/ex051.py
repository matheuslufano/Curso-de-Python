"""
====================================================================
DESAFIO - 051
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
no final, mostre os 10 primeiros termos dessa progressão.
====================================================================
"""

print('10 Termos de um PA')

p1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = p1 + (10 - 1) * r
for c in range(p1,decimo,r):
    print('{} '.format(c), end=' ⇒ ')
print('acabou')