# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
6

Exemplos de Saída
2^2 = 4
4^2 = 16
6^2 = 36
"""
from math import pow

def quadrado_pares(valor):
	for v in range(1, valor+1):
		if v % 2 == 0:
			quadrado = pow(v, 2)
			print(f'{v}^2 = {quadrado:.0f}')


dados = int(input())
quadrado_pares(dados)