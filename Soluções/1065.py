# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
7
-5
6
-4
12

Exemplos de Saída
3 valores pares
"""
def pares(valores):
	
	par = 0
	for valor in valores:
		if valor % 2 == 0:
			par += 1

	print(f'{par} valores pares')


dados = list()
# Lendo 5 valores
for leia in range(5):
	dados.append(int(input()))

pares(dados)