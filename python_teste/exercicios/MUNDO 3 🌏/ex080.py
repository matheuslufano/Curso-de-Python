"""
====================================================================
DESAFIO - 080
Crie um programa que o usuário possa digitar 5 valores e cadastre-os
em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.
====================================================================
"""

num =list()
for n in range(0,5):
    res = int(input('Digite um valor: '))
    if n == 0 or res > num[-1]:
        num.append(res)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(num):
            if res <= num[pos]:
                num.insert(pos, res)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-='*20)
print(num)

# num = [1, 2, 3, 4, 5]
# num[2] = 80 #substitui o valor no determinado posição
# num.append(50) #adiciona valor
# num.insert(2,13) #substitui a posição e matem os demais valores
# # num.sort() #põe em ordem
# print(num)