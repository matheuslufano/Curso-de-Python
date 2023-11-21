# DESAFIO 004 (VÍDEO EM CURSO) - Faça um programa que leia algo pelo teclado e
# mostre na tela o "seu tipo primitivo" e "todos as informações" possiveis sobre ele.

x = input ("Pressione uma tecla: ")

print ('O seu tipo primitivo é?', type(x))
print ('É um númerico?', x.isnumeric())
print ('É alfabético?', x.isalpha())
print('É alfanumérico?', x.isalnum())
print('Só tem espaço?', x.isspace())
print ('Estar em maiúscula? ', x.isupper())
print('Estar em minúsculas?', x.islower())
print('Estar capitalizada?', x.istitle())
