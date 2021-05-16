# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
5

Exemplos de Saída
1 1 1
1 2 2
2 4 8
2 5 9
3 9 27
3 10 28
4 16 64
4 17 65
5 25 125
5 26 126
"""
nvalor = int(input())

for c in range(1, nvalor+1):
	res = c * c
	resf = res * c
	print(f'{c} {res} {resf}')
	print(f'{c} {res + 1} {resf + 1}')
