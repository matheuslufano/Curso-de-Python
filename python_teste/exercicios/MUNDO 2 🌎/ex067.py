"""
====================================================================
DESAFIO - 067
Faça um programa que mostre a tabuada de vários números, um de cada vez,
o programa será interrompido quando o numero for negativo.
====================================================================
"""

while True:
    print('='*40)
    tabuada = int(input('Você quer a tabuada de qual número: '))
    if tabuada < 0:
        print('=' * 40)
        print(f'O programa não reconhece o número "{tabuada}"\npois ele é negativo')
        break
    print('=' * 40)
    num = 0
    while num <=10:
        print(f'{tabuada} x {num} = {tabuada*num}')
        num += 1