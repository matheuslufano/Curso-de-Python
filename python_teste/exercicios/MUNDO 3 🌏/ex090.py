"""====================================================================
DESAFIO - 090
Faça um programa que leia nome e média de um aluno, guardando também
a situação em um dicionário. No Final mostre o conteúdo da estrutura
na tela
===================================================================="""

nome = str(input('Nome: '))
média = int(input(f'Média de {nome}: '))
if média > 6:
    situação = 'Aprovada'
else:
    situação = 'Reprovada'
print(f'Nome é igual a {nome}\n'
      f'Média é igual a {média}\n'
      f'Situação é igual a {situação}')