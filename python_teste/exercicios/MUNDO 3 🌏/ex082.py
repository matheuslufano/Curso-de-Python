"""
Desafio 82
Crie um que leia various números e colocar em uma lista.

Depois disso crie duas listas extras que vão conter apenas
os valores pares e os valores impares digitados, respectivamente.
Ao fim mostre o conteúdo das 3 listas.
"""
list_c = []
par = []
impar = []
resp = 0
while True:
    list_c.append(int(input("Digite um número: ")))
    sair = str(input('Quer continuar? [S/N]')).upper()
    if sair in 'SN':
        if sair == 'N':
            break
for l in list_c:
    if l % 2 == 0:
        par.append(l)
    else:
        impar.append(l)
print('-='*20)
print(f'A lista completa é de {len(list_c)} valores: {list_c}\n'
      f'A lista de pares é: {par}\n'
      f'A lista de impares é: {impar}\n')







