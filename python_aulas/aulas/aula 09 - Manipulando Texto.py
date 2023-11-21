"""
DESAFIOS DA AULA 09

Ex022) Crie um programa que leia o nome completo de uma pessoa e mostre:

	- O nome com todas letras maiúsculas
	- O nome com todas minúsculas.
	- Quantas letras ao todo (sem considerar espaços).
	- Quantas letras tem o primeiro nome.

Ex023) Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex: Digite um número: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1

Ex024) Crie um programa que leia o nome de uma cidade e digite se ela começa ou não com o nome "Santo".

Ex025) Crie uma programa que leia o nome de uma pessoa e digite se ela tem 'silva' no nome.

Ex026) Faça uma programa que leia uma frase pelo teclado e mostre:
	- Quantas vezes aparece a letra 'a'
	- Em que posição ela aparece a primeira vez.
	- Em que posição ela aparece a última vez.

Ex027) Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza
"""
# Curso Python #09 - Manipulando Texto
#======================================================================================
"""
 Manipulando Texto
aula 09 - curso em vídeo

Nessa aula, vamos aprender operações com Sting no Python.
As principais operações que vamos aprender são o
	• Fatiamento de Sting;
	• Análise com: len(), count(), find();
	• transformações com: replace(), upper(), lower(), capitalize(), title()strip();
  • junção com: join().

    Frase = "Curso em vídeo Python"
                      ↪️há 20 caracteres

 cadeia
Fatiamento de Sting:
Há como fatiar um algoritmo numa variável
 usando os "[ ]" (coxetes) como por exemplo:

>>>Frase [9] #Isso irar imprimir o somente o algoritmo em 9° lugar.
V
>>>Frase [9:13]  #irar ser impresso do 9 ao 12, o 13 irar ficar de fora.
Vide
>>>Frase [9:21:2] #(o uso do terceiro elemento serve para pular pelo valor dele)
Vdopto
>>>Frase [:13] #irar se imprimido até o 12.
Curso em vídeo
 >>>Frase [15:] #irar começar do 15° algoritmo até o fim.
Python
 >>>Frase [9::3]
v**e**p**h**
#está indicando que irar começar no 9 e vai até o final,
2° Dois pontos (::) significa, ignorar a cada 3, mostrando somente o
Primeiro número dos 3.

Cadeia
Análise de Sting:
>>>len('frase') : 'len-->comprimento'
# serve para ver informar quantos algoritmos tem na mensagem

>>>frase.count('o') # irar mostrar somente os algoritmos dentro da condição do 'x'
 3
>>>frase.count(''o', 0,13') # do começo ao fim, irar ser mostrado os algoritmos 'o'
4
Ou
>>>frase.find('deo') # mostra a posição do fatiamento da mensagem
11-13
>>>frase.find('android')
Não foi encontrado ou (-1)
>>>'curso' in frase
Resultado: true ou false

Cadeia
Transformação:
>>> Frase.replace('python','androide') # substituiria python por androide.
Curso em vídeo Python
Curso em vídeo androide
>>> frase.upper() # Deixara tudo maiúsculo.
CUSSO EM VIÍDEO PYTHON
>>> frase.lower() # Deixara tudo em minúsculo.
Curso em vídeo python
>>> frase.capitaliza() # deixara todas as 1° letras em caixa alta.
Curso Em Vídeo Python
>>> frase.strip() # removerá os espaços inícios no fim da frase.
___Curso em vídeo Python___
Curso em vídeo Python
>>> frase.rstrip() # removerá os espaços começo/esquerdo da frase
___Curso em vídeo Python___
Curso em vídeo Python___
>>> frase.lstrip() # removerá os espaços fim/direito da frase.
___Curso em vídeo Python___
___Curso em vídeo Python


Cadeia
Divisão: dividir mensagens
>>>frase.split() # onde houver espaço, serrar dividido em uma lista.
Curso em vídeo Python
[Curso,   em,   vídeo,   Python]


Cadeia
Junção:
>>> '-'.join(frase) # gera uma Stig com '-' no lugar do espaço
Curso-em- vídeo-Python
"""
