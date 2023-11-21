#            DESAFIOS DA AULA #10 - Condições (Parte 1)
#=======================DESAFIO-35===================================
"""Desenvolva um programa que leia o comprimento de três retas e diga
ao usuário se elas podem ou não formar um triângulo.

Triângulo Equilátero: É um triângulo que possui todos os três lados
iguais. Além disso, todos os seus ângulos internos também são iguais
e medem 60 graus cada.

Triângulo Isósceles: É um triângulo que possui dois lados iguais.
Os ângulos opostos aos lados iguais também são iguais. O terceiro
lado, chamado de base, geralmente tem um comprimento diferente dos
outros dois lados.

Triângulo Escaleno: É um triângulo que possui todos os três lados
diferentes. Os ângulos internos também têm medidas diferentes. Nesse
tipo de triângulo, não há lados nem ângulos iguais."""
#====================================================================


print('=-='*8)
t1 = float(input('Digite a 1° reta: '))
t2 = float(input('Digite a 2° reta: '))
t3 = float(input('Digite a 3° reta: '))
print('=-='*8)
if t1 == t2 and t1 == t3:
    print("Triângulo Equilátero: \nÉ um triângulo que possui todos os três lados iguais.")
elif t1 == t2 or t1 == t3 or t3 == t2:
    print("Triângulo Isósceles: \nÉ um triângulo que possui dois lados iguais.")
else:
    print("Triângulo Escaleno: \nÉ um triângulo que possui todos os três lados diferentes. ")




