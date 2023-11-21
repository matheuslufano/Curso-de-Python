"""
====================================================================
DESAFIO - 045
Crie um programa que faça o computador jogar Jokanpô com você.
pedra, papel, tesoura.
====================================================================

"""
print("\033[34mGAME: Pedra Papel e Tesoura\033[m")
print("="*27)
print("Suas opções: "
    "\n[ 1 ] PEDRA🪨 " # 1)  empate 1\perdi 2\ganha 3
    "\n[ 2 ] PAPEL🧻 "# 2) empate 2\perdi 3\ganha 1 
    "\n[ 3 ] TESOURA✂️")# 3) empate 3\perdi 1\ganha 2



from time import sleep
jogada = int(input("\nQual é a sua jogada: "))
sleep(1)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("Po!!!")



from random import randint
computador = randint (1,3)

print("="*27)
if jogada == 1:     #PEDRA🪨
    if computador == 1:
        print('\033[34mEMPATE 🪨x🪨\033[m')
    elif computador == 2:
        print('\033[31m     Computador ganhou!\033[m '
              '\n                  🪨x🧻!')
    elif computador == 3:
        print('\033[32m     jogador ganhou!\033[m '
              '\n               🪨x✂️')

if jogada == 2:     #PAPEL🧻
    if computador == 2:
        print('\033[34mempate 🧻x🧻\033[m')
    elif computador == 3:
        print('\033[31m     Computador ganhou!\033[m '
              '\n                   🧻x✂️')
    elif computador == 1:
        print('\033[32m     jogador ganhou!\033[m '
              '\n               🧻x🪨')

if jogada == 3:     #TESOURA✂️
    if computador == 3:
        print('\033[34mempate ✂️x✂️\033[m')
    elif computador == 1:
        print('\033[31m     Computador ganhou!\033[m '
              '\n                ✂️x🪨')
    elif computador == 2:
        print('\033[32m     jogador ganhou!\033[m '
              '\n               ✂️x🧻')
print("="*27)

if jogada == 1:
    jogada = "PEDRA🪨"
elif jogada == 2:
    jogada = "PAPEL🧻"
elif jogada == 3:
    jogada = "TESOURA✂️"

if computador == 1:
    computador = "PEDRA🪨"
elif computador == 2:
    computador = "PAPEL🧻"
elif computador == 3:
    computador = "TESOURA✂️"

print("Jogador joga {}\nComputador joga {}".format(jogada, computador))




