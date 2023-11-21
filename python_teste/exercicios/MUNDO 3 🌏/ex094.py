"""
====================================================================
DESAFIO - 094
Crie um programa que leia nome, sexo e idade de várias pessoas, guar-
dando os dados de cada pessoa em um dicionário e todos os dicionários
em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima de média.
====================================================================
"""
# list = [{'cadastro': 1, 'nome': 'matheus', 'idade': 23, 'sexo': 'M'},
# {'cadastro': 2, 'nome': 'carla', 'idade': 20, 'sexo': 'F'},
# {'cadastro': 3, 'nome': 'heloisa', 'idade': 19, 'sexo': 'F'}]
# mulheres = [{'heloisa', 'carla'}]
# dict = {'idade': 62}
# cont = 3
# idade = 62

# list = []
# mulheres = []
# dict = {}
# cont = 0
# idade = 0
# while True:
#     cont += 1
#     print('-' * 30, f'\nCadastro (0{cont})')
#     dict['cadastro'] = cont
#     dict['nome'] = str(input('Nome: '))
#     dict['idade'] = int(input('Idade: '))
#     idade += idade
#
#     while True:
#         dict['sexo'] = str(input('Sexo: [M/F/X] ')).upper()
#         if dict['sexo'] in "MFX":
#             list.append(dict.copy())
#             if dict['sexo'] == 'F':
#                 mulheres.append(dict['nome'])
#             break
#
#     sair = ' '
#     while sair not in 'NS':
#         sair = str(input('Quer continuar: [S/N] ')).upper().strip()[0]
#
#     if sair == "N":
#         print('-'*30, '\nLista: ')
#         break
# média = idade / cont
# for c in list:
#     print(c)
#
#
# # A) Quantas pessoas foram cadastradas.
# # B) A média de idade do grupo.
# # C) Uma lista com todas as mulheres.
# # D) Uma lista com todas as pessoas com idade acima de média.
# print('-'*30)
# print(f"""
# A) O grupo tem {cont} pessoas.
# B) a média de idade é {média:.2f} anos.
# C) As mulheres cadastradas foram: {mulheres}.
# D) lista das pessoas que estão acima da média:
# """)
# for c in list:
#     if c['idade'] >= média:
#         print(f'    ↪ {c["nome"]} com {c["idade"]} anos.')

#===============CURSO EM VÍDEO================
galera = list()
pessoa = dict()
soma = média = 0
while True:
    print('-' * 30)
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F/X] ')).upper()[0]
        if pessoa['sexo'] in 'MFX':
            break
        print("""Identidade de gênero não identificada:
        M - Masculino
        F - Feminino
        X - Não binario e outras""")
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-' * 30)
print(galera)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma/len(galera)
print(f'B) A media de idade é de {média:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end ='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for i in galera:
    if i['idade'] >= média:
        print(f'    "↪ {i["nome"]} com {i["idade"]} anos. ')
print('<<< ENCERRADO >>>')