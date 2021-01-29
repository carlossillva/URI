# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
3
9

Exemplos de Saída
PROD = 27
"""

def produto(a, b):
	return a * b


a = int(input())
b = int(input())

prod = produto(a, b)
print(f'PROD = {prod}')