#            DESAFIOS DA AULA #10 - Condições (Parte 1)
#==============================DESAFIO-34================================

"""Escreva um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para os inferiores ou igual, o aumento é de 15%."""
#=========================================================================

salario = float(input('Qual é o seu salario? '))
if salario > 1250:
    aumento = salario * 0.10
    print("-=-" * 10)
    print("Seu salario era: R$ {:.2f}\n"
          "Com o aumento de 10%: R$ {:.2f}\n"
          "Seu salario será: R$ {:.2f}".format(salario,aumento, salario + aumento))
    print("-=-" * 10)

else:
    aumento = salario * 0.15
    print("-=-" * 10)
    print("Seu salario era: R$ {:.2f}\n"
          "Com o aumento de 15%: R$ {:.2f}\n"
          "Seu salario será: R$ {:.2f}".format(salario,aumento, salario + aumento))
    print("-=-" * 10)