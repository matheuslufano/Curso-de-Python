"""
\033[estilo:texto:fundo m

"""
print("\033[1;45mOlá mundo!\033[m")
a = 3
b = 5
nome = 'Matehus'
print("Os valores são \033[31m{}\033[m   e  \033[33m{}\033[m".format(a,b))
# {cor inicio} {variavel} {cor de fim}
print("Olá, muito prazer em te conhecer, {}{}{}!!!".format('\033[7m' ,nome, '\033[m'))

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'roxo':'\033[35m',
         'preto_branco':'\033[7;30m'}

cores = {'limpar':'\033[m',
        'branco':'\033[30m',
        'vermelho':'\033[31m',
        'verde':'\033[32m',
        'amarelo':'\033[33m',
        'azul':'\033[34m',
        'roxo':'\033[35m',
        'azul_claro':'\033[36m',
        'cinza':'\033[37m'}

print("olá gay! {}{}{}{}{}{}{}{}{} gls, como vai?".format(cores['vermelho'],'g',cores['limpa'],cores['amarelo'],'l',cores['limpa'],cores['roxo'],'s',cores['limpa']))