"""
====================================================================
DESAFIO - 086
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com
valores lidos pelo teclado.
No final mostre a matriz na tela, com a formatação correta.
====================================================================
 """
# matriz = [[], [], [], [], [], [], [], [], []]
# for c in range(0,9):
#     valor = int(input(f'Digite um valor para [0, {c}]: '))
#     matriz[c].append(valor)
# print(matriz[0], matriz[1], matriz[2])
# print(matriz[3], matriz[4], matriz[5])
# print(matriz[6], matriz[7], matriz[8])

#====código em vídeo=========
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite p/ posição [{l}, {c}]: '))
print('='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()