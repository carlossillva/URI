# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
2 2
3 -2
-8 -1
-7 1
0 2

Exemplos de Saída
primeiro
quarto
terceiro
segundo
"""
while True:
	dados = str(input()).split()
	x, y = int(dados[0]), int(dados[1])

	if x > 0 and y > 0:
		print('primeiro')
	elif x < 0 and y > 0:
		print('segundo')
	elif x < 0 and y < 0:
		print('terceiro')
	elif x > 0 and y < 0:
		print('quarto')
	elif x == 0 or y == 0:
		break