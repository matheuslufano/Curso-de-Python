"""
Curso Python #17 - Listas (Parte 1)
https://youtu.be/N1hTsbW50eM
=============================================================================
Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
As listas são variáveis compostas que permitem armazenar vários valores em
uma mesma estrutura, acessíveis por chaves individuais.
=============================================================================
Tuplas = () # se usa parentes e são imutáveis
Listas = [] # se usa colchetes

Obs.:
.append() # para se adicionar algo ao fim da lista, se utiliza o comando
.insert(0,cachorro quante')  # Para se adicionar ao antes de uma variável, se pode usar reposicionamento da lista
.Del lanche[3] # Para apagar um dado pode se utilizar o comando:
.pop(3) # apaga a última variável
.remove(pitzza) # Remove uma variável
	If  'pitzza' in lanche:
	Lanche.remove('pitzza')

É possivel declarar uma variaveu como lista
Valor = lista(ranfel(4,11))
> valor 4, 5,  6, 7, 8, 9, 10
>..........1, 2 , 3, 4, 5, 6.

Uma lista fora de ordem pode se organizada pela função:
Valores = [8,  9,  6 , 7, 3, 1, 2, 4, 5
valores.sort() # organizar por ordem numérica.
> 1, 2, 3, 4, 5, 6, 7, 8, 9
valores.sorte(reverso=True) # inverte a ordem.
> 9, 8,  7,  6,  5, 4, 3, 2, 1
"""
# =======tupla ()========
num = (2, 3, 9, 1)
print(num)

# # ========lista []=======
# num = [2, 4, 5, 7] #lista.
# num[2] = 3 #altera 2 por 3.
# num.append(7) #adiciona 0 7 a lista.
# num.sort(reverse=True) #inverte a ordem da lista.
# num.insert(2, 2) #na segunda variable da lista (3º) e adicionado 0.
# num.pop() #remove o ultimo valor
# num.pop(2) #remover a segunda variaveu
# num.remove(2) #remove o 2 (nesse caso, o 1º dois)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos.')

# =========NOVA LISTA=============
valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
# for v in valores:
#     print(f'{v}...', end='')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Chequei ao fim da lista.')

#===========ligação entre lista=========
a = [2, 3, 4, 5]
b = a #b recebe + ligação "a"
b [2] = 8 #ao alterar uma, altera as duas
print(f'lista A: {a}')
print(f'lista A: {b}')

# uma cópia pode ser feita usando o fatiamento de str
a = [ 1, 7, 4, 3]
b = a [:]   # b = a [:] copia toda a lista
b [2] = 3
print(f'lista A: {a}')
print(f'lista A: {b}')