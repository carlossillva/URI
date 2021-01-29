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
7.4
"""
def media_positivos(valores):

	for valor in valores:
		if valor < 0:
			valores.remove(valor)
			
	media = sum(valores) / len(valores)

	print(f'{len(valores)} valores positivos')
	print(f'{media:.1f}')


dados = list()
# Lendo 6 valores
for leia in range(6):
	dados.append(float(input()))

media_positivos(dados)