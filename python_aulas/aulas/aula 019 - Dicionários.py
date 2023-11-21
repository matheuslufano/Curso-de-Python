# Variáveis Compostas (Dicionários)
# ===================================
"""Nessa aula, vamos aprender o que
são DICIONÁRIOS e como utilizar
dicionários em Python. Os dicionários
são variáveis compostas que permitem
armazenar vários valores em uma mesma
estrutura, acessíveis por
chaves literais."""
# ==================================
# Recaptulando da aula anterior
# Trabalhamos com listas.
dados = list()  # Se cria uma lista.
dados.append('Pedro')  # Se adiciona um elemento a lista. dados ['Pedro']
dados.append(25)  # Adcionou mais um elemento. dados ['Pedro', '25']
print(dados[0])  # se printa o elemento zero da lisa. 'Pedro'
print(dados[1])  # se printa o segundo elemento. 25

""" Os dicionários são como as tuplas e as listas, porem com a possibilidade de
ser poder personalizar os indices com nomes"""

# Tuplas (): Se usa parentes
# Dicionários {}: Se usa chaves
# Listas []: Se uas couchettes

# PARA SE TRABALHAR COM DICIONÁRIOS:
dados = dict()  # dessa forma declaramos uma dicionários.
dados = {'nome': 'Pedro', 'idade': 25} #desta forma se cria um elemento
print(dados['nome']) #Pedro
print(dados['idade']) #25
dados['sexo'] = 'M' # p/ criar elementos, basta declara um elemento e atribuir um objeto
del dados['idade'] #se elimina o elemento 'idade

#Dicionario mais elabora:
filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
}

"""
'titulo': 'Star Wars',
'ano': 1977,
'diretor': 'George Lucas'
"""
# valores: são os objetos atribuídos aos indices
# ['Star Wars', '1977' e 'George Lucas']

# Chaves/keys(): são os indices
# [titulo', 'ano' e 'diretor']
# items():
# São ambos os valores

print(filme.values()) # values()/alores(), retorna todos os valores: ['Star Wars', '1977' e 'George Lucas']
print(filme.keys()) # Chaves/keys(): Retorna as chaves que contem os valores: [titulo', 'ano' e 'diretor']
print(filme.items()) # items(): Retorna as chaves e os valores nelas.['titulo': 'Star Wars','ano': 1977, 'diretor': 'George Lucas']
#itens, chaves, elemento ou simplificando valores (values)#

"""Essas três funções podem ser usadas nos laços de repetições.
Com na função 'for':
"""
# ex:
# k (chave)
# c (valor)
for c, v in filme.items():
    print(f'O {c} é {v}.')
#       O titulo é Star Wars.
#       O ano é 1977.
#       O diretor é George Lucas.

# Obs.: Se pode juntar listas, Tuplas e Dicionários em uma estrutura só.
# lista = [ dicionário = { tuplas = ()}]
# ==============================================
#          exemplo: de uma estrutura (locadora[3 elementos])
# lista = locadora (composto de 3 elementos 0,1,2)
# dicionario = [titulo', 'ano' e 'diretor']
# tuplas =
# locadora = [
#             ['titulo': 'Star Wars','ano': 1977, 'diretor': 'George Lucas'], #elemento "0"
#             ['titulo': 'Avengens', 'ano': 2012, 'diretor': 'Joss Whedon'],  #elemento "1"
#             ['titulo': 'Matrix', 'ano': 1999, 'diretor': 'Irmãs machowski'],#elemento "2"
#]
# print(locadora[0]['ano'])   1977
# print(locadora[2]['titulo'])  Matrix

#=======================Aula pratica====================================
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())
#  =============2º ex==================================
print()
for a in pessoas.values(): #values(), keys(), items()
    print(f'valor = {a}')
# ou
for a, b in pessoas.items():
    print(f'Chave {a} = valor {b}')

#  obs.: dicionario não possui a função enumerate, porem há ".items()" que faz a mesma coisa

# Há a possibilidade de apagar elementos:
del pessoas['sexo'] # irar apagar o elemento "sexo" da lista.

# alterar um elemento:
pessoas['nome'] = 'matheus' #altera o elemento "nome"
pessoas['peso'] = 63 #adiciona o elemento "peso"

print('\n 2º Exemplo:')
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('\n 3º Exemplo:')
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['uf'])

print('\n 4º Exemplo:')

estado = dict() #variavel declarada como dicionario
brasil = list() #variavel declarada como lista
for c in range(0 ,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #copy(função de copiar)
for e in brasil:
    for v in e.values():
        print(v, end = ' ')
    print(e)