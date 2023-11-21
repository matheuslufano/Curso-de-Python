"""
====================================================================
DESAFIO - 079
Crie um programa onde o usuário pode digitar various valores e
cadastre em uma lista.
Caso o número já exista na lista, não será adicionado.
Ao fim do program será exibido todos os valores únicos digitados, em
ordem crescente.
====================================================================
"""
lista = []
while True:
    res = int(input('Digite um valor: '))
    if res not in lista:
        lista.append(res)
        print('\033[32mValor adicionado com sucesso!\033[m')
    else:
        print('\033[31mValor duplicado!!!\033[m')
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if sair == 'N':
        print('-='*20)
        print('Você digitou os valores', lista)
        break