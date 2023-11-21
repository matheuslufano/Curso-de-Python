"""
DESAFIO - 104
Crie um programa que tenha a função leiaint(),
que vai funcionar de forma semelhante à função
input() do python, só que fazendo a validação
para aceitar apenas um valor numérico.
ex:
n=leiaInt('Digite um n')
"""
def leiaInte(n):
    while True:
        if n.isnumeric():
            return n
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            n = input('Digite um número: ')


# programa principal
n = leiaInte(input('Digite um número: '))
print(f'Você acabou de digitar o número {n}')
