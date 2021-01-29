# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
5 6 7 8

2 3 2 6

Exemplos de Saída
Valores nao aceitos

Valores aceitos
"""
# B > C & D > A == True 
# C + D > A + B
# C & D == +
# A == Par

X = str(input()).split()
A, B, C, D = X

A = int(A)
B = int(B)
C = int(C)
D = int(D)

if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A % 2 == 0:
	print('Valores aceitos')
else:
	print('Valores nao aceitos')