"""
====================================================================
DESAFIO - 085
Crie um programa onde o usuário passa digitar sete números e cadastre-os
em uma única lista que os mantenha separados por impares e pares. Ao final
mostre os valores pares e impares em ordem crescente.
====================================================================
"""
lista = [[], []] # Para criar sub lista usa 1 ou + pares de "[]" com vírgulas.
for n in range(1,8):
    valor = int(input(f'Digite o {n}° número: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print('(￣y▽￣)╭ Ohohoho...................')
lista[0].sort()
lista[1].sort()
print(f'Os números pares são: {lista[0]}\n'
      f'E os impares são: {lista[1]}')