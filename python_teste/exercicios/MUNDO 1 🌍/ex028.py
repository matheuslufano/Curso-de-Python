#DESAFIOS DA AULA #10 - Condições (Parte 1)

#================Desafio 028========================
"""
    DESAFIO-028
Escrava um programa que faça o computador "pensar" em um número inteiro
entre O a 5 e peça para o usuário tentar descobrir qual foi o número
escolhido pelo computador.
O programa deverá escrever na tala se o usuário venceu ou perdeu.
"""

from random import randint  # importar variaveu aleatória (x,y)
computador = randint(0, 5)  # vai fazer a variaveu sortear o número
from time import sleep

print(10*"\033[33m-=-\033[m")
print('\033[36m   Estou pensando em número!\033[m')
print(10*"\033[33m-=-\033[m")
jogador = int(input('Adivie qual número de (0-5) é: ')) # resposta do jogador
print('\033[35mPROCESSANDO...\033[m')
sleep(2) # vai demorar 3 segundo para dar a resposta

if jogador == 44:
    print('\033[32m         Você venceu!\033[m')
else:
    print('\033[31m         Você perdeu!\npensei no n° {} e não no nº {} \033[m'.format(computador,jogador))

