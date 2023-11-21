"""Curso Python#21-Funções(Parte2)
Nessaaula,vamoscontinuarnossosestudosdefunçõesemPython,aprendendomaissobre
Tópicos:
- Interactive Help em Python;
- Docstrings (para documentar nossas funções);
- Argumentos opcionais (para dar mais dinamismo em funções Python);
- Escopo de variáveis (entenda quando nasce, morre e está visível uma variável);
- Retorno de resultados.
=========================
    1° Tópico:
    INTERACTIVE HELP
    (Ajuda interativa)
==========================
Help():
Para usar essa função, basta digitar ela no campus python console
-------------------------------------------------------------------------------------------------
 help():
help> print
Help on built-in function print in module builtins:
print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.
-------------------------------------------------------------------------------------------------
Outra maneira é usar a essa função dentro do seu terminar de código, basta chamar a função e por entre parentes a outra função que quer saber mais.
Help(print)

Ao dar run do programa será exibido seu resultado e a definição da função entre parentes.
-------------------------------------------------------------------------------------------------
Ou usar a função:
Print(input.__doc__)
Read a string from standard input.  The trailing newline is stripped.

The prompt string, if given, is printed to standard output without a
trailing newline before reading input.

If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
On *nix systems, readline is used if available.

-------------------------------------------------------------------------------------------------
"""
print('Olá, mundo')
# INTERACTIVE HELP
print(input.__doc__)

"""
-------------------------------------------------------------------------------------------------
=============================
        2° Tópico:
        DOCSTRINGS
(Comentário de instruções)
=============================

É quando são mensagens usando as ("'" texto "'") assim é possível usar a
função help em funções que o dev crio, como por exemplo a função contador(),
ao criar sua função basta fazem um comentario com as extruções de uso, usando
aspas tripas ("""""").
def contador(i, f, p):
    "'"
    --> Faz uma contagem e mostra na tela.
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: sem retorno
    "'"
    c = 1
    while c <= f:
        print(f'(c)', end='..')
        c += p
    print('FIM')
help(contador)


contador(2, 10, 2)
#os parâmetros 2, 10, 2 são transferidos pra i, f, p.
>>>mostra:
contador, começa no 2, termina no 10, pulando 2 em 2
-----------------------------------------------------------------------------
"""
def contador(i, f, p):
    # DOCSTRINGS ⤵
    """
    --> Faz uma contagem e mostra na tela.
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: sem retorno
    Função criada por gustavo de curso em vídeo
    """
    c = 1
    while c <= f:
        print(f'(c)', end='..')
        c += p
    print('FIM')
help(contador)

"""
-----------------------------------------------------------------------------
===========================
        3° Tópico:
    PARÂMETROS OPCIONAIS
===========================
Obs: O exemplo é de parâmetros obrigatório;
logo a segui tem um exemplo de parâmetros obrigatório;
caso queira multiples parâmetros usar (*).

Oa criar uma função nova com o 'def', é possivel definir parâmetros opcionais.
ex:
    def somar(a, b, c):
        s = a + b + c
        print(f'A soma vale (s)')

    somar(1,4,5)
---------------------------------------
Ao fazer isso, os parâmetros da
nova função tem que nercessariamente
serem 3 valores, caso informe apena
2 valores a função "soma(a,b)"
pode dar erro.
---------------------------------------
#porem ao atribuir outros valores
aos parâmetros a,b,c como o valor
0 (sero) a sua função não dará erro

def somar(a=0, b=0, c=0):
        s = a + b + c
        print(f'A soma vale (s)')

somar(1,4,5)
-----------------------------------------------------------------------------
"""
# dessa maneira se pode definir parâmetros, nesse caso foram 3,
# para se usar mais de um paramentros se deve usar o '*' para amazenar
# varios parâmetros
def somar(a=0, b=0, c=0): # PARÂMETROS OPCIONAIS (a=0, b=0, c=0)
    s = a + b + c
    print(f'A soma vale ({s})')

somar(9,3)
somar(b=4, c=4)

"""
-------------------------------------------------------------------------------------
================================
    4° Tópico:
    ESCOPO DE VARIÁVEIS
    (Escopo de declarações)
================================
É o local onde a variável vai existi e onde ela não vai mais existir dentro das endentação
-------------------------------------------------------------------------------------
"""
# exemplos:
# 1º Exemplo: escoplo locale
print('-'*40)
print('1º Exemplo: escoplo locale')
def texte():
    x = 8 # escopo local (funciona apenas dentro de def)
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

#programa principal
n = 2 # escopo global (funciona em toda a pra baixo e dentro de def)
print(f'No programa principal, n vale {n}')
texte()
# print(f'No programa principal, x vale {x}')
#  vai dar erro, pq x = 8 é uma variável local.
#=====================================================================

# 2° exemplo: Valores dentro e fora da endentação
print('-'*40)
print('2° exemplo: Valores dentro e fora da endentação')
def texte1(b): # escopo local
    a = 8
    b += 4 # escopo local
    c = 2 # escopo local
    print(f'    A dentro vale ({a})')
    print(f'    B dentro vale ({b})')
    print(f'    C dentro vale ({c})')

#programa principal
a = 5 # escopo global
texte1(a)
print(f'A dentro vale ({a})')
# print(f'B dentro vale ({b})') # vai dar erro pq não existe as variáveis (b, c) no escopo global
# print(f'C dentro vale ({c})')


# =====================================================================
# 3° Exemplo: função "global" para manter o valor do escopo global
print('-'*30)
print('3° Exemplo: função "global"')
def texte2(b): # escopo local
    global a
    a = 8 # escopo global
    b += 4 # escopo local
    c = 2 # escopo local
    print(f'    A dentro vale ({a})')
    print(f'    B dentro vale ({b})')
    print(f'    C dentro vale ({c})')

#programa principal
a = 5
texte2(a)
print(f'A dentro vale ({a})')
print('-'*30)
"""
------------------------------------------------------------------------------
================================
        5° Tópico:
    Retornando valores
        (return)
================================
As funções em python pode retornar um valor e pode não retornar.
A função 'return' serve para retornar um valor feito na função def
para uma variável fora da função.
"""
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(2)
print(f'As somas derão {r1}, {r2} e {r3}')




# ==================================================================================
# PRATICANDO O QUE FOI PASSADO EM AULA
#
#
#      FUNÇÃO 'DEF' ALIADA A 'RETURN'
#  ---------------------------------------------------------
def fatorial(num=1):
    f = 1 #variável local
    for c in range(num, 0, -1): #começa em num, vai até o 0 (zero), intervalo diminuindo um número (-1)
        f *= c # a variável f mais c (for)
    return f # retorna o valor a variável

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(6)
f3 = fatorial()
print('O fatorial de:\n'
      ' fatorial(5)\n'
      ' fatorial(6)\n'
      ' fatorial()\n'
      f'São: {f1}, {f2}, {f3}')

    # A FUNÇÃO RETURN VOLTA OUTRO VALORES ALÉM DE NÚMERO
    # VERDADEIRO OU FALSO
    # ---------------------------------------------------------------

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')

