"""
================================================================
DESAFIO - 097
Faça um program que tenha uma função chamada 'ecreva()' que receba um
texto qualquer como parâmetro e mostre uma mensagem com tamanho adap-
tável.
Ex:
escreva("Olá, mundo!")
saida:
---------------
  Olá, mundo!
---------------
====================================================================
"""
for c in range(0,3):
    def escreva(txt):
        tam = (len(txt)+4)*'-'
        print(f'{tam}\n'
              f'  {txt}\n'
              f'{tam}')


    escreva(str(input('Digite um texto: ')))
    # texto = 'Olá, mundo'
    # escreva('Matheus')