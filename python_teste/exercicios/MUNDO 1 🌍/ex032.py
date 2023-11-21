#DESAFIOS DA AULA #10 - Condições (Parte 1)

#================Desafio 032========================
"""    DESAFIO-32
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO."""

"""
Para calcular os anos bissextos, utilizam-se estas regras: 
- A cada quatro anos, há um ano bissexto; 
- São bissextos todos os anos múltiplos de 400, exceto se for múltiplo de 100, 
mas não de 400, por exemplo: 1996, 2000, 2004, 2008, 2012, 2016, 2020; 
- Não são bissextos os anos múltiplos de 100."""

ano = int(input('Ano: '))

if ano % 400 == 0:
    print('Anos', ano, 'É um ano bissexto! ')

elif not ano % 100 == 0:
    print('Anos',ano, 'Não é bissexto! (multiple de 100)')

else:
    print('Anos',ano, 'Não é bissexto!')