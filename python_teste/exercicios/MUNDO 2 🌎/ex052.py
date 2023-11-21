"""
====================================================================
DESAFIO - 052
faça um program que leia um número inteiro e diga se ele é ou não um
número primo. (eles são dívisiveu por 1 e por ele mesmo)
====================================================================
"""
num = int(input('Digite um número inteiro: '))
if num % num == 0 and not num % 2 == 0:
    print(num, 'é um número primo ')
else:
    print("{} Não é um númeor primo!".format(num))


# núm = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end='')
        tot = tot + 1
    else:
        print('\033[31m', end='')
    print("{} ".format(c), end='')
print('\n\033[mO número {} foi divisível \033[32m{}\033[m vezes'.format(num, tot))