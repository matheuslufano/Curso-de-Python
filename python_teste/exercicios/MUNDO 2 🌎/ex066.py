"""
Desafio 066
Crie um programa que leia various números inteiros.
O programa para ao digitar o valor 999 'condição de parada'
por fim, mostre quantos nº foram digitados e qual foi a soma entre eles.
"""
soma = 0
quantidade = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
    quantidade += 1
print(f'Foram {quantidade} números digitados, a sua soma vale {soma}.')
