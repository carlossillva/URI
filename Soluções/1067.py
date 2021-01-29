# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
8

Exemplos de Saída
1
3
5
7
"""
def numeros_impares(valor):

	for x in range(0, valor+1):
		if x % 2 != 0:
			print(x)

numeros_impares(int(input()))
