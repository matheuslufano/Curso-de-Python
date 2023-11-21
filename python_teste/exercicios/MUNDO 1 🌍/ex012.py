#DESAFIOS DA AULA #07 DE PYTHON (OPERADORES ARITIMÉTICOS)

#================Desafio 012========================
"""            (Calculador de descontos)
Faça um algoritmo que leia o preço de um produto e
mostre seu novo preço, com 5% de desconto.
"""
#===================================================
# simbolo de % (percentual) significa resto da divisão.
# para efetuar o desconto desse produto, basta usar regra de 3.
# x - (x*5/100)

preço = float(input('Informe o preço de um produto: R$  '))
desconto = preço - (preço*5/100)
print("O desconto é de 5%, o produto que custava R$ {:.2f}\nNessa promoção, ele irar custar R$ {:.2f} ".format(preço, desconto))