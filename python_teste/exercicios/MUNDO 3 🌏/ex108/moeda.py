def aumentar(preço = 0, taxa = 0):
    res = preço + (preço * taxa/100)
    return res



def diminuir(preço = 0, taxa = 0):
    res = preço - (preço * taxa/100)
    return res


def dobro(preço = 0):
    res = preço * 2
    return res


def metade(num = 0):
    resp = num - (num/2)
    return resp


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',') #replace(substitua)