"""
    Curso Python #22 - Módulos e Pacotes
---------------------------------------------
--> Modularização: Ato de construir modulos.
Esse conceito surgiu na década de 60, com os
sistemas ficando cada vez maiores.
* Foco da modularização:
    - Dividir um programa grande
    - Aumentar a legibilidade
    - Facilitar a manutenção

A modularização vai funcionar da seguinte maneira,
em um projeto você pode criar um arquivo separado
com varis funções especificas e dai importar o arquivo
inteiro como se fosse uma biblioteca, ou funções especificas
dentro de arquivo.

No exemplo a seguir temos vários 'def', isso pode atrapalhar
a visualização do código por inteiro, por tanto se criou um
arquivo chamado 'uteis.py' e dentro do arquivo atual podemos
importar funções de 'uteis.py'.

---------------------------------------------------------------------------------------------
def fatorial(n):   # função de fatorar
    f = 1
    for c in range(1, n+1):
        print(f'{f} x {c} = {f*c}')
        f *= c
    return f

def dobro(n):
    return n * 2

def triplo(n):
    return n * 3

# Programa principal
num = int(input('Digite m valor: '))
fat = fatorial(num) # Caso uma função não exista, o pychame possui uma função de p/ automaticamente.
print(f'O fatorial de {num} é {fat}.\n'
      f'O dobro de {num} é {dobro(num)}\n'
      f'O triplo {num} é {dobro(num)}')
-------------------------------------------------------------------------------------------------------------
"""

# Com as funções criadas no arquivo uteis, já podemos importar unções.
# 1.º caso, importando toda a função, o que pode consumir muita memória!
import uteis

num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {uteis.dobro(num)}')

# 2.º caso, importando partes de uma função, é mais indicado e economiza memoria.
from uteis import fatorial, dobro

num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {dobro(num)}')

"""
VANTAGENS DAS MODULARIZAÇÕES

- Organização do código: Ao modularizar estamos dividindo problemas
maiores em problemas menores.

- Facilidade na manutenção: Caso dei um problema basta ir até a função 
e arruma, sem ter que mexer em varias outras parte do código.

- Ocultação do código detalhando: A maioria das funções no código não
precisamos saber exatamente como é feita tofo o se processo, por isso 
podemos ocultar boa parte.

- Reutilização em outros projetos: 😍 isso é maravilhoso, é possível reciclar as função
em outros projetos.
-----------------------------------------------------------------------------------------
--> PACOTES:
Pacotes no python é o ator de armazenar varias funções separadas por pastas
e utilidade em uma só pasta pasta.
que será chamado de pacotes:
  - Pacotes uteis/
        Dentro dele haverá varias unções que pode ser 
        separadas por categorias como em uma biblioteca
        como:
        - números
            def...()
            def...()
        - strings
            def...()
            def...()
            ...
        - datas
            def...()
            def...()
            ...
        - cores
            def...()
            def...()
Para se utilizar uma das funções, basta importar todas funções ou parte das unções        
ex.:
    import uteis
    #importe uteis
            ou
    from uteis import datas
    #dentro de uteis import datas

Em cada arquivo no pacote deverá conter um arquivo:
 #que conterá um arquivo chamado (__init__.py)
    python package:
        "__init__.py"
           
"""
from uteis import números

num = int(input('Digite um valor: '))
fat = números.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {dobro(num)}')