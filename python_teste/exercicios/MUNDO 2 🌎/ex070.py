"""
====================================================================
DESAFIO - 070
Faça um programa que lei o nome e o preço de vários produtos. O pro-
deverá perguntar se o usuário vai continuar. No final mostre:
A) Qual é o total de gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.
 ====================================================================
"""
total = mais_1000 = menor = cont = 0
barato = ''
while True:
    print('--------CAIXA--------')
    nome_produto = str(input('Nome do produto? '))
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        mais_1000 += 1

    if cont == 1 or preço < menor:
        menor = preço
        barato = nome_produto
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Quer continuar? [S/N] ')).upper().strip()[0] #strip 1º letra
        print()
    if sair == 'N':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi de R$ {total:.2f}\n' #  {total:.2f} 2 casas decimais 
      f'Temos {mais_1000} produtos que custam mais de R$ 1.000,00\n'
      f'O produto mais barato foi {barato} que custa {menor:.2f}') #:.2f} 2 casas decimais