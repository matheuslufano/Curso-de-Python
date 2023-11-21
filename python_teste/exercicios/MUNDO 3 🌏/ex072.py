"""
                        Número por Extenso
====================================================================
DESAFIO - 072
Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20) e
mostrá-lo por extenso.
====================================================================
"""
# for c in range(0,21):
#     print(f'{c}, ',end='')

#====================== meu código ==================================================
while True:
    num = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
            'seis', 'sete','oito', 'nove', 'dez', 'onze', 'dose',
            'treze', 'catorze', 'quinze', 'dezesseis',
            'dezessete', 'dezoito', 'dezenove', 'vinte')
    res = int(input('Digite um número entre 0 a 20: '))
    if res > 20:
        res = int(input('Tente novamente.\n'
                        'Digite um número entre 0 a 20: '))
    if res == num[res]:
        print(f'Você digitou o número {cont[res]}')
        break

#=========== código curso em vídeo =================================================
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'dose',
        'treze', 'catorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
        break
    print('tente novamente. ', end='')
print(f'Você digitou o número {cont[núm]}')