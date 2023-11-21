# importe
# =================================
# > Importe sorteio de números:
#     from random import randint
#     computador = randint (0, 10)
# ==================================
# > Importe tempo:
#     from time import sleep
#     sleep(1)  #segundos
#     print("texto")


# ==================================
# Função de maior e menor na Tupla
# max(+)
# menor (-)
# sorte = (randint(0,10), randint(0,10), randint(0,10),
#          randint(0,10), randint(0,10))
# print(f'\nO maior valor foi {max(sorte)}\n'
#       f'O menor valor foi {min(sorte)}')

# #========deseja sair?===============
# sair = ' '
# while sair not in 'SN':
#     sair = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
# if sair == 'N':
#     break
#============OU====================
# resp = str(input("Quer continuar? [S/N] ")).upper()
#     if resp in 'NS':
#         if resp == 'N':
#             break

# # ========lista []=======
# num = [2, 4, 5, 7] #lista.
# num[2] = 3 #altera 2 por 3.
# num.append(7) #adiciona 0 7 a lista.
# num.sort(reverse=True) #inverte a ordem da lista.
# num.insert(2, 2) #na segunda variable da lista (3º) e adicionado 0.
# num.pop() #remove o ultimo valor
# num.pop(2) #remover a segunda variaveu
# num.remove(2) #remove o 2 (nesse caso, o 1º dois)
# lista = [[], []] # Para criar sub lista usa 1 ou + pares de "[]" com vírgulas.

#==========ano atual===============
# from datetime import datetime
# datetime.now()

# sum(cont) #função de somar de uma lista.
# ===========dicionario ex. do ex094==============
# para mostrar o mesmo valor de um dicionário
# podemos usar o 'for':
# galera = [{'nome': 'maria'}]
# pessoa = {'sexo': 'feminino'}
# for p in galera:
#     if p['sexo'] in 'F':
#         print(f'{p["nome"]} ', end='')