# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
5
6
7
8

Exemplos de Saída
DIFERENCA = -26
"""

def diferenca(A, B, C, D):
	return ((A * B) - (C * D))


A = int(input())
B = int(input())
C = int(input())
D = int(input())

print(f'DIFERENCA = {diferenca(A, B, C, D)}')
