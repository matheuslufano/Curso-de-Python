#DESAFIOS DA AULA #07 DE PYTHON (OPERADORES ARITIMÉTICOS)

#================Desafio 013========================
'''            (Reajuste Salarial)
Faça um algoritmo que leia o salário de um
funcionário e mostre seu novo salário,
com 15% de aumento.
'''
#===================================================
#s = salario
s = float(input('Digite o valor do seu salario: R$ '))
aumento = s + (s*15/100)
print('O seu salario irar ser de R$ {:.2f}'.format(aumento))
print('A diferença é de R$ {:.2f}'.format(s*15/100))