"""'
====================================================================
DESAFIO - 076
Crie um programa que tenha uma tupla única com nomes de produtos e
seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizado os dados em forma
tabular.
====================================================================
"""''
print('{}\n{: ^35}\n{}'.format('-'*35,'LISTAGEM DE PREÇOS','-'*35))

lista = ('cerial', 10,'pâo', 7, 'presunto', 8,'frango', 15, 'carne moída', 30)
# print('{:.<30}R$ {}'.format(lista[0], lista[1]))
# print('{:.<30}R$ {}'.format(lista[2], lista[3]))

cont = 0
preç = 1
for l in lista:
    print('{:.<30}R$ {}'.format(lista[cont], lista[preç]))
    cont += 2
    preç += 2

print('{:-^40}'.format('FIM DO PROGRAMA'))