"""
====================================================================
DESAFIO - 058
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um
número entre 0 e 10. Só que agora o jogodor vai tentar adivinhar até
acertear, mostrando no final quantos palpites foram necessários pra
vencer.
====================================================================
"""
#DESAFIOS DA AULA #10 - Condições (Parte 1)
#================Desafio 028========================
"""
    DESAFIO-028
Escrava um programa que faça o computador "pensar" em um número inteiro
entre O a 5 e peça para o usuário tentar descobrir qual foi o número
escolhido pelo computador.
O programa deverá escrever na tala se o usuário venceu ou perdeu.
"""
# from random import randint  # importar variaveu aleatória (x,y)
# computador = randint(0, 5)  # vai fazer a variaveu sortear o número
# from time import sleep
# print(10*"\033[33m-=-\033[m")
# print('\033[36m   Estou pensando em número!\033[m')
# print(10*"\033[33m-=-\033[m")
# jogador = int(input('Adivie qual número de (0-5) é: ')) # resposta do jogador
# print('\033[35mPROCESSANDO...\033[m')
# sleep(2) # vai demorar 3 segundo para dar a resposta
#
# if jogador == 44:
#     print('\033[32m         Você venceu!\033[m')
# else:
#     print('\033[31m         Você perdeu!\npensei no n° {} e não no nº {} \033[m'.format(computador,jogador))
# ==========================================================================================================
#                   Desafio 058
# O PC deve escolher um número de 0 a 10 de forma aleatória.
# O jogar tem que tentar ater adivinhar
# tem que mostrar por fim a quantidade de tentativa e o número escolhido.

from random import randint
computador = randint (0, 10)
print('\033[31m👁️👁️ Sou seu computador...💻\033[m'
    '\n\033[35mAcabei de pensar em um númeor entre 0 e 10.'
    '\nSera que você conceque advinhar qual foi? \033[m')
acertou = False
palpites = 0
while not acertou:
    print(14*'-=-')
    jogador = int(input('Qual é seu palpite? '))
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\033[31mMais... Tente mais uma vez.\033[m')
        elif jogador > computador:
            print('\033[31mMenos... Tente mais uma vez.\033[m')
print("\033[32mAcertou miseraveu! com {} tentativas\033[m".format(palpites))
