"""
====================================================================
DESAFIO - 084
Faça um programa que leia nome e peso de várias pessoas, guardando tudo
em uma lista. No final mostre:
a) Quantas pessoas foram cadastradas.
b) Uma listagem com as pessoas mais pesadas.
c) uma listagem com as pessoas mais leves.
====================================================================
"""
# galerinha = []
# pessoa = []
# pessoa_g = 0
# pessoa_p = 0
# pesado = 0
# leve = 0
# listpesado = []
# listleve = []
# sair = ' '
# while True:
#     pessoa.append(str(input('Nome: ')))
#     pessoa.append(int(input('Peso (Kg): ')))
#     galerinha.append(pessoa[:])
#     pessoa.clear()
#
#     sair = str(input('Quer continuar? [S/N] ')).upper()
#     if sair in 'NS':
#         if sair == 'N':
#             break
#
# print(f'Foram {len(galerinha)} pessoas cadastradas.')
# pesado = galerinha[0][1]
# leve = galerinha[0][1]
#
# for p in galerinha:
#     if p[1] >= pesado:
#         pesado = p[1]
#         pessoa_g = p[0]
#         listpesado.append(p[0])
#         listpesado.append(pesado)
#     elif p[1] <= leve:
#         leve = p[1]
#         pessoa_p = p[0]
#         listleve.append(p[0])
#         listleve.append(leve)
# print(f'A pessoa mais pesada é {pessoa_g} com {pesado} Kgs.\n'
#       f'A pessoa mais leve é {pessoa_p} com {leve } Kgs')
# print(listpesado, listleve)
# #galera: [['matheus', 63], ['superman', 100], ['monica', 65]]
# # print(f'Pessoas: {pessoa}\n'
# #       f'galera: {galerinha}')

#===========código do exercício da aula=========


#lista temporaria
temp = []
#lista principal
princ = []
maior = menor = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: kg  ')))
    if len(princ) == 0:
        maior = menor = temp[1] #A variaveu "temp" na posição [1] é o peso.
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append((temp[:])) #[:] copia tudo na lista
    temp.clear()# isso irar limpar a variaveu 'temp'.
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'Ao todo, foram cadastrado {len(princ)} pessoas.')
print(f'O maior peso foi de {maior} Kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print()
print(f'O menor peso foi de {menor} Kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}', end='')
print()