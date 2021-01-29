# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
3
6.5 4.3 6.2
5.1 4.2 8.1
8.0 9.0 10.0

Exemplos de Saída
5.7
6.3
9.3
"""
n = int(input())

for leia in range(n):
	a, b, c = str(input()).split()
	media = ((float(a) * 2) + (float(b) * 3) + (float(c) * 5)) / 10
	print(f'{media:.1f}')
	