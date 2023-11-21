#DESAFIOS DA AULA #08 DE PYTHON (Utilizando Módulos)

#================Desafio 020========================
"""      (Sorteando uma ordem na lista)
O mesmo professor do desafio anterior quer sortear
a ordem de apresentação de trabalho dos alunos.
Faça um programa que leia o nome dos quatro alunos
e mostre a ordem sorteada.

veja a aula de novo pra tentar responder.
"""
#===================================================
import random
# importe aleatorio
a1 = str(input("Digite o nome de um aluno(a/u): "))
a2 = str(input("Digite o nome de um aluno(a/u): "))
a3 = str(input("Digite o nome de um aluno(a/u): "))
a4 = str(input("Digite o nome de um aluno(a/u): "))

lista = [a1, a2, a3, a4]
random.shuffle(lista)
print("1º opção de lista: ", lista)

# importando apena a função shuffe da biblioteca random
from random import shuffle
lista2 = [a1, a2, a3, a4]
shuffle(lista2)
print("2º opção de lista: ", lista2)