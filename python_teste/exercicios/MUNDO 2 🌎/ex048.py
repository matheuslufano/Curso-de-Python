"""
====================================================================
DESAFIO - 048
Faça um programa que calcule a soma entre todos os números impares
que são múltiplos de três sendo encontrado no intervalo de 1 ate 500.
====================================================================
"""
s = 0
for c in range(1,500,2):
    if c % 3 == 0:
        print('{} + {} = {}'.format(s, c, c + s))
        s = s + c

soma = 0
for i in range(1, 501):
    if i % 2 == 1 and i % 3 == 0:
        soma += i
print('A soma de todos os múltiplos de 3\nque são impares = ',soma)