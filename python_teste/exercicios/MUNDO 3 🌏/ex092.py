"""
====================================================================
DESAFIO - 092
Crie um programa que leia nome, ano, de nascimento e carteira de tra-
balho, cadastre - os em um dicionário se por acaso a CTPS for dife-
rente de zero (0), o dicionário recebera o ano de contratação e o
salário. Calcule e acrescente, além da idade, com quantos anos a
pessoa vai se aposentar.
====================================================================
"""
# 'nome'
# 'ano'
# 'nascimento'
# 'carteira'
# 'salario'
from datetime import datetime
dados = dict()
dados['nome'] = str(input("Nome: "))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctds'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctds'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

print('-='*20)
for k,v in dados.items():
    print(f'  - {k} tem o valor {v}')