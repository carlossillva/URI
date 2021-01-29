# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
8

Exemplos de Saída
9
11
13
15
17
19
"""
def next_impares(valor):

	xtemp = list()
	while True:
		if valor % 2 != 0:
			xtemp.append(valor)
		
		valor += 1

		if len(xtemp) == 6:
			return xtemp


x = next_impares(int(input()))

for item in x:
	print(item)