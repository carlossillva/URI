# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
13

Exemplos de Saída
2
15
28
41
...
"""
n = int(input())

for res in range(1, 10001):
	if res % n == 2:
		print(res)
