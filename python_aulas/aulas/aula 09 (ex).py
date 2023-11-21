# AULA TEORICA #09 - Manipulando Texto
frase = 'Curso em vídeo python'
print(frase[::2])
print('oi')
# print("""Nessa aula, vamos aprender operações com String no Python.\n
# As principais operações que vamos aprender são o Fatiamento\n
# de String, Análise com len(), count(), find(), transformações\n
# com replace(), upper(), lower(), capitalize(), title(), strip(),\n
# junção com join().""")

print(frase.upper().count('0'))
print(frase.count('o'))
print(len(frase.strip()))
print(frase.replace('python','android'))
dividido = frase.split()
print(dividido[2][3])
print()
print()
print()
