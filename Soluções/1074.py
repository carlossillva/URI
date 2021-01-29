# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
4
-5
0
3
-4

Exemplos de Saída
ODD NEGATIVE
NULL
ODD POSITIVE
EVEN NEGATIVE
"""
def check(valores):
	for valor in valores:
		if valor == 0:
			string = 'NULL'
		else:
			pn = 'POSITIVE' if valor > 0 else 'NEGATIVE'
			if valor % 2 == 0:
				string = f'EVEN {pn}'
			else:
				string = f'ODD {pn}'
		print(string)


N = int(input())

dados = list()

for leia in range(N):
	dados.append(int(input()))

check(dados)
