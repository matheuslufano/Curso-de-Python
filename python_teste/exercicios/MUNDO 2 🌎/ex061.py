"""
====================================================================
DESAFIO - 061
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
====================================================================
"""
print('10 Termos de um PA')

p1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
x = 0
t = p1
while x <= 9:
    x += 1
    print(p1,' -> ', end='')
    p1 += r
print(' acabou')