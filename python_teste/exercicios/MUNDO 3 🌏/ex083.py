"""
====================================================================
DESAFIO - 083
Crie um programa onde o usuário digite uma expressão qualquer que
use parênteses. Seu aplicativo deverá analisar se a expressão passada
está com os parenteses abertos e fechados na ordem correta.
====================================================================
"""
# frase = str(input('Digite uma expressão com parentes: '))
# cochete_a = 0
# cochete_f = 0
# for p in range(len(frase)):
#     if frase[p] == '(':
#         cochete_a += 1
#     if frase[p] == ')':
#         cochete_f += 1
# if cochete_f == cochete_a:
#     print('Expressão ok')
# else:
#     print('Expressão invalida!')

#======== CÓDIGO do curso =========
expr = str(input('Digite a expressão: '))
parentes = []
for símb in expr:
    if símb == '(':
        parentes.append('(')
    elif símb == ')':
        if len(parentes) > 0:
            parentes.pop()
        else:
            parentes.append(')')
            break
if len(parentes) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')