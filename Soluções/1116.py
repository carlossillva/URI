# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
3
3 -2
-8 0
0 8

Exemplos de Saída
-1.5
divisao impossivel
0.0
"""

fluxo = int(input())

for c in range(0, fluxo):
	a, b = str(input()).split()
	a, b = int(a), int(b)

	try:
		print(a / b)
	except:
		print('divisao impossivel')
