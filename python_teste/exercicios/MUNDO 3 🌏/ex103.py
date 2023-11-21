"""
DESAFIO - 103
Faça um programa que tenha uma função chamada "ficha()", que
receba dois parâmetros opcionais:
    - Nome de um jogador.
    - Gols feitos

O program deverá conseguir mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente.
"""
def ficha(nome='<desconhacido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


# Programa principal
n = str(input("Nome do jogador: "))
g = str(input("Número de gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() =='':
    ficha(gols=g)
else:
    ficha(n, g)