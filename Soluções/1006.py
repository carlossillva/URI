# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
5.0
6.0
7.0

Exemplos de Saída
MEDIA = 6.3
"""

def media(A, B, C):

	return (((A * 2) + (B * 3) + (C * 5)) / 10)


A = float(input())
B = float(input())
C = float(input())

print(f'MEDIA = {media(A, B, C):.1f}')
