"""
====================================================================
DESAFIO - 056
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
- A média de idade do grupo.
- Qual o é o nome do homem 🙄 mais velho.
- Quantas mulheres tem menos de 20 anos.
====================================================================
"""
# idade = 0
# idade_M = 0
# idade_O = 0
# idade_X = 0
#
# for p in range(1,5):
#     sexo = str(input("Sendo (M) Mulher, (O) Homem e (X) Não binario"
#                "\nCom qual gênero você se identifica? ")).upper()
#
#     if sexo == "M":
#         nome = str(input("Qual é o seu nome: "))
#         idade = int(input("Quartos anos você tem: "))
#         idade_M = idade_M + idade
#     elif sexo == "O":
#         nome = str(input("Qual é o seu nome: "))
#         idade_O = int(input("Quartos anos você tem: "))
#         idade_O = idade_O + idade
#     elif sexo == "X":
#         nome = str(input("Qual é o seu nome: "))
#         idade_X = int(input("Quartos anos você tem: "))
#         idade_X = idade_X + idade
#
# media = (idade_X + idade_M + idade_O)/3
# print('A média de pessoas é ',media)


somaidade = 0
médiaidade = 0
maior_idade_homem = 0
nome_velho = 0
totmulher20 = 0
x = 0
for p in range (1,4):
    print("-----{}° PESSOA-----".format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('[F] Mulher'
                   '\n[M] Homem'
                   '\n[X] N.Binario'
                   '\nIdentidade de gênero: ')).strip()
    somaidade += idade


    if p == 1 and sexo in "Mm":
            maior_idade_homem = idade
            nome_velho = nome
    elif sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    elif sexo in 'Ff' and idade > 20:
        totmulher20 += 1
    # if p == 1 and sexo == 'X':
    elif sexo == 'Xx':
        x = x + 1
médiaidade = somaidade / 3
print("A média de idade do grupo é de {} anos".format(médiaidade))
print('O homem mais velhor tem {} anos e se chama {}.'.format(maior_idade_homem,nome_velho))
print('Ao total, são {} mulheres com menos de 20 anos'.format(totmulher20))
print('Há {} não binaril no grupo'.format(x))
