"""
====================================================================
DESAFIO - 102
Crie um programa que tenha uma função fatorial() que receba dois
parâmetros:
    1°) Número (Indique o número a calcular)
    2°) Show (valor lógico "opcional")
====================================================================

"""
def fatorial(num, show=False):
    fat = 1
    for c in range(num, 0, -1 ):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= c
    return fat



print(fatorial(5, show=True))