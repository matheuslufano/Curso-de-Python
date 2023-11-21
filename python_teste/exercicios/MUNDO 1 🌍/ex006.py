#DESAFIOS DA AULA #07 DE PYTHON (OPERADORES ARITIMÉTICOS)

#================Desafio 006========================
"""Crie um algoritmo que leia um número e mostre
o seu dobro, triplo e a sua raiz quadrada."""
#===================================================

#(não esqueça de usar o input para ler a variavel)
v1 = int(input("Disgite um valor: "))
d = v1 * 2
t = v1 * 3
q = v1 ** (1/2)

'''------------(forma completa)----------------------
print("O dobro do número {} = {}".format(v1,d))
print("O triplo do número {} = {}".format(v1,t))
print("A raiz quadrada de {} = {}".format(v1,q))
---------------------------------------------------'''


#-----------forma seme completa---------------------------------------------------------------------------------
#print('O dobro de {} é igual a {}, o seu triplo é igual a {}\ne a sua raiz quadrada é {}'.format(v1, d, t, q))
#----------------------------------------------------------------------------------------------------------------



#------------------(forma redusida e mais simples)-------------------------------------------
print ('O dorbro de ({}) vale ({});\nO seu tripo é igual a ({});'.format (v1,(v1*2),(v1**3)))
print('E a raiz quadrada de ({}) é igual a ({}).'.format(v1, (v1**(1/2))))
#--------------------------------------------------------------------------------------------