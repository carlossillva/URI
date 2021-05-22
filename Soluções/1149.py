# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
3 -1 0 -2 2

Exemplos de Saída
7
"""

def checker(n):
	i = 1
	while (n[i] <= 0):
		i += 1
		if n[i] > 0:
			break
	summ(n[0], n[i])


def summ(x, n):
	soma = 0
	for c in range(0, n):
		print(c)
		soma = soma + x + c
	print(soma)


checker(list(map(int, input().split())))
