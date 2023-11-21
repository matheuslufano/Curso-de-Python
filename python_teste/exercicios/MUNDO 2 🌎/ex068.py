"""
====================================================================
DESAFIO - 068
Faça um jogo que jogue par ou impar com o pc, o jogo só é interrompido
depois que o jogador perder.
por fim mostre o total de vitoria consecutivas no fim da partida.

====================================================================
"""
# no play 1 tem q escolher se ele vai ser par ou impar
# o pc tem que sortear o número.
# caso o jogador perca, o jogo acaba.
jogador = 0
pc = 0
while True:
    print('🟥🟧🟨🟩🟦🟪️'*2)
    print('🦄GAME: PAR OR IMPAR 🎮🙅‍ ')

    from random import randint
    computador = randint (0,100)
    # print(computador)
    print('-'*28)
    num = int(input('🦉\033[33mDigite um valor: '))
    play1 = str(input('Escolha 🦩Par ou Impar🐿️ [P/I]:\033[m ')).upper()
    resultador = computador + num
    print('-'*28)
    print(f'Play1 escolheu ({num}) e pc ({computador})')
    print('-'*28)

    if resultador % 2 == 0:
        print('O resultado é PAR 🦜')
        if play1 == 'P':
            print(f'     \033[32mPlay1 ganhou ({play1})\033[m 👏🥳')
            jogador += 1
        else:
            pc += 1
            print('     \033[31mGAME OVER! 🥺\033[m\n'
                  f'Você ganhou {jogador} vezes.'
                  f'placar {jogador}/{pc}')
            break
    else:
        print('O resultado é IMPAR 🐦')
        if play1 == 'P':
            print(f'     \033[32mPlay1 ganhou ({play1})\033[m 👏🥳')
            jogador += 1
        else:
            pc += 1
            print('     \033[31mGAME OVER! 🥺\033[m\n'
                  f'Você ganhou {jogador} vezes.'
                  f'\nplacar {jogador}/{pc}')
            print('⬛⬛⬛⬛⬛'*2)
            break