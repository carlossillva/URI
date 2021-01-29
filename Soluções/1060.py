# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
7
-5
6
-3.4
4.6
12

Exemplos de Saída
4 valores positivos
"""
num_positivos = 0

for leia in range(6):
	dados = float(input())
	if dados >= 0:
		num_positivos += 1

print(f'{num_positivos} valores positivos')