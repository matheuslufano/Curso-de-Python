#DESAFIOS DA AULA #08 DE PYTHON (Utilizando Módulos)

#================Desafio 019========================
"""      (Sorteando um item na lista)
Um professor quer sortear um dos seus quatro alunos
para apagar o quadro. Faça um programa que ajude ele,
lendo o nome deles e escrevendo o do escolhido.

veja a aula de novo pra tentar responder.
"""
#===================================================
# random é uma biblioteca
import random
print("="*5,"Programa de QUEM VAI APAGAR O QUADRO","="*5)
#aluno == a
a1 = str(input("Digite o nome de um aluno(a/u): "))
a2 = str(input("Digite o nome de um aluno(a/u): "))
a3 = str(input("Digite o nome de um aluno(a/u): "))
a4 = str(input("Digite o nome de um aluno(a/u): "))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print(escolhido)