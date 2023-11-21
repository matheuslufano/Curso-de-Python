"""
DESAFIO - 105
Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes infor-
mações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicionar também as docstrings da função.
"""
def notas(*resp, sit=False):
    """
    -> Função para analisar notas e a situação de vários alunos
    :param resp: (resposta) Uma ou mais notas dos alunos (Aceira várias)
    :param sit: (Situação) Valor opcional, indicando se deve ou não adicionar a situação
    :return: Retorna um dicionário com várias informações sobre a situação da turma.
    """
    dict = {}
    # Valores das notas: maior, menor e media
    maior = resp[0]
    menor = resp[0]
    media = 0
    for c in resp:
        media += c
        # maior e menor:
        if c > maior:
            maior = c
        if c < menor:
            menor = c

    dict['Total'] = len(resp)
    dict['Maior'] = maior
    dict['Menor'] = menor
    dict['Média'] = media / len(resp)
    sit = dict['Média']

    # situação
    if sit:
        if dict['Média'] > 7:
            dict['Situação'] = 'BOA'
        elif dict['Média'] > 6 and dict['Média'] < 7:
            dict['Situação'] = 'RAZOÁVEL'
        else:
            dict['Situação'] = 'Ruim'


    print(dict)
    return resp


# Programa Principal
resp = notas(5.5, 7, 6, 6, sit=True) #sit=True
print('Notas: ', resp)
help(notas)

#==================resposta===========================================
# def notas(*n, sit=False):
#     """
#     --> Função para analisar notas e situações de vários alunos.
#     :param n: Uma ou mais notas dos alunos (aceita várias)
#     :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
#     :return: Dicionario com várias informações sobre a situação da turma.
#     """
#     r = dict()
#     r['total'] = len(n)
#     r['maior'] = max(n)
#     r['menor'] = min(n)
#     r['média'] = sum(n)/len(n)
#     if sit:
#         if r['média'] >= 7:
#             r['situação'] = 'BOA'
#         elif r['média'] >= 5:
#             r['situação'] = 'RAZOÁVEL'
#         else:
#             r['situação'] = 'RUIM'
#     return r
#
#
# # Programa Principal
# resp = notas(5.5, 2.5, 7, 4, 9, sit=True)# notas é um dicionario
# print(resp)
# help(notas)
