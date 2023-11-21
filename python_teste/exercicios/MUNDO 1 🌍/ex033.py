""""
#============================DESAFIO-33====================================

Faça um programa que leia três números e mostre qual é o maior e qual
é, qual é o menor.
=========================================================================="""

num1 = input("Digite um número: ")
num2 = input("Digite um número: ")
num3 = input("Digite um número: ")

# Maior númeor
if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
else:
    maior = num3
# Menor númeor
if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
else:
    menor = num3


print('     {} é Maior número!'.format(maior))
print('     {} é Menor número!'.format(menor))