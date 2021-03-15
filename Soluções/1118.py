# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
-3.5
3.5
11.0
10.0
4
1
8.0
9.0
2

Exemplos de Saída
nota invalida
nota invalida
media = 6.75
novo calculo (1-sim 2-nao)
novo calculo (1-sim 2-nao)
media = 8.50
novo calculo (1-sim 2-nao)
"""

def medias():
	notas_validas = notas = 0
	while True:
		dados = float(input())
		if dados < 0 or dados > 10:
			print('nota invalida')
			continue
		else:
			notas_validas += 1
			notas += dados
			if notas_validas == 2:
				print(f'media = {(notas / 2):.2f}')
				break

while True:
	medias()
	while True:
		print('novo calculo (1-sim 2-nao)')
		fluxo = str(input())
		if fluxo not in '12':
			continue
		else:
			if fluxo == '1':
				medias()
			else:
				break
	if fluxo == '2':
		break
