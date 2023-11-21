"""
===================================================================
DESAFIO - 057
Faça um programa que leia o sexo de uma pessoa, mas só aceite os va-
lores 'M', 'F' e 'X'. Caso esteja errado, peça a digitações novamen-
te até ter um valor correto.
====================================================================
"""
# Perguntar qual é a identidade de gênero da pessoa.
# Mostras as opções e analisar a resposta.
# Responder
sexo = False
while sexo == False:
      print('-=-'*10)
      print('[F] Feminino'
            '\n[M] Masculino'
            '\n[X] Não Binário')
      print('-=-'*10)
      sexo = str(input("Com qual gênero você se indenti: ")).upper()

      if sexo == 'F':
            sexo = True
      elif sexo == 'M':
            sexo = True
      elif sexo == 'X':
            sexo = True
      else:
            print('Digite novamente!')
            sexo = False