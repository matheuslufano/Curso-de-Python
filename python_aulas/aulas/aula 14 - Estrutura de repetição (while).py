"""
ESTRUTURA DE REPETIÇÃO
Muitos problemas exigem repetições para chegarmos a uma solução:
* Escrever "GOL DA ALEMANHA" contra o Brasil, 7 vezes (vídeo for)
* Percorrer listas de alunos para calcular a menção a partir de cada nota
* Imprimir itens do menu, até aparecer "camarão" (pense na fome)

temos basicamente dois tipos de repetições:
- repetições pré-definidas
- repetições sem pré-definição

"""



#ESTRUTURA DE REPETIÇÃO COM "FOR"
"""
for c in range(1, 10):
    print(c)
print('fim')"""

#ESTRUTURA DE REPETIÇÃO COM "WHILE"
"""
c = 1
while c < 10:
    print(c)
    c = c + 1
print("Fim")
"""
#ESTRUTURA DE REPETIÇÃO COM "FOR"
"""for c in range(1, 5):
    n = int(input("Digite um valor: "))
print("Fim")
"""
#Condição de parada COM WHILE
"""n = 1
while n != 0: # continua a te digitar '0'
    n=int(input("Digite um valor: "))
print("Fim")"""

# # OUTRO EXPLO (continuar até digitar 'N')
# r = "S"
# while r == "S":
#     n = int(input("Digite um valor: "))
#     r = str(input('Quer continuar? [S/N]')).upper() #
# print("FIM")


# 1° ex. usando o for e o while para mostra 1 a 10 e fim.
"""for c in range(1,10):
    print(c)
print('FIM')

c = 1
while c < 10:
    print(c)
    c = c + 1 
print("Fim")
"""
# O 'for' pode rodar finitas vezes, conforme a sua condição.
"""
for c in range(1,5):
    n = int(input("Digite um valar: "))
print("Fim")
"""
# O 'while' pode se repetir infinitas vezes ou só até o bloco for verdadeiro.
"""
n = 1
while n != 0:
    n = int(input("Digite um valor: "))
print('Fim!')
"""
# O while pode se usado como 'sim' ou 'não' para, / continuar, ou para.
"""r = "S"
while r == "S":
    n = int(input("Digite um valor: "))
    r = str(input("Quer continuar? [S/N] ")).upper()
print("Fim")"""


# Aqui o while vai repetir o bloco enquanto a condição diferir de 0 (zero)
# n = 1
# par = impar = 0
# while n != 0:
#     n = int(input('Digite um valor: '))
#     if n % 2 == 0:
#         par += 1
#     else:
#         impar += 1
# print('Você digitou {} números impares e {} números pares'.format(impar, par))















