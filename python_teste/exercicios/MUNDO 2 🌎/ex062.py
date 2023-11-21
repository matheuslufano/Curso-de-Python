"""
====================================================================
DESAFIO - 062
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encarra quando ele disser que quer mostrar
O Termos.
====================================================================
"""

# opção = str(input('Quer continuar? (S/N) ')).upper()

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} ⇨ '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você que mostrar a mias? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
