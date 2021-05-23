# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
3
6
5
28
Exemplos de Saída
6 eh perfeito
5 nao eh perfeito
28 eh perfeito
"""
lop = int(input())

for a in range(lop):

	n = int(input())
	divisores = list()

	for c in range(1, n):
		if n % c == 0:
			divisores.append(c)
	if sum(divisores) == n:
		print(f'{n} eh perfeito')
	else:
		print(f'{n} nao eh perfeito')
			
