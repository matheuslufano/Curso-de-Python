#DESAFIOS DA AULA #07 DE PYTHON (OPERADORES ARITIMÉTICOS)

#================Desafio 009========================
'''               (Tabuada)
Faça um programa que lei um número inteiro qualquer 
e mostre na tela a sua tabuada.
'''
#===================================================
print("="* 14)
num = int(input('Digite um número para ver a sua tabuada de mutiplicação: '))
print('='* 14)
#print('='* 14) dar para mutiplicar uma mensagem
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
print("=" * 14)
#(códico que achei na internet )
#tabuada = int(input("Tabuada do número: "))
#for count in range(10):
#   print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)))