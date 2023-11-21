"""
====================================================================
DESAFIO - 073
Crie uma tabela preenchida com 20 primeiros colocados da tabela do
campeonato brasileiro de futebol, na ondem de colocação. Depois mostra:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da chapecoense.
====================================================================
"""
# há uma pequena modificaçãozinha, 🤫 na liga de futebol, me sentir mais confortaveu
# vou fazer um programa sobre a liga de futebol gay 🏳️‍🌈

# Crie uma tabela preenchida com 12 primeiros colocados da tabela Champions Ligay 2018,
# na ondem de colocação. Depois mostra:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da chapecoense.

"""
Rio de Janeiro:
- BeesCats (7º)
- Alligaytors (11º) 
---------------------------------
São Paulo:
- Futeboys (01º)
- Unicorns (02º)
- Afronte FC (10º)
- Bulls Football (03º) 
---------------------------------
Belo Horizonte:
- Bharbixas (04º) 
---------------------------------
Brasília:
- Bravus (08º) 
---------------------------------
Porto Alegre:
- Magia (06º) 
- PampaCats (05º) 
---------------------------------
Florianópolis:
- Sereyos (12º) 
---------------------------------
Curitiba
- Capivara FC (09º)
---------------------------------
"""

print('\033[33m2ª Edição da Champions Ligay 2018\n'
      'conta com 12 times:\033[m')
print('🟥🟧🟨🟩🟦🟪🟪🟦🟩🟨🟧🟥')
"""
- Futeboys (01º)
- Unicorns (02º)
- Bulls Football (03º)
- Bharbixas (04º) 
- PampaCats (05º) 
- Magia (06º) 
- BeesCats (7º)
- Bravus (08º) 
- Capivara FC (09º)
- Afronte FC (10º)
- Alligaytors (11º) 
- Sereyos (12º) 
"""
times = ('01º - Futeboys',
         '02º - Unicorns',
         '03º - Bulls Football',
         '04º - Bharbixas',
         '05º - PampaCats',
         '06º - Magia',
         '07º - BeesCats',
         '08º - Bravus',
         '09º - Capivara FC',
         '10º - Afronte FC',
         '11º - Alligaytors',
         '12º - Sereyos',)
times_em_ondem = ('Futeboys',
                  'Unicorns',
                  'Bulls Football',
                  'Bharbixas',
                  'PampaCats',
                  'Magia',
                  'BeesCats',
                  'Bravus',
                  'Capivara FC',
                  'Afronte FC',
                  'Alligaytors',
                  'Sereyos',)

for t in times:
    print(f'{t}')
print('\n🟥🟧🟨🟩🟦🟪🟪🟦🟩🟨🟧🟥')
#----------------------------------------------
# A) Apenas os 5 primeiros colocados.
print('🏳️‍🌈 \033[33mOS CINCO PRIMEIROS COLOCADOS SÃO:\033[m')
cont = 0
for c in range(0,5):
    print(times[cont])
    cont += 1

#----------------------------------------------
 # B) Os últimos 4 colocados da tabela.
print('\n🟥🟧🟨🟩🟦🟪🟪🟦🟩🟨🟧🟥')
print('🏳️‍🌈 \033[33mOS ÚLTIMOS 4 COLOCADOS DA TABELA\033[m')
cont = 8
for c in range(8,12):
    print(times[cont])
    cont += 1

#----------------------------------------------
# C) Uma lista com os times em ordem alfabética.
print('\n🟥🟧🟨🟩🟦🟪🟪🟦🟩🟨🟧🟥')
print('🏳️‍🌈 \033[33mLista com os times em ordem alfabética:\033[m')
for t in sorted(times_em_ondem):
    print(t)
#----------------------------------------------
# D) Em que posição na tabela está o time da chapecoense.
print('\n🟥🟧🟨🟩🟦🟪🟪🟦🟩🟨🟧🟥')
print('🏳️‍🌈 \033[33mEm qual posição está o time Futeboys.\033[m' )
print(f'O Foteboys está na {times_em_ondem.index("Futeboys")+1}° posição')
print(f"                FIM                                  ")


print()
print('===========Curso em vídeo===========')
for t in times:
    print(t)
print(f'Lista de times gay do Brasil:\n{times}')
print('-=-' * 15)
#----------------------------------------------
# A) Apenas os 5 primeiros colocados.
print('\nOS CINCO PRIMEIROS COLOCADOS SÃO: '
      f'\n{times[0:5]}')
#----------------------------------------------
 # B) Os últimos 4 colocados da tabela.
print('\nOS ÚLTIMOS 4 COLOCADOS :'
      f'\n{times[-4:]}')

#----------------------------------------------
# C) Uma lista com os times em ordem alfabética.
print(f'Times em ordem alfabética: {sorted(times)}')
#----------------------------------------------
# D) Em que posição na tabela está o time da chapecoense.
print(f'O Futeboys está na {times_em_ondem.index("Futeboys")+1} ° posição')

