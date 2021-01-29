# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
10.0 20.1 5.1

0.0 20.0 5.0

Exemplos de Saída
R1 = -0.29788
R2 = -1.71212

Impossivel calcular
"""
from math import sqrt, pow

a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

try:
	d = sqrt(pow(b, 2) - (4 * (a * c)))
	r1 = (-b + d) / (2 * a)
	r2 = (-b - d) / (2 * a)
except Exception as erro:
	#print(erro.__class__)
	print('Impossivel calcular')
else:
	print(f'''R1 = {r1:.5f}
R2 = {r2:.5f}''')
