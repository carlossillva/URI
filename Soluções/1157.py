# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
6
Exemplos de Saída
1
2
3
6
"""

n = int(input())

for c in range(1, n+1):
	if n % c == 0:
		print(c)
