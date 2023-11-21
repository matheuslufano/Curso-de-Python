"""
====================================================================
DESAFIO - 087
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O mair valor da segunda linha.
====================================================================
"""
# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# par = 0
# coluna3 = 0
# maior = 0
# for coluna in range(0,3):
#     for linha in range(0,3):
#         valor = int(input(f'Digite um valor para [{coluna}/{linha}]: '))
#         matriz[coluna][linha] = valor
#         if valor % 2 == 0:
#             par += valor
#         if coluna == 2:
#             coluna3 += valor
#         if linha == 1:
#             if matriz[1][0] == 0:
#                 maior = valor
#             if valor > matriz[1][0]:
#                 maior = valor
# print('='*30)
# for c in range(0, 3):
#     for l in range(0, 3):
#         print(f'[{matriz[l][c]:^5}]', end='')
#     print()
# print('='*30)
# print(f'A soma de todos valores pares é: {par}\n'
#       f'A soma dos valores da 3º coluna é {coluna3}\n'
#       f'O maior valor da segunda linha é {maior}\n')

# =============Código visão e vídeo==================
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite p/ posição [{l}, {c}]: '))
print('='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz [l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('='*30)
print(f'A soma dos valores pares é {spar}.')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')