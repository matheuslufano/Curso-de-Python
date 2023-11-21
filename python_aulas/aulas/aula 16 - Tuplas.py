"""
Curso Python #16 - Tuplas

lanche = hambúrguer  #(=) recebe ou atribuição
lanche = suco # o dado suco substitui hambúrguer e não armazena os dois
Curso de Python 3 - Mundo 3: Estruturas Compostas
Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python. As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

Lanche = hambúrguer  #(=) recebe ou atribuição
Lanche = suco #o dado "suco" substitui "hambúrguer" e não armazena os dois



Uma variável pode guardar:
- Um dado (variável simples);
- Ou vários dados ( variável composta).

As variáveis compostas podem ser feitas por:
- Tuplas
- Lista
- Dicionários

TUPLAS:
 Em Python, uma tupla é uma estrutura de dados que permite armazenar um conjunto ordenado de elementos. A principal característica das tuplas é que elas são imutáveis, o que significa que, uma vez criadas, não é possível alterar seus elementos. Isso as diferencia das listas, que são mutáveis.

As tuplas são definidas utilizando parênteses "(" e ")". Os elementos dentro da tupla são separados por vírgulas. Veja um exemplo simples de como criar e trabalhar com tuplas em Python:
...
python
# Criando uma tupla
tupla_exemplo = (1, 2, 3, 4, 5)

# Acessando elementos da tupla
primeiro_elemento = tupla_exemplo[0]  # Resultado: 1
segundo_elemento = tupla_exemplo[1]   # Resultado: 2

# Tentativa de modificar um elemento (resultará em um erro)
# tupla_exemplo[0] = 10 # Isso não é permitido, pois as tuplas são imutáveis

# Comprimento da tupla
tamanho_tupla = len(tupla_exemplo)   # Resultado: 5

# Verificar se um elemento está na tupla
esta_na_tupla = 3 in tupla_exemplo    # Resultado: True

# Concatenando tuplas
outra_tupla = (6, 7, 8)
tupla_concatenada = tupla_exemplo + outra_tupla   # Resultado: (1, 2, 3, 4, 5, 6, 7, 8)

# Desempacotando tupla
a, b, c, d, e = tupla_exemplo
print(a, b, c, d, e)  # Resultado: 1 2 3 4 5
....

As tuplas são muito úteis quando você deseja criar coleções de elementos que não devem
ser modificados após a criação. Elas também podem ser utilizadas para retornar múltiplos
valores de uma função.

Lembre-se de que, como as tuplas são imutáveis, caso precise modificar os elementos,
é necessário criar uma tupla com os valores desejados. Se você precisar de uma
coleção mutável, utilize listas em vez de tuplas.
"""
print('='*20,'1° exemplo','='*20)
#================================1° exemplo===========================================
'Os elementos estão em ordem '
# 1° ->'Hambúrguer',
# 2° -> 'Suco',
# 3° -> 'Pizza',
# 4° -> 'Pudim'

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche) # mostra todas variáveis
print(lanche[1:3])
print(lanche[2])	# Printa segunda variável na tuplas
print(lanche[0:2])	#  Vai mostrar a variável na posição 0 a antepenúltima variável da condição (que é 2 nesse caso )
print(lanche[1:])	# Mostra da posição 1 ao fim na tuplas
print(lanche[-1])	# uma variável numa tuba pode ser mostrada de duas formas, pela posição ou pela ordem negativa com o "- 1" que mostra a primeira variável
len(lanche)	# len (mostra o Comprimento )
print(sorted(lanche)) #printa em ordem alfabetica




#============================2° exemplo===============================================
print('='*20,'2° exemplo','='*20)

# Há varias formas de se usar o for com tuplas. As 3 principais são:

# for para printar todas as variáveis
for c in lanche: 	# O for pode ser usada com Tuplas, mostrando que tem dentro da tuplas na ordem
    print(c)




#=============================3° exemplo==============================================
print('='*20,'3° exemplo','='*20)

# for pra mais completos pra mostras tadas as variáveis
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!\n')





#===========================4° exemplo================================================
print('='*20,'4° exemplo','='*20)

# for pra mais completos pra mostras tadas as variáveis incluindo a última
for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posição {cont}')





#===========================5° exemplo================================================
print('='*20,'5° exemplo','='*20)

a = (2, 5, 4)
b = (5, 8, 1, 3)
c = a + b #printa a e depois b
print(c)
print(c.count(2)) #quantas vezes aparece x variaveu
print(c.index(8)) #em qual posição está o "8"?





#===========================6° exemplo================================================
print('='*20,'6° exemplo','='*20)

pessoa = ("Matheus", 23, 'M', 60) #Tuplas aceita qualquer dados
# del (pessoa) #del apaga variaveu
print(pessoa)

