print("\033[34mGAME: Pedra Papel e Tesoura\033[m")
print("="*27)
print("Suas opções: "
    "\n[ 0 ] PEDRA🪨 " # 1)  empate 1\perdi 2\ganha 3
    "\n[ 1 ] PAPEL🧻 "# 2) empate 2\perdi 3\ganha 1 
    "\n[ 2 ] TESOURA✂️")# 3) empate 3\perdi 1\ganha 2
jogador = int(input("Qual é a sua jogada: "))
from time import sleep
sleep(1)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("Po!!!")



print('-='*15)
from random import randint
itens = ("Pedra🪨", "Papel🧻", "Tesoura✂️")
computador = randint(0,2)
print("O Jogador jogou {}".format(itens[jogador]))
print("O Computador jogou {}".format(itens[computador]))
print('-='*15)


if computador == 0: # computador jogou pedra
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print('COMPUTAR VENCE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1: # computador jogou papel
    if jogador == 0:
        print('COMPUTAR VENCE')
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA!')
elif computador == 2: # computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTAR VENCE')
    elif jogador == 2:
        print("EMPATE")
    else:
        print('JOGADA INVALIDA!')
else:
        print('JOGADA INVALIDA!')