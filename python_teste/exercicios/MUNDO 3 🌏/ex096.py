"""
(Desafio - 96)
Faça um programa que tenha uma função chamada área(), que receba as dimensões de
um terreno retangular (largura e comprimento) e mostre a aréa do terreno
"""
def área(a, b):
   x = (a * b)/2
   print('\033[33mA área de um terreno\n'
         f'  {a} X {b} = {x}m²\033[m')


print('Controle de terrenos')
print("-"*22)
l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))
área(l, c)