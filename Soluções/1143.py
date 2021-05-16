# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
5

Exemplos de Saída
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
"""
nvalor = int(input())

for c in range(1, nvalor+1):
	res = c * c
	resf = res * c
	print(f'{c} {res} {resf}')
