'''
Curso Python #17 - Listas (Parte 2)
Nessa aula, vamos aprender o que são LISTAS e como utilizar
listas em Python. As listas são variáveis compostas que
permitem armazenar vários valores em uma mesma estrutura,
acessíveis por chaves individuais.
'''

# Função lista composta:
# ela é como um dicionário, sendo possível armazenar dados
# dentro de estruturas, dentro de outras estruturas.
# =====================
# 1º) Exemplo:

# lista = list()
# lista.append('Gustavo')
# lista.append(40)
# galera = list()
# galera.append(lista[:])
# lista[0] = 'maria'
# lista[1] = 22
# galera.append(lista[:])
# print(galera)

# 2º) exemplo:

# # lista Composta:
# #        [   0 [0,1],     1 [0, 1],     2 [0, 1],       3[0, 1]   ]
# galera = [['Jão', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# # print(galera[2][1])
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade.')

# 3° Exemplo:
galera = list()
dado = list()
totmai = 0
totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])# copiar: [:]
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')