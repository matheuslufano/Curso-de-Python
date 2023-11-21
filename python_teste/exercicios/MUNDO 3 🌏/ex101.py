"""
====================================================================
DESAFIO - 101
Crie um programa que leia uma função chamada voto() que vai receber
parâmetro o ano de nascimento de uma pessoa, retornando um valor
literal, indicando se uma pessoa tem idade o suficiente para vota:
 menor que de 18 anos: voto NEGADO
 maior ou igual 18 anos: voto OBRIGATÓRIO
 Maior ou igual a 65 anos: OPCIONAL
====================================================================
"""
# # Escopo de importação
#
# import datetime
# ano = datetime.datetime.now().year
# print(ano)
# def voto (n):
#     idade = ano - nasc
#     print(f'Com {idade} anos: ', end='')
#     if idade < 18:
#         print('VOTO NEGADO')
#     elif idade >= 18 and idade < 65:
#         print('VOTO OBRIGATÓR')
#     elif idade >= 65:
#         print('VOTO OPCIONAL')
#
# nasc = int(input('Em que ano você nasceu? '))
# voto(nasc)

# ==============================================
def voto(ano):
    from datetime import date
    atual = date.today().year #ano atual
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

# Program principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))