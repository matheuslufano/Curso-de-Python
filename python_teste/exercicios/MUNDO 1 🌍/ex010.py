#DESAFIOS DA AULA #07 DE PYTHON (OPERADORES ARITIMÉTICOS)

#================Desafio 010========================
'''         (Conversor de moedas)
Crie um  progroma que leia o quanto dinheiro uma
pessoa tem em sua carteria e mostre quantos Dólares
ela pode comprar.

(considerando US$1,00 == RS$3,27)
'''
#===================================================
real = float(input("Quantos de dinheiro você tem na carteira? R$ "))
us = (real/3.27)
print('Essa quantidade R$ {:.0f} em real, pode comprar US$ {:.2f} de dolar'.format(real, us))
