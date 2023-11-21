"""
Desafio - 078

Faça um programa que leia 5 valores numéricos e
guardeos em uma lista.
No final, mostre qual foi o mair e o menor valor.
"""

valor = []
mai = 0
men = 0
posição_mai = []
posição_men = []
for c in range(0,5):
    valor.append(int(input(f'Digite um para a posição {c}: ')))
    if c == 0:
        mai = men = valor[c]
    else:
        if valor[c] > mai:
            mai = valor[c]
        if valor[c] < men:
            men = valor
print('—'*30)
for i, v in enumerate(valor):
    if v == mai:
        posição_mai.append(i)
    if v == men:
        posição_men.append(i)
print(f'Você digitou os valores {valor}\n'
      f'O maior número é {mai}, nas posições {posição_mai}\n'
      f'O menor número é {men}, nas posições {posição_men}')
