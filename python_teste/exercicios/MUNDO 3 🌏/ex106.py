"""
====================================================================
DESAFIO - 106
Faça um mini-sistema que utilize o interactive help do python. O usuário
vai digitar o comando e o manual vai aparecer. Quando o usuário digitar
a palavra 'FIM', o programa se encerrá.
OBS: use cores.
====================================================================
"""
# cores = {'branco': '\033[7:40m',
#          'vermelho': '\033[41m',
#          'verde': '\033[42m',
#          'amarelo': '\033[43m',
#          'azul': '\033[44m',
#          'roxo':  '\033[45m',
#          'azulclaro': '\033[46m',
#          'preto': '\033[42m',
#          'fim': '\033[m'}
# def titulo(t, cor):
#     tamanho = len(t)
#     print(f"{cor}{tamanho * '~'}\n{t}\n{tamanho * '~'}")
#     print(end=f'{cores["fim"]}')
#
# def manual(aju):
#     if aju == 'fim':
#         return aju
#     texto = f'Acessando manual do comando {aju}'
#     tamanho = len(texto)
#     print(f"{cores['azul']}{tamanho * '~'}\n{texto}\n{tamanho * '~'}\n{cores['branco']}")
#     print(f'{help(aju)}')
#     print(end=f'{cores["fim"]}')
#
#
#
# #programa principal
# while True:
#     titulo('SISTEMA DE AJUDA PYHELP', cores['verde'])
#     manual(str(input('Função ou Biblioteca > ')))
#     if manual('fim'):
#         titulo('Até logo', cores['vermelho'])
#         break
#============RESPOSTA============================================
from time import sleep
c = ('\033[m',             # 0 - sem cor
     '\033[7;37;40m',      # 1 -branco
     '\033[0;37;41m',      # 2 - vermelho
     '\033[0;37;42m',      # 3 - verde
     '\033[0;37;43m',      # 4 - amarelo
     '\033[0;37;44m',      # 5 - azul
     '\033[0;37;45m',      # 6 - roxo
     '\033[0;37;46m',      # 7 - azulclaro
     '\033[0;37;47m'       # 8 - preto
     );

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'',5)
    print(c[1])
    print(help(com))
    print(c[0])
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg)+4
    print(f'{c[cor]}{tam*"~"}\n  {msg}\n{tam*"~"}')
    print(end=f'{c[0]}')
    sleep(1)

# Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 3)
    comando = str(input(f'{c[0]}Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 2)

