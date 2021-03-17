# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
10
18

Exemplos de Saída
12
13
17
"""

x = int(input())
y = int(input())

ma = x if x > y else y
me = y if y < x else x

for c in range(me+1, ma):
	if c % 5 == 3 or c % 5 == 2:
		print(c)
