"""
Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar
funções em Python. Funções são trechos de código que podem ser
executados em momentos diferentes de nossos códigos em Python.
Veja como funciona o comando "def" em Python e como utilizá-lo
com parâmetros simples e múltiplos.
"""

"""
funções vinculada a rotina.
Rotina são atividade que fazemos constantemente como:
    print()
    len()
    input()
    int()
    float()
O def serve pra criar funções personalizadas, sendo:
ex: 
    def mostraLinha():
        print('---------------------------------')

mostraLinha():
print('     SISTEMA DE ALUNOS       ')
mostraLinha():
print('     cadastro de funcionários    ')
mostraLinha():
print('         ERRO DE SISTEMA     ')
mostraLinha():
"""
#======================================================
def linha():
    print('-'*30)
linha()
print('Olá mundo!')
linha()
#======================================================
# A função def é muito mais potente, sendo possível por adicionar paramentros:
def linha2(txt): #é dentro do parendesse que se recebe o paramentro
    print('-'*30)
    print(txt)
    print('-'*30)

# a variavel def linha2 mistra o texto dos parametros.
linha2('    Curso em Vídeo      ')
linha2('    APRENDA PYTHON      ')
linha2('    Matheus Lufano      ')
#======================================================
#Fução para somar
def soma(a, b):
    s = a + b
    print(f'{a} + {b} = {s}')
#Programa Principal
soma(4, 5)
soma(8, 9)
soma(29, 2)
# Outra maneira de fazer é, onde os parametros são mais especificas:
soma(b=13, a=17)
print()
#======================================================
# Empacotamento, a função def pode empacotar valores
# em cituações que não sabemos a quantidade exata de parametros,
# basta usar "*" e uma variable. ex:
def contador(*núm): #núm (parametros)
    print(núm)
    for valor in núm:
        print(f'{valor}  ', end='')
    print('FIM')
    tam = len(núm)
    print(f'Recebi os valores {núm} e sãoao todo {tam} números')

contador(1,3,5,7,8,10)
contador(9, 3, 5, 4)
#==========================================================
print()
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
valores = [6,0,3,4,9,5]
print(valores)
dobra(valores)
print(valores)