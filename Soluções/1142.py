# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
7

Exemplos de Saída
1 2 3 PUM
5 6 7 PUM
9 10 11 PUM
13 14 15 PUM
17 18 19 PUM
21 22 23 PUM
25 26 27 PUM
"""
n = int(input())

valor1 = 1
valor2 = 2
valor3 = 3

for c in range(0, n):
	print(f"{valor1} {valor2} {valor3} PUM")
	valor1 += 4
	valor2 += 4
	valor3 += 4
