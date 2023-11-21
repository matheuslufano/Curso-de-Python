"""
====================================================================
DESAFIO - 081
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
a) Quantos números foram digitados.
b) A lista de valores, ordenada de forma decrescente.
c) Se o valor 5 foi digitado e está ou não na lista.
====================================================================
"""
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input("Quer continuar? [S/N] ")).upper()
    if resp in 'NS':
        if resp == 'N':
            break
valores.sort(reverse=True)
print('-='*20)
print(f'Você digitou {len(valores)} elementos.\n'
      f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')