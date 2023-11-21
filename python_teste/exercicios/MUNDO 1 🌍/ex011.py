#DESAFIOS DA AULA #07 DE PYTHON (OPERADORES ARITIMÉTICOS)

#================Desafio 011========================
'''            (Pintando parede)
Faça um programa que leia a largura e a altura de uma
parede em metros, calcule a sua área e a quantidade
de tinta necessária para pintá-la, sabendo que cada
litro de tinta, pinta uma área de 2m².
'''
#===================================================

'''
- Leia a altura e largura da parede em metros
- calculo da área
- quantidade de tinta 
obs.: 1L de tinta -> área de 2M²
'''
print("Programa para pintar parede")
x = float(input('Qual a altura da parede? '))
y = float(input('E qual é a largura dessa parede? '))
a = x * y
l = a / 2
print('\nO tamanho da área é ({:.2f} M²), Sera preciso \n({:.2f} L) para pintar toda a parede'.format(a,l))