# Aula - entrada e saida
# int (tipo primitivo que declara a variavel em número inteiro)
# inpúte (leia)
# print (escreva)
#.format() --> nova sintaxe do python para adicionar uma variavel a uma mensagem
#===========================================================#
n1 = int(input('Digite um valor: '))
n2 = int(input("Digite outro valor: "))
s = n1 + n2
# print("A soma netre", n1, "e", n2,"vale", s)
print('A soma entre {} e {} vale: {}'.format(n1, n2, s)) #NOVA sintaxe do python