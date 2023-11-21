"""
            Curso de Python 3 - Mundo 2: Estruturas de Controle
 ========================================================================
Nessa aula, vamos aprender como utilizar a instrução break e os loopings
infinitos a favor das nossas estratégias de código. É muito importante
saber usar o break no Python, já que em alguns casos precisamos interromper
um laço no meio do caminho.

A estrutura break serve para sair do laço de repetição while caso a condição
esteja True, caso seja false, a repetição continuará.

estrutura break (interromper)
"""
# Ex.: 1º)
# contador = 1
# while True:             #(while True) é um estrutura que repete pra sempre
#     print(contador, '-> ', end='')
#     contador += 1
# print('Acabou')

# Ex.: 2º)
# n = 0
# while n != 999: #enquanto a variaveu 'n' for diferente de '999'
#     n = int(input('Digite um número: ')) #variaveu 'n'.

# Ex.: 2ºa)
# n = cont = 0 # 'n' recebe 'cont' que recebe '0'
# while cont < 5: # enquanto 'cont' não for maior que 5, repetir o bloco.
#     n = int(input('Digite um número: '))
#     cont += 1 # a variaveu cont é um contador que soma 1 a cada repetição.

# Ex.: 3º) [repete o bloco e soma]

#   SEM O BREANK (INTERRUPTOR)
# n = s = 0 # 'n' recebe 's' que recebe '0'.
# while n != 999:
#     n = int(input(('Digite um número: ')))
#     s += n
# print('A soma vale: ',s)

  # COM O BREANK (INTERRUPTOR)
n = s = 0
while True:
    n = int(input(('Digite um número (só não 999): ')))
    if n == 999:
        break
    s += n
print('A soma vale: {} '.format(s)) # NOVA FUNÇÃO QUE PODE SUBSTITUIR '.format()'.python 3
print(f'A soma vale: {s} ')  #basta usar o 'f' minusculo antes da str, e a variaveu nas chaves .python 3.6
print('A soma vale: %s ' %(s)) #OBS.: função antiga do print: % .python2

# # Ex.: 4º bonus) [EXEMPLOS DO 'f str']
# nome = 'José'
# idade = 28
# salário = 1350.50
# print(f'TITULO:  {nome:^20}\n' #obs ^20 (centraliza) < ou > (centraliza pra uma direção.
#       f'{nome:=>10}' )
# print(f'O {nome:=^6} tem {idade} anos e ganha R$ {salário:.2f}')

