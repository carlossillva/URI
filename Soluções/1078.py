# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
140

Exemplos de Saída	
1 x 140 = 140
2 x 140 = 280
3 x 140 = 420
4 x 140 = 560
5 x 140 = 700
6 x 140 = 840
7 x 140 = 980
8 x 140 = 1120
9 x 140 = 1260
10 x 140 = 1400
"""
n = int(input())

for c in range(1, 11):
	print(f'{c} x {n} = {c * n}')