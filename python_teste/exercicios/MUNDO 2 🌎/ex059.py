"""
DESAFIO - 059
Crie um programa que leia dois valores e :
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

# leia dois valores
# mostre um menu na tela
num1 = int(input("      Digite um número: "))
num2 = int(input("      Digite outro: "))

resposta = 0
while resposta != 5:
    resposta = int(input(""
   " -------------------------⨏"
   "\n [1] Somar ➕            ⨎"
   "\n [2] Multiplicar✖️       ⨖"
   "\n [3] Maior⚖️             ⨕"
   "\n [4] Novos Números🆕     ⨚"
   "\n [5] Sair do programa😽  ⨗"
   "\n ------------------------⨙"
   "\n \033[33mEscolha uma opção:\033[m "))


    if resposta == 1:
        print(' ---> [1] Somar\n'
              ' ---> \033[32m{} + {} = {}\033[m'.format(num1,num2,num1+num2))
    elif resposta == 2:
        print(' ---> [2] MULTIPLICAÇÃO\n'
              ' ---> \033[32m{} X {} = {}\033[m'.format(num1,num2,num1*num2))
    elif resposta == 3:
        if num1 > num2:
            print(' ---> [3] Maior\n'
                  ' ---> \033[32m{} é mais que {}\033[m'.format(num1,num2))
        else:
            print(' ---> [3] Maior\n'
                  ' ---> \033[32m{} é mais que {}\033[m'.format(num2,num1))

    elif resposta == 4:
        print('[4] Novos Números🆕\n'
              'Digite novamente os números!')
        num1 = int(input("Digite um número: "))
        num2 = int(input("igite outro: "))

    elif resposta > 5 or resposta < 1:
        print('Opção invalidada!\n'
              'Digite novamente!')
print('Até mais 😽')