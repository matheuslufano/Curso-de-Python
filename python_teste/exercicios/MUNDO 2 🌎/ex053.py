"""
====================================================================
DESAFIO - 053
Crie um programa que leia uma frase qualquer e diga se ela é um
palíndromo, desconsiderando os espaços.

(A frase escrita de trás para a frente continua tendo o mesmo sentindo
EX:
APOS A SOPA;
A SACADA DA CASA;
A TORRE DA DERROTA;
O LOBO AMA O BOLO;
ANOTARAM A DATA DA MARATONA.)
====================================================================
"""

frase = str(input("Digite uma frase: ")).strip().upper() #1º tirar os espaços, 2º variaveu será mostrada em maiúsculo
palavras = frase.split()    #separou as palavas
junto = "".join(palavras)   #juntou as palavras
inverso = ""
for letra in range(len(junto) - 1, - 1, -1):
    inverso = inverso + junto[letra]
print('O inverso da frase "{}" é " {}"'. format(frase, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

#               OU REDUZA: "inverso = junto[::-1]"
# frase = str(input("Digite uma frase: ")).strip().upper() #1º tirar os espaços, 2º variaveu será mostrada em maiúsculo
# palavras = frase.split()    #separou as palavas
# junto = "".join(palavras)   #juntou as palavras
# inverso = junto[::-1]
# print('O inverso da frase "{}" é " {}"'. format(frase, inverso))
# if inverso == junto:
#     print('Temos um palíndromo!')
# else:
#     print('A frase digitada não é um palíndromo!')