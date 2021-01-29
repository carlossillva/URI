# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
5 4
7 2
3 8
2 2

Exemplos de Saída
Decrescente
Decrescente
Crescente
"""
while True:
	x, y = str(input()).split()
	x = int(x)
	y = int(y)
	if x == y:
		break
	print('Decrescente' if x > y else 'Crescente')