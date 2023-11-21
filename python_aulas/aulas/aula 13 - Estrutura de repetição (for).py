"""
Curso Python #013 - Estrutura de repetição for
De <https://www.youtube.com/watch?v=cL4YDtFnCt4&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=60>
        AULA LAÇOS DE REPETIÇÃO (parte 1)
Estrutura de Controle (ou laço, repetições ou iteraçãos)
Nessa aula, vamos começar nossos estudos com os laços e vamos fazer
primeiro o "for", sendo uma estrutura versátil e simples de entender.
Por exemplo:

Laço c no intervalo(0,10)
	passo
Pegar
------------------------------
For c in range(0,10):
	Passo
Pegar


'' for c in range(0, 4):
	 print(c)
Print ('Acabou') ''
"""

# for c in range(0,6):
#     print('oi ') # condiçao = (c), mostra de todos os numero na range.
# print('fim')

# n = int(input('Inicio: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))
# for c in range(n, f+1, p): # 0 a 9-> (0,10) ou 9 a 0-> (10, 0, -1) ou 0, 9, pulando de 2->(0, 10, 2
#     print(c)
# print('fim')

# s = 0
# for c in range(0, 4):
#     n = int(input('Digite um valor: '))
#     s = s + n # ou s += n
# print("A somo de todos os número é = ", s)

# n = int(input('Digite um número: '))
# for c in range(0,4):
#     print(c)

# for c in range (1, 6):
#     print('oi')
# print('fim')


#  condição pode iniciar, pode ter um fim e pular de casa
i = int(input('Em qual número vai iniciar: '))
f = int(input('Em qual número vai ser o fim: '))
p = int(input('Em quantos números vai pular: '))
for c in range (i, f+1,p):
    print(c)
print('fim')

#=====vai repetir a variaveu 'n' de com a condição for====
for c in range (0,3):
    n = int(input("Digite um valor: "))
print('Fim!')


#=====dessa vez alem de repetir, a variaveu será somada e guardada==
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n
print("A soma de todos os números foi ", s)


