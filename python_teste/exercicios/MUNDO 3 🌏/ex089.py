"""
====================================================================
DESAFIO - 089
Crie um programa que leia nome e duas notas de vários alunos e guarde
tudo em uma lista composta. No Final, mostre um boletim contendo a média
de cada um e permita que o usuário possa mostrar as nostas de cada aluno
individualmente.
====================================================================
"""
lista = []
listNota = []#['Matheus ', 10], ['Fulano', 4.5], ['Ciclano', 6.0]
tet = []
notas = []#[10, 10], [6, 7], [8, 6]

while True:
    nome = str(input('Nome: '))
    n1 = float(input('Note 1: '))
    n2 = float(input('Note 2: '))
    media = n1 + n2 / 2
    lista.append(nome)
    lista.append(media)
    listNota.append(lista[:])
    tet.append(n1)
    tet.append(n2)
    notas.append(tet[:])
    lista.clear()
    tet.clear()

    sair = str(input('Quer sair? [S/N] ')).upper()
    if sair == 'S':
        break
print('-='*20)
print('No. NOME         MÉDIA\n'
      '_____________________________________')
for i, l in enumerate(listNota):
    print(f"{i}  {l[0]}              {l[1]}")
print('_____________________________________')
while True:
    aluno = int(input('Mostrar notas de qual aluno da lista? (999 sair): '))
    print(f'As notas de "{listNota[aluno][0]}" são:\n'
          f'- Nota 1: {notas[aluno][0]} pontos. \n'
          f'- Nota 2: {notas[aluno][1]} pontos.')
    print('____________________________________________________________')
    if aluno == 999:
        break
# print(listNota)
# print(notas)
