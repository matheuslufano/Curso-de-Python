"""
====================================================================
DESAFIO - 049
Refaça o desafio 009, mostrando a tabuada de um número que o usuário
escolher, porem utilizando um laço de repetição "for".


    DESAFIOS 009 (Tabuada) DA AULA
    #07 DE PYTHON - OPERADORES ARITIMÉTICOS
----------------------------------------------------
Faça um programa que lei um número inteiro qualquer
e mostre na tela a sua tabuada.
----------------------------------------------------
"""
# MEUS ANTIGO CÓDIGO
print("="* 60)
num = int(input('Digite um número para ver a sua tabuada de mutiplicação: '))
print('='* 60)
#print('='* 14) dar para multiplicar uma mensagem
#{:2} serve para mostrar uma determinada quantidade de números

print("{} X {:2} = {}".format(num, 1, num*1))
print("{} X {:2} = {}".format(num, 2, num*2))
print("{} X {:2} = {}".format(num, 3, num*3))
print("{} X {:2} = {}".format(num, 4, num*4))
print('{} X {:2} = {}'.format(num, 5, num*5))
print("{} X {:2} = {}".format(num, 7, num*7))
print("{} X {:2} = {}".format(num, 8, num*8))
print("{} X {:2} = {}".format(num, 9, num*9))
print("{} X {:2} = {}".format(num, 10, num*10))
print("=" * 60)
#(códico que achei na internet )
#tabuada = int(input("Tabuada do número: "))
#for count in range(10):
#   print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)))

# num = float(input("Digite um número: "))
for c in range (1,11):
    print('{:.0f} x {} = {:.0f}'.format(num, c, c*num))
print("=" * 60)