#DESAFIOS DA AULA #07 DE PYTHON (OPERADORES ARITIMÉTICOS)

#================Desafio 008========================
"""Escreva um programa que leia um valor em metros e
o exiba convertido em centimetros e milimetros."""
#===================================================
# km, hm, dam, m, dm, cm, mm (0,000000)
# 1M = 1000MM
# 1M = 100CM

m = float(input("Digite uma medida em metros: "))
km = m / 1000
hm = m / 100
dam = m / 10
cm = m * 100
mm = m * 1000

print("=====conversão de metros======\n{}m é igual a {}cm".format(m,cm))
print("{}m é igual a {}mm".format(m,mm))
print("{}m é igual a {}km".format(m,km))
print("{}m é igual a {}hm".format(m,hm))
print("{}m é igual a {}dam".format(m,dam))
