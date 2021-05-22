# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
5

Exemplos de Saída
0 1 1 2 3
"""
n = int(input())

fibonnaci = list()


a, b = 0, 1

for c in range(1, n+1):
	if c < n:
		print(a, end=' ')
	else:
		print(a)
	a, b = b, a + b
