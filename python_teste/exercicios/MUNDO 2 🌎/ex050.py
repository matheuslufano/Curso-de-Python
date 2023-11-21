"""====================================================================
DESAFIO - 050
Desenvolva um programa que leia seis números inteiros e mostre a soma
apenas daqueles que forem pares. Se o valor digitador for impar,
desconsidere-o.
===================================================================="""

s = 0
for c in range(0,6):
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        s = num + s
print(s)
