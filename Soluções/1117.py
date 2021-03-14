# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
-3.5
3.5
11.0
10.0

Exemplos de Saída
nota invalida
nota invalida
media = 6.75
"""
notas = 0
qnotas = 0
while True:
	na = float(input())
	
	if na >= 0 and na <= 10:
		notas += na
		qnotas += 1
		if qnotas == 2:
			media = notas / 2
			print(f'media = {media:.2f}')
			break
	else:
		print('nota invalida')
