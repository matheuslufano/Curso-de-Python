#DESAFIOS DA AULA #08 DE PYTHON (Utilizando Módulos)

#================Desafio 017========================
"""            (Catetos e Hipotenusa)
Faça um programa que leia o comprimento do cateto aposto
e do cateto adjacete de um triãngulo retângulo, calcuçe
e mostre o comprimento da hipotenusa.

 O teorema de Pitágoras determina que o
 quadrado da medida da hipotenusa (c2)
 é igual à soma dos quadrados das medidas
 dos catetos (a2+b2). Portanto, a fórmula
 do teorema de Pitágoras é c2=a2+b2.
"""
#===================================================
# HÁ DUAS MANEIRAS DE SE FAZER ESSE PROGRAMA!

print("comprimento da hipotenusa\n          "
      "do\ntriãngulo retângulo")

print()
from math import sqrt
co = float(input("Qual o comprimento do cateto aposto: "))
ca= float(input("Qual o comprimento do cateto adjacete: "))

hi = (co ** 2 + ca ** 2) ** (1/2)
print("A hipotenusa é: {:.2f}".format(hi))
#----------------------------------------------------------------------
#                importação

import math
co = float(input("Qual o comprimento do cateto aposto: "))
ca= float(input("Qual o comprimento do cateto adjacete: "))
hi1 = math.hypot(co,ca)
print("A hipotenusa com importão: {:.2f}".format(hi))

# OU
from math import hypot

co = float(input("Qual o comprimento do cateto aposto: "))
ca= float(input("Qual o comprimento do cateto adjacete: "))
hi1 = hypot(co,ca)
print("A hipotenusa com importão: {:.2f}".format(hi))