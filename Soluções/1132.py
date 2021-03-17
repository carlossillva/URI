# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
100
200

Exemplos de Saída
13954
"""
x = int(input())
y = int(input())
soma = 0

me = x if x < y else y
ma = y if y > x else x

for c in range(me, ma + 1):
	if c % 13 != 0:
		soma += c
print(soma)