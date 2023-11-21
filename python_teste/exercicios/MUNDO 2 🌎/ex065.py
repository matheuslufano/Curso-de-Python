"""
====================================================================
DESAFIO - 065
Crie um programa que leia vários números inteiros pelo teclado. No
final da execução, mostre a média entre todos os valores e qual foi
o maior e o menor valores lidos. O programa deve perguntar ao usuário
se ele quer ou não continuar a digitar valores.
====================================================================
"""

num = 0
para = 0
soma = 0
media = 0
maior = 0
menor = 0

while para != 'N':
    num = int(input('Digite um número: '))
    para = str(input('[S/N]: ')).upper()
    soma += num
    media += 1
    if num > maior:
        maior = num
    elif num < menor:
        menor = num

media = soma / media
print('Soma: {}, Media: {:.2f}, Maior: {} e Menor: {} '.format(soma, media, maior, menor))
