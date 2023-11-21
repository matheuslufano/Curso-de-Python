"""
Desafio - 098
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros:
início, fim e passo e realize a contagem.

Seu program tem que realizar três contagens através da função criada:
A) De 1 até 10, de 1 em 1.
B) De 10 até 0, de 2 em 2.
C) Uma contagem personalizada.
"""
# from time import sleep
# inicio = 1
# fim = 10
# passo = -1
#
#
# print(passo)
# if inicio < fim:
#     print('if 1')
#     if passo < 0:
#         passo = -(passo)
#         print(passo)
#     while True:
#         print(inicio, end=' ')
#         sleep(0.2)
#         inicio += passo
#         if inicio == fim:
#             print(fim)
#             break
#
# if inicio > fim:
#     print('if 2')
#     if passo < 0:
#         passo = -(passo)
#     while True:
#         print(inicio, end=' ')
#         sleep(0.20)
#         inicio -= passo
#         if inicio < fim:
#             break

# ===========Curso em vídeo=====================
from time import sleep
# inicio = i
# fim = f
# passo = p
def contador(i, f, p):  # indices
    # correções:
    if p < 0:  # passo negativo
        p *= -1
    if p == 0:
        p = 1
        
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.4)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.2)
            cont -= p
        print('FIM!')
    print('-'*32)

#   Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)