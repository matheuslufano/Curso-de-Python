#DESAFIOS DA AULA #10 - Condições (Parte 1)

#================Desafio 029========================
"""
    DESAFIO-029
Escrava um programa que leia a velocidade de um carro.

Sa ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
Foi multado.

A multa vai custar RS 7,OO por cada km acima do limita.
"""

velocidade = float(input('Qual a velocidade do carro: '))
if velocidade < 80:
    print('velocidade {} km/h é dentro do limite'.format(velocidade))
else:
    multa = (velocidade - 80) * 7
    print('Você foi multado em R$ {} por correr {:.2f} km/h \n'
          'em uma estrada que só é permitido 80 km/h'.format(multa,velocidade))