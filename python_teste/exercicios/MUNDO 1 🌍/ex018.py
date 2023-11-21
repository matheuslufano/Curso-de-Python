#DESAFIOS DA AULA #08 DE PYTHON (Utilizando Módulos)

#================Desafio 018========================
"""           (seno, cosseno e tangente)
Faça um pragrama que leia um ângulo qualquer e mostre
na tela o valor do seno, cosseno e tangente
desseãngulo.
"""
#===================================================
import math
ângulo = float(input("\033[33mDigite um angulo qualquer: "))
# seno, cosseno e tangente
# uso da funções sin, cos e tan da biblioteca math

seno = math.sin(math.radians(ângulo))
print("O ângulo de {}º tem o SENO de {:.2f}".format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print("O ângulo de {}º tem o COSSENO de {:.2f}".format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print("O ângulo de {}º tem a TANGENTE de {:.2f}".format(ângulo, tangente))

#---------------------ou simplificando----------------------------------------------------------------------------------
# É possiveu simpplificar, baixando apenas as funções que vão ser usadas

from math import radians, sin, cos, tan
ângulo = float(input("\033[7;33mDigite um angulo qualquer:\033[m "))

seno1 = sin(radians(ângulo))
print("\033[31mO ângulo de {}º tem o SENO de {:.2f}".format(ângulo, seno1))
cosseno1 = cos(radians(ângulo))
print("O ângulo de {}º tem o COSSENO de {:.2f}".format(ângulo, cosseno1))
tangente1 = tan(radians(ângulo))
print("O ângulo de {}º tem a TANGENTE de {:.2f}".format(ângulo, tangente1))