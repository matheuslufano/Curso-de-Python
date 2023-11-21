"""
====================================================================
DESAFIO - 069
Crie um programa que leia a idade e o sexo de várias pessoas. A cada
pessoa cadastrada, o programa deverá perguntar se o usuário quer ou
não continuar. No final mostre:
a) Quantas pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos.
====================================================================
"""

# Idade
# Sexo 😏#
maior = 0
homem = 0
mulher = 0
while True:
    print('...' * 10)
    print('       CADASTRO DE PESSOA')
    print('...' * 10)
    i = int(input('Idade: '))
    if i >= 18:
        maior += 1
    x = ' '
    while x not in 'FMX':
        x = str(input('Sexo: [F/M/X] ')).upper()
        if x == 'M':
            homem += 1
        if i < 20 and x == 'F':
            mulher += 1
    # print('___' * 10)
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if sair == 'N':
         break
print('<>' * 20)
print(f'Tem {maior} maiores que 18 anos.')
print(f'Tem {homem} homens que foram cadastrados. ')
print(f'tem {mulher} mulheres com menos de 20 anos.')
print('<>' * 20)
# a) Quantas pessoas tem mais de 18 anos.
# b) Quantos homens foram cadastrados.
# c) Quantas mulheres tem menos de 20 anos.