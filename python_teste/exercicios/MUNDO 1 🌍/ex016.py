#DESAFIOS DA AULA #08 DE PYTHON (Utilizando Módulos)

#================Desafio 016========================
"""         (Quebrando um número)
Crie um programa que leia um númeor real qualquer
pelo teclado e mostre na tela a sua porção inteira.

EX:
Digite um número: 6.127
O némero 6.127 tem a parte inteira "6".

dica: dar uma olhada em todas as funçôes que tem dentro
da classe do modeulo messi que importamos em aula #08.

"""
#===================================================
import math
import os
x = float(input("Digite um número quabrado: "))
inteiro = math.trunc(x)
print("Nº quebrado é {}, seu número inteiro é{}".format(x,inteiro))
# ou --> print("O valor quebrado é {} e a sua porção inteira é {}".format(x,int(x)))
