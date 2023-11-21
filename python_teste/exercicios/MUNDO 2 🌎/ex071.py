"""
====================================================================
DESAFIO - 071
Crie um programa simulador de caixa eletrônico.
Iniciando qual será o valor sacado (int) e o programa vai informar
quantas cédulas de cada valor serão entregues.
obs: considerando que o caixa tem cédulas de
R$ 50, 20, 10 e 1.
====================================================================
"""
print('='*30)
print('{:^30}'.format('BANCO MAT'))
print('='*30)
ced50 = ced20 = ced10 = ced1 = 0
saque = int(input('Quanto quer sacar? R$ '))
while saque > 50:
    ced50 = saque //50
    saque = saque % 50
    break
while saque < 50:
    ced20 = saque //20
    saque = saque % 20
    break
while saque < 20:
    ced10 = saque //10
    saque = saque % 10
    break
while saque < 10:
    ced1 = saque //1
    break
print('As cédulas que serão sacadas, são:\n'
      f'💵 {ced50} cédulas de R$ 50,00\n'
      f'💵 {ced20} cédulas de R$ 20,00\n'
      f'💵 {ced10} cédulas de R$ 10,00\n'
      f'💵 {ced1} cédulas de R$ 1,00 ')

print('='*30)
print('{:^30}'.format('BANCO CURSO EM VÍDEO'))
print('='*30)
valor = int(input("Qual valor você quer sacar? R$ "))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'- Total de {totcéd} cédulas de R$ {céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO MAT')