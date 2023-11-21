#DESAFIOS DA AULA #10 - Condições (Parte 1)

#================Desafio 031========================
"""
DESAFIO-31
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando RS 0,50 por Km para
viagens de até 200Km e 0,45 para viagens mais longas.
"""

km = float(input('Qual a distancia em km da sua viagem: '))
if km < 200:
    print('{:.0f} Km vale R$ 0,50 por km.\nSua passagem custarar: R$'.format(km), km * 0.50 )
else:
    print('{:0f} Km vale R$ 0,45 por km.\nSua passagem custarar: R$'.format(km), km * 0.45 )