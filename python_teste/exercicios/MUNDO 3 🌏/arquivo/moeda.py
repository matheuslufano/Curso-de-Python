def moeda(valor):
    num = f"{valor:.2f}"
    return num


def metade(num):
    resp = num - (num/2)

    return resp


def dobro(num):
    resp = num * 2
    return resp


def acréscimo(n, p):
    acre = n * (p/100)
    resp = n + acre
    return resp

def desconto(n, d):
    des = n * (d/100)
    resp = n - des
    return resp


# p = float(input('valor: '))
# print(f'A metade de {moeda(p)}')