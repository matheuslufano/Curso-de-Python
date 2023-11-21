"""
====================================================================
DESAFIO - 077
Crie um programa que tenha uma tupla com várias palavas
(ñ usar acentos). A pois isso, mostre, para cada palavra, quais são as
suas vogais.
====================================================================
"""

frase = 'punheta', 'pau', 'porra', 'cueca'
# for tupla in frase:
#     print(f'\nA palavra {tupla.upper()} tem (', end= ' ')
#     for c in tupla:
#         if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
#             print(c, end=' ')
#     print(') vogais', end=' ')

for p in frase:
    print(f'\nNa palavra {p.upper()} tem (', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print(') de vogais ',end=" ")


