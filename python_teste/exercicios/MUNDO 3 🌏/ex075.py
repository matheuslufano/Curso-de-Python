"""""
====================================================================
DESAFIO - 075
Desenvolva um programa que leia 4 valores pelo teclado e guarde-os 
em uma tupla. No final, mostre:
a) quantas vezes apareceu o valor 9.
b) em que posição foi digitado o primeiro valor 3. 
c) quais foram os números pares.
====================================================================
"""""

# ⬇️ meu código não funcionou.

# print('Digite 4 números: ')
# num1 = int(input('número 01: '))
# num2 = int(input('número 02: '))
# num3 = int(input('número 03: '))
# num4 = int(input('número 04: '))
# tupla = (num1, num2, num3, num4)
# print(f'Você digitou: {tupla}')
# # a) quantas vezes apareceu o valor 9.
# cont = 0
# pos = 0
# par = ''
# for num in tupla:
#     pos += 1
#     if num == 9:
#         cont += 1
#     # b) em que posição foi digitado o primeiro valor 3.
#     if num == 3:
#         posição = pos
#     # c) quais foram os números pares.
#     if num % 2 == 0:
#         par += str(num)
# print(f'a) O valor "9" foi digitado {cont} vezes.')
# print(f'b) O valor (3) foi digitado na {posição}° vezes.')
# print(f'c) Os números pares são: ', par)

# ⬇️ código da resolução.
print('Digite 4 números: ')
núm = (int(input("Número 01: ")),
       int(input("Número 02: ")),
       int(input("Número 03: ")),
       int(input("Número 04: ")))
print(f'\nVocê digitou os valores {núm}.')
print(f'a) O valor 9 apareceu {núm.count(9)} vezes.')
if 3 in núm:
    print(f'b) O valor 3 apareceu na {núm.index(3)+1}ª posição.')
else:
    print('b) O valor 3 não foi digitado em nenhuma posição.')
print('c) Os valores pares são: ', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')