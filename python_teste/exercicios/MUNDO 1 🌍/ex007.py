#DESAFIOS DA AULA #07 DE PYTHON (OPERADORES ARITIMÉTICOS)

#================Desafio 007========================
""" Desenvolva um programa que leia as duas notas
de um aluno, calcule e mostre a sua média. """
#===================================================
#----------> {:.f1}
print("==========================")
print("MEDIA DO ALUNO!!!")
print("==========================")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Diginte a segunda nota: "))
m = (n1 + n2)/2

print("A media da 1º nota ({:.2f}) e 2º nota ({:.2f}) é: {:.2f}".format(n1,n2,m))

"""
usa-se esse comando -> (:.1f) 
para mostrar apenas 1 ou mais números apos a virgula.
ex.: 1,4854 = 1,4
"""